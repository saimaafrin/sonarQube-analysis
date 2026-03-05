
import unicodedata
import requests

URL = 'https://api.github.com/users/'

def task_func(username):
    try:
        response = requests.get(URL + username)
        if response.status_code == 200:
            data = response.json()
            normalized_data = {
                'id': data['id'],
                'login': data['login'],
                'avatar_url': data['avatar_url'],
                'html_url': data['html_url'],
                'followers': data['followers'],
                'following': data['following'],
                'public_repos': data['public_repos'],
                'total_gists': data['total_gists'],
                'score': data['score']
            }
            for key, value in normalized_data.items():
                if isinstance(value, str):
                    normalized_data[key] = unicodedata.normalize('NFKD', value).encode('ascii', 'replace').decode('utf-8')
            return normalized_data
        else:
            raise requests.exceptions.HTTPError(response.text)
    except requests.exceptions.HTTPError as e:
        raise e