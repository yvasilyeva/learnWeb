import requests
def weather_in_city(city_name):
	weather_url="http://api.worldweatheronline.com/premium/v1/weather.ashx"
	params={
	"key": "dfa639c75f0043ac8e3115948180712",
	"q": city_name,
	"format": "json",
	"num_of_days": 1,
	"lang": "ru"
	}
	try:
		result=requests.get(weather_url, params=params)
		result.raise_for_status()
		weather=result.json()
		if 'data' in weather:
			if 'current_condition' in weather['data']:
				try:
					return weather['data']['current_condition'][0]
				except(IndexError,TypeError):
					return False
	except(requests.RequestException, ValueError):
		print("Network error")
		return False
if __name__ == '__main__':
		print(weather_in_city("Moscow,Russia"))
		