from django.db import models


class Card(models.Model):
    card_number = models.IntegerField()

    def __str__(self):
        return f"Card #{self.card_number}"#عني بتدمج النص + الرقم في سطر واحد أنيق.
    #or return str(self.card_number)
    #عني لما تطبع الكائن، يرجع لك رقم البطاقة حقه كنص مب رقم لازم استعملها (String).

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name # هنا بما انها string نكتبها  كذا 
   

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})" # يكتب كذا # (Cs234)تقنيات الويب   
#هذي اذا عندي اثنين ابغاهم كلهم ترجعهم string كذا كتابتها 
# ليش استعمل f لانها تعني f-string في python معنتاها اكتبها عشان تحول الي بين الاقواس او ""الي نص 
#هذي مثل name = "Ali" print(f"Hello {name}") بايثون يكتبها كذا لازم f 

class Address(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"#  هنا استعملنا شكل يعنيby ترابط بين العنوان والموالف فا عند الكتابة يكتب اسم الكتاب by الموالف ترتب 

class Student(models.Model):
    name = models.CharField(max_length=100)#هنا معناتها اعرف حقل (filed )داخل قاعدة البيانات باسم (name )نوع الحقل 
    #charfield معناتها نوع الحقل هو نص يحتوي اكبر شي 100 حرف 
    age = models.IntegerField()
    #اما هنا با انه age معناتها رقم فا احط نوع الحقل integerfield 
    card = models.OneToOneField(Card, on_delete=models.PROTECT)#one to one معناتها احفظ بيانات اذا انحذفات ما تتاثر 
    #معنات PROTECT هنا انه اذا حاولت ان البطاقة المرتبطة بشخص النظام يمنع ويرسل رسلة خطاء 
    department = models.ForeignKey(Department, on_delete=models.CASCADE) #  معناتها كل موظف ينتمي الي قسم واحد ثمن بين قوسن many to one
    #اما معنات on_delete=mdels.CASCADE معنات cascade ان اذا القسم الرتبط في الموظف انحذف ينحذف الموظف 
    course = models.ManyToManyField(Course)#many to many هنا 
    address = models.ForeignKey(Address, on_delete=models.PROTECT)#معناتها many to one

    def __str__(self):
        return self.name # اسوي هذا اذا كان في ارتباط بين 2 models
######################################## many- to- many    
class Address2(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city
    
class Student2(models.Model):
    name = models.CharField(max_length=100)#هنا معناتها اعرف حقل (filed )داخل قاعدة البيانات باسم (name )نوع الحقل 
    #charfield معناتها نوع الحقل هو نص يحتوي اكبر شي 100 حرف 
    age = models.IntegerField()
    address = models.ManyToManyField(Address2)#معناتها many to many

    def __str__(self):
        return self.name # اسوي هذا اذا كان في ارتباط بين 2 models
    
    
    #  ملاحظة مهمه لازم الكلاسات تكون في نفس الخط لي الكلاس ولا ما راح تعرف كا كلاس 
    ####################################################
class Profile(models.Model):# هذي المودل عشان اضيف الاسم +الصورة 
    name = models.CharField(max_length=100)#هنا معناتها اعرف حقل (filed )داخل قاعدة البيانات باسم (name )نوع الحقل 
    photo = models.ImageField(upload_to = 'profile_photos/')#هنا استعملنا لي اضافت ملف   FileField or ImageField نوعة صور حقل ميديا 

    def __str__(self):
        return self.name    
    
#class Card1(models.Model):
   # card_number1=models.IntegerField()
  #  def __str__(self):
 #       return str(self.card_number1)

#class Department1(models.Model):
   # name = models.CharField(max_length=100)
  #  def __str__(self):
 #       return self.name# هنا بما انها string نكتبها  كذا 
        
#class Course1(models.Model):
    #title1 = models.CharField(max_length=100)
   # code1 = models.IntegerField()
  #  def __str__(self):
 #       return f"{self.title1} ({self.code1})"
#class Student1(models.Model):
    #name= models.CharField(max_length=100)
    #card1 = models.OneToOneField(Card1, on_delete=models.PROTECT)
    #department1 = models.ForeignKey(Department1, on_delete=models.CASCADE)
   # course1 = models.ManyToManyField(Course1)
    
   
