# Survey app

A basic survey web app written in Django with no JavaScript.

This is a website where users can create surveys and get answers to their questions. A user can sign up, create a survey, add questions to the survey, and then send a link to other people. When the survey is complete, the user can see what percentage of people answered each question.

![preview](docs/preview.png)

# Setup

Requires Python 3 and the pip package manager.

```bash
# Optional - create virtualenv
virtualenv env
. env/bin/activate
# Install requirements
pip install -r requirements.txt
# Setup database
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
