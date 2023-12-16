from celery import Celery, shared_task

from main import main as tg_task
from celerys import celeryconfig

app = Celery('tasks', broker='redis://redis:6379/0')


app.config_from_object(celeryconfig)


@shared_task
def repeating_task():
    tg_task()


app.conf.beat_schedule = {
    'run_every_3_hours': {
        'task': 'tasks.repeating_task',
        'schedule': 3 * 60 * 60
    }
}
app.conf.timezone = 'UTC'

# # # для первого запуска приложения
# if __name__ == '__main__':
#     repeating_task()
