import requests
from io import BytesIO
import random

def generate_waifu_image(emotion="default"):
    # API gratuita para imagens de anime
    tags = {
        "happy": ["smile", "happy"],
        "sad": ["cry", "sad"],
        "love": ["blush", "embarrassed"],
        "default": ["peace"]
    }
    
    api_url = "https://api.waifu.im/search"
    params = {
        "included_tags": tags.get(emotion, tags["default"]),
        "height": ">=600"
    }
    
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data['images']:
            img_url = data['images'][0]['url']
            img_data = requests.get(img_url).content
            return BytesIO(img_data)
    
    # Fallback se API falhar
    return generate_fallback_image(emotion)

def generate_fallback_image(emotion):
    # Imagens pré-definidas como fallback
    fallback_images = {
        "happy": "https://i.imgur.com/example1.jpg",
        "sad": "https://i.imgur.com/example2.jpg",
        "love": "https://i.imgur.com/example3.jpg",
        "default": "https://i.imgur.com/example4.jpg"
    }
    img_url = fallback_images.get(emotion, fallback_images["default"])
    img_data = requests.get(img_url).content
    return BytesIO(img_data)
