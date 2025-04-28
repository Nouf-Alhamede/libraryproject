from django import forms
from .models import Book,Student,Address,Student2,Address2 ,Profile

class BookForm(forms.ModelForm):
    class Meta:
      model = Book # ما هو الموديل الي احتاجة 
      fields = ['title','author']#وش الاشياء الي ابي اضيفها لي النموذج 
      
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student 
        fields = ['name','age','address']
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address 
        fields = '__all__' #هنا ابغى كل الي في جدول Address
        
########################## many-to-many
class StudentForm2(forms.ModelForm):
    class Meta:
        model = Student2 
        fields = ['name','age','address']
        
class AddressForm2(forms.ModelForm):
    class Meta:
        model = Address2 
        fields = '__all__'#هنا ابغى كل الي في جدول Address
        
class ProfileForm(forms.ModelForm):# form لي عرض الصور 
    class Meta:
        model = Profile
        fields = '__all__'
        