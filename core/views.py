from django.shortcuts import render, redirect
from .forms import QuotationForm

def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def quotation_view(request):
    form = QuotationForm()
    return render(request, 'core/quotation.html', {'form':form})

def submit_quotation(request):
    if request.method == "POST":
        form = QuotationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/submmitted.html')
    else:
        form = QuotationForm()
    return render(request, 'core/submmitted.html', {'form': form})