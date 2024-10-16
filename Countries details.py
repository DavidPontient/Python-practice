# countries details
from bs4 import BeautifulSoup
import requests
page= requests.get("https://www.scrapethissite.com/pages/simple/")
soup= BeautifulSoup(page.text, "html.parser")

countries= soup.findAll("h3", attrs={"class":"country-name"})
capitals= soup.findAll("span", attrs={"class":"country-capital"})
population= soup.findAll("span", attrs={"class":"country-population"})
area= soup.findAll("span", attrs={"class":"country-area"})

print("Enter name of Country or (all) to for all countries" )
name= input("Country: ").strip()
#Flag to check if any country was found
country_found = False

for country,capital,people,size in zip(countries, capitals, population, area):
    country_name=country.text.strip()
    if country_name == name.strip():
        print(f"Country: {country_name} \nCapital: {capital.text}\nPopulation: {people.text}\nArea (km^2): {size.text}\n")
        country_found= True #mark as done
    elif name == "all":
        print(f"Country: {country_name} \nCapital: {capital.text}\nPopulation: {people.text}\nArea (km^2): {size.text}\n")
        country_found =True #mark as done
if name.lower() != "all" and not country_found:
    print("Country not found")
    
    