import csv
import requests
from bs4 import BeautifulSoup

# Url of the website
response = requests.get("https://www.scrapethissite.com/pages/simple/")
soup = BeautifulSoup(response.text, "html.parser")

# Get all the country blocks HTML Element
country_blocks = soup.find_all("div", {"class": "col-md-4 country"})

result = []

for block in country_blocks:

    # Get Content with Specific Element
    name_element = block.find("h3", {"class": "country-name"})
    country_name = name_element.get_text(strip=True)

    capital_element = block.find("span", {"class": "country-capital"})
    capital_name = capital_element.get_text(strip=True)

    population_element = block.find("span", {"class": "country-population"})
    population_name = population_element.get_text(strip=True)

    # Add to result
    result.append(
        {
            "name": country_name,
            "capital": capital_name,
            "population": population_name
        }
    )


# Loop the result
for item in result:
    print(
        {
            f"Country: {item['name']}, Capital: {item['capital']}, Population: {item['population']}"
        }
    )


# Export to CSV
# with open("country.csv", "w", newline="", encoding="utf-8") as csvfile:
#     fieldnames = ["name", "capital", "population"]
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()

#     for item in result:
#         writer.writerow(item)