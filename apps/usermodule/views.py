from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm#هذي هي اصلن بدال form الي كنا نسويها ما يحتاج اضيف فورم 
from django.contrib import messages #هذي عشان الرسال الي توصل عند الدخول خطا او صح 
from django.contrib.auth.views import LoginView #هذي اضفتها عشان فنكشن login 
from django.contrib.auth import logout
from django.urls import reverse_lazy


def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you have successfully register')# كذا تستعمل الرسالة 
            return redirect('login')# اذا ايوزر دخل المعلومات دخله على login
        else:
           messages.error(request,'please correct the error') #هنا لما يكون ادخال خطاء 
    else:
        form =UserCreationForm()
    return render(request,'usermodule/register.html',{'form':form}) 

class CustomLoginView(LoginView):
    template_name = 'usermodule/login.html'
    next_page = reverse_lazy('list_student')
    
def Logout_view(request):
   logout(request)
   return redirect('login')