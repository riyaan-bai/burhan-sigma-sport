from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2406358762',
        'name': 'Riyaan Baihaqi',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)