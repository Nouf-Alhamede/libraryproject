from django.shortcuts import render

from django.http import HttpResponse

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

def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    if targetBook is None:
        return HttpResponse("Book not found", status=404)  # 

    # 
    context = {'book': targetBook}  # 
    return render(request, 'bookmodule/index.html', context)

 


