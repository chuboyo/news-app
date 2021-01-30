from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # should be above create view to be read first
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin, ListView):
   model = Article
   template_name = 'articles_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
   model = Article
   template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
   model = Article
   template_name = 'article_update.html'
   fields = ('title', 'body',)

   def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
   model = Article
   template_name = 'article_delete.html'
   success_url = reverse_lazy('articles_list')

   def test_func(self):
      obj = self.get_object()
      return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView): #the mixin should be to the left of createview to be read first
   model = Article
   template_name = 'article_new.html'
   fields = ('title', 'body',) #author field was removed and the create view was customized.

   def form_valid(self, form): 
      form.instance.author = self.request.user
      return super().form_valid(form)