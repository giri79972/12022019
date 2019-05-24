from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def create_cooke(request):
    if not request.COOKIES.get('color'):
        response=HttpResponse('Cookie is Created')
        response.set_cookie('color','blue')
        return response
    else:
        return HttpResponse("Your Favorite color is {0}".format(request.COOKIES['color']))
def count_cookie(request):
    if not request.COOKIES.get('visits'):
        response=HttpResponse("This is your First Visit to the site,"
                              "From now on i will track"
                              "Your visits to this site.")
        response.set_cookie("visits",'1')
    else:
        visits=int(request.COOKIES.get("visits"))+1
        response=HttpResponse("This is your {0} visit".format(visits))
        response.set_cookie('visits',str(visits))
    return response
def delete_cookie(request):
    if request.COOKIES.get('visits'):
        response=HttpResponse('Cookies Cleared')
        response.delete_cookie("visits")
    else:
        response =HttpResponse("We are not Tracking you.")
    return response