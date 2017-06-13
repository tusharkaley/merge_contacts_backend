from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
from django.views.decorators.cache import never_cache
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse
from .models import Users,Contacts,Phones,Emails
import json
import random
import redis
import django
from django.db import transaction

@never_cache
def index(request):
	django.db.connection.close()
	usersdb1 = Users.objects.using('db1').all()
	usersdb2 = Users.objects.using('db2').all()
	
	resp =[]
	
	if usersdb1:
		for user in usersdb1:
			userData = {}
			userData['user_id'] = user.id
			userData['firstname'] = user.first_name
			userData['lastname'] = user.last_name
			userData['phone'] = user.phone_number
			userData['email'] = user.email_id
			
			resp.append(userData)
	if usersdb2:
		for user in usersdb2:
			userData = {}
			userData['user_id'] = user.id
			userData['firstname'] = user.first_name
			userData['lastname'] = user.last_name
			userData['phone'] = user.phone_number
			userData['email'] = user.email_id
			
			resp.append(userData)	
    
	response = JsonResponse(resp,content_type="application/json", safe=False)	
	return response

@csrf_exempt
def add_user(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	database =''
	test = random.random()
	if test<0.5:
		database = 'db1'
	else:
		database = 'db2'	
	cache.set(body['phone'],database ,timeout=None)
	print(cache.get(body['phone']))

	add_user = Users.objects.using(database).create(first_name=body['fname'],last_name=body['lname'],phone_number=body['phone'],email_id=body['email'])
	add_user.save();
	resp ={}
	resp['status'] = 'success'
	resp['resop_text'] ="Done"
	response = JsonResponse(resp,content_type="application/json", safe=False)
	transaction.commit(using=database) 
	return response	

@never_cache
def user_contacts(request):
	user_phone = request.GET.get('user_phone', '')
	database = cache.get(user_phone)
	contacts = Contacts.objects.using(database).filter(user__phone_number = user_phone)
	#phone_nos = Phones.objects.filter()
	resp =[]
	for contact in contacts:
		userData = {}
		userData['firstname'] = contact.first_name
		userData['lastname'] = contact.last_name
		userData['phonenumbers'] = []
		userData['emails'] = []
		
		numbers = Phones.objects.using(database).values_list('phone' ,flat=True).filter(contact__id = contact.id)
		for number in numbers:
			userData['phonenumbers'].append(number)
			#userData['phonenumbers'].append(numbers)
		emails = Emails.objects.using(database).values_list('email_id',flat=True).filter(contact__id = contact.id)
		for email in emails:
			userData['emails'].append(email)
		resp.append(userData)

	response = JsonResponse(resp,content_type="application/json", safe=False)	
	return response;

@csrf_exempt
def new_contact(request):
	body_unicode = request.body.decode('utf-8')
	body = json.loads(body_unicode)
	phone_numbers = body['phone_numbers']
	email_ids = body['email_ids']
	#print('tushar debug')
	
	#print(body['user_phone'])
	database = cache.get(body['user_phone'])
	user_id = Users.objects.using(database).get(phone_number__exact = body['user_phone']).id
	add_contact = Contacts.objects.using(database).create(user_id=user_id,first_name=body['fname'],last_name=body['lname'])
	
	add_contact.save();
	contact_id = add_contact.id
	for phone in phone_numbers:
		if phone != '':
			add_phone = Phones.objects.using(database).create(phone=phone,contact_id=contact_id,user_phone=body['user_phone'])
			add_phone.save();
	for email in email_ids:
		if email != '':
			add_email = Emails.objects.using(database).create(email_id=email,contact_id=contact_id,user_phone=body['user_phone'])
			add_email.save();
	transaction.commit(using=database) 

	resp ={}
	resp['status'] = 'success'
	resp['resop_text'] ="Done"
	response = JsonResponse(resp,content_type="application/json", safe=False)
	return response	

def trials(request):

	return HttpResponse('ygygyg')
@never_cache	
def merge_candidates(request):
	user_phone = request.GET.get('user_phone', '')
	database = cache.get(user_phone)
	dict1 = {}
	dict2 = {}
	resp =[]
	phone_numbers = Phones.objects.using(database).filter(user_phone = user_phone).order_by('phone')
	prev_phone = ''
	prev_buck_id = 0
	dict1[1] = []
	counter = 0
	for number in phone_numbers:
		if number.phone != prev_phone:
			if number.contact_id not in dict2:
				dict1_upd_key = counter+1
				dict1_upd_val = []
				dict1_upd_val.append(number.contact_id)
				dict1[dict1_upd_key] = dict1_upd_val
				dict2[number.contact_id] = counter+1
				prev_buck_id = prev_buck_id+1
				counter = counter + 1
			else:
				prev_buck_id = dict2[number.contact_id]

		else:
			if number.contact_id not in dict2:
				dict1_val = dict1[prev_buck_id]
				dict1_val.append(number.contact_id)
				dict1[prev_buck_id] =dict1_val
				dict2[number.contact_id] = prev_buck_id
			else:
				old_buck = 	dict2[number.contact_id]
				dict1_values = dict1[old_buck]
				dict1[old_buck] = dict1_values+dict1[prev_buck_id]
				for custid in dict1[prev_buck_id]:
					dict2[custid] = old_buck
				dict1.pop(prev_buck_id)
				if counter != prev_buck_id:
					prev_buck_id =counter
				else:	
					prev_buck_id = prev_buck_id-1
					counter = 	counter - 1
		prev_phone =	number.phone
	if counter != prev_buck_id:
		prev_buck_id =counter
	email_ids = Emails.objects.using(database).filter(user_phone = user_phone).order_by('email_id')
	prev_email =''
	
	for email in email_ids:
		if email.email_id != prev_email:
			if email.contact_id not in dict2:
				dict1_upd_key = counter+1
				dict1_upd_val = []
				dict1_upd_val.append(email.contact_id)
				dict1[dict1_upd_key] = dict1_upd_val
				dict2[email.contact_id] = counter+1
				prev_buck_id = prev_buck_id+1
				counter = counter + 1
			else:
				prev_buck_id = dict2[email.contact_id]
		else:
			if email.contact_id not in dict2:
				dict1_val = dict1[prev_buck_id]
				dict1_val.append(email.contact_id)
				dict1[prev_buck_id] =dict1_val
				dict2[email.contact_id] = prev_buck_id
			else:
				old_buck = 	dict2[email.contact_id]
				dict1_values = dict1[old_buck]
				dict1[old_buck] = dict1_values+dict1[prev_buck_id]
				for custid in dict1[old_buck]:
					dict2[custid] = old_buck
				dict1.pop(prev_buck_id)	
				if counter != prev_buck_id:
					prev_buck_id =counter
				else:	
					prev_buck_id = prev_buck_id-1	
					counter = 	counter - 1
		prev_email	 = email.email_id	
		
	user_contacts = Contacts.objects.using(database).filter(user__phone_number = user_phone)	
	name_id_mapping = {}
	for contact in user_contacts:
		name_id_mapping[contact.id] = contact.first_name+" "+contact.last_name+"  "
	for key in dict1:
		merge_data = []
		for contact_id in dict1[key]:
			merge_data.append(name_id_mapping[contact_id])
		resp.append(merge_data)	
	response = JsonResponse(resp,content_type="application/json", safe=False)
	return response		
				 
        























	





