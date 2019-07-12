from django import forms
from SGApp.models import AClist,Buy,Quotation
# from SGApp.valid import validate
import re

class BuyForm(forms.ModelForm):
    class Meta:
        model = Buy
        fields = ['Name','Phone','Address']
    # 
    # def clean_Name(self):
    #     super(BuyForm,self).clean()
    #     Name = self.cleaned_data.get('Name')
    #     Phone = self.cleaned_data.get('Phone')
    #     Address = self.cleaned_data.get('Address')
    #     # if len(Name<5):
    #     #     self._errors['Name'] = self.error_class(['only Alphabets allowd For Name'])
    #     # else:
        #     Name

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [
                'Brand',
                'Tons',
                'Phone',
                'Email',
                'Query'
                 ]
