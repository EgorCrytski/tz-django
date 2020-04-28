from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book, User


def index(request):
    users_list = User.objects.order_by('user_name')
    return render(request, 'library/list.html', {'users_list': users_list})


def user_books(request, user_id):
#try:
    user = User.objects.get(id = user_id)
    book_list = Book.objects.filter(user_id=user_id)
    print(user.user_name+'\n')
    print(book_list)

    #except:
        #raise Http404("User not found")

    return render(request, 'library/userbooks.html', {'books': book_list, 'user': user})


def add_user(request):
    a = User(user_name=request.POST['name'])
    a.save()
    return HttpResponseRedirect(reverse('library:index'))


def add_book(request):
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    user = User.objects.get(id=request.POST['userid'])
    print(user.id)
    a = Book(book_name=request.POST['book_name'], book_author = request.POST['book_author'],
             book_year = request.POST['book_year'], user_id = user)
    print(a.user_id)
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    a.save()
    return HttpResponseRedirect(reverse('library:user_books', args = (user.id,)))


def book(request, book_id):
    a = Book.objects.get(id=book_id)
    pass
