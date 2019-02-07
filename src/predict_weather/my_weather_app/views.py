import requests # used to send requests without much manual labour
from django.shortcuts import render,redirect
from my_weather_app.models import City
from my_weather_app.forms import CityForm
from django.views.decorators.http import require_POST
# Create your views here.
#think as of two cases one is the one when page is viewed and other is when finding the weather
def index(request):

    # url='https://api.openweathermap.org/data/2.5/weather?q={}&APPID=365a9cdd0b5c3311e3232c7e9c6c4a9b'
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=365a9cdd0b5c3311e3232c7e9c6c4a9b'
    form=CityForm()

    #creating instance of class in views.py file
    #requests is a python library for grabing ,posting etc data from the web
    #get method is used to get data from a web and using get("http://www....") ie giving url as parameter
    #allows to grab data from the given web page
    #r is a response object so we can convert to text using r.text not r.txt
    weather_data=[]
    cities=City.objects.all()
    for city in cities:
        r=requests.get(url.format(city.name)).json()
        city_weather={
          'city':city,
          'temperature':r['main']['temp'],
          'description':r['weather'][0]['description'],
          'icon':r['weather'][0]['icon']
          }
        # print(city_weather)
        # if 'main' in r:
        #     print("yes")
        weather_data.append(city_weather)
    context= {'weather_data':weather_data,'form':form}
    return render(request,"my_weather_app/index.html",context)
@require_POST
def addCity(request):
    url='http://api.openweathermap.org/data/2.5/weather?q={}&APPID=365a9cdd0b5c3311e3232c7e9c6c4a9b'
    form=CityForm(request.POST)
    if(form.is_valid()):
        form.save()
    return redirect('index')


    #print(r.text) as once converted to json data cant do r.text as text is no such argument


    #now we will pass the data to the templates,so far we need name of city ,
    #temp ,description of weather and icon ,so temp,description and icon comes from the api while
    #the name of city comes from our app.So we will make a dictionary(not json data) that will represent all our info
    #and we also convert result above ie response object to json object.
    #dont forget that dictionary in python have keys and values and it is not compulsary to keep any of them in ""
    #besides on rhs here is the value stored
