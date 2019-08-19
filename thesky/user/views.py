from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import Usercreationform
from .models import Football

def register(request):
    if request.method=="POST":
        form=Usercreationform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            messages.success(request,f' تهانينا{username}تم التسجيل بنجاح')
        return redirect('home')
    else:form=Usercreationform()
    return render(request,'user/register.html',{'title': 'التسجيل'  ,'form':form, })

# Create your views here.
def profile(request):

    return render(request,'user/profile.html',{'title':'الملف الشخصي',})



def football(request):
     test=Football.objects.all()
     context = {
        'title': 'الصفحة الرئيسية',
         'footballs':test,

    }
     return render(request,'user/football.html',context)