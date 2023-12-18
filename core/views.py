from datetime import datetime
from django.shortcuts import render

# from django.http import HTTP404

from . import renderer


def pdf_view(request, *args, **kwargs):
    data = {
        "today": datetime.date.today(),
        "amount": 39.99,
        "customer_name": "Cooper Mann",
        "invoice_number": 1233434,
    }
    return renderer.render_to_pdf("core/pdf_template.html", data)


# Create your views here.
def home(request):
    context = {
        "test": "TEST",
    }
    return render(request, "core/home.html", context=context)
