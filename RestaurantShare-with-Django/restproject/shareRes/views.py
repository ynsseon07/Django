from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    #return HttpResponse('index')
    categories = Category.objects.all() # select * from shareRes_category;
    restraunts = Restaurant.objects.all()
    content = {'categories' : categories, 'restaurants': restraunts}
    return render(request, 'shareRes/index.html', content)

def categoryCreate(request):
    #return HttpResponse('categoryCreate')
    return render(request, 'shareRes/categoryCreate.html')

def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name = category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantCreat(request):
    categories = Category.objects.all()
    content = {'categories': categories}
    return render(request, 'shareRes/restaurantCreate.html', content)

def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name = name, restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantDetail(request, res_id):
    restaurant = Restaurant.objects.get(id = res_id) # select * from shareRes_restaurant where id=3(res_id)
    content = {'restaurant' : restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)

def restaurantUpdate(request, res_id):
    categories  = Category.objects.all()
    restaurant = Restaurant.objects.get(id = res_id) # select * from shareRes_restaurant where id=3(res_id)
    content = {'categories' : categories, 'restaurant' : restaurant}
    return render(request, 'shareRes/restaurantUpdate.html', content)

def Update_restaurant(request):
    resId = request.POST['resId']
    change_category_id = request.POST['resCategory']
    # select * from shareRes_restaurant where id=3(res_id)
    change_name = request.POST['resTitle']
    change_category = Category.objects.get(id = change_category_id) 
    change_link = request.POST['resLink']
    change_content = request.POST['resContent']
    change_keyword = request.POST['resLoc']

    # update category=change_category, restaurant_name = change_name, ....
    # from shareRes_restaurant
    # where id=3
    
    before_restaurant = Restaurant.objects.get(id = resId)
    before_restaurant.category = change_category
    before_restaurant.restaurant_name = change_name
    before_restaurant.restaurant_link = change_link
    before_restaurant.restaurant_content = change_content
    before_restaurant.restaurant_keyword = change_keyword
    before_restaurant.save()
    return HttpResponseRedirect(reverse('resDetailPage', kwargs={'res_id':resId}))

def Delete_restaurant(request):
    res_id = request.POST['resId']

    #delete from shareRes_restaurant where id=res_id
    restaurant = Restaurant.objects.get(id = res_id)
    restaurant.delete()
    return HttpResponseRedirect(reverse('index'))