from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Member
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from pprint import pprint

# Create your views here.
def home(request):
	template = loader.get_template('home.html')
	return HttpResponse(template.render())

def members(request):
	members = Member.objects.order_by('-id').all().values()
	template = loader.get_template('index.html')
	context = {
		'members': members,
	 }
	return HttpResponse(template.render(context, request))

def member_create(request):
	template = loader.get_template('add.html')
	if request.method == 'POST':
		obj = Member()
		obj.name = request.POST.get('name')
		obj.email = request.POST.get('email')
		obj.phone = request.POST.get('phone')
		obj.note = request.POST.get('note')
		obj.joined_at = datetime.now().date()
		obj.save()
		return redirect('members')
	return HttpResponse(template.render({}, request))

def member_edit(request, id):
	template = loader.get_template('edit.html')
	obj = get_object_or_404(Member, pk=id)
	if request.method == 'POST':
		obj.name = request.POST.get('name')
		obj.email = request.POST.get('email')
		obj.phone = request.POST.get('phone')
		obj.note = request.POST.get('note')
		obj.save()
		return redirect('members')
	return HttpResponse(template.render({'member': obj}, request))

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