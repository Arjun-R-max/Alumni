from django.shortcuts import render
def register(request):
    return render(request, 'alumni_app/register.html')
def jobs(request):
    return render(request, 'alumni_app/jobs.html')
def events(request):
    return render(request, 'alumni_app/events.html')
def networking(request):
    return render(request, 'alumni_app/networking.html')