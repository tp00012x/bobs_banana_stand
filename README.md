# bobs_banana_stand

virtualenv -p python3 bobs_banana_stand

source venv/bin/activate

python -m pip install -r requirements.txt

python manage.py runserver

celery -A bobs_banana_stand beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

celery -A bobs_banana_stand worker -l info

