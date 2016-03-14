median_microservice: gunicorn -b 0.0.0.0:8000 median.app:app
median_worker: celery worker -A median.tasks -l INFO -Q median
schedule_worker: celery worker -B -A median.tasks -l INFO -Q scheduled
#redis: redis-server
#rabbit: rabbitmq-server
