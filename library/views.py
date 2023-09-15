from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests 
from django.db.models import Count, F, Value, Sum
from .models import *
# Create your views here.

def index(request):
    return render(request,'index.html')


def get_frappe_books(request):
    context={}
    page=request.GET.get('page')
    title=request.GET.get('title')
    isbn=request.GET.get('isbn')
    authors=request.GET.get('authors')
    publisher=request.GET.get('publisher')
    num=request.GET.get('num')
    URL=f'https://frappe.io/api/method/frappe-library?page={page}&title={title}&authors={authors}&isbn={isbn}&publisher={publisher}'
    r = requests.get(url = URL)
    data = r.json()
    print('------response ',data)
    num1=0
    if num=="":
        num=20
    print('----',page)
    print('----',title)
    print('----',authors)
    print('----',isbn)
    print('----',publisher)
    if page!='' or title!='' or authors!='' or isbn!='' or publisher!='':
        print('----insisde')
        for i in data['message']:
            if int(num1)<=int(num):
                Books.objects.create(b_id=i['bookID'],title=i['title'],authors=i['authors'],isbn=i['isbn'],publication_date=i['publication_date'],language_code=i['language_code'])
                num1=num1+1
    else:
        print('----iouttsidensisde')
        context['msg']='Please enter one of any field.'
        books=Books.objects.all()
    context['books']=books
    return render(request,'books.html',context)
    return HttpResponse('Hello')


def books_list(request):
    context={}

    books=Books.objects.all()
    context['books']=books
    return render(request,'books.html',context)


def books_view(request,id):
    context={}

    books=Books.objects.get(id=id)
    context['books']=books
    return render(request,'book_issue.html',context)

def book_issue(request):
    context={}
    books=Books.objects.all()
    mem=Members.objects.all()
    context['books']=books
    context['members']=mem
    if request.method=='POST':
        books=request.POST.get('books')
        member=request.POST.get('member')
        amount=request.POST.get('amount')
        mm=Transactions.objects.filter(id=member,return_date__isnull=True).aggregate(Sum('amount'))
        # print('------',mm['amount__sum'])
        if mm['amount__sum']:
            total_amount=int(mm['amount__sum'])+int(amount)
            if total_amount<=500:
            
                transactions=Transactions.objects.create(books_id=books,amount=amount,
                members_id=member)
            else:
                context['msg']='Sorry! Your outstanding is reached 500Rs'
                return render(request,'book_issue.html',context)        
        else:
            transactions=Transactions.objects.create(books_id=books,amount=amount,
                members_id=member)
        return redirect('issued_Books')
    return render(request,'book_issue.html',context)

def book_issue_submit(request,id):
    
    date=request.GET.get('date')
    print('-----daaa',date)
    Transactions.objects.filter(id=id).update(return_date=date)
    return redirect('issued_Books')



def Issued_Books(request):
    context={}

    transactions=Transactions.objects.filter(return_date__isnull=True)
    context['transactions']=transactions
    return render(request,'history.html',context)

def history(request):
    transactions=Transactions.objects.all()
    context={'transactions':transactions}
    return render(request,'history.html',context)

def all_members(request):
    members=Members.objects.all()
    context={'members':members}

    if request.method=='POST':
        name=request.POST.get('name')
        print(name)
        members=Members.objects.create(name=name)
        
    return render(request,'all_members.html',context)
    