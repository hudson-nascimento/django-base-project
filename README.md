# A simple base to start new Django project (API)

Using the best tools and settings to save your time.

## Getting Started

To start a new project, only clone this repository and create your favorite database, then start your code.

### Prerequisites

To use this project, you'll need [Pipenv](https://github.com/pypa/pipenv) and [Python](https://www.python.org/) 3.7 (I recommend use [Pyenv](https://github.com/pyenv/pyenv) to manager Python versions) 

### Installing

To start a new project go to a folder and follow this.

```
$ git clone https://github.com/silasvasconcelos/django-base-project.git project-name
```
```
$ pyenv install 3.7 # install python 3.7
```

```
$ pipenv install --dev # create a virtualenv and install dependencies including dev
```

### Running the project

```
$ cp .env.example .env # copy settings from .env.example to .env
```

```
$ pipenv run python manage.py migrate # create database and run migrations
```

```
$ pipenv run python manage.py createsuperuser # create a admin user
```

```
$ pipenv run python manage.py runserver # start dev server
```


## Built With

* [Django 2.2](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Pip (Through pipenv)](https://maven.apache.org/) - Dependency Management
* [Pyenv](https://github.com/pyenv/pyenv) - Python version Management
* [Django REST Framework](https://rometools.github.io/rome/) - Used to create web api
* [DRF Generators](https://github.com/brobin/drf-generators) - Used to generate DRF code (serializers, views, urls and more)
* [Django cors headers](https://github.com/adamchainz/django-cors-headers) - App that adds Cross-Origin Resource Sharing (CORS) headers to responses.

## Author

* [Silas Vasconcelos](https://github.com/silasvasconcelos)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/silasvasconcelos/django-base-project/blob/master/LICENSE) file for details
