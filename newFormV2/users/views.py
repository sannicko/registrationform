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
from employee.models import *
# from teachers.models import teacher
import re
User = get_user_model()

#user logout
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:user_login'))

#user login
class LoginView(account.views.LoginView):
    template_name = "main.html"
    form_class = userLoginForm

    def form_valid(self, form):
        auth.login(self.request, form.user)
        self.after_login(form)
        user = self.request.user
        print 'current user is ', user.is_authenticated()
        print 'user phone number is : ',user.phoneNumber
        return HttpResponseRedirect(reverse('users:user_home'))



class UserSignUpView(SignupView):
    template_name = "main.html"
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
        return render(request, 'home.html', {'success':"TRUE"})

class UserHome(TemplateView):
    def get(self, request, *args, **kwargs):

        employeeForm = EmployeeForm()
        print '>>>logged in user is : ',self.request.user.email
        # allFriends = Friend.objects.filter(current_user = self.request.user,
        #     is_activeFriend=True)
        # new_list = []
        # for counter in allFriends:
        #     new_list.append(counter.friend.id)

        # print '>>now list is : ',new_list
        # getAllUsers = ApplicationUser.objects.all().exclude(id = self.request.user.id).exclude(id__in=new_list)
        # # getAllUsers = Friend.objects.values('friend')
        # print '>>>users count is : ',getAllUsers.count()
        # print '>>>friends are : ',allFriends
        # return render(request, 'home.html', {'getAllusers':getAllUsers,'allFriends' :allFriends})

        return render(request, 'home.html', {'employeeForm':employeeForm})




class UserProfile(TemplateView):
    template_name='profile.html'
    def get(self, request, *args, **kwargs):
        user_id = request.GET.get('userId', None)
        print '>>>now id is : ',user_id
        getUser = Friend.objects.get(id=user_id)
        print '>>usr is : ',getUser
        return render(request, 'profile.html', {'userObject':getUser})




# class NewFriend(TemplateView):
#     def get(self, request, *args, **kwargs):
#         user_id = request.GET.get('userId', None)
#         print '>>>friend id is : ',user_id
#         currentUser = request.user
#         print '>>>>current user id is : ',currentUser.id
#         newFriend = ApplicationUser.objects.get(id=user_id)
#         print '>>newFriend is :',newFriend 
#         friendObject = Friend()
#         newFriend.isFriendAdded = True
#         newFriend.save()
#         friendObject.current_user = currentUser
#         friendObject.friend  = newFriend
#         friendObject.save()
#         return HttpResponseRedirect("/users/home/")
    

# class RemoveFriend(TemplateView):
#     def get(self, request, *args, **kwargs):
#         user_id = request.GET.get('userId', None)
#         currentUser = request.user
#         getFriend = Friend.objects.get(id=user_id)
#         getFriend.is_activeFriend = False
#         getFriend.current_user = currentUser
#         getFriend.save()
#         return HttpResponseRedirect("/users/home/")