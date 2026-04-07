from dotenv import load_dotenv
from langchain_groq import ChatGroq
from tools import battery_check, weather_check, no_fly_zone_check
from memory import save_mission, show_history

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

print("===== UAV MISSION PLANNER =====\n")

mission_type = input("Enter mission type: ")
source = input("Enter source location: ")
destination = input("Enter destination location: ")
distance_km = float(input("Enter distance in km: "))
battery_percent = float(input("Enter battery percentage: "))
weather_condition = input("Enter weather condition: ")
wind_speed = float(input("Enter wind speed in km/h: "))
no_fly_zone_input = input("Is there a no-fly zone? (yes/no): ").strip().lower()

if no_fly_zone_input == "yes":
    no_fly_zone = True
else:
    no_fly_zone = False

battery_result = battery_check(distance_km, battery_percent)
weather_result = weather_check(weather_condition, wind_speed)
zone_result = no_fly_zone_check(no_fly_zone)

prompt = f"""
You are a UAV Mission Planner.

Analyze this mission and give:
1. Mission Summary
2. Tool Results
3. Final Decision
4. Reason
5. Recommendation

Mission Details:
Mission Type: {mission_type}
Source: {source}
Destination: {destination}
Distance: {distance_km} km
Battery: {battery_percent}%
Weather: {weather_condition}
Wind Speed: {wind_speed} km/h
No Fly Zone: {no_fly_zone}

Tool Results:
- {battery_result}
- {weather_result}
- {zone_result}
"""

response = llm.invoke(prompt)

print("\n===== UAV MISSION PLAN =====\n")
print(response.content)

mission_input = {
    "mission_type": mission_type,
    "source": source,
    "destination": destination,
    "distance_km": distance_km,
    "battery_percent": battery_percent,
    "weather_condition": weather_condition,
    "wind_speed": wind_speed,
    "no_fly_zone": no_fly_zone
}

save_mission(mission_input, response.content)

print("\n===== STORED MISSION HISTORY =====\n")
print(show_history())