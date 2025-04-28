from django.contrib import admin 
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting', views.formatting, name="books.formatting"),
    path('html5/text/listing', views.listing, name="books.listing"),
    path('html5/text/tables',views.tables, name="books.tables"),
    path('html5/text/search',views.search, name="books.search"),
    path('simple/query',views.simple_query),
    path('complex_query',views.complex_query),
    path('lab8/task1/',views.task1),
    path('lab8/task2/',views.task2),
    path('lab8/task3/',views.task3),
    path('lab8/task4/',views.task4),
    path('lab8/task5/',views.task5),
    path('lab8/task7/',views.task7),
    path('lab9/task1lab9/',views.task1lab9),
    path('lab9/task2lab9/',views.task2lab9),
    path('lab9/task3lab9/',views.task3lab9),
    path('lab9/task4lab9/',views.task4lab9),
    #################### part1 lab 10 
    path('lab9_part1/listbooks/',views.listbooks,name="list_books"),
    path('lab9_part1/addbooks/',views.addbooks,name="add_book"),
    path('lab9_part1/editbook/<int:id>',views.editbook,name="edit_book"),
    path('lab9_part1/deletebook/<int:id>',views.deletebook,name="delete_book"),#ليش حطينا <int:id >لانه راح يعدل علي شي محدد ولي هو id 
    #################### part2 lab 10 
    path('lab9_part2/listbooks2/',views.listbooks2,name="list_books2"),
    path('lab9_part2/addbooks2/',views.addbooks2,name="add_book2"),
    path('lab9_part2/editbook2/<int:id>',views.editbook2,name="edit_book2"),
    path('lab9_part2/deletebook2/<int:id>',views.deletebook2,name="delete_book2"),#ليش حطينا <int:id >لانه راح يعدل علي شي محدد ولي هو id 
    ###################### lab 11 -1 one to many 
    path('lab11/list_student/',views.list_student,name="list_student"),
    path('lab11/add_student/',views.add_student,name="add_student"),
    path('lab11/edit_student/<int:id>',views.edit_student,name="edit_student"),
    path('lab11/delete_student/<int:id>',views.delete_student,name="delete_student"),
    #########################lab 11 -2 many to many 
    path('lab11/list_student2/',views.list_student2,name="list_student2"),
    path('lab11/add_student2/',views.add_student2,name="add_student2"),
    path('lab11/edit_student2/<int:id>',views.edit_student2,name="edit_student2"),
    path('lab11/delete_student2/<int:id>',views.delete_student2,name="delete_student2"),
    ##########################lab 11 -3 هنا اضافة الصور 
     path('list_profiles/',views.list_profiles,name="list_profiles"),
    path('add_profile/',views.add_profile,name="add_profile"),
    path('edit_profile/<int:id>',views.edit_profile,name="edit_profile"),
    path('delete_profile/<int:id>',views.delete_profile,name="delete_profile"),
]

