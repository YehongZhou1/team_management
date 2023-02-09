import datetime

from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from team.models import Member

from .forms import AddMemberForm


def add_member(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddMemberForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            member = Member()
            member.first_name = form.cleaned_data['first_name']
            member.last_name = form.cleaned_data['last_name']
            member.email = form.cleaned_data['email']
            member.phone_number = form.cleaned_data['phone_number']
            member.isAdmin = False if form.cleaned_data['role'] == 'RG' else True
            member.save()
            print(member.__str__())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('team:index') )

    # If this is a GET (or any other method) create the default form.
    else:
        form = AddMemberForm()

    return render(request, 'team/member.html', {'form' : form, 'isEdit':False})

def index(request):
    member_list = Member.objects.all()
    return render(request, 'team/team.html', {'list':member_list})

def edit_member(request, pk):
    member=get_object_or_404(Member, pk = pk)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddMemberForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            member.first_name = form.cleaned_data['first_name']
            member.last_name = form.cleaned_data['last_name']
            member.email = form.cleaned_data['email']
            member.phone_number = form.cleaned_data['phone_number']
            member.isAdmin = False if form.cleaned_data['role'] == 'RG' else True
            member.save()   
            print(member.__str__())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('team:index') )

    # If this is a GET (or any other method) create the default form.
    else:
        data = {
            'first_name' : member.first_name,
            'last_name' : member.last_name,
            'email' : member.email,
            'phone_number' : member.phone_number,
            'role' : 'AD' if member.isAdmin else 'RG' 
        }

        form = AddMemberForm(initial = data)

    return render(request, 'team/member.html', {'form' : form, 'isEdit' : True, 'uuid':pk})

def delete_member(request, pk):
    member=get_object_or_404(Member, pk = pk)
    if request.method == 'POST':
        if member.isAdmin:
            raise PermissionDenied
        else:
            member.delete()
    return HttpResponseRedirect(reverse('team:index') )
