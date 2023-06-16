from django.db import models
from django.contrib.auth.models import User 
from django.core.mail import send_mail, EmailMultiAlternatives, EmailMessage
from django.shortcuts import get_object_or_404
from django.conf import settings

from cloudinary.models import CloudinaryField


from django.template.loader import render_to_string
from django.utils.html import strip_tags

import string    
import random

# email html template path
email_html_template = "account/validation_email.html"


def generate_token():
    """RETURN RANDOM GENERATED CHARATER TO BE USED AS TRANSACTION BATCH"""
    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 12)))



# SENDING EMAIL TO USER WHEN DOCUMENTS ARE VALIDATED
def send_mail_to_user(username, name, user_email, token):
    """SENDS EMAIL TO THE USER"""
    context = {
        "name": name,
        "username": username,
        "token": token,
        "content": "We have successfully Validated your account. You can login now and cast your vote",
    }
    html_content = render_to_string(email_html_template, context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(    
        "Account Validated Successfully",
        text_content,
        settings.EMAIL_HOST_USER,
        [user_email,]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

    return None

POSITIONS = (
    
    ("PRESIDENT", "PRESIDENT"),
    ("VICE PRESIDENT", "VICE PRESIDENT"),
    ("DIRECTOR OF SPORTS", "DIRECTOR OF SPORTS"),
    ("STUDENT AFFAIRS", "STUDENT AFFAIRS")
    
)


class Candidate(models.Model):
    candidate_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITIONS)
    photo = CloudinaryField("media/candidates/")
    vote_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.candidate_name}: {self.vote_count}"
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    validation_method = models.CharField(max_length=100)
    validation_number = models.CharField(max_length=100)
    validated = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        super(UserProfile, self).save(*args, **kwargs)
        if self.validated == True:
            user = self.user
            _user = get_object_or_404(User, username=user)
            _user_email = _user.email
            _username = _user.username
            _user_full_name =  f"{str(_user.first_name)} {str(_user.last_name)}"
            
            # SETTING THE PASSWORD OF THE USER TO THE TOKEN
            _token = generate_token()
            _user.set_password(_token)
            _user.save()
            
            # SENDING EMAIL TO THE USER ABOUT PASSWORD
            try:
                send_mail_to_user(_username, _user_full_name, _user_email, _token)
            except:
                pass
        return super().save()
    
    def __str__(self):
        return self.user.username
    