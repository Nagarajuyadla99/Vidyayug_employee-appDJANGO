from django import forms
from .models  import Employees,Department

class DepartmenForm(forms.ModelForm):
    class Meta:
        model=Department
        fields='__all__'
        widgets={
            'dep_name':forms.TextInput(attrs={'class':'form-control'})
        }



class EmployeesForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields='__all__'
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.NumberInput(attrs={'class':'form-control'}),
            'designation':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_joining':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'dep':forms.Select(attrs={'class':'form-control'}),

        }



    def clean_phone(self):
        phone=self.cleaned_data.get('phone')
        if not phone.isdigit():
            massage = "Phone number must contain only digits."
            raise forms.ValidationError(massage)
        if len(phone)!=10:
            massage = "Phone number must be exactly 10 digits."
            raise forms.ValidationError(massage)
        if phone[0] not in ['6','7','8','9']:
            massage = "Phone number must start with 6, 7, 8, or 9."
            raise forms.ValidationError(massage)
        return phone
    

    def clean_age(self):
        age=self.cleaned_data.get('age')
        if age<18 or age>65:
            massage = "Age must be between 18 and 65."
            raise forms.ValidationError(massage)
        return age
    def clean_email(self):
        email=self.cleaned_data.get('email')
        if Employees.objects.filter(email=email).exclude(id=self.instance.id).exists():
            massage = "Email already exists. Please use a different email."
            raise forms.ValidationError(massage)
        return email
    def clean_name(self):
        name=self.cleaned_data.get('name')
        cleaned_name = name.strip()
        
        if cleaned_name == "":
            massage = "Name cannot be empty or just spaces."
            raise forms.ValidationError(massage)


        if not cleaned_name.replace(" ", "").isalpha():
            massage = "Name can only contain alphabetic characters and spaces."
            raise forms.ValidationError(massage)


        return cleaned_name