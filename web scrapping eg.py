from bs4 import BeautifulSoup
import requests

# page= requests.get("https://www.merriam-webster.com/dictionary/scrape")
# soup= BeautifulSoup(page.text, "html.parser")

# quotes= soup.findAll("span", attrs={"class":"dtText"})
# num= soup.findAll("span", attrs={"class":"lext"})

# # for quote in quotes:
# #     print(quote.text)
# for number in num:
#     print(number.text)

page= requests.get("https://www.scrapethissite.com/pages/simple/")
soup= BeautifulSoup(page.text, "html.parser")

countries= soup.findAll("h3", attrs={"class":"country-name"})
capital= soup.findAll("span", attrs={"class":"country-capital"})

for country,city in zip(countries, capital):
    name="Rwanda".lower()
    country_name=country.text.strip().lower()
    #country_name= len(country.text.strip()) # removes extra white space/ this will display character length of country
    if country_name == str(name):
        print(f"Country name: {country.text.strip()} \nCapital city: {city.text}\n ")
 
 
 
 
 
 
 
 
 