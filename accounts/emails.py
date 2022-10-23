from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth import get_user_model

User = get_user_model()

def sendEmail(email):
    sucject = 'Your account verification email Djangommerce'
    randomNumber = random.randint(1000,9999)
    
    userEmail = User.objects.get(email=email)
    userEmail.verificationCode = randomNumber
    userEmail.save()
    
    message = f'Your verification code: {randomNumber}'
    emailFrom = settings.EMAIL_HOST
    
    send_mail(sucject,message,emailFrom,[email])
    
    
    