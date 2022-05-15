from django import forms  
from main_app.models import List  

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = "__all__"
        
    def clean_field(self):
        item = self.cleaned_data['item']
        if len(item) < 3:
            raise forms.ValidationError("Need at least three characters")
        return item
    