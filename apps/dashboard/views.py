from django.shortcuts import render


def index_view(request):
    """
    Dashboard homepage with links to all key sections of the application.
    """
    return render(request, "dashboard/index.html")
