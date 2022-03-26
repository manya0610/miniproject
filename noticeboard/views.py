# Notices/views.py
from urllib import request
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Notice,Comment
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # new
from .forms import CommentForm
from django.shortcuts import render


class NoticeListView(LoginRequiredMixin ,ListView):
    model = Notice
    template_name = 'notice_list.html'

class NoticeDetailView(LoginRequiredMixin ,DetailView): # new
    model = Notice
    template_name = 'notice_detail.html'
    def get(self,request,pk,*args,**kwargs):
        notice=Notice.objects.get(pk=pk)
        form=CommentForm()
        comments=Comment.objects.filter(notice=notice)
        context={
            'notice':notice,
            'form':form,
            'comments':comments,
        }
        return render(request,'notice_detail.html',context)
    def post(self,request,pk,*args,**kwargs):
        notice=Notice.objects.get(pk=pk)
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.author=request.user
            new_comment.notice=notice
            new_comment.save()
        comments=Comment.objects.filter(notice=notice)
        context={'notice':notice,
            'form':form,
            'comments':comments,}
        return render(request,'notice_detail.html',context)

class NoticeUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView): # new
    model = Notice
    fields = ('title', 'body',)
    template_name = 'notice_edit.html'
    def test_func(self):
        obj=self.get_object()
        if(self.request.user.is_superuser):
            return True
        return obj.author==self.request.user

class NoticeDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView): # new
    model = Notice
    template_name = 'notice_delete.html'
    success_url = reverse_lazy('notice_list')
    def test_func(self): # new
        obj = self.get_object()
        if(self.request.user.is_superuser):
            return True
        return obj.author == self.request.user

class NoticeCreateView(LoginRequiredMixin ,CreateView):
    model=Notice
    template_name='notice_new.html'
    fields = ('title', 'body',)
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Comment
    template_name="comment_delete.html"
    success_url = reverse_lazy('notice_list')
    def test_func(self): # new
        obj = self.get_object()
        if(self.request.user.is_superuser):

            return True
        else:
            return obj.author == self.request.user