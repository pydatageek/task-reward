# Task Reward
## Users are awarded after doing tasks

## Used technology:
Django (Python) + Jquery, Bootstrap

# Please follow the process below to install

1. Clone this repository (use `git clone https://github.com/pydatageek/task-reward.git`)

### setting up a development environment
2. start an environment with requirements
   e.g. pipenv install -r <project-folder>/requirements.txt

### migrating the already defined models and creating the super user
3. python manage.py migrate

### super user should be created before the dummy data be loaded!
4. python manage.py createsuperuser

### loading dummy data
5. python manage.py loaddata data.json
