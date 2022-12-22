from celery import shared_task
from .models import Post, Reply, Category
from django.core.mail import send_mail
import time


# Уведомление об отклике
@shared_task
def send_notify_email(reply_id):
    time.sleep(2)
    print('id reply = ' + str(reply_id))
    reply = Reply.objects.get(id=reply_id)
    recipient_list = [reply.user.email]
    print('recipient_list = ' + str(recipient_list))

    #  Отправляем письмо
    send_mail(
        subject=f'Вы отправили отклик на сайте!',
        message='Краткое содержание: ' + reply.text[0:200] + '\n' + f'Перейти на сайт: http://127.0.0.1:8000',
        from_email='info@vikingservice72.ru',
        recipient_list=recipient_list
    )



