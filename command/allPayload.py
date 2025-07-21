#ALL PAYLOAD
def gamePL(uuid, 
           name, 
           status=None):
    return {
    "id":uuid,
    "name": name,
    "status":status
    }

def varPL(uuid, 
          name, 
          game_id, 
          status=None):

    return {
    "id":uuid,
    "name": name,
    "game":game_id,
    "status":status
    }

def setPL(
        uuid, 
        variant_id, 
        name, 
        product_code, 
        metadata=None,  
        release_date=None, 
        status=None,
        card_sized_image=None,
        banner_sized_image=None):
    return {
    "id":uuid,
    "description": metadata,
    "name": name,
    "product_code": product_code,
    "variant": variant_id,
    "release_date":release_date, 
    "status":status,
    "card_sized_image":card_sized_image,
    "banner_sized_image":banner_sized_image
    }

def prodPL(uuid, 
           name, 
           description, 
           product_code, 
           rarity, 
           variant_id, 
           metadata=None,
           status=None):
    return {
    "id":uuid,
    "name":name,
    "description": description,
    "product_code": product_code,
    "rarity": rarity,
    "attributes": metadata,
    "variant":variant_id,
    "status":status
    }

def prod_to_set(id_, products_id, sets_id):
    return {
        "relation_id":id_,
        "products_id":products_id,
        "sets_id":sets_id
    }

def prod_to_img(id_, products_id, directus_files_id):
    return {
        "relation_id":id_,
        "products_id":products_id,
        "directus_files_id":directus_files_id
    }