import logging

from django_twilio.decorators import twilio_view
from django_twilio.request import decompose
from twilio.twiml import Response 
from twilio.rest import TwilioRestClient

from django.conf import settings
from django.http import HttpResponse

from interactions.models import Inbound, Outbound, TwilioNumber, User, Action

client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

logger = logging.getLogger(__name__)

@twilio_view
def sms(request):
	twilio_request = decompose(request)

	user, created = User.objects.get_or_create(number=twilio_request.from_)
	twilio_number, created = TwilioNumber.objects.get_or_create(number=twilio_request.to)
	
	body = twilio_request.body.lower()

	if body == 'subscribe':
		user.subscribe(twilio_number)
		return HttpResponse()

	inbound = Inbound()
	inbound.from_number = user
	inbound.to_number = twilio_number
	inbound.body = body
	inbound.twilio_sid = twilio_request.smssid
	inbound.save()

	try:
		action = Action.objects.get(keyword=inbound.body, twilio_number=twilio_number)
		action.perform(user)

		inbound.action = action
		inbound.save()

	except Action.DoesNotExist:
		# Code here to send the catchall message
		fallback_message = "I didn't quite get that. Please check your spelling and try again."

		message = client.messages.create(
				body=fallback_message,
				to=user.number,
				from_=twilio_number.number 
			)
		pass

	sender = getattr(twilio_request, 'from_', 'No sender provided with request')
	
	return HttpResponse()

@twilio_view
def followup(request):
	twilio_request = decompose(request)
	outbound = Outbound.objects.get(twilio_sid=twilio_request.callsid)

	outbound.send_followup()

	return HttpResponse()








