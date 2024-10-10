from django.shortcuts import render
from main.models import Books
from main.models import Users
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse

@csrf_exempt
def get_books(request):
    books = Books.objects.all()
    return JsonResponse({"status": 200, "data": list(book.to_dict() for book in books)})

@csrf_exempt
def create_book(request):
    req = json.loads(request.body)
    book_name = req["book_name"]
    author_name = req["author_name"]
    publication_year = req["publication_year"]
    price = req["price"]
    
    book = Books.objects.create(book_name=book_name, author_name=author_name, publication_year=publication_year, price=price)
    return JsonResponse({"status": 201, "data": book.to_dict()})

@csrf_exempt
def delete_book(request):
    req= json.loads(request.body)
    id = req["id"]
    
    book = Books.objects.get(id=id)
    book.delete()   
    return JsonResponse({"status":200,"message": "Book deleted successfully!"})

@csrf_exempt
def update_book(request):
    req = json.loads(request.body)
    id = req["id"]
    book = Books.objects.get(id=id)
    
    if "book_name" in req:
        book.book_name = req["book_name"]
    if "author_name" in req:
        book.author_name = req["author_name"] 
    if "publication_year" in req:
        book.publication_year = req["publication_year"]  
    if "price" in req:
        book.price = req["price"]

    book.save() 
    return JsonResponse({"status": 200, "data": book.to_dict()})


@csrf_exempt
def book_by_id(request):
    req=json.loads(request.body)
    id = req["id"]
    
    book = Books.objects.get(id=id)  
    return JsonResponse({"status":200, "data": book.to_dict()})
    
    
@csrf_exempt
def filter_book(request):
    req = json.loads(request.body)
    
    if "id" in req:
        id = req["id"]
        books = Books.objects.filter(id=id)

    elif "book_name" in req:
        book_name = req["book_name"]
        books = Books.objects.filter(book_name=book_name)
        
    elif "author_name" in req:
        author_name = req["author_name"]
        books = Books.objects.filter(author_name=author_name)
        
    elif "price" in req:
        lb = req["price"]["lb"]
        ub = req["price"]["ub"]
        books = Books.objects.filter(price__range=(lb, ub))
    
    return JsonResponse({"status": 200, "data": list(book.to_dict() for book in books)})


@csrf_exempt
def create_user(request):
    req= json.loads(request.body)
    User_name = req["User_name"]
    user_id = req["user_id"]
    user_phone_no = req["user_phone_no"]
    user = Users.objects.create(User_name=User_name, user_id=user_id, user_phone_no=user_phone_no)
    
    return JsonResponse({"status": 201, "data": user.user_dict()})

@csrf_exempt
def get_all_users(request):
    users = Users.objects.all()
    return JsonResponse({"status": 200, "data": list(user.user_dict() for user in users)})

@csrf_exempt
def user_details(request):
    req = json.loads(request.body)
    if "User_name" in req:
        User_name = req["User_name"]
        users = Users.objects.filter(User_name=User_name)
      
    elif "user_id" in req:
        user_id = req["user_id"]
        users = Users.objects.filter(user_id=user_id)
      
    elif "user_phone_no" in req:
        user_phone_no = req["user_phone_no"]
        users = Users.objects.filter(user_phone_no=user_phone_no)
    
    return JsonResponse({"status": 200, "data": list(user.user_dict() for user in users)})

@csrf_exempt
def update_user(request):
    req = json.loads(request.body)
    user_id = req["user_id"]
    
    user = Users.objects.get(user_id=user_id)
    
    if "User_name" in req:
        user.User_name = req["User_name"]
    elif "user_phone_no" in req:
        user.user_phone_no = req["user_phone_no"]
    
    user.save()
    return JsonResponse({"status": 200, "data": user.user_dict()})

@csrf_exempt
def delete_user(request):
    req = json.loads(request.body)
    user_id = req["user_id"]
    user = Users.objects.get(user_id=user_id)
    user.delete()
    
    return JsonResponse({"status": 200, "message": "User deleted successfully!"})
