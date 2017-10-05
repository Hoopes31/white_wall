from django.shortcuts import render, HttpResponse, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from forms import Update
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

@login_required
def index(request):
    users = User.objects.all().values()
    return render(request, 'dash/index.html', {'users':users})

@login_required
@staff_member_required(login_url='/login/')
def admin_dash(request):
    users = User.objects.all().values()
    return render(request, 'dash/admin.html', {'users':users})

@login_required
def show(request, num):
    context = User.objects.get(id=num)
    return render(request, 'dash/show.html', {'context':context})

@login_required
@staff_member_required(login_url='/login/')
def edit(request, num):
    form = Update
    return render(request, 'dash/edit.html', {'form': form, 'num': num})

@login_required
@staff_member_required(login_url='/login/')
def update(request, num):
    form = Update(request.POST)
    if form.is_valid():
        form = form.cleaned_data
        user = User.objects.get(id=num)
        user.first_name = form['first_name']
        user.last_name = form['last_name']
        user.email = form['email']
        user.save()
        return redirect(reverse('dash:root'))
    else:
        return redirect('dash:edit', num)
    
@login_required
@staff_member_required(login_url='/login/')
def delete(request, num):
    if num:
        context = {'id': num}
        user = User.objects.get(id=num)
        user.delete()

    return render(request, 'dash/delete.html', {'context': context})

@login_required
@staff_member_required(login_url='/login/')
def delete_check(request, num):
    return render(request, 'dash/delete_check.html', {'num':num})
