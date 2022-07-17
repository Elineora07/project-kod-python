# calendar
# import calendar
# print(calendar.month(2022, 2))

emojies = {
    'clear sky': {'d': '☀️', 'n': '🌑'},
    'few clouds': {'d': '🌤', 'n': '☁️'},
    'scattered clouds': {'d': '☁️', 'n': '☁️'},
    'broken clouds': {'d': '☁️', 'n': '☁️'},
    'shower rain': {'d': '🌧', 'n': '🌧'},
    'rain': {'d': '🌦 ', 'n': '🌧'},
    'thunderstorm': {'d': '🌩', 'n': '🌩'},
    'snow': {'d': '❄️', 'n': '❄️'},
    'mist': {'d': '🌫', 'n': '🌫'},
    }
print(emojies['shower rain']['d'])