# celeryconfig.py

CELERYBEAT_SCHEDULE_MAX_INTERVAL = 3 * 60 * 60
broker_url = 'redis://localhost:6379/0'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Europe/Dublin'
enable_utc = True
