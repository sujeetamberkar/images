from django import forms
class ArithmeticForms(forms.Form):
    number1 = forms.IntegerField(label="Number 1")
    number2 = forms.IntegerField(label="Number 2")
    OPPERATION_CHOICES = [
        ('add','Add'),
        ('subtract','Subtract'),
        ('multiply','Multiply'),
        ('divide','Divide'),
        ]
    opperation = forms.ChoiceField(choices=OPPERATION_CHOICES,label="Opperation")