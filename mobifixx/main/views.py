from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import Contact

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        dab= Contact.objects.all()
        if form.is_valid():
            form.save()
            return redirect('home')

    form = ContactForm()
    context={
    'form':form
    }
    return render(request,'main/index.html',context)
