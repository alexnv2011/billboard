from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .filters import ReplyFilter

@login_required
def accept_me(request, pk):
    reply = Reply.objects.get(id=pk)
    reply.accepted = True
    reply.save()
    #  Отправляем письмо
    recipient_list = [reply.user.email]
    send_mail(
        subject=f'Ваш отклик принят на сайте!',
        message='Краткое содержание отклика: ' + reply.text[0:200] + '\n' + f'Перейти на сайт: http://127.0.0.1:8000',
        from_email='info@vikingservice72.ru',
        recipient_list=recipient_list
    )
    return redirect('replies')


class PostsList(ListView):
    model = Post
    ordering = '-time_create'
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.all()


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_data'

    def post(self, request, pk):
        current_user = request.user
        print(str(request.user))
        post = Post.objects.get(pk=pk)
        print(str(pk))
        if request.POST['text']:
            reply = Reply(text=request.POST['text'], user=current_user, post=post)
            reply.save()

        else:
            raise ValidationError({
                "text": "Текст не может быть пустым."
            })
        return redirect('/')


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = reverse_lazy('posts')


class PostEdit(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'
    context_object_name = 'post_data'
    # extra_context = {'post_type': 'news',
    #                  'current_time': timezone.now(),
    #                  'timezones': pytz.common_timezones
    #                  }
    success_url = reverse_lazy('posts')


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')


class RepliesList(LoginRequiredMixin, ListView):
    model = Reply
    ordering = '-time_create'
    template_name = 'replies.html'
    context_object_name = 'replies'

    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        queryset = queryset.filter(post__author__id=self.request.user.id)
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict,
        # Сохраняем нашу фильтрацию в объекте класса, чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = ReplyFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


class ReplyCreate(LoginRequiredMixin, CreateView):
    form_class = ReplyForm
    model = Reply
    template_name = 'reply_create.html'
    success_url = reverse_lazy('replies')


class ReplyDelete(LoginRequiredMixin, DeleteView):
    model = Reply
    template_name = 'reply_delete.html'
    success_url = reverse_lazy('replies')

