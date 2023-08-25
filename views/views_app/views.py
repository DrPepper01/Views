from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.base import ContextMixin, TemplateResponseMixin, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class PostsView(ListView):
    model = Post
    paginate_by = 1
    context_object_name = 'posts'
    # template_name = 'views_app/post_list.html'
    # allow_empty: bool - предотвращает ошибку 404, если записей не существует
    # paginate_by: int - сколько записей будет выводиться на экран
    # context_object_name: str - название массива объектов в контексте

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['posts'] = Post.objects.filter(status='p')
        return context

    # template_name = 'views_app/post_list.html'

    # ContentMixin.get_context_data()
    # TemplateResponseMixin.render_to_response()
    #
    # def get_context_data(self, **kwargs):
    #     return {'posts': Post.objects.filter(status='p')}


class PublishAuthors(TemplateView):
    template_name = 'views_app/base.html'

    def get_context_data(self, **kwargs):
        return {'authors': Author.objects.all()}


class PostsById(DetailView):
    # model с которой мы хотим работать
    model = Post

    # pk_url_kwarg = 'pk'
    # template_name = 'views_app/post_detail.html'
    context_object_name = 'post'




'''
def get_posts(request):
    published_posts = Post.objects.filter(status='p')
    list_of_posts = []
    for post in published_posts:
        list_of_posts.append({
            'title': post.title,
            'author': post.author.name,
            'categories': [category.name for category in post.categories.all()],
            'views': post.views,
            'content': post.content
        })
    # За формирование ответа на самом низком уровне в Django отвечает класс HttpResponse
    # В его конструкторе можно определить такие значения как статус-код нашего ответа, тип данных или HTTP-заголовки
    return HttpResponse(list_of_posts) 
'''

'''
def get_post(request, post_id):
    # функция get_object_or_404 принимает первым аргументом желаемую модель, а затем - значения, по которым нам
    # необходимо доставать наш объект
    post = get_object_or_404(Post, pk=post_id) # Post.objects.get(pk=post_id)
    return HttpResponse(post)


def get_posts(request: HttpRequest):
    # request.GET - словарь с парметрами: передаваемыми при помощи метода GET в запросе
    # request.POST - словарь параметров, но для POST-запроса
    # request.method - по нему можно понять с каким методом пришел запрос
    # request.headers - тут хранятся HTTP заголовки запроса
    # request.body - это "тело" запроса
    published_posts = Post.objects.filter(status='p')
    template = get_template('views_app/post_list.html')
    context = {'posts': published_posts}
    return HttpResponse(template.render(request=request, context=context))
'''
