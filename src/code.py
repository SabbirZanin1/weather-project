import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Load dataset
df = pd.read_csv("data\weather_data.csv")

# First 5 rows
#print(df.head())
print(df)

#Dataset info
print(df.info())
avg_temp = df["temperature_C"].mean()
total = df["temperature_C"].sum()

print("Average Temperature:", round(avg_temp, 2), "°C")

highest = df.loc[df["temperature_C"].idxmax()]

print("Highest Temperature Day:")
print("Day:", highest["day"])
print("Temperature:", highest["temperature_C"], "°C")

# Statistics
#print(df.describe())

# Missing values
#print(df.isnull().sum())





fig, ax = plt.subplots(figsize=(12,5))

x = df["day"]
y = df["temperature_C"]

line, = ax.plot([], [], color="#00bfff", linewidth=3, marker="o")

ax.set_xlim(1, 30)
ax.set_ylim(min(y)-2, max(y)+2)

ax.set_xlabel("Day")
ax.set_ylabel("Temperature (°C)")
ax.set_title("Animated Temperature Chart")

def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = FuncAnimation(
    fig,
    animate,
    frames=len(x)+1,
    interval=300,
    blit=True
)

plt.grid(True)
plt.savefig("output/animated_temperature.png")


plt.show()








plt.figure(figsize=(14,3))

heat_data = [df["temperature_C"]]

sns.heatmap(
    heat_data,
    annot=True,
    fmt=".0f",
    cmap="coolwarm",
    cbar_kws={"label": "Temperature °C"},
    xticklabels=df["day"],
    yticklabels=["Temp"]
)

plt.title("Monthly Temperature Heatmap")


#plt.show()




plt.figure(figsize=(12,5))

plt.plot(
    df["day"],
    df["temperature_C"],
    color="#41119b",
    linewidth=3,
    marker="o"
)

plt.fill_between(
    df["day"],
    df["temperature_C"],
    color="#ffa500",
    alpha=0.3
)

plt.xticks(df["day"])

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")

plt.title("Monthly Temperature Analysis")

plt.grid(True, linestyle="--", alpha=0.5)
plt.savefig("output/monthly_temperature.png")
plt.show()











#Pi chart

weather_count = {
    "Hot Days": 10,
    "Rainy Days": 12,
    "Cloudy Days": 8
}

labels = weather_count.keys()
values = weather_count.values()

plt.figure(figsize=(6,6))

plt.pie(values, labels=labels, autopct="%1.1f%%")

plt.title("Weather Condition Distribution")
plt.savefig("output/piChart.png")


plt.show()
                                                                                                            #show



#Temp graph....
plt.plot(df["day"], df["temperature_C"])

plt.xticks(df["day"])

plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trend")
plt.grid(True)  #point grid line plt.show()
plt.savefig("output/temp_chart1.png")



plt.figure(figsize=(8,5))

plt.scatter(df["humidity"], df["rainfall_mm"])

plt.xlabel("Humidity (%)")
plt.ylabel("Rainfall (mm)")
plt.title("Humidity vs Rainfall")

plt.grid(True)
plt.savefig("output/humidity_vs_rainfall.png")


plt.show()                                                                                  #show()







###Extraaaaa








