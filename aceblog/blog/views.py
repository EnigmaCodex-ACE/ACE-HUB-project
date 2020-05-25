from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post,Comment
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from users.models import Profile

def home(request):
    context = {
        'posts': Post.objects.all() ,
        'title':"ACE Students",
        'user':User.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False


class UserPostListView(ListView):
    model = Profile
    template_name = 'blog/user_profile.html'
    allow_empty = False  #this will show 404 if the username does not exists

    def get(self,request,*args, **kwargs):
        username = self.kwargs['username']
        user_profile = User.objects.get(username=username)
        return render(request,'blog/user_profile.html',{'user_profile':user_profile,
                                                        'name':username})
    

def about(request):
    return render(request,'blog/about.html',{'title':"An About Page"})

