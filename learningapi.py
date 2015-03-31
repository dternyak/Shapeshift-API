import json
import requests
import codecs

amount = 0.003
address = '1DxUV8BYNPNHJYC3dDtZur4i4tVdnw3B7E'
pair = 'btc_ltc'

def check_deposit(pair):
	url2 = 'https://shapeshift.io/limit/' + pair

	g = requests.get(url2)

	json_code2 = g.json()

	limit = json_code2["limit"]

	print json_code2

	print limit

check_deposit('nmc_btc')


def new_payment(amount, address, pair):
	payload = {"amount": amount,
    "withdrawal": address,
    "pair": pair}
	headers = {
	  'Content-Type': 'application/json'
	}
	

	url = 'https://shapeshift.io/sendamount'

	r = requests.post(url, headers=headers, data=json.dumps(payload))

	json_code = r.json()
	print json.dumps(json_code, indent=4, sort_keys=True)

	deposit = json_code["success"]["deposit"]

	deposit_amount = json_code["success"]["depositAmount"]

	withdrawal = json_code["success"]["withdrawal"]

	print deposit

	print deposit_amount

	print withdrawal

def get_coins():

	url = 'https://shapeshift.io/getcoins'

	r = requests.get(url)

	coin = r.json()

	print json.dumps(coin, indent=4, sort_keys=True)

	uni = coin.keys()

	string = [str(x) for x in uni]

	print string


