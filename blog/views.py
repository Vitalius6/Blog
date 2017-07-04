from models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect, Http404
from blog.forms import CommentForm, AddPostForm

class HomePageView(TemplateView):

    template_name = "home.html"


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'


class DetailPost(DetailView):
    model = Post
    template_name = 'detail_post.html'


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'create_post.html'

    def get_initial(self):
        self.initial.update({ 'author': self.request.user })
        return self.initial

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect('/')


class EditPost(UpdateView):
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'context']
    success_url = '/'


class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = '/'


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")


class AddComment(CreateView):
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = '/'

    def get_initial(self):
        self.initial.update({ 'author': self.request.user })
        return self.initial

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return HttpResponseRedirect('/')