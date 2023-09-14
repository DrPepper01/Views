from django.http import HttpResponse, HttpResponseNotFound, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest, \
    request
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import get_template
from django.views import View
from django.views.generic.base import ContextMixin, TemplateResponseMixin, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.apps import apps
from django.contrib.auth.models import User

from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin

from . import forms
from ..accounts.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('main_page')
    template_name = 'accounts/signup.html'


class CreateCategoryView(UserPassesTestMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'views_app/form_category.html'
    success_url = '/category/'

    def test_func(self):
        return self.request.user.is_superuser


class DeleteCategoryView(PermissionRequiredMixin, DeleteView):
    model = Category
    fields = '__all__'
    template_name = 'views_app/form_category.html'
    success_url = '/category/'
    permission_required = 'views_app.delete_category'


class UpdateCategoryView(UpdateView):
    model = Category
    fields = '__all__'  # ['name', 'bio']
    success_url = '/category/{id}/detail'
    template_name = 'views_app/form_category.html'
    context_object_name = 'form_category'
    # pk_url_kwarg = 'pk'  # default


class CategoryList(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'views_app/category_list.html'


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'views_app/category_detail.html'


# 31.08 Create View функционал
class CreateAutorView(LoginRequiredMixin, CreateView):  # modelFormMixin
    model = Author
    fields = '__all__'
    template_name = 'views_app/form.html'
    success_url = '/authors/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание автора'
        return context


class DeleteAuthorViews(PermissionRequiredMixin, DeleteView):
    model = Author
    template_name = 'views_app/form.html'
    success_url = '/authors/'
    permission_required = 'views_app.delete_author'


class UpdateAuthorView(UpdateView):
    model = Author
    fields = '__all__'  # ['name', 'bio']
    success_url = '/authors/{id}'
    template_name = 'views_app/form.html'
    context_object_name = 'form'
    pk_url_kwarg = 'pk'  # default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Обновить автора'
        context['update_text'] = True
        context['action'] = 'обновить'
        context['model'] = str(self.model)
        return context


class AuthorList(LoginRequiredMixin, ListView):
    model = Author
    context_object_name = 'authors'
    paginate_by = 2


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'


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


#-------------------------------------------------------


class CreatePostView(CreateView): # modelformmixin
    model = Post
    form_class = forms.PostFormAlt
    template_name = 'views_app/form.html'
    success_url = '/posts/{id}'


class DeletePostView(UserPassesTestMixin, DeleteView):
    # login_url = 'accounts/login/'
    # redirect_field_name = 'next'
    model = Post
    template_name = 'views_app/form.html'
    success_url = '/posts/'

    def test_func(self):
        return self.request.user == self.get_object().author.user or self.request.user.is_superuser


class UpdatePostView(UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'author', 'content', 'categories', 'status']
    success_url = '/posts/{id}'
    template_name = 'views_app/form.html'

    def test_func(self):
        return self.request.user == self.get_object().author.user


class PostList(ListView):
    model = Post
    context_object_name = 'posts' # Author.objects.all()


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class MainPage(TemplateView):
    template_name = 'views_app/main_page.html'

    def get_context_data(self, **kwargs):

        context = {}
        context['range'] = [i for i in range(10, 20)]
        context['first_condition'] = True
        context['second_condition'] = False
        return context


def paginator_view(request: HttpRequest):
    authors = Author.objects.all()
    paginator = Paginator(authors, 2) # authors/?page=1
    paginator.orphans = 2
    if 'page' in request.GET: # request.GET = {'page': 1}
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'authors': page.object_list, 'page': page}
    return render(request, 'views_app/authors_paginator.html', context)


#-------------------------------------------------------


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


class UserRegistrationView(FormView):
    template_name = 'views_app/form.html'
    form_class = forms.UserRegistrationForm

    def form_valid(self, form):
        return HttpResponse('form valid')

    def form_invalid(self, form):
        return HttpResponse('form invalid')


def add_record(requset: HttpRequest):
    if requset.method == 'POST':
        form = forms.SimpleForm(requset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category_list'))
    elif requset.method == 'GET':
        form = forms.SimpleForm
        context = {'form': form}
        return render(requset, 'views_app/form.html', context)
    else:
        return HttpResponseBadRequest()


def update_category(request: HttpRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    # try:
    #     category = Category.objects.get(pk=pk) # Category.DoesNotExist
    # except Category.DoesNotExist:
    #     return HttpResponseBadRequest()
    if request.method == 'POST':
        form = forms.SimpleForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category_detail', kwargs={'pk': pk}))
        else:
            return HttpResponseBadRequest()
    elif request.method == 'GET':
        form = forms.SimpleForm(instance=category)  # initial
        context = {'form': form}
        return render(request, 'views_app/form.html', context)
    else:
        return HttpResponseBadRequest


def add_author(request: HttpRequest, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        form = forms.AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author_detail', kwargs={'pk': pk}))
        else:
            return HttpResponseBadRequest()
    elif request.method == 'GET':
        form = forms.AuthorForm(instance=author)
        context = {'form': form}
        return render(request, 'views_app/form.html', context)


def add_author2(requset: HttpRequest):
    if requset.method == 'POST':
        form = forms.AuthorForm(requset.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author_list'))
    elif requset.method == 'GET':
        form = forms.AuthorForm
        context = {'form': form}
        return render(requset, 'views_app/form.html', context)
    else:
        return HttpResponseBadRequest()


def authors(request):
    if request.method == 'POST':
        formset = forms.Formset(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('author_list')
    else:
        formset = forms.Formset()
        context = {'formset': formset}
        return render(request, 'views_app/authors_formset.html', context)


class CaptchaView(FormView):
    form_class = forms.CaptchaForm
    template_name = 'views_app/form.html'






















