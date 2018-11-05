# from datetime import timedelta
#
# from django.core.mail import send_mail
# from django.utils import timezone
#
# from config import celery_app
# from todo.models import Todo
#
#
# __all__ = (
#     'send_notification_mail',
#     'send_test_mail',
# )
#
#
# @celery_app.task
# def send_notification_mail():
#     todos = Todo.objects.all().exclude(is_done=True).exclude(expiration=None)
#     now = timezone.localtime()
#     zero = timedelta(0)
#     an_hour = timedelta(hours=1)
#     mail_results = list()
#     for todo in todos:
#         td = todo.expiration - now
#         if zero < td <= an_hour:
#             result = send_mail(
#                 subject=f'마감 알림 메일: {todo.title}',
#                 message=f"""아래 할일 마감이 1시간 남았습니다.
#                 제목: {todo.title}
#                 내용: {todo.content}
#                 기한: {todo.expiration}""",
#                 recipient_list=['joo2theeon@gmail.com'],
#                 from_email='',
#             )
#             mail_results.append(result)
#
#     return mail_results
#
#
# @celery_app.task(name='send_test_mail')
# def send_test_mail():
#     todo = Todo.objects.first()
#     send_mail(
#         subject=f'마감 알림 메일: {todo.title}',
#         message=f"""아래 할일 마감이 1시간 남았습니다.
# 제목: {todo.title}
# 내용:
# {todo.content}
# 기한: {todo.expiration}""",
#         recipient_list=['joo2theeon@gmail.com'],
#         from_email='',
#     )
