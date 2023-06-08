from django.shortcuts import render,redirect
from .forms import CustomerForm

# Create your views here.
def home(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/thankyou')
    else:
        context = {'form': form}       
    return render(request, 'home.html', context)
   

def thankyou(request):
    return render(request, 'thankyou.html')
