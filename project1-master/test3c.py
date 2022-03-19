import re
import json
# from urllib import urlopen
import urllib

url = 'http://ipinfo.io/json'
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
# response = urlopen(url)
data = json.load(external_ip)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
import urllib.request

# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

# print(external_ip)
