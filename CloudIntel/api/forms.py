from django import forms

class APICallForm(forms.Form):
    param1 = forms.IntegerField(label='param1', max_value=100)
    param2 = forms.IntegerField(label='param2', max_value=100)
    param3 = forms.IntegerField(label='param3', max_value=100)
    param4 = forms.IntegerField(label='param4', max_value=100)

class CallbackFunction(forms.Form):
    callback = forms.Textarea()