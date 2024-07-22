from bs4 import BeautifulSoup
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


URL="https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
}



response = requests.get(URL, headers=header)
bs = BeautifulSoup(response.text, "html.parser")
product_title = bs.find("span", id="productTitle")
product_title = ' '.join(product_title.text.split()).encode('ascii', 'ignore').decode('ascii')

whole_price = bs.find("span", class_="a-price-whole").get_text()
fraction_price = bs.find("span", class_="a-price-fraction").get_text()

complete_price = float(f"{whole_price}{fraction_price}")

if complete_price < 100.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.getenv("MY_EMAIL"), password=os.getenv("MY_PASSWORD"))
        connection.sendmail(
            from_addr=os.getenv("MY_EMAIL"),
            to_addrs="test@gmail.com",
            msg=f"Subject:Amazon Price Drop Alert!\n\nHey There,\n\n {product_title} is now available at {complete_price}"
        )
