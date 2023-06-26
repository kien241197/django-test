from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Member
from .models import Company
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from pprint import pprint
from . import forms
from django.db.models import Q
from django.contrib.auth.hashers import make_password

# Create your views here.
def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def members(request):
	query = request.GET.get('search')
	members = Member.objects.order_by('-id')
	if query:
		members = members.filter(
			Q(name__icontains=query) | Q(email__icontains=query) | Q(note__icontains=query)
		)
	template = loader.get_template('member/index.html')
	context = {
		'members': members,
	 }
	return HttpResponse(template.render(context, request))

def member_create(request):
	form = forms.Member()
	template = loader.get_template('member/add.html')
	if request.method == 'POST':
		form = forms.Member(request.POST)
		if form.is_valid():
			obj = Member()
			obj.name = request.POST.get('name')
			obj.email = request.POST.get('email')
			obj.phone = request.POST.get('phone')
			obj.note = request.POST.get('note')
			obj.company_id = request.POST.get('company')
			obj.joined_at = datetime.now().date()
			obj.password = make_password(request.POST.get('password'))
			obj.save()
			return redirect('members')
	return HttpResponse(template.render({'form': form}, request))

def member_edit(request, id):
	template = loader.get_template('member/edit.html')
	obj = get_object_or_404(Member, pk=id)
	form = forms.Member()
	if request.method == 'POST':
		form = forms.Member(request.POST)
		if form.is_valid():
			obj.name = request.POST.get('name')
			obj.email = request.POST.get('email')
			obj.phone = request.POST.get('phone')
			obj.note = request.POST.get('note')
			obj.company_id = request.POST.get('company')
			obj.password = make_password(request.POST.get('password'))
			obj.save()
			return redirect('members')
	return HttpResponse(template.render({'member': obj, 'form': form}, request))

def member_delete(request, id):
    try:
        # Retrieve the object you want to delete
        obj = Member.objects.get(id=id)
        # Delete the object
        obj.delete()
        # Return a success response
        return JsonResponse({'message': 'Member deleted successfully'})
    except Member.DoesNotExist:
        # Return an error response if the object doesn't exist
        return JsonResponse({'message': 'Object not found'}, status=404)

def companies(request):
	query = request.GET.get('search')
	companies = Company.objects.order_by('-id')
	if query:
		companies = companies.filter(
			Q(name__icontains=query) | Q(address__icontains=query) | Q(note__icontains=query)
		)
	template = loader.get_template('company/index.html')
	context = {
		'companies': companies,
	 }
	return HttpResponse(template.render(context, request))

def company_create(request):
	form = forms.Company()
	template = loader.get_template('company/add.html')
	if request.method == 'POST':
		form = forms.Company(request.POST)
		if form.is_valid():
			obj = Company()
			obj.name = request.POST.get('name')
			obj.address = request.POST.get('address')
			obj.note = request.POST.get('note')
			obj.created_at = datetime.now().date()
			obj.save()
			return redirect('companies')
	return HttpResponse(template.render({'form': form}, request))

def company_edit(request, id):
	template = loader.get_template('company/edit.html')
	obj = get_object_or_404(Company, pk=id)
	form = forms.Company()
	if request.method == 'POST':
		form = forms.Company(request.POST)
		if form.is_valid():
			# obj.name = request.POST.get('name')
			# obj.email = request.POST.get('email')
			# obj.phone = request.POST.get('phone')
			# obj.note = request.POST.get('note')
			# obj.company_id = request.POST.get('company')
			# obj.password = make_password(request.POST.get('password'))
			# obj.save()
			return redirect('companies')
	return HttpResponse(template.render({'company': obj, 'form': form}, request))

def company_delete(request, id):
    try:
        # Retrieve the object you want to delete
        obj = Company.objects.get(id=id)
        # Delete the object
        obj.delete()
        # Return a success response
        return JsonResponse({'message': 'Company deleted successfully'})
    except Member.DoesNotExist:
        # Return an error response if the object doesn't exist
        return JsonResponse({'message': 'Object not found'}, status=404)

def login(request):
	template = loader.get_template('login.html')
	return HttpResponse(template.render({}, request))