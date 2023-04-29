# Modules
import requests as req

# Variables
url = 'https://raw.githubusercontent.com/noidentity29/AppliedCryptoPython/master/secret.txt'
r = req.get(url)
file = open('text.txt', 'wb')

# Response and file operations
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.content)
file.write(r.content)
