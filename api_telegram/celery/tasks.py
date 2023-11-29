from celery import Celery, shared_task

from ..main import main as tg_task
from . import celeryconfig


app = Celery('tasks', broker='redis://localhost:6379/0')


app.config_from_object(celeryconfig)


@shared_task
def repeating_task():
    tg_task()


app.conf.beat_schedule = {
    'run_every_3_hours': {
        'task': 'api_telegram.celery.tasks.repeating_task',
        'schedule': 8 * 60 * 60
    }
}
app.conf.timezone = 'UTC'

# для первого запуска приложения
if __name__ == '__main__':
    repeating_task()
