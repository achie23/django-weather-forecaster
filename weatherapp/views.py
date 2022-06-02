from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=e16ee997807b8a2cbf152eb8b77d71da').read()
        json_data = json.loads(res)
        data = {
            "name": str(json_data['name']),
            "country_code": str(json_data['sys']['country']),
            "lon": str(json_data['coord']['lon']),
            "lat": str(json_data['coord']['lat']),
            "temp": str(round(json_data['main']['temp'] - 273.15, 1)) +'°C',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "weather": str(json_data['weather'])      
        }
        
    else:
        city = ''
        data = {}
        
    return render(request, 'index.html', {'city': city, 'data': data})