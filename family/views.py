# articles/views.py
from urllib import request
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import FamilyMember, Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # new


class FamilyMemberListView(LoginRequiredMixin ,ListView):
    model = FamilyMember
    template_name = 'familymember_list.html'

class FamilyMemberDetailView(LoginRequiredMixin ,DetailView): # new
    model = FamilyMember
    template_name = 'familymember_detail.html'

class FamilyMemberUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView): # new
    model = FamilyMember
    fields = ('name','age','birthdate','phonenumber')
    template_name = 'familymember_edit.html'
    def test_func(self):
        obj=self.get_object()
        return obj.relatedto==self.request.user or self.request.user.is_superuser 

class FamilyMemberDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView): # new
    model = FamilyMember
    template_name = 'familymember_delete.html'
    success_url = reverse_lazy('familymember_list')
    def test_func(self): # new
        obj = self.get_object()
        return obj.relatedto == self.request.user or self.request.user.is_superuser 

class FamilyMemberCreateView(LoginRequiredMixin ,CreateView):
    model=FamilyMember
    template_name='familymember_new.html'
    fields = ('name','age','birthdate','phonenumber')
    def form_valid(self, form):
        form.instance.relatedto= self.request.user
        return super().form_valid(form)