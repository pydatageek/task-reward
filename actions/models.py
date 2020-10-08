from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator, MinValueValidator)
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ActionLevel(models.Model):
    """Depending on the level, points can be:
    VE: 1-3, E: 3-5, M: 5-7, H: 8-10, VH: 11-15
    """

    name = models.CharField(
        _('name'), unique=True, max_length=50)
    level_up_point = models.PositiveIntegerField(
        _('level up point'))
    min_point = models.PositiveSmallIntegerField(
        _('min point'),
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        help_text=_('point depends on the level'))
    max_point = models.PositiveSmallIntegerField(
        _('max point'),
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        help_text=_('point depends on the level'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Action Level')
        verbose_name_plural = _('Action Levels')

    def get_absolute_url(self):
        return reverse('action-level-detail', args=[self.id])


class Action(models.Model):
    """Action is the main model of the app.
    Everything is built on/related with it.
    According level, points can be:
    VE: 1-3, E: 3-5, M: 5-7, H: 8-10, VH: 11-15
    """
    name = models.CharField(
        _('action'), max_length=255)
    level = models.ForeignKey(
        ActionLevel, on_delete=models.CASCADE,
        related_name='actions', verbose_name=_('level'))

    point = models.SmallIntegerField(
        _('point'),
        validators=[MinValueValidator(1), MaxValueValidator(15)],
        help_text=_('points depend on the level of the action'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Action')
        verbose_name_plural = _('Actions')
        unique_together = ('name', 'level')

    def get_absolute_url(self):
        return reverse('action-detail', args=[self.id])

    def clean(self):
        level = self.level
        point = self.point

        if not (level.min_point <= point <= level.max_point):
            raise ValidationError(
                _(f'points should be between {level.min_point}-{level.max_point}, inclusive'),
                code='invalid',
            )

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
