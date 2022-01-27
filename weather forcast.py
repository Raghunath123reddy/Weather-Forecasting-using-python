import requests
city = input("input the city name ")
print(city)

print("Diplaying weather report for : " + city)

url = "https://wttr.in/{}".format(city)

result = requests.get(url)

print(result.text)
