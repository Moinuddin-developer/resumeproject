from django.shortcuts import render

# Create your views here.
def home(request):
  context = {'home': 'active'}
  return render(request, 'core/index.html', context)

def contact(request):
  context = {'contact': 'active'}
  return render(request, 'core/contact.html', context)

def qualification(request):
  context = {'qualification': 'active'}
  return render(request, 'core/qualification.html', context)

def language(request):
  context = {'language': 'active'}
  return render(request, 'core/language.html', context)

def project(request):
  context = {'project': 'active'}
  return render(request, 'core/project.html', context)

def softskill(request):
  context = {'softskill': 'active'}
  return render(request, 'core/softskill.html', context)

def emp(request):
  context = {'emp': 'active'}
  return render(request, 'core/emp.html', context)