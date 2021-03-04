import datetime

from django import forms
from django.core.exceptions import ValidationError
#from django.utils.translation import ugettext_lazy_as_

class EmployeesDataForm(forms.Form):
	checkHireDate = forms.DateField(help_text = "please enter a date less than or equal to currentdate")
	
	def CleancheckHireDate(self):
		checkHireDate = self.cleaned_data['checkHireDate']
		if (checkHireDate > date.time.date.today()) or (checkHireDate != datetime.date.today()):
			raise ValidationError(_('Invali Hiredate, cannot be accepted'))
		return checkHireDate