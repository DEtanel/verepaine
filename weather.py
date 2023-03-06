import pyowm
owm =pyowm.OWM('f8c43bbd601d39c177afabec2d050d04')
mgr = owm.weather_manager()
weather_pressure = mgr.weather_at_place('Helsinki').weather.pressure  # 'weather', not 'observation'
pressure_value=weather_pressure['press']
print(pressure_value)


# Weather = mgr.weather_at_place('Helsinki')
# Data = Weather.weather
# temp = Data.pressure
# print(temp)
