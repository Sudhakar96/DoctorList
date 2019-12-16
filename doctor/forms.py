from django import forms
from .models import Doctor


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = ('full_name','contact','d_id','post')
        labels = {
            'full_name':'Full Name',
            'd_id':'D. Id'
        }

    def __init__(self, *args, **kwargs):
        super(DoctorForm,self).__init__(*args, **kwargs)
        self.fields['post'].empty_label = "Select"
        self.fields['d_id'].required = False
