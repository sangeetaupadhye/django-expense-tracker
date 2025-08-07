# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password.')

#     return render(request, 'login.html')  # ← renders your custom template

# def logout_user(request):
#     logout(request)
#     return redirect('login')

# def home(request):
#     return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')


def add_expense(request):
    return render(request, 'add_expense.html')

def all_expenses(request):
    return render(request, 'all_expense.html')
