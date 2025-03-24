from config.env import env

CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://redis:6379")
CELERY_RESULT_BACKEND = env.str("CELERY_RESULT_BACKEND", "redis://redis:6379")
