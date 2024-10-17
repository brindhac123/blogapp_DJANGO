from django.shortcuts import render

def custom_page_not_found(request,exception):
    return render(render,'404.html',status=404)