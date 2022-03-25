import requests
from sys import argv


def main():
    poke_id = argv[1]

    user_info = get_user_info(poke_id)

    if user_info:
      pastebin_strings = get_title_and_text(user_info)
      pastebin_url = post_to_pastebin(pastebin_strings[0], pastebin_strings[1])
      print(pastebin_url)

def post_to_pastebin(title, body_text):

    print("Posting to PasteBin...", end='')

    params = {
      'api_dev_key': "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X",
      'api_option': 'paste',
      'api_paste_code': body_text,
      'api_paste_name': title
    }
    URL = 'https://pastebin.com/api/api_post.php'
    response = requests.post(URL, data=params)

    if response.status_code == 200:
      print('success')
      return response.text # Converts response body to a string
    else:
      print('failed. Response code:', response.status_code)
      return response.status_code


  



def get_title_and_text(user_dict):

    body_text = ""

    for ability in user_dict["abilities"]:
        body_text += str(user_dict["abilities"][0]["ability"]["name"])
          
      
        print(body_text)

        title = user_dict['name'] + "'s abilities"

        return (title, body_text)
    

def get_user_info(poke_id):
      
      print("Getting user information.")
      response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_id))

      if response.status_code == 200:
        print('Success')
        return response.json()
      else:
        print('Failed, Response code:', response.status_code)
        return
    

main()