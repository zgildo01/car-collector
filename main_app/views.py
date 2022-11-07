from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Mod
from .forms import ServicingForm
from django.views.generic import ListView, DetailView

# Define the home view
class CarCreate(CreateView):
  model = Car
  fields = '__all__'
  success_url = '/cars/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all()
  return render(request, 'cars/index.html', { 'cars': cars })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  servicing_form = ServicingForm()
  return render(request, 'cars/detail.html', {
    'car': car,
    'servicing_form': servicing_form
  })

class CarUpdate(UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars/'

def add_servicing(request, car_id):
  form = ServicingForm(request.POST)
  if form.is_valid():
    new_servicing = form.save(commit=False)
    new_servicing.car_id = car_id
    new_servicing.save()
  return redirect('cars_detail', car_id=car_id)

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'

class ModList(ListView):
  model = Mod

class ModDetail(DetailView):
  model = Mod

class ModUpdate(UpdateView):
  model = Mod
  fields = '__all__'

class ModDelete(DeleteView):
  model = Mod
  success_url = '/mods/'