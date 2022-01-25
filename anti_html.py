from cgitb import reset
from urllib import response
import requests
from bs4 import BeautifulSoup
import sys

if __name__ == "__main__":

    # url = 'https://www.geeksforgeeks.org/python-map-function/'
    url = sys.argv[1]

    response = requests.get(url)
    print(response.status_code, response.reason)
    soup = BeautifulSoup(response.content,'html.parser')
    print(soup.text)