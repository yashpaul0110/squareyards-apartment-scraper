import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://www.squareyards.com/sale/property-in-bangalore?listing_type=sale&city_name=Bangalore&search_type=city&property_type=ready-to-move")
time.sleep(5)

try:
    apt_filter = driver.find_element("xpath", "//label[contains(., 'Apartment')]")
    apt_filter.click()
    time.sleep(5)
except Exception as e:
    print("Apartment filter could not be applied:", e)

for _ in range(10):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

soup = BeautifulSoup(driver.page_source, 'html.parser')
listings = soup.find_all("div", class_="propCard", limit=100)

data = []
for card in listings:
    try:
        name = card.find("h2").get_text(strip=True)
        location = card.find("div", class_="locWrap").get_text(strip=True)
        price_str = card.find("div", class_="priceSection").get_text(strip=True)
        p = price_str.replace('₹', '').replace('Onwards', '').split('-')
        min_price = p[0].strip()
        max_price = p[1].strip() if len(p) > 1 else min_price
        photo_url = card.find("img")['src'] if card.find("img") else ""
        listing_url = "https://www.squareyards.com" + card.find("a", href=True)['href']
        data.append([name, location, min_price, max_price, photo_url, listing_url])
    except Exception as e:
        print("Error in one listing:", e)

df = pd.DataFrame(data, columns=[
    "Apartment Name", "Location", "Minimum Price",
    "Maximum Price", "Photo URL", "Listing URL"
])
df.to_csv("apartments_data.csv", index=False)

driver.quit()
