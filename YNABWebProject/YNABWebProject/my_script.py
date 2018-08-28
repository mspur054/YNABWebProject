from passwords import YNAB_KEY
import json
import requests, sys, socket


KEY = YNAB_KEY
BASE_URL = 'https://api.youneedabudget.com/v1'

r = requests.get(BASE_URL + '/user', headers = {'Authorization': YNAB_KEY}

