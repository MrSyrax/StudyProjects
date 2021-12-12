from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

MY_EMAIL = 'kevinlearningpython@gmail.com'
PASSWORD = '5426233Kk!!'
MAX_PRICE = 110.00

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Accepted-Language': 'en-US,en;q=0.9'
}
url = 'https://www.amazon.com/dp/B0833MMN67/ref=sspa_dk_hqp_detail_aax_0?spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTlJTOEw1RVBZNlA2JmVuY3J5cHRlZElkPUEwMDkwNDE3WVcwUTBYTjUxMlcmZW5jcnlwdGVkQWRJZD1BMDE0ODg3NU9DTjBOQkwzN1JXJndpZGdldE5hbWU9c3BfaHFwX3NoYXJlZCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1'

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
price_data = soup.find(id='apex_desktop')
price = price_data.span.span.get_text()
price_as_float_formatted = float(price.split('$')[1])

if price_as_float_formatted < MAX_PRICE:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='kevincarrillo89@yahoo.com',
            msg=f'Subject:AMAZON Price Alert!\n\nprice for OLIGHT Baldr Pro 1350 Lumens is now only: {price_as_float_formatted}! LINK:{url}'
        )

