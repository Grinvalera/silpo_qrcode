from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"autofocus": "", "placeholder": "Send your visit on us"}))

    class Meta:
        model = Feedback
        fields = ['text', 'name', 'contact']