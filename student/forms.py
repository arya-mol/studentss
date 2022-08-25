from django import forms

class StudentForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    def __str__(self):
        return self.title