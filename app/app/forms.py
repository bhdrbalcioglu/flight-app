from django import forms
class FlightForm(forms.Form):
    departing_date = forms.DateField()
    deptAirport = forms.CharField()
    arrAirport = forms.CharField()
    duration = forms.CharField()
    airline = forms.CharField()
    price = forms.CharField()
    deptCity = forms.CharField()
    arrCity = forms.CharField()
    deptHour = forms.CharField()
    arrHour = forms.CharField()
