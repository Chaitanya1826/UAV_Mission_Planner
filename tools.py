def battery_check(distance_km, battery_percent):
    required_battery = distance_km * 5

    if battery_percent >= required_battery:
        return f"Battery OK. Required: {required_battery}%, Available: {battery_percent}%"
    else:
        return f"Battery LOW. Required: {required_battery}%, Available: {battery_percent}%"

def weather_check(weather_condition, wind_speed):
    weather_condition = weather_condition.lower()

    if weather_condition in ["storm", "thunderstorm", "heavy rain"]:
        return "Weather UNSAFE for mission"

    if wind_speed > 25:
        return f"Weather UNSAFE: wind speed {wind_speed} km/h is too high"

    if weather_condition in ["rain", "drizzle"]:
        return "Weather RISKY: fly with caution"

    return "Weather SAFE for mission"

def no_fly_zone_check(no_fly_zone):
    if no_fly_zone:
        return "Mission REJECTED: route is in no-fly zone"
    return "No no-fly zone issue"