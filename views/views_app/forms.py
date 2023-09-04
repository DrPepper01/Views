from django import forms
from .models import Author, Post, Category
from django.forms import modelform_factory
from django.contrib.auth.models import User


author_form = modelform_factory(Author, fields='__all__')


class PostForm(forms.ModelForm):

    class Meta:
        # обязательные
        model = Post
        fields = '__all__'
        #exclude = ['views']
        labels = {'title': 'Название текста', 'content': 'Содержание текста'}
        help_text = {'title': 'Введите название поста'}
        widgets = {'authors': forms.widgets.Select(attrs={'size': 2})}


class PostFormAlt(forms.ModelForm):

    title = forms.CharField(label='Название поста')
    content = forms.CharField(label='Содержание поста', widget=forms.widgets.Textarea())
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label='Автор', help_text='Выберите категории',
                                    widget=forms.widgets.Select(attrs={'size': 2})) # <select size=2></select>
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Категории',
                                                widget=forms.widgets.SelectMultiple(attrs={'size': 2}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'categories', 'views', 'status']


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label='Пароль', widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.widgets.PasswordInput())
    my_site = forms.URLField(min_length=1, max_length=100)
    regex_field = forms.RegexField('^[a-zA-Z]{4}$')
    is_client = forms.BooleanField()
    decided_to_join = forms.NullBooleanField()
    number_of_goods = forms.IntegerField()
    rate = forms.FloatField()
    balance = forms.DecimalField(max_digits=10, decimal_places=2)
    choice = forms.ChoiceField(choices=(('f', 'first'), ('s', 'second',)))
    choice2 = forms.MultipleChoiceField (choices=(('f', 'first'), ('s', 'second',)))

    # label: str, который будет отображаться в хтмл-форме
    # help_text: str, который будет отображаться рядом с полем
    # initial: Any значение: которое будет вводится в форму по умолчанию
    # required: bool True
    # widget: Any класс : который мы передаем для того чтобы указать джанго, какой хтмл-таг использовать
    # validator: list

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class SimpleForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'


class AuthorForm(forms.ModelForm):

    class Meta:
        model = Author
        fields = '__all__'












