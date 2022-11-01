from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import HotelForm
from .models import Hotel
# from django.core.exceptions import ValidationError
import os


# Create your views here.
# def validate_file_extension(request):
# 	if request.method == 'POST':

# 		form = HotelForm(request.POST, request.FILES)
# 		if form.is_valid():
# 			form.save()
# 			text = os.path.splitext(request.name)[1]
# 			valid_extensions = ['.json','.txt']

# 	if not text in valid_extensions:

#         	raise ValidationError(u'File not supported!')


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)
        print(type(form))
        if form.is_valid():
            print(type(request.FILES))
            # newdoc = Hotel(hotel_Main_Img=request.FILES['hotel_Main_Img'])

            b =str(newdoc)
            d = b[-4:]
            e = b[-5:]

            if d== '.txt' and e == '.json':
                newdoc.save()

                return HttpResponse('success')

            else:

                return HttpResponse('invalid fileformat')

    else:

        form = HotelForm()

    return render(request, 'index.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
