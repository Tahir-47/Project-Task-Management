from django import forms
from .models import Project

class AddProjectForm(forms.ModelForm):
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Project title", "class":"form-control"}), label="")
	description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Project description", "class":"form-control"}), label="")


	class Meta:
		model = Project
		fields = ('title', 'description')