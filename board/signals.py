from django.db.models.signals import post_save  # сигнал на сохранение в БД
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from django.core.mail import send_mail
from .models import Reply


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender=Reply)
def notify_user_reply(sender, instance, created, **kwargs):
    recipient_list = [instance.post.author.email]

    #  Отправляем письмо
    send_mail(
        subject=f'Новый отклик на ваш пост на сайте!',
        message='Краткое содержание: ' + instance.text[0:200] + '\n' + f'Перейти на сайт: http://127.0.0.1:8000',
        from_email='info@vikingservice72.ru',
        recipient_list=recipient_list
    )