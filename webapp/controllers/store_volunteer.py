import logging
from contrib import web

from django.utils import simplejson

from google.appengine.api import search
from models import Volunteer

class store_volunteer:

	def POST(self):

		web.header('Access-Control-Allow-Origin',      '*')
		web.header('Access-Control-Allow-Credentials', 'true')

		volunteerItem = simplejson.loads(web.data())

		existingVolunteer = Volunteer.GetByEmail(volunteerItem['volunteer_email'])

		if (existingVolunteer):
			return "{ status: 'Error - Volunteer Exists'}"

		else:              # not existing, create new database record
			newVolunteer = Volunteer( 
					volunteer_name = volunteerItem['volunteer_name'],
					volunteer_email = volunteerItem['volunteer_email'],
					volunteer_phone = volunteerItem['volunteer_phone'],
					address_street = volunteerItem['address_street'],
					address_street2 = volunteerItem['address_street2'],
					address_city = volunteerItem['address_city'],
					address_state = volunteerItem['address_state'],
					address_zipcode = volunteerItem['address_zipcode']
   								)	
			newVolunteer.put()

		return "{ status: 'Success'}"


