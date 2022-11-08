from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car, Mod
from .forms import ServicingForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Define the home view
class CarCreate(LoginRequiredMixin, CreateView):
  model = Car
  fields = ['make', 'model', 'year', 'quote', 'mods']
  success_url = '/cars/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def cars_index(request):
  cars = Car.objects.filter(user=request.user)
  return render(request, 'cars/index.html', { 'cars': cars })

@login_required
def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  mods_car_doesnt_have = Mod.objects.exclude(id__in = car.mods.all().values_list('id'))
  servicing_form = ServicingForm()
  return render(request, 'cars/detail.html', {
    'car': car,
    'servicing_form': servicing_form,
    'mods': mods_car_doesnt_have
  })

class CarUpdate(LoginRequiredMixin, UpdateView):
  model = Car
  fields = '__all__'

class CarDelete(LoginRequiredMixin, DeleteView):
  model = Car
  success_url = '/cars/'

@login_required
def add_servicing(request, car_id):
  form = ServicingForm(request.POST)
  if form.is_valid():
    new_servicing = form.save(commit=False)
    new_servicing.car_id = car_id
    new_servicing.save()
  return redirect('cars_detail', car_id=car_id)

class ModCreate(LoginRequiredMixin, CreateView):
  model = Mod
  fields = '__all__'

class ModList(LoginRequiredMixin, ListView):
  model = Mod

class ModDetail(LoginRequiredMixin, DetailView):
  model = Mod

class ModUpdate(LoginRequiredMixin, UpdateView):
  model = Mod
  fields = '__all__'

class ModDelete(LoginRequiredMixin, DeleteView):
  model = Mod
  success_url = '/mods/'

@login_required
def assoc_mod(request, car_id, mod_id):
  Car.objects.get(id=car_id).mods.add(mod_id)
  return redirect('cars_detail', car_id=car_id)

@login_required
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('cats_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)