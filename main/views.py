from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245560',
        'name': 'Salsabila Arumdapta',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
