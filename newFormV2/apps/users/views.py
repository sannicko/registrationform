from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.template.context import RequestContext
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect

from django.db.models import Q
from .forms import *
# from .decorators import redirect_to_home

from account.views import *
from django.views.generic import View, TemplateView,FormView
from apps.employee.models import *
# from teachers.models import teacher
import re
User = get_user_model()

#user logout
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:user_login'))

#user login
class LoginView(account.views.LoginView):
    template_name = "users/main.html"
    form_class = userLoginForm

    def form_valid(self, form):
        auth.login(self.request, form.user)
        self.after_login(form)
        user = self.request.user
        print 'current user is ', user.is_authenticated()
        print 'user phone number is : ',user.phoneNumber
        return HttpResponseRedirect(reverse('users:user_home'))



class UserSignUpView(SignupView):
    template_name = "users/main.html"
    form_class = UserSignUpForm

    def form_valid(self, form):
        if form.is_valid():
            try:
                password = form.cleaned_data.get('password')
                phoneNumber = form.cleaned_data.get('phoneNumber')
                firstName = form.cleaned_data.get('first_name')
                lastName = form.cleaned_data.get('last_name')
                print '>>phone Number is : ',phoneNumber
                print '>>phone Number is : ',firstName
                print '>>phone Number is : ',lastName
                if firstName and lastName:
                    user = ApplicationUser(firstName=firstName,lastName=lastName,
                        phoneNumber = phoneNumber)
                else:
                    user = ApplicationUser(phoneNumber = phoneNumber)
                user.set_password(password)
                user.save()
                user = authenticate(phoneNumber=phoneNumber, password=password)
                login(self.request, user)
                return HttpResponseRedirect(reverse('users:user_home'))

            except Exception as e:
                print 'In exception part and exception is : ', e


def form_submit(request):
    form = EmployeeForm(request.POST or None)
    if form.is_valid():
        print '>>>cleaned data is : ',form.cleaned_data

        print 'celeing mechanic value is : ',form.cleaned_data['ceiling_mechanic']
        print 'framing_mechanic value is : ',form.cleaned_data['framing_mechanic']
        print 'drywall_hanger value is : ',form.cleaned_data['drywall_hanger']
        print '>>>brick layer value is : ',form.cleaned_data['masonry_bricklayer']
        print '>>>martial status is : ',form.cleaned_data['Martial_status']
        print 'state is : ',form.cleaned_data['state']
        print 'date of birth is : ',form.cleaned_data['dateOFBirth']
        form.save(commit=True)
        print '>>>after saving the form/user <<<'
        return render(request, 'employee/home.html', {'success':"TRUE"})

class UserHome(TemplateView):
    def get(self, request, *args, **kwargs):
        employeeForm = EmployeeForm()
        print '>>>logged in user is : ',self.request.user.email
        return render(request, 'employee/home.html', {'employeeForm':employeeForm})




class UserProfile(TemplateView):
    template_name='profile.html'
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('userId', None)
        print '>>>now id is : ',user_id
        getUser = Friend.objects.get(id=user_id)
        print '>>usr is : ',getUser
        return render(request, 'profile.html', {'userObject':getUser})
