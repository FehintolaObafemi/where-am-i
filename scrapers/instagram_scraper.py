import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json

def insta_scraper(username):
    response = requests.get(f"https://www.instagram.com/{username}")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    else:
        return "User doesn't exist"
    
    scripts = soup.find_all('script')

    for s in scripts:
        try:
            content = s.contents[0]
            data_object = content[content.find('{"config"') : -1]

            # check if object exists
            if data_object != '':
                data_json = json.loads(data_object)
                break
        except Exception as e:
            print(f'Error has occurred: {e}')

    data_json = data_json['entry_data']['ProfilePage'][0]['graphql']['user']
    
    result = {
            'biography': data_json['biography'],
            'external_url': data_json['external_url'],
            'followers_count': data_json['edge_followed_by']['count'],
            'following_count': data_json['edge_follow']['count'],
            'name': data_json['full_name'],
            'is_private': data_json['is_private'],
            'verified': data_json['is_verified'],
            'is_business_account': data_json['is_business_account'],
            'pfp_url': data_json['profile_pic_url_hd'],
            'total_posts': data_json['edge_owner_to_timeline_media']['count'],
            'url': f'https://www.instagram.com/{username}'
        }

    return result
