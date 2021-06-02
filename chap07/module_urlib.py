from urllib import request

target = request.urlopen("http://www.google.com")
output = target.read()

print(output)