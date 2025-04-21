from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm
from django.shortcuts import get_object_or_404
from .models import Tag

# Create your views here.
class PostView(View):
    '''Вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'main/index.html', {'post_list': posts})
def index(request):
    return render(request, 'main/index.html')
    tags = Tag.objects.all()
    return render(request, 'main/index.html', {'tags': tags})

def about(request):
    return render(request, 'main/about.html')

class PostDetail(View):
    '''отдельная страница записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, 'main/blog_detail.html', {'post': post})

class AddComments(View):
    '''этот класс отвечает за добавление комментариев к посту'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

'''так как нам нужны только лайки от индивидуальных пользователей,
 мы будем смотреть на ip адрес'''
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}')
        # Если будет ошибка, то мы создаем новый лайк
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}')

class DelLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}')
        except:
            return redirect(f'/{pk}')

def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag).order_by('-date')
    return render(request, 'main/index.html', {
        'post_list': posts,
        'current_tag': tag
    })