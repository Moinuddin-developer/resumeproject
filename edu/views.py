from django.shortcuts import render

# Create your views here.
def skill(request):
  context = {'skill': 'active'}
  return render(request, 'edu/skill.html', context)

def office(request):
  context = {'office': 'active'}
  return render(request, 'edu/officeSkill.html', context)