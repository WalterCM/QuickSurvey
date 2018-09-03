from django import forms
from django.contrib.auth.models import User
from .models import Survey
from .services import get_categories

YEARS = ['2000', '1999', '1998', '1997', '1996', '1995', '1994', '1993', '1992', '1991',
         '1990', '1989', '1988', '1987', '1986', '1985', '1984', '1983', '1982', '1981',
         '1980', '1979', '1978', '1977', '1976', '1975', '1974', '1973', '1972', '1971',
         '1970', '1969', '1968', '1967', '1966', '1965', '1964', '1963', '1962', '1961',
         '1960']

class SurveyForm(forms.ModelForm):
    category = forms.CharField(label="Categoria", max_length=50, widget=forms.Select(choices=get_categories()))
    class Meta:
        model = Survey
        fields = ('first_name', 'last_name', 'dni', 'sex', 'birthdate', 'email', 'category', 'reason')
        widgets = {
            #'sex': forms.RadioSelect(),
            'birthdate': forms.SelectDateWidget(years=YEARS),
            'reason':forms.Textarea(),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']