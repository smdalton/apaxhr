
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse

from users.forms import EmployeeCreationForm

# Create your views here.
from users.models import Employee


class UserCreatView(CreateView):
    model = Employee
    form_class = EmployeeCreationForm
    template_name = 'users/user-creation.html'
    def get_success_url(self):
        return reverse('core-hr:landing')
#
# def register(request):
#     if request.method == 'POST':
#         f = CustomApplicantCreationForm(request.POST)
#         if f.is_valid():
#             f.save()
#             messages.success(request, 'Account Created Successfully')
#             # return redirect('documents')
#             return redirect('core-hr:landing')
#     else:
#         f = CustomApplicantCreationForm()
#     return render(request, 'users/user-creation.html', {'form':f})