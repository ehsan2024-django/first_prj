from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
import ephem
from .models import City


# Create your views here.
def findNorth(request):

        # تاریخ و زمان را مشخص کنید
    date_1 = datetime.datetime.now()
    dHour = date_1.hour
    dMinute = date_1.minute
    if dMinute <30 :
        dMinute = dMinute+30
        dHour = dHour-4
    else:
        dMinute = dMinute-30
        dHour = dHour-3
    date = str(date_1.year)+'/'+str(date_1.month)+'/'+str(date_1.day)+' '+ str(dHour)+ ':'+str(dMinute)+ ':'+str(date_1.second)

    # مختصات جغرافیایی را مشخص کنید
    city_info = City.objects.all()
    for cityinfo in city_info:
        city_name = cityinfo.city_name
        city_lat = cityinfo.city_lat
        city_long = cityinfo.city_long
    lat = str(city_lat)  # عرض جغرافیایی
    lon = str(city_long)  # طول جغرافیایی
    #print(lat , lon)
    # زمان محلی را مشخص کنید

    # شیء Observer را ایجاد کنید
    obs = ephem.Observer()
    obs.date = date
    obs.lat = lat
    obs.lon = lon
    

    # خورشید را به عنوان یک شیء Sun ایجاد کنید
    sun = ephem.Sun()

    # خورشید را در مختصات جغرافیایی و تاریخ مشخص شده قرار دهید
    sun.compute(obs)

    # سمت و ارتفاع خورشید را محاسبه کنید
    azimuth = sun.az
    altitude = sun.alt


    dic_date_time = {'Date':date_1.date,'Time':date_1.time,'Azimuth':azimuth,'Elevation':altitude}
    #html = "<html><body>It is now %s.</body></html>" % now
    #return HttpResponse(html)
    return render(request,'index.html',context=dic_date_time)

def start(request):
    return redirect('home')

def stop(request):
    return redirect('home')
