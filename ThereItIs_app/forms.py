# from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit
# from .models import User

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','email','password')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method="post"
#         self.helper.add_input(Submit('submit','Register'))