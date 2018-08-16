from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.urls import reverse_lazy
from .models import *

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkCV(LoginRequiredMixin,CreateView):
    model = Bookmark
    template_name_suffix = '_create'
    fields = ['site_name', 'url']
    success_url = reverse_lazy('bookmark:index')
    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form': form})

class BookmarkUV(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDetailV(LoginRequiredMixin, DetailView):
    model = Bookmark

class BookmarkDeleteV(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')