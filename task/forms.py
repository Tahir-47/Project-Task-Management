from django import forms
from .models import Project, tasks

class AddProjectForm(forms.ModelForm):
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Project title", "class":"form-control"}), label="")
	description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Project description", "class":"form-control"}), label="")


	class Meta:
		model = Project
		fields = ('title', 'description')


class AddTaskForm(forms.ModelForm):
	project = forms.ModelChoiceField(queryset=Project.objects.get(pk=Project.id)) 
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Task", "class":"form-control", "autocomplete":"off" }), label="")
	description = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control", "autocomplete":"off"}), label="")


	class Meta:
		model =tasks
		fields ='__all__'