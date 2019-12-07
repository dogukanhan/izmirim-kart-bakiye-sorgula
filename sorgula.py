import requests
import sys
import re
pattern = re.compile("[\d]{5}[-][\d]{5}[-][\d]")

cookies = {
    'eshcookie2': 'eshot'
}

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Origin': 'https://online.eshot.gov.tr',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://online.eshot.gov.tr/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
}





if len(sys.argv) < 2:
	print("Lutfen kart numarasini girin")
	exit()

kartNumarasi = sys.argv[1]

if not pattern.match(kartNumarasi):
	print("Numara XXXXX-XXXXX-X formatinda olmalidir")
	exit()

data = {
  'aliasNo': kartNumarasi
}

response = requests.post('https://online.eshot.gov.tr/BakiyeSorgula/BakiyeSorgula/', headers=headers, cookies=cookies, data=data)

print(response.text)



