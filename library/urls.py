from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name='library'),
    path('get_frappe_books/',views.get_frappe_books,name='get_frappe_books'),  
    path('books_list/',views.books_list,name='books_list'),  
    path('issued_Books/',views.Issued_Books,name='issued_Books'),  
    path('book_issue/',views.book_issue,name='book_issue'),  
    path('book_issue_submit/<int:id>/',views.book_issue_submit,name='book_issue_submit'),  
    path('all_members/',views.all_members,name='all_members'),  
    path('history/',views.history,name='history'),  
    # path('book_issue_submit/<int:id>/',views.book_issue_submit,name='book_issue_submit'),  

]
