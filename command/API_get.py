from command.arcadia_functions import arcadia
from command.get_token import token_details
from dataclasses import dataclass, field
from dotenv import load_dotenv
import os

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

@dataclass
class APIget:
    """API endpoint\n 
    games | variants | sets | products | products_files | products_sets"""
    endpoint: str
    url: str = field(init=False)
    END_URL: str = field(init=False)
    
    def __post_init__(self):
        self.END_URL = self.locate_endpoint()
        self.url = f'{BASE_URL}{self.END_URL}'

    def locate_endpoint(self) -> str:
        API_ENDPOINT = {
            'games': '/items/games',
            'variants': '/items/variants',
            'sets': '/items/sets',
            'products': '/items/products',
            'products_files':'/items/products_files',
            'products_sets':'/items/products_sets',
            'directus_files':'/files'
        }
        try:
            return API_ENDPOINT[self.endpoint]
        except KeyError:
            raise ValueError('Invalid API endpoint. Choose from: game, variants, sets, products_files, products_sets, directus_files')

    def access(self):
        API_TOKEN = token_details()
        headers = { 
            "Content-Type": "application/json",
            "User-Agent": "insomnia/10.1.1",
            "Authorization": f'Bearer {API_TOKEN}'
        }
        return arcadia(url=self.url, headers=headers)
    
    def All(self) -> list:
        all_data = []
        offset = 0
        limit = 1000
        retry = 0
        max_retry = 10
        while retry<max_retry:
            data = self.access()
            params = {"limit": limit, "offset": offset}
            response = data.getting(params=params)

            if response.status_code == 200 and response.json()['data'] != []:
                all_data.extend(response.json()['data'])
                offset += limit
            elif response.json()['data'] == []:
                break
            elif response.status_code != 200 and retry == 9:
                retry += 1
                print(f'Max retry reached - Unable to Reach Server\nStatus Code: {response.status_code}\nText: {response.text}')
            else:
                retry += 1

        return all_data
    
    def Large_Data_Get(self, offset:int=0, limit:int=1000):
        """Manual input of offset and limit, in the case where large amount of data cannot be stored in cache"""
        data = self.access()
        params = {"limit": limit, "offset": offset}
        response = data.getting(params=params)
        return response

    def ByExactName(self, name: str):
        data = self.access()
        params = {"filter[name][_eq]": name}
        response = data.getting(params=params)
        return response
    
    def ByExactKeyValue(self, key:str, value:str):
        data = self.access()
        params = {f"filter[{key}][_eq]": value}
        response = data.getting(params=params)
        return response
    
    def BySetId(self, set_id: str):
        data = self.access()
        params = {"filter[set][_eq]": set_id}
        response = data.getting(params=params)
        return response
    
    def ByVariantId(self, variant_id: str):
        data = self.access()
        params = {"filter[variant][_eq]": variant_id}
        response = data.getting(params=params)
        return response
    
    def ByGameId(self, game_id:str):
        data = self.access()
        params = {"filter[game][_eq]": game_id}
        response = data.getting(params=params)
        return response
    
    def ById(self, id_: str):
        data = self.access()
        params = {"filter[id][_eq]": id_}
        response = data.getting(params=params)
        return response