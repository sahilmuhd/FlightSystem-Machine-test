<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:0d0221,50:7b2ff7,100:00f0ff&text=Flight%20System&fontColor=00f0ff&fontSize=48&fontAlignY=38&desc=Django%20machine%20test%20for%20airport%20route%20nodes&descAlignY=58&descSize=16&animation=fadeIn" alt="Flight System"/>

<img src="https://img.shields.io/badge/Python-0d0221?style=for-the-badge&logo=python&logoColor=00f0ff"/>
<img src="https://img.shields.io/badge/Django-0d0221?style=for-the-badge&logo=django&logoColor=7b2ff7"/>
<img src="https://img.shields.io/badge/PostgreSQL-0d0221?style=for-the-badge&logo=postgresql&logoColor=ff2a6d"/>
<img src="https://img.shields.io/badge/Bootstrap-0d0221?style=for-the-badge&logo=bootstrap&logoColor=00f0ff"/>

</div>

## // OVERVIEW

Machine test submission: a small Django app that stores airport routes (airport code, Left/Right position, duration in minutes) and lets you query them through simple pages.

## // FEATURES

- Add an airport route (airport code, position Left or Right, duration in minutes)
- Find the Nth Left or Right node (1-based, ordered by insertion)
- Find the longest node by duration
- Find the shortest node by duration between a source and destination airport code
- Django templates for each page

## // TECH_STACK

- Python and Django (app: `flights`, project: `FlightSystem`)
- PostgreSQL (database `flights` on `127.0.0.1:5432`, user `postgres`, configured in `settings.py`)
- Bootstrap in the templates

## // GETTING_STARTED

```bash
cd FlightSystem
python -m venv venv && source venv/bin/activate
pip install django psycopg2-binary   # the repo has no requirements.txt

# create a PostgreSQL database named "flights" and adjust DATABASES in FlightSystem/settings.py if needed
python manage.py migrate
python manage.py runserver
```

Pages: `/` (home), `/add/`, `/find-nth/`, `/longest/`, `/shortest/`.

## // PROJECT_STRUCTURE

```
FlightSystem
├── FlightSystem   # Django project settings and urls
├── flights        # app: models, forms, views, templates, migrations
└── manage.py
```

## // AUTHOR

Sahil, [github.com/sahilmuhd](https://github.com/sahilmuhd)

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=100&color=0:00f0ff,50:7b2ff7,100:0d0221&section=footer" alt="footer"/>

Built by [Sahil](https://github.com/sahilmuhd) · [sahilmuhd.com](https://sahilmuhd.com)

</div>
