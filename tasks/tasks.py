from celery import shared_task
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_task_notification(task_id, action):
    # Имитация отправки уведомления (например, email)
    logger.info(f"Task {task_id} was {action}. Notification sent.")
    return f"Notification for task {task_id} sent."
