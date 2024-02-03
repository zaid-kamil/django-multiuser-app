from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.models import User, Group
from .models import ManagerProfile, EmployeeProfile, CustomerProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from common.decorators import user_in_group_required

def login_options_view(request):
    return render(request, 'account/login_options.html')

def register_options_view(request):
    return render(request, 'account/register_options.html')

def manager_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        print('log',request.POST)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.groups.filter(name=group).exists():
                login(request, user)
                return redirect('manager_profile')
            else:
                messages.error(request, 'You are not a manager')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/manager_login.html')

def manager_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        group = request.POST.get('group')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        elif password != password2:
            messages.error(request, 'Passwords do not match')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            group = Group.objects.get(name=group)
            user.groups.add(group)
            user.save()
            # create profile
            profile = ManagerProfile(user=user)
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('manager_login')
    return render(request, 'account/manager_register.html')

@login_required(login_url='manager_login')
def manager_profile_view(request):
    profile = ManagerProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'account/manager_profile.html', context)

@login_required(login_url='manager_login')
def manager_profile_update_view(request):
    profile = ManagerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.image = request.FILES.get('image')
        profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('manager_profile')
    context = {'profile': profile}
    return render(request, 'account/manager_profile_update.html', context)

def employee_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name=group).exists():
                login(request, user)
                return redirect('employee_profile')
            else:
                messages.error(request, 'You are not an employee')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/employee_login.html')


@user_in_group_required(['manager'])
@login_required(login_url='manager_login')
def employee_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            group = Group.objects.get(name=group)
            user.groups.add(group)
            user.save()
            # create profile
            profile = EmployeeProfile(user=user)
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('employee_login')
        else:
            messages.error(request, 'Username already exists')
    return render(request, 'account/employee_register.html')

@login_required(login_url='employee_login')
def employee_profile_view(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'account/employee_profile.html', context)

@login_required(login_url='employee_login')
def employee_profile_update_view(request):
    profile = EmployeeProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.image = request.FILES.get('image')
        profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('employee_profile')
    context = {'profile': profile}
    return render(request, 'account/employee_profile_update.html', context)

def customer_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.groups.filter(name=group).exists():
                login(request, user)
                return redirect('customer_profile')
            else:
                messages.error(request, 'You are not a customer')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'account/customer_login.html')

def customer_register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        group = request.POST.get('group')
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, password=password)
            group = Group.objects.get(name=group)
            user.groups.add(group)
            user.save()
            # create profile
            profile = CustomerProfile(user=user)
            profile.save()
            messages.success(request, 'Account created successfully')
            return redirect('customer_login')
        else:
            messages.error(request, 'Username already exists')
    return render(request, 'account/customer_register.html')

@login_required(login_url='customer_login')
def customer_profile_view(request):
    profile = CustomerProfile.objects.get(user=request.user)
    context = {'profile': profile}
    return render(request, 'account/customer_profile.html', context)

@login_required(login_url='customer_login')
def customer_profile_update_view(request):
    profile = CustomerProfile.objects.get(user=request.user)
    if request.method == 'POST':
        profile.image = request.FILES.get('image')
        profile.save()
        messages.success(request, 'Profile updated successfully')
        return redirect('customer_profile')
    context = {'profile': profile}
    return render(request, 'account/customer_profile_update.html', context)

def logout_view(request):
    # get group of user
    group = request.user.groups.all()[0].name
    logout(request)
    if group == 'manager':
        return redirect('manager_login')
    elif group == 'employee':
        return redirect('employee_login')
    else:
        return redirect('customer_login')

