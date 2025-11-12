from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            return JsonResponse({
                "status": True,
                "message": "Login successful!",
                "username": user.username
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, account is disabled."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check username and password again."
        }, status=401)

@csrf_exempt
@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return JsonResponse({
        "status": True,
        "message": "Logout successful!",
    }, status=200)

@csrf_exempt
def register(request):
    username = request.POST['username']
    password = request.POST['password']
    password_confirm = request.POST['password_confirm']
    
    if password != password_confirm:
        return JsonResponse({
            "status": False,
            "message": "Passwords do not match!"
        }, status=400)
    
    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": False,
            "message": "Username already exists!"
        }, status=400)
    
    user = User.objects.create_user(username=username, password=password)
    user.save()
    
    return JsonResponse({
        "status": True,
        "message": "User created successfully!"
    }, status=201)
