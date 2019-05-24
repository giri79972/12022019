from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test_session(request):
    request.session.set_test_cookie()
    return HttpResponse("Cookie is Set in the server")
def test_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response=HttpResponse("Session Deleted")
    else:
        response=HttpResponse("Session is not Available")
    return response
def save_session_data(request):
    request.session['Eno']=1001
    request.session['Ename']='Narayana'
    request.session['Language']='Python'
    request.session['Framework']='Django'
    return HttpResponse("Session Data Saved")
def access_session_data(request):
    response=""
    if request.session.get('Eno'):
        response+="Eno:{0}<br>".format(request.session.get('Eno'))
    if request.session.get('Ename'):
        response+="Eno:{0}<br>".format(request.session.get('Ename'))
    if request.session.get('Language'):
        response+="Eno:{0}<br>".format(request.session.get('Language'))
    if request.session.get('Framework'):
        response+="Eno:{0}<br>".format(request.session.get('Framework'))
    if not response:
        return HttpResponse("No Session data")
    else:
        return HttpResponse(response)
def delete_session_data(request):
    try:
        del request.session['Eno']
        del request.session['Ename']
        del request.session['Language']
        del request.session['Framework']
    except KeyError:
        pass
    return HttpResponse("Session Data Cleared")