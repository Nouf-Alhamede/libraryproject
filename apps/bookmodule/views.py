from django.shortcuts import render,redirect,get_object_or_404

from django.db.models import Q # هذي اضفتها عشان advanced models عشان استعين فيها لي وضع عددت شروط في خطا واحد واستعمل Qكا ابجكت 
from django.http import HttpResponse
from .models import Book, Address, Student,Card,Department,Course , Address2, Student2 ,Profile #لازم اضيف الموديل هنا الي هو الكلاسات الي كتبتهم 

from django.db.models import Count, Min, Max, Sum, Avg #هذي مهمه لما استعمل aggregatoin عشان تحسب لي اصغر واكبر ومتوسط وغيرها مهمه 

from .forms import BookForm,StudentForm,StudentForm2 ,ProfileForm

def index(request):
    name = request.GET.get("name") or "world!"  
    return render(request, "bookmodule/index.html", {"name": name})

# 
def index2(request, val1):
    return render(request,"bookmodule/index.html", {"name": f"Value is {val1}"})
  
def index(request):
    return render(request,"bookmodule/index.html")
 
def list_books(request):
    return render(request,'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request,'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request,'bookmodule/aboutus.html')
 
def links (request):
    return render (request,'bookmodule/links.html')#هذي داله توجه لي الصفحة links عند الطلب 

def formatting (request):
    return render (request,'bookmodule/formatting.html')#هذي داله توجه لي الصفحة links عند الطلب 

def listing (request):
    return render (request,'bookmodule/listing.html')#هذي داله توجه لي الصفحة links عند الطلب 

def tables(request):
    return render(request,'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})
    return render(request, 'bookmodule/search.html', {'books': []})
 
def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).filter(price__gte = 100)[:10]
    #filter تسوي لي فلتر لي بين القوسين الي اذا كان اكبر او اضعر او اكبر يسوي او اضغر يساوي الي هم gte,gt,it,its ,icontains معناتها تحتوي على احرف and وعندنا عكس الفلتر الي هي exclude معناتها اذا انا ابغى يجب لي اكبر سعر فانه في تفيذها راج تجب العكس الي هو الاصغر 
    #[:10]يعني يبحث من 0 الي 10 اما 
    #[10:] يبداء البحث من 10 الى ما ينتهي 
    if len(mybooks)>=1:
        #هنا عشان تقرا لي النواتج بحيث اذا كان طول البيانات الي في mybook = book اكبر او تساوي 1 يعطيني السطر الاول اذا لا يروح لي elss صفحة اخرى
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
def task1(request):
    books = Book.objects.filter(Q(price__lte = 100))
    return render(request, 'bookmodule/bookList.html', {'books':books})
#طيب، ليه نستخدم Q؟لأننا نبغى نستخدم شروط معقدة فيها AND و OR مع بعض.في Django، إذا حاولت تكتب OR أو AND بدون Q، ما راح تضبط.Q تسمح لك تكتب تعبيرات منطقية مثل:Q(...) & Q(...) = شرط AND.Q(...) | Q(...) = شرط OR.~Q(...) = نفي الشرط.
#هنا نبغى نسوي فلتر بستعمال ابجكت Q عشان تودين الي الموديل واحط شرط اذا كان السعر اصغر او يساوي 100 رجع لي صفحة booklist 
def task2(request):
    books = Book.objects.filter(Q(edition__gt = 2) & (Q(title__icontains = 'a') | Q(author__icontains ='a')))
    return render(request, 'bookmodule/bookList.html', {'books':books})
#هنا استعمل اكثر من شرط بستخدام and & or | اسعملنا Q مع الشروط المعقدة 
#معنات {'books':books}

def task3(request):
    books = Book.objects.filter(~Q(edition__gt = 2) & (~Q(title__icontains = 'qu') | ~Q(author__icontains ='qu')))
    return render(request, 'bookmodule/bookList.html', {'books':books})
#استعملنا الشروط مع ~Q تعني نفي لا تساي لا تحتوي اذا قال اكبر مناتها اصغر 
#أرسلي المتغير books إلى القالب باسم books".
def task4(request):
    books = Book.objects.order_by('title')# order by تعني ترتيب 
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task5(request):
    quary = Book.objects.aggregate(
        count=Count('id'),
        total_price =Sum('price'),
        average_price=Avg('price'),
        min_price=Min('price'),
        max_price=Max('price')
    )
    print(quary)
    return render(request, 'bookmodule/task5.html', {'quary':quary})
#aggregate  معناتها ان استعمل اصغر واكبر ومعدل كلهم لي السعر وجمع 

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    #معنا annotate  يعني كل مدينة/عنوان يرجع معاه كم طالب مرتبط فيه 
    return render(request, 'bookmodule/task7.html', {'cities':cities})

def task1lab9(request):
    departments = Department.objects.annotate(student_count=Count('student'))# department متغير جديد ثمن = Department اسم الموديل 
    #ثمن احط ابجكت واحط annotate عشان تحسب لي كم عدد الطلاب المسجلين في هذا القسم student_count متغر استعملة في ملف html
    return render(request, 'bookmodule/department.html', {'departments': departments})
   #هنا يبغى يعرض لي كم طالب مسجل في كل قسم 

def task2lab9(request):
    course = Course.objects.annotate(student_count=Count('student'))#student نفس اسم الكلاس الطلاب الي موجود في الموديل 
    return render(request, 'bookmodule/course.html', {'course': course})
#هنا ابغى اعرض كم طالب مسجل في هذي المادة 

def task3lab9(request):#هنا الفكرة اني اظهر اسم اكبر طالب في كل قسم ومعناتها او الي له اصغر ID جامعي 
    departments = Department.objects.annotate(oldest_student_id=Min('student__id'))
    #هنا ابغى department= سجلي اوبجكت اسمه Department وخلي فيه ابجكت ثاني oldest_student_id وخليه يشير الي اصغر طالب من حيث student__id 
    department_data = [] #اضيف list راح يكون فيها اسم القسم +اسم اكبر طالب 

    for department in departments:#احط for عشان تدور على كل الاقسام 
       # if department.oldest_student_id is not None:# اذا كانت القسم الي في اكبر طالب مب فارغ 
            oldest_student = department.student_set.get(id=department.oldest_student_id)
            department_data.append(
                {
                    'department_name': department.name,
                    'oldest_student_name': oldest_student.name
                }
            )

    return render(request, 'bookmodule/task3.html', {'department_data': department_data})

def task4lab9(request):#اعرض لي القسم الي عنده اكثر من 2 student بستعمل by order 
    departments = ( Department.objects.annotate(student_count=Count('student'))
        .filter(student_count__gt=2)#هنا سوينا فلتر لي لي الابجكت الي يعد الطلاب ونطلع اكبر من الي هي gt =2 
        .order_by('student_count')#هنا خليته يرتبها 
    )

    return render(request, 'bookmodule/task4.html', {'departments': departments})

#################################################part1 lab10
def listbooks(request):
    books = Book.objects.all()#عشان يعرض لي كل الكتوب 
    return render(request, 'bookmodule/lab9_listbook.html',{'books':books})

def addbooks(request):# اضيف كتاب 
    if request.method =="POST":#اذا دخل اليوز معلومات 
        Book.objects.create(#ليش create لاني ابغى اضيف كتاب جديد 
            title=request.POST['title'],
            author=request.POST['author'])
        return redirect('list_books')#ابغى اذا عدل يرجع لهذي الصفحة 
    return render(request,'bookmodule/lab9_addbook.html')

def editbook(request, id ):#اعدل كتاب على شي محدد فا لازم احط id 
    book = get_object_or_404(Book,id=id)#هنا اذا وجد الكتاب يرجع book  واذا لا يرجع 404 الخطاء تلقائي 
    #هنا كانه يخذ كتاب معين ويعدل عليه طيب ليش get_object لان راح ياخذها من نفس الصفحة او 404 الخطاء 
    # هنا فقط عدل كاني قلت له شفت المتغر book سويت له get من نفس id حق الكتاب 
    if request.method =="POST":#ثمن خليته يعدل عليها هنا 
        book.title = request.POST['title']#اخذ الجديدات الي سويتهم وحطهم في book.title الي انا اخذتها سويت لها get 
        book.author = request.POST['author']#نفس الي فوق بس book.author
        book.save()#اذا عدل اسوي حفظ 
        return redirect('list_books')#اذا عدل يرجع لي لي الصفحة الرئسية 
    return render(request,'bookmodule/lab9_editbook.html',{'book':book})#اضيف متغير book

def deletebook(request,id):#احذف كتاب 
   book = get_object_or_404(Book,id=id)#نفس شرح edit 
   book.delete()#اسوي حذف فقط 
   return redirect('list_books')#اذا حذف يرجع لي لي الصفحة الرئسية 

#################################################part2 lab10
def listbooks2(request):
    books = Book.objects.all()#عشان يعرض لي كل الكتوب 
    return render(request, 'bookmodule/lab9_listbook2.html',{'books':books})

def addbooks2(request):# اضيف كتاب 
    if request.method =="POST":# اذا دخل اليوز معلومات سو طلب اضغط 
        form = BookForm(request.POST)# الطلب الي جاء راح يكون داخل المتغير راح ياخذ بس الطلب form
        if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
            form.save()
            return redirect('list_books2')#ابغى اذا عدل يرجع لهذي الصفحة 
    else:#اذا ما جاء طلب  خل متغير from يساوي bookfrom وارسله المغير لي صفحة 
        form =BookForm()
    return render(request,'bookmodule/lab9_addbook2.html',{'form':form})#راح ارسله لي الصفحة form 

def editbook2(request, id ):#اعدل كتاب على شي محدد فا لازم احط id 
    book = get_object_or_404(Book,id=id) #هنا كانه يخذ كتاب معين ويعدل عليه طيب ليش get_object لان راح ياخذها من نفس الصفحة او 404 الخطاء 
    # هنا فقط عدل كاني قلت له شفت المتغر book سويت له get من نفس id حق الكتاب 
    if request.method =="POST":#ثمن خليته يعدل عليها هنا 
       form = BookForm(request.POST, instance = book)# هنا راح ياخذ الطلب +book instance هو book
       if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
            form.save() 
       return redirect('list_books2')#اذا عدل يرجع لي لي الصفحة الرئسية 
    else:#اذا ما جاء طلب  خل متغير from يساوي bookfrom وارسله المغير لي صفحة 
        form =BookForm(instance = book) #عشان ياخذ نفس الكتاب 
    return render(request,'bookmodule/lab9_editbook2.html',{'form':form})#اضيف متغير book

def deletebook2(request,id):#احذف كتاب 
   book = get_object_or_404(Book,id=id)#نفس شرح edit 
   book.delete()#اسوي حذف فقط 
   return redirect('list_books2')#اذا حذف يرجع لي لي الصفحة الرئسية 
########################################### lab 11

def list_student(request):
    Students = Student.objects.all()#عشان يعرض لي كل الكتوب 
    return render(request, 'bookmodule/list_student.html',{'Students':Students})

def add_student(request):# اضيف كتاب 
    if request.method =="POST":# اذا دخل اليوز معلومات سو طلب اضغط 
        form = StudentForm(request.POST)# الطلب الي جاء راح يكون داخل المتغير راح ياخذ بس الطلب form
        if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
            form.save()
        return redirect('list_student')#ابغى اذا عدل يرجع لهذي الصفحة 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =StudentForm()
    return render(request,'bookmodule/add_student.html',{'form':form})#راح ارسله لي الصفحة form 

def edit_student(request, id ):#اعدل كتاب على شي محدد فا لازم احط id 
    Students = get_object_or_404(Student,id=id) #هنا كانه يخذ كتاب معين ويعدل عليه طيب ليش get_object لان راح ياخذها من نفس الصفحة او 404 الخطاء 
    # هنا فقط عدل كاني قلت له شفت المتغر student سويت له get من نفس id حق الكتاب 
    if request.method =="POST":#ثمن خليته يعدل عليها هنا 
       form = StudentForm(request.POST, instance = Students)# هنا راح ياخذ الطلب +Studrnt instance هو student
       if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
          form.save() 
       return redirect('list_student')#اذا عدل يرجع لي لي الصفحة الرئسية 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =StudentForm(instance = Students) #عشان ياخذ نفس الكتاب 
    return render(request,'bookmodule/edit_student.html',{'form':form})#اضيف متغير book

def delete_student(request,id):#احذف كتاب 
   Students = get_object_or_404(Student,id=id)#نفس شرح edit 
   Students.delete()#اسوي حذف فقط 
   return redirect('list_student')#اذا حذف يرجع لي لي الصفحة الرئسية 
##########################################lab 11 2
def list_student2(request):
    Students = Student2.objects.all()#عشان يعرض لي كلالطلاب 
    return render(request, 'bookmodule/list_student2.html',{'Students':Students})

def add_student2(request):# اضيف كتاب 
    if request.method =="POST":# اذا دخل اليوز معلومات سو طلب اضغط 
        form = StudentForm2(request.POST)# الطلب الي جاء راح يكون داخل المتغير راح ياخذ بس الطلب form
        if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
            form.save()
        return redirect('list_student2')#ابغى اذا عدل يرجع لهذي الصفحة 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =StudentForm2()
    return render(request,'bookmodule/add_student2.html',{'form':form})#راح ارسله لي الصفحة form 

def edit_student2(request, id ):#اعدل كتاب على شي محدد فا لازم احط id 
    Students = get_object_or_404(Student2,id=id) #هنا كانه يخذ كتاب معين ويعدل عليه طيب ليش get_object لان راح ياخذها من نفس الصفحة او 404 الخطاء 
    # هنا فقط عدل كاني قلت له شفت المتغر student سويت له get من نفس id حق الكتاب 
    if request.method =="POST":#ثمن خليته يعدل عليها هنا 
       form = StudentForm2(request.POST, instance = Students)# هنا راح ياخذ الطلب +Studrnt instance هو student
       if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
          form.save() 
       return redirect('list_student2')#اذا عدل يرجع لي لي الصفحة الرئسية 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =StudentForm2(instance = Students) #عشان ياخذ نفس الكتاب 
    return render(request,'bookmodule/edit_student2.html',{'form':form})#اضيف متغير book

def delete_student2(request,id):#احذف كتاب 
   Students = get_object_or_404(Student2,id=id)#نفس شرح edit 
   Students.delete()#اسوي حذف فقط 
   return redirect('list_student2')#اذا حذف يرجع لي لي الصفحة الرئسية 

############################################## lab 11 3
def list_profiles(request):
    Profiles = Profile.objects.all()#عشان يعرض لي كلالطلاب 
    return render(request, 'bookmodule/list_profile.html',{'Profiles':Profiles})

def add_profile(request):# اضيف كتاب 
    if request.method =="POST":# اذا دخل اليوز معلومات سو طلب اضغط 
        form = ProfileForm(request.POST, request.FILES)#الشي المختلف في اضافة الصور هي فقط اضافة request.FILES اضفنا طلب ملف 
        if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
            form.save()
            return redirect('list_profiles')#ابغى اذا عدل يرجع لهذي الصفحة 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =ProfileForm()
    return render(request,'bookmodule/add_profile.html',{'form':form})#راح ارسله لي الصفحة form 

def edit_profile(request, id ):#اعدل كتاب على شي محدد فا لازم احط id 
    Profiles = get_object_or_404(Profile,id=id) #هنا كانه يخذ كتاب معين ويعدل عليه طيب ليش get_object لان راح ياخذها من نفس الصفحة او 404 الخطاء 
    # هنا فقط عدل كاني قلت له شفت المتغر student سويت له get من نفس id حق الكتاب 
    if request.method =="POST":#ثمن خليته يعدل عليها هنا 
       form = ProfileForm(request.POST, request.FILES, instance =Profiles)# هنا راح ياخذ الطلب +Studrnt instance هو student
       if form.is_valid():#تبي تشوف اذا عندي مشكلة او لا 
          form.save() 
       return redirect('list_profiles')#اذا عدل يرجع لي لي الصفحة الرئسية 
    else:#اذا ما جاء طلب  خل متغير from يساوي studentfrom وارسله المغير لي صفحة 
        form =ProfileForm(instance = Profiles) #عشان ياخذ نفس الكتاب 
    return render(request,'bookmodule/edit_profile.html',{'form':form})#اضيف متغير book

def delete_profile(request,id):#احذف كتاب 
   profiles = get_object_or_404(Profile,id=id)#نفس شرح edit 
   profiles.delete()#اسوي حذف فقط 
   return redirect('list_profiles')#اذا حذف يرجع لي لي الصفحة الرئسية 

