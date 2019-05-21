# bobs_banana_stand


virtualenv -p python3 bobs_banana_stand

source bobs_banana_stand/bin/activate  

python -m pip install -r requirements.txt


celery -A bobs_banana_stand beat     
celery -A bobs_banana_stand worker -l info

celery -A bobs_banana_stand beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
