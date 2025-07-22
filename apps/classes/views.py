from django.contrib import messages
from django.shortcuts import render, redirect
from apps.classes.forms import EnrollmentForm
from django.contrib.auth.decorators import login_required

@login_required
def enrollment_create_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student enrolled successfully!")
            return redirect('enrollment_create')
    else:
        form = EnrollmentForm()
    
    return render(request, 'classes/enrollment_form.html', {'form': form})
