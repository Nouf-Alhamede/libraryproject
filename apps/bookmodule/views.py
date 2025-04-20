from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q

from .models import Book, Address, Student,Card,Department,Course

from django.db.models import Count, Min, Max, Sum, Avg

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
 


def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
def task1(request):
    books = Book.objects.filter(Q(price__lte = 100))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task2(request):
    books = Book.objects.filter(Q(edition__gt = 2) & (Q(title__icontains = 'a') | Q(author__icontains ='a')))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task3(request):
    books = Book.objects.filter(~Q(edition__gt = 2) & (~Q(title__icontains = 'qu') | ~Q(author__icontains ='qu')))
    return render(request, 'bookmodule/bookList.html', {'books':books})

def task4(request):
    books = Book.objects.order_by('title')
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

def task7(request):
    cities = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/task7.html', {'cities':cities})

def task1(request):
    departments = Department.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/department.html', {'departments': departments})

def task2(request):
    course = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/course.html', {'course': course})

def task3(request):
    departments = Department.objects.annotate(oldest_student_id=Min('student__id'))
    
    department_data = []

    for department in departments:
        if department.oldest_student_id is not None:
            oldest_student = department.student_set.get(id=department.oldest_student_id)
            department_data.append(
                {
                    'department_name': department.name,
                    'oldest_student_name': oldest_student.name
                }
            )

    return render(request, 'bookmodule/task3.html', {'department_data': department_data})

def task4(request):
    departments = (
        Department.objects
        .annotate(student_count=Count('student'))
        .filter(student_count__gt=2)
        .order_by('student_count')
    )

    return render(request, 'bookmodule/task4.html', {'departments': departments})
