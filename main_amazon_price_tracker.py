"""
    Use BeautifulSoup to Scrape the Product Price in amazon web site
"""
import requests
import lxml
from bs4 import BeautifulSoup

# Find a product on Amazon that you want to track and get the product URL or just use the one I'm tracking.
#url = "https://www.amazon.com/Duo-Evo-Plus-esterilizadora-vaporizador/dp/B07W55DDFB/ref=sr_1_4?qid=1597660904"
url = "https://www.amazon.com/dp/B0849SDZX7/ref=sbl_dpx_kitchen-electric-cookware_B01MFEBQH1_0?th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

"""
#print(soup.prettify())
....
<span id="productTitle" class="a-size-large product-title-word-break">Aroma Housewares ARC-994SB Rice &amp; Grain Cooker Slow Cook, Steam, Oatmeal, Risotto, 8-cup cooked/4-cup uncooked/2Qt, Stainless Steel</span>
....
<div id="apex_desktop" class="celwidget" data-feature-name="apex_desktop" data-csa-c-id="6l35s5-n192ll-2usxwf-r1droy" data-cel-widget="apex_desktop">
    <span class="a-price a-text-price a-size-medium apexPriceToPay" data-a-size="b" data-a-color="price">
        <span class="a-offscreen">$38.56</span>
        <span aria-hidden="true">$38.56</span>
    </span>
</div>
"""
title = soup.find(id="productTitle").get_text().strip()
print(title)
# title : <span id="productTitle" class="a-size-large product-title-word-break">Aroma Housewares ARC-994SB Rice &amp; Grain Cooker Slow Cook, Steam, Oatmeal, Risotto, 8-cup cooked/4-cup uncooked/2Qt, Stainless Steel</span>

span_price = soup.select_one("div#apex_desktop span.a-price span.a-offscreen")
# span_price : <span class="a-offscreen">$38.56</span>

price = span_price.get_text()
# price = $38.56

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
# price_as_float = 38.56
print(price_as_float)




# Send Email if PRICE is lower than we expected
# import smtplib
# BUY_PRICE = 200
# if price_as_float < BUY_PRICE:
#     message = f"{title} is now {price}"
#
#     with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
#         connection.starttls()
#         result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
#         connection.sendmail(
#             from_addr=YOUR_EMAIL,
#             to_addrs=YOUR_EMAIL,
#             msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
#         )
