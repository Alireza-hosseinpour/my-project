from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import NewsletterForm

# Create your views here.
def home(request):
    return render(request,'website/index.html')

def about(request):
    return render(request,'website/about.html')

def contact(request):
    from .forms import ContactForm
    if request.method == 'POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})

def newsletter_view(request):
    
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    form = NewsletterForm()
    return render(request,'website/newsletter.html',{'form':form})