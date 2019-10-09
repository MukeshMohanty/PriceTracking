from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'user': 'Jon',
        'product': 'Perfume',
        'url': 'https://amazon.com/perfume',
        'date_posted': 'August 27, 2019'
    }
]


def home(request):
    context = {
        'posts': Post.objects.all(),
        'title': 'Amazon'
    }
    return render(request, 'user/home.html', context)
