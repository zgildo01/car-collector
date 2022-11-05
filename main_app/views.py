from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Car

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
  return render(request, 'cars/detail.html', { 'car': car })

