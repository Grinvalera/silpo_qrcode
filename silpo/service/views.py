from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import FeedbackForm


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'service/qr.html'


# Create your views here.
