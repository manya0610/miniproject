# apartments/views.py
from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new
from django.urls import reverse_lazy # new
from .models import Apartment,Building
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin # new
from .forms import ApartmentForm
from django.shortcuts import render

class BuildingListView(LoginRequiredMixin ,ListView):
    model = Building
    template_name = 'building_list.html'

class BuildingDetailView(LoginRequiredMixin ,DetailView): # new
    model = Building
    template_name = 'building_detail.html'
    def get(self,request,pk,*args,**kwargs):
        building=Building.objects.get(pk=pk)
        form=ApartmentForm()
        apartments=Apartment.objects.filter(building=building)
        context={
            'building':building,
            'form':form,
            'apartments':apartments,
        }
        return render(request,'building_detail.html',context)
    def post(self,request,pk,*args,**kwargs):
        building=Building.objects.get(pk=pk)
        form=ApartmentForm(request.POST)
        if form.is_valid():
            new_apartment=form.save(commit=False)
            new_apartment.author=request.user
            new_apartment.building=building
            new_apartment.save()
        apartments=Apartment.objects.filter(building=building)
        context={'building':building,
            'form':form,
            'apartments':apartments,}
        return render(request,'building_detail.html',context)

class BuildingUpdateView(LoginRequiredMixin,UserPassesTestMixin ,UpdateView): # new
    model = Building
    fields = ('name',)
    template_name = 'building_edit.html'
    def test_func(self):
        obj=self.get_object()
        return True

class BuildingDeleteView(LoginRequiredMixin,UserPassesTestMixin ,DeleteView): # new
    model = Building
    template_name = 'building_delete.html'
    success_url = reverse_lazy('building_list')
    def test_func(self): # new
        obj = self.get_object()
        return True

class BuildingCreateView(LoginRequiredMixin ,CreateView):
    model=Building
    template_name='building_new.html'
    fields = ('name',)
    # def form_valid(self, form):
    #     form.instance.author= self.request.user
    #     return super().form_valid(form)

class ApartmentDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Apartment
    template_name="apartment_delete.html"
    success_url = reverse_lazy('building_list')
    def test_func(self): # new
        obj = self.get_object()
        if(self.request.user.is_superuser):

            return True
        else:
            return obj.author == self.request.user
