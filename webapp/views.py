from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User, Owner, Staff


# Create your views here.

def home(request):
    return render(request, 'login.html')




def owner_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_owner:
            login(request, user)
            return redirect('owner_dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials for owner.'})
    return render(request, 'login.html')

def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff_member:
            login(request, user)
            return redirect('staff_dashboard')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials for staff member.'})
    return render(request, 'login.html')

@login_required
def owner_dashboard(request):
    owner_profile = Owner.objects.get(user=request.user)
    context = {'owner_profile': owner_profile}
    return render(request, 'Owner_dashboard.html', context)

@login_required
def staff_dashboard(request):
    staff_profile = Staff.objects.get(user=request.user)
    context = {'staff_profile': staff_profile}
    return render(request, 'staff_dashboard.html', context)

@login_required
def owner_profile(request):
    owner_profile = Owner.objects.get(user=request.user)
    context = {'owner_profile': owner_profile}
    return render(request, 'owner_profile.html', context)

@login_required
def staff_profile(request):
    staff_profile = Staff.objects.get(user=request.user)
    context = {'staff_profile': staff_profile}
    return render(request, 'staff_profile.html', context)


from django.contrib.auth.models import User
from .forms import OwnerRegistrationForm, StaffRegistrationForm

def owner_register(request):
    if request.method == 'POST':
        form = OwnerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Adjust the redirect URL as needed
    else:
        form = OwnerRegistrationForm()
    return render(request, 'registration/owner_register.html', {'form': form})

def staff_register(request):
    if request.method == 'POST':
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')  # Adjust the redirect URL as needed
    else:
        form = StaffRegistrationForm()
    return render(request, 'registration/staff_register.html', {'form': form})