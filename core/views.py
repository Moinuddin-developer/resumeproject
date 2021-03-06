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
  return render(request, 'core/language_skill.html', context)

def academic(request):
  context = {'academic': 'active'}
  return render(request, 'core/accadmic_skill.html', context)

def project(request):
  context = {'project': 'active'}
  return render(request, 'core/project.html', context)

def softskill(request):
  context = {'softskill': 'active'}
  return render(request, 'core/softskill.html', context)

def status(request):
  context = {'status': 'active'}
  return render(request, 'core/mystatus.html', context)

def ProcVacc(request):
  return render(request, 'Project/Covid19Vacci.html')

def Procodeath(request):
  return render(request, 'Project/Covid19Death.html')

def hotelrevenue(request):
  return render(request, 'Project/HotelRevenue.html')

def aireline(request):
  return render(request, 'Project/aireline.html')