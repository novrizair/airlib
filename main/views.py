import datetime
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ItemForm
from main.models import Item
from django.views.decorators.csrf import csrf_exempt
import json

# Mau redeploy
@login_required(login_url='/login')
def show_main(request):
    items = Item.objects.filter(user=request.user)
    counting = items.count()

    context = {
        'nama': request.user.username,
        'kelas': 'PBP A', 
        'aplikasi': "airlib",
        'counting': counting,
        'items': items,
        #'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            #response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    #response.delete_cookie('last_login')
    return response

def adding_amount(request, id):
    try:
        items = Item.objects.get(pk=id)

        if request.method == 'GET':
            items.amount += 1
            items.save()
            return redirect('main:show_main')
        return redirect('main:show_main')
    
    except Item.DoesNotExist:
        raise Http404("Item Anda tak dapat ditemukan.")
    
def removing_amount(request, id):
    try:
        items = Item.objects.get(pk=id)

        if request.method == 'GET':
            items.amount -= 1
            items.save()

            if items.amount == 0:
                items.delete()
            return redirect('main:show_main')
        return redirect('main:show_main')
    
    except Item.DoesNotExist:
        raise Http404("Item Anda tak dapat ditemukan.")
    

def deleting_amount(request, id):
    try:
        items = Item.objects.get(pk=id)

        if request.method == 'GET':
            items.delete()
            return redirect('main:show_main')
        return redirect('main:show_main')
    
    except Item.DoesNotExist:
        raise Http404("Item Anda tak dapat ditemukan.")

def edit_item(request, id):
    # Get item berdasarkan ID
    items = Item.objects.get(pk = id)

    # Set item sebagai instance dari form
    form = ItemForm(request.POST or None, instance=items)

    if form.is_valid() and request.method == "POST":

        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_item.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        price = request.POST.get("price")  # Get the price from the request
        description = request.POST.get("description")
        user = request.user

        new_product = Item(name=name, amount=amount, description=description, price = price, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])
    item.delete()

    return HttpResponse("DELETED", status = 200)

@csrf_exempt
def add_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])
    
    item.amount += 1
    item.save()

    return HttpResponse(status = 200)

@csrf_exempt
def remove_amount_ajax(request):
    data = json.loads(request.body.decode("utf-8"))
    item = Item.objects.get(pk=data["id"])

    if item.amount > 1:
        item.amount -= 1
        item.save()

    return HttpResponse(status = 200)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            amount = int(data["amount"]),
            price = int(data["price"]),
            description = data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)