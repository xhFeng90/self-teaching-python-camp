import requests
import os


r = requests.get('https://httpbin.org/get')

f = open('response.txt','w')
f.write(r.text)



print(r.json()['origin'])
