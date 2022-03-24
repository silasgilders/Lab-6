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

      print("Posting to PasteBin.", end='')

      pastebin_params = {
      'api_dev_key': "jhEO8O21WXqbcq8pNdhYWgqJOiNFXgd-",
      'api_option': 'paste',
      'api_paste_code': body_text,
      'api_paste_name': title
    }
    

      response = requests.post('https://pastebin.com/api/api_post.ph', data = pastebin_params)

      if response.status_code == 200:
        print('Success')
        return response.json()
      else:
        print('Failed, Response code:', response.status_code)
        return


  



def get_title_and_text(user_dict):

    body_text = ""

    for ability in user_dict["abilities"]:
        body_text += str(user_dict["abilities"])
      
        print(body_text)

        title = user_dict['name'] + "'s Abilities"

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