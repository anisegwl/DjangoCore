from django import forms
from .models import Questions


class QuestionForm(forms.ModelForm):
   class Meta:
       model = Questions
       fields = '__all__'
       widgets = {
           'question_text': forms.TextInput(attrs={
               'class': 'form-control',
               'placeholder': 'Enter question text'
           }),
           'choice_1': forms.TextInput(attrs={'class': 'form-control'}),
           'choice_2': forms.TextInput(attrs={'class': 'form-control'}),
           'choice_3': forms.TextInput(attrs={'class': 'form-control'}),
           'choice_4': forms.TextInput(attrs={'class': 'form-control'}),
           'correct_answer': forms.RadioSelect(attrs={'class': 'form-check-input'})
       }
