import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


API_KEY = 'YOUR_API_KEY'  # Replace with your API key from https://openweathermap.org/
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'


response = requests.get(URL)
data = response.json()


dates = []
temps = []
humidities = []

for entry in data['list']:
    dt = datetime.strptime(entry['dt_txt'], '%Y-%m-%d %H:%M:%S')
    temp = entry['main']['temp']
    humidity = entry['main']['humidity']

    dates.append(dt)
    temps.append(temp)
    humidities.append(humidity)

#Create Visualization 
plt.figure(figsize=(14, 6))

# Temperature Plot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temps, color='tomato')
plt.title(f'Temperature Forecast in {CITY}')
plt.xlabel('Date-Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)

# Humidity Plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidities, color='royalblue')
plt.title(f'Humidity Forecast in {CITY}')
plt.xlabel('Date-Time')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()
plt.show()
