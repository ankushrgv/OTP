from django import forms

## Form to be displayed on Send SMS page
class OTPForm(forms.Form):
	msg = forms.CharField()
	otp = forms.CharField(widget=forms.HiddenInput())
	phone = forms.CharField(widget=forms.HiddenInput())