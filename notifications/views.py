from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from notifications.tasks import send_async_email

class SendEmailView(APIView):
    def post(self, request):
        send_async_email.delay(
            'Async Hello!',
            'This email was sent using Celery.',
            'your-email@example.com',
            ['recipient@example.com'],
        )
        return Response({'status': 'email task queued'})