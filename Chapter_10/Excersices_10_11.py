import json


def store_numbers():
    
    fileNam = "FavNumbers.json"
    
    try:
        with open(fileNam) as f:
            favNum = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return favNum


def get_new_favoriteNumber():
    favorite_number = input('Insert your favorite number ')
    fileNam = "FavNumbers.json"
    
    with open(fileNam, 'w') as f:
        json.dump(favorite_number, f)
    
    return favorite_number

def mainRead():
    
    favNumber = store_numbers()
    if favNumber:
        print(f'i know your favorite number is {favNumber}')
    else:
        favNumber = get_new_favoriteNumber()
        print(f'thanks, now i know your favorite number is {favNumber}')
        
mainRead()
            
        