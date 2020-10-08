from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator, MinValueValidator)
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from actions.models import Action

User = get_user_model()


class UserLevel(models.Model):
    """"""

    name = models.CharField(
        _('name'), unique=True, max_length=50)
    level_up_point = models.PositiveIntegerField(
        _('level up point'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User Level')
        verbose_name_plural = _('User Levels')

    def get_absolute_url(self):
        return reverse('user-level-detail', args=[self.id])


class UserActions(models.Model):
    """Actions completed by user"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='useractions', verbose_name=_('user'))
    action = models.ForeignKey(
        Action, on_delete=models.CASCADE,
        related_name='useractions', verbose_name=_('action'))
    point_earned = models.SmallIntegerField(
        _('point earned'), blank=True, null=True)

    timestamp = models.DateTimeField(
        _('date'), default=timezone.now, editable=False)

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = _('User Action')
        verbose_name_plural = _('User Actions')
        # unique_together = ('user', 'action')
        db_table = 'useractions'

    def get_absolute_url(self):
        return reverse('user-action-detail')

    def save(self, *args, **kwargs):
        self.point_earned = self.action.point
        return super().save(*args, **kwargs)


class UserStatus(models.Model):
    """User's total points and level status are defined by accomplished actions"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='userstatus', verbose_name=_('user'))
    level = models.ForeignKey(
        UserLevel, on_delete=models.CASCADE, blank=True, null=True,
        related_name='userstatus', verbose_name=_('level'))

    total_points = models.PositiveIntegerField(
        _('total points'), blank=True, null=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = _('User Status')
        verbose_name_plural = _('Users Statuses')
        db_table = 'userstatus'

    def get_absolute_url(self):
        return reverse('user-status-detail')


@receiver(post_save, sender=UserActions, dispatch_uid='update_user_status')
def update_user_status(sender, instance, **kwargs):
    """UserStatus is updated after an action is accomplished by the user"""

    levels = UserLevel.objects.order_by('-level_up_point')

    user_status, created = UserStatus.objects.update_or_create(
        user=instance.user,
    )
    if created:
        user_status.total_points = instance.point_earned
    else:
        user_status.total_points += instance.point_earned

    for level in levels:
        if user_status.total_points >= level.level_up_point:
            user_status.level = level
            break

    user_status.save()
