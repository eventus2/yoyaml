from  django import forms
from .models import Feedback

class FeedbackMessage(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('client_name', 'email', 'topic', 'message')