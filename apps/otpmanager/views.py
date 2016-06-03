import requests
import urllib

from ordereddict import OrderedDict

from django.conf import settings
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_protect

from .forms import OTPForm
from .models import Message, KisanUser

import json
import random

class Index(TemplateView):
    """
    Renders the index view template
    """

    template_name = 'otpmanager/index.html'
    typemap = OrderedDict()
    typemap['contacts'] = {'model':KisanUser, 'order':'first_name'}
    typemap['messages'] = {'model':Message, 'order':'-sent_time'}
    

    def get_context_data(self, **kwargs):

        page_no = self.request.GET.get('page', 1)
        
        context = super(Index, self).get_context_data(**kwargs)
        
        list_type = self.request.GET.get('type', 'contacts')
        
        _type = self.typemap.get(list_type)

        model = _type.get('model')
        order = _type.get('order')

        results = model.objects.order_by(order).all()
        

        norm_list = 0

        if list_type == 'messages':
            norm_list = 1

        p = Paginator(results, settings.PAGINATION_STEP)

        context['page'] = p.page(page_no)
        context['paginator'] = p
        context['tabtypes'] = self.typemap.keys()
        context['norm_list'] = norm_list

        return context


class SendMessage(FormView):
    """
    Renders the index view template
    """

    template_name = 'otpmanager/send_msg.html'
    form_class = OTPForm
    success_url = '/home/?type=messages'

    def get_context_data(self, **kwargs):
        
        context = super(SendMessage, self).get_context_data(**kwargs)
		
        user_id = self.request.GET.get('user-id')
        user_obj = KisanUser.objects.get(id=user_id) 
        otp = random.randint(100000, 999999)
        context['otp'] = otp
        context['user_id'] = user_id
        context['ph_number'] = user_obj.phone_number

        return context

    def get_sms_url(self, data):
   		base_url = settings.NEXMO_BASE_URL

   		url_context = {
   			"api_key" : settings.NEXMO_API_KEY,
   			"api_secret": settings.NEXMO_API_SECRET,
   			"from": settings.NEXMO_DEFAULT_FROM,
   			"text": data.get("msg"),
   			"to": data.get("phone")
   		}

   		context = urllib.urlencode(url_context)
   		return base_url % context
   		
    def form_valid(self, form, *args, **kwargs):
    	## send otp to the user.
    	url = self.get_sms_url(form.cleaned_data)
    	# nexmo_response = requests.get("https://www.google.co.in")
    	nexmo_response = requests.get(url)

    	user_id = self.request.GET.get('user-id')
    	k_otp = self.request.POST.get('otp')
    	k_msg = self.request.POST.get('msg')

    	k_user = KisanUser.objects.get(id=user_id)

    	if nexmo_response.status_code == 200:
    		status = nexmo_response.json()["messages"][0]["status"]

    		k_status = "Failed"
    		if int(status) == 0:
				k_status = "Sent Successfully"

	    	Message.objects.create(
    			kisan_user = k_user,
    			otp = k_otp,
    			msg = k_msg,
    			status = k_status)

	    	k_user.otp_count = k_user.otp_count + 1
	    	k_user.save()

    	else:
            pass 

    	return super(SendMessage, self).form_valid(form, *args, **kwargs)



def jsonresponse(json_data):
	return HttpResponse(json.dumps(json_data), content_type="application/json")


def get_user_details(request):
    string_id = request.GET.get('s')
    try:
        details = []
        k_user = KisanUser.objects.get(id=string_id)        

        details.append(k_user.first_name)
        details.append(k_user.last_name)
        details.append(k_user.phone_number)
        details.append(k_user.id)

    except (NormalizedInstitute.DoesNotExist, Exception) as err:
        details = []
    return jsonresponse(details)