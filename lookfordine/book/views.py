from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from book.models import Booking


# Create your views here.

@login_required(login_url='/auth/login')
def reserveTable(request):

    if request.method == 'POST':

        customer = request.user
        name = request.POST.get('name')
        datetime = str(request.POST.get('date'))
        people = int(request.POST.get('people'))
        message = request.POST.get('message')
        branch = request.POST.get('branch')

        new = Booking(name=name,user=customer,branch=branch,people=people,datetime=datetime,message=message)
        new.save()

        context = {'status':"booked"}

        return render(request, 'book/reserve.html', context)

    else:
        context = {'notbooked':"Notbooked"}
        return render(request, 'book/reserve.html', context)


@login_required(login_url='/auth/login/')
def checkStatus(request):

    reservations = Booking.objects.filter(user=request.user)
    # print(reservations)

    context = {'reservations':reservations}
    return render(request, 'book/check.html', context)