from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    posts_list = Post.objects.order_by('-pub_date')
    context = {'posts_list': posts_list}
    return render(request, 'micro/index.html', context)

def send(request):
    try:
        new_post = Post(post_text=request.POST['post'], pub_date=timezone.now())
    except (KeyError, Post.DoesNotExist):
        # обновить
        posts_list = Post.objects.order_by('-pub_date')
        return render(request, 'micro/index.html', {
            'posts_list': posts_list,
            'error_message': "Ошибка",
        })
    else:
       new_post.save() 
       return HttpResponseRedirect('/')