from django.shortcuts import render
from django.views.generic.edit import FormView
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.shortcuts import render
# from qr_code.qrcode.utils import QRCodeOptions

from .models import Feedback
from .forms import FeedbackForm
from .models import QRCode


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'service/qr.html'
    success_url = reverse_lazy('service:ok')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


# def myview(request):
#     # Build context for rendering QR codes.
#     context = dict(
#         my_options=QRCodeOptions(size='t', border=6, error_correction='L'),
#     )
#
#     # Render the view.
#     return render(request, 'service/qr.html', context=context)


class QRListView(ListView):
    model = QRCode
# Create your views here.
