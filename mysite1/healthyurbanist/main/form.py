from django import forms
from .models import Comments
'''from captcha.fields import CaptchaField'''

class CommentsForm(forms.ModelForm):
    '''captcha = CaptchaField()'''
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_comments')