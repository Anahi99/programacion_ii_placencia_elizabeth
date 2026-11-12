from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('catalogo.view_home', raise_exception=True)
def home(request):
    return render(request, 'catalogo/home.html')
