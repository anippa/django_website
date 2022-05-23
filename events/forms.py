from django import forms
from django.forms import ModelForm
from .models import Venue,Event


#Create a Venue Form
class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('name','address','zip_code','phone','web','email_adress','venue_image')
		labels = {
		'name': '',
		'address': '',
		'zip_code': '',
		'phone': '',
		'web': '',
		'email_adress': '',
		'venue_image': '',
		}

		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Venue Name'}),
		'address': forms.TextInput(attrs={'class':'form-control','placeholder':'Adress'}),
		'zip_code': forms.TextInput(attrs={'class':'form-control','placeholder':'Zip Code'}),
		'phone': forms.TextInput(attrs={'class':'form-control','placeholder':'Phone'}),
		'web': forms.TextInput(attrs={'class':'form-control','placeholder':'Web Address'}),
		'email_adress': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
		}

#Admin SuperUser Event Form
class EventFormAdmin(ModelForm):
	class Meta:
		model = Event
		fields = ('name','event_date','venue','manager','description','attendees')
		labels = {
		'name': '',
		'event_date': 'YYYY-MM-DD HH:MM:SS',
		'venue': 'Venue',
		'manager': 'Manager',
		'description': '',
		'attendees': 'Attendees',
		}

		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
		'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}),
		'venue': forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
		'manager': forms.Select(attrs={'class':'form-select','placeholder':'Manager'}),
		'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
		'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
		}

#User Event Form
class EventForm(ModelForm):
	class Meta:
		model = Event
		fields = ('name','event_date','venue','description','attendees')
		labels = {
		'name': '',
		'event_date': 'YYYY-MM-DD HH:MM:SS',
		'venue': 'Venue',
		'description': '',
		'attendees': 'Attendees',
		}

		widgets = {
		'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Event Name'}),
		'event_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Date'}),
		'venue': forms.Select(attrs={'class':'form-select','placeholder':'Venue'}),
		'description': forms.Textarea(attrs={'class':'form-control','placeholder':'Description'}),
		'attendees': forms.SelectMultiple(attrs={'class':'form-control','placeholder':'Attendees'}),
		}