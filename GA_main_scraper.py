import requests
from command.tools.ArcaneUtils import fetch_json
import json
from pathlib import Path


def img_grab(link, card_name, set):


    folder_path = Path(f"{set}")
    folder_path.mkdir(parents=True, exist_ok=True)
    url = f"https://api.gatcg.com{link}"

    response = requests.get(url)

    # Save image to file
    with open(f"{folder_path}/{card_name}.jpg", "wb") as f:
        f.write(response.content)

page = 0
total_pages = 1 ##Placeholder, if updating the file, you might have to manual input the new amount of total pages
while page < total_pages:
    try:
        page += 1
        response = requests.get("https://api.gatcg.com/cards/search",
    params={
      "page": f"{page}"
    }
)
        data = response.json()
        for card in data["data"]:
            set_name = card["result_editions"][0]["set"]["prefix"]
            card_name = card["name"]
            img_link = card["editions"][0]["image"]
            img_grab(img_link, card_name, set_name)
            f1 = fetch_json(file_name=f"{set_name}/{set_name}_scrapper")
            f1.add(card)

        total_pages = data["total_pages"]
        
    except:
        break


'''
file_path = "GA_scrapper.json"
with open(file_path, "r") as f:
    all_cards = json.load(f)
f2 = fetch_json(file_name="GA_Card_list")
card_data = f[0]["data"] ##First index is all list of all dictionaries of cards
for card in card_data:
    card_dat = {
        "product_code": 
    }
'''
###Due to hiatus on the app, uuid not implemented yet, however image generation and card data is scrapped

