from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# ✅ Home Page (Requires Login)
@login_required(login_url='login')
def HomePage(request):
    return render(request, 'home.html')

# ✅ Signup Page
def SignupPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmpassword')

        # ❌ Passwords do not match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("signup")

        # ❌ User already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            messages.warning(request, "Account already exists! Please log in.")
            return redirect("login")  # Redirect to login if user already exists

        # ✅ Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Signup successful! Please log in.")
        return redirect("login")  # Redirect to login after successful signup

    return render(request, "signup.html")

# ✅ Login Page with Error Message
def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to HomePage after login
        else:
            messages.error(request, "Invalid username or password!")  # Use messages for errors
            return redirect('login')  

    return render(request, 'login.html')

# ✅ Logout Page
def LogoutPage(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('login')
