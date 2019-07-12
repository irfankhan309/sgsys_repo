from django.shortcuts import render
from django.views import View
from SGApp.models import AClist,Buy,Quotation
from SGApp import forms
from django.contrib import messages
# from SGApp.valid import validate

def Index(request):
    lists = AClist.objects.all()
    args={'lists':lists}
    return render(request,'SGApp/index.html',args)

def Quote_view(request):
    QForm =forms.QuoteForm()
    if request.method == 'POST':
        QForm = forms.QuoteForm(request.POST)
        if QForm.is_valid():
            QForm.save()
            return render(request,'SGApp/thanks.html')
        else:
            QForm = forms.QuoteForm()
    args ={'QForm':QForm}
    return render(request,'SGApp/Quotation.html',args)


def Buy_view(request):
    Form = forms.BuyForm()
    if request.method=='POST':
        Form = forms.BuyForm(request.POST)
        if Form.is_valid():
            Form.save()
            return render(request,'SGApp/Index.html')
        else:
            # messages.error(request, 'invalid.')
            Form = forms.BuyForm()
    args = {'Form':Form}
    return render(request,'SGApp/buy.html',args)


def About_view(request):
    return render(request,'SGApp/About.html')


def Contact_view(request):
    return render(request,'SGApp/contact.html')

def Services_view(request):
    return render(request,'SGApp/services.html')

def QuotationList(request):
    QList=Quotation.objects.all()
    args={'QList':QList}
    return render(request,'SGApp/QuotationList.html',args)
