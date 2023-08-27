from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

from .models import Project, tasks
from .forms import AddProjectForm, AddTaskForm

# Create your views here.
def home(request):
    form = AddProjectForm(request.POST or None)

    projects = Project.objects.all()

    #Check to see if logging in 
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == "add_record":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        else:
            username = request.POST['username']
            password = request.POST['password']
            #Authenticate
            user = authenticate(request, username=username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in!")
                return redirect('home')
            else:
                messages.success(request, "There was an error logging in")
                return redirect('home')
    else:
        return render(request, 'task/home.html',{'projects':projects, 'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out")
    return redirect('home')
 

def add_project(request):
	form = AddProjectForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_project = form.save()
				return redirect('home')
		return render(request, 'task/home.html', {'form':form})
	else:
		messages.success(request, "You Must Be Logged In...")
		return redirect('home')

def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Project.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Record Deleted Successfully...")
		return redirect('home')
	else:
		messages.success(request, "You Must Be Logged In To Do That...")
		return redirect('home')

def task_List(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    project_tasks = project.tasks.all()
    form = AddTaskForm(request.POST or None)
  

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Task Added...")
            task_list_url = reverse('task_List', args=[project_id])
            return redirect(task_list_url)
            
    else:
        return render(request, 'task/taskList.html',{'project':project,'project_tasks':project_tasks,'form':form})

    return render(request, 'task/taskList.html', {'project':project,'project_tasks':project_tasks, 'form':form} )