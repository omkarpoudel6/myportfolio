from django.shortcuts import render
from .models import Projects
from .forms import Contact

# Create your views here.

def Home(request):
    if request.method=="POST":
        form=Contact(request.POST)
        if form.is_valid():
            form.save()
            context={
                'information':'Message submitted sucessfully, you will be contacted via your email.'
            }
            return render(request,'index.html',context)
            print("Form submitted by the user")
        else:
            context = {
                'information': 'Message submission unsucessfull, please enter valid information.'
            }
            return render(request, 'index.html',context)

    else:
        obj=Projects.objects.order_by('-timestamp')
        context={
            'projects':obj
        }
        return render(request,'index.html',context)