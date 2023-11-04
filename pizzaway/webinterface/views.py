from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponseRedirect, Http404, HttpResponse
from django.http.request import HttpRequest
from django.urls import reverse

from .models import Order, Pizza, PizzaOrder
from employee.models import Employee

#the most of our views are rather basic

def index(request: HttpRequest):
    return render(request, "index.html", {"pizzas": Pizza.objects.all()})

def order(request: HttpRequest):
    return render(request, "order.html", {"pizzas": Pizza.objects.all()})

def contact(request: HttpRequest):
    return render(request, "contact.html", {})

def imprint(request: HttpRequest):
    return render(request, "imprint.html", {})

def privacy(request: HttpRequest):
    return render(request, "privacy.html", {})


def add_order(request: HttpRequest): #this is the only interesting thing
    #first we retrieve all the arguments from the post list
    name = request.POST.get("customer")
    email = request.POST.get("email")
    notes = request.POST.get("notes")
    pizzas = request.POST.getlist("selected_pizzas[]")
    
    #then we create a order object just to save it again
    #even though there is an easier way to do this which i've used in other parts
    # (i just noticed i even used it in the loop below this... so yeahhh)
    order = Order(customer=name, email=email, notes=notes)
    order.save()

    for pizza in pizzas: # try to create an entry in PizzaOrder for every different pizza
        try:
            p = get_object_or_404(Pizza, name=pizza)
            amount = request.POST.get(f"{p.name}_amount")
            PizzaOrder.objects.create(pizza=p, order=order, amount=amount)
        except Http404: #and return a string if it didn't work because i won't code an entire page just for one edgecase
            return HttpResponse(f"{pizza} was not found in database")
        
    return HttpResponseRedirect(reverse("index")) #and we look up what the url for index is and redirect the user there


def remove_order(request: HttpRequest):
    #delete the order associated with the order_id in the post list
    order = get_object_or_404(Order, id=request.POST.get("order_id"))
    order.delete()
    #and raise the score of the employee that sent the request
    employee = get_object_or_404(Employee, id=request.POST.get("emp_id"))
    employee.orders_cooked += 1
    employee.save()
    return HttpResponseRedirect(reverse("emp_index")) #and back you go weeeee....
