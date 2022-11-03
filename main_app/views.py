from django.shortcuts import render

# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Car:  # Note that parens are optional if not inheriting from another class
  def __init__(self, make, model, quote, year):
    self.make = make
    self.model = model
    self.quote = quote
    self.year = year

cars = [
  Car('Vector', 'WX8 Hypercar', 'The Car of the Future.', 2007),
  Car('Rolls-Royce', 'Phantom', '0-60 in 5.5 seconds.', 2022),
  Car('Cadillac', 'CT-5', 'Take the next step.', 2023),
  Car('Nissan', '350Z', 'Part of a long family tree', 2006)
]

# Define the home view
def home(request):
  return HttpResponse('<h1>Car Time</h1>')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', {'cars': cars})