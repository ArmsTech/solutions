"""Settings for celery, redis, etc."""

from datetime import timedelta

from kombu import Exchange, Queue

BROKER_URL = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_QUEUES = (
    Queue('default', Exchange('default'), routing_key='default'),
    Queue('median', Exchange('median'), routing_key='median'),
    Queue('scheduled', Exchange('scheduled'), routing_key='scheduled')
)
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ROUTES = {
    'median.tasks.get_median_for_last_min': {
        'queue': 'median', 'routing_key': 'median'},
    'median.tasks.remove_old_integers': {
        'queue': 'scheduled', 'routing_key': 'scheduled'}
}
CELERY_TASK_RESULT_EXPIRES = 60
CELERY_TASK_SERIALIZER = 'json'
CELERYBEAT_SCHEDULE = {
    'remove_old_integers': {
        'task': 'median.tasks.remove_old_integers',
        'schedule': timedelta(seconds=120),
        'options': {'queue': 'scheduled'}
    }
}
CELERY_TIMEZONE = 'UTC'
