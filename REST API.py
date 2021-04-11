import requests                                                                       #This module allows you to send HTTP requests using python
response = requests.get('https://www.google.com')                                     #Get is used to retrieve data from the website in between the brackets
print(response.status_code)                                                           #Status code is used to display the status code of the response received.
