from django.shortcuts import render
from .models import Category, Photo
import locale

# Create your views here.
def gallery(request):
   
    category = request.GET.get('category')
    if category == None : 
        photos = Photo.objects.all()
    else :
        photos = Photo.objects.filter(category__name__contains=category)    
    
    categories = Category.objects.all()    
    
    context = {'categories' : categories , 'photos' : photos}
    return render(request,'photo/galery.html', context)

def detailPhoto(request, pk):
    locale.setlocale(locale.LC_ALL, 'id_ID')
    photo = Photo.objects.get(id=pk)
    formatted_price = locale.currency(photo.price, grouping=True, symbol=False)
    return render(request,'photo/detailPhoto.html', {'photo' : photo, 'formatted_price': formatted_price})

def home(request):
    category1 = 'Ngabers'
    category2 = 'Basement'

    photosCarousel = Photo.objects.filter(category__name__contains=category1)
    photosPigora = Photo.objects.filter(category__name__contains=category2)
    context = {'photosCarousel' : photosCarousel, 'photosPigora' : photosPigora}
    return render(request,'photo/home.html', context)