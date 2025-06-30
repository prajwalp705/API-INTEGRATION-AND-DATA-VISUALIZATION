import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# === CONFIGURATION ===
API_KEY = "852ec963443225132496c17cde11004a"  # 👈 Paste your key here
CITY = "Mumbai"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# === FETCHING DATA ===
response = requests.get(URL)
data = response.json()

# === EXTRACT TEMPERATURE DATA ===
dates = []
temps = []

for entry in data['list']:
    dt = datetime.datetime.fromtimestamp(entry['dt'])
    temp = entry['main']['temp']
    dates.append(dt)
    temps.append(temp)

# === VISUALIZATION ===
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker="o", color="orange")

plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
