import random

import requests

from time import sleep





# Function to get a list of English words from a remote source

def get_english_words():

    response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')



    if response.status_code == 200:

        words = response.text.split()

        return set(word.lower() for word in words)

    else:

        print(f"Failed to fetch English words. Status code: {response.status_code}")

        return set()





# Load the English words set

english_words = get_english_words()



# Discord webhook URL

discord_webhook_url = "https://discord.com/api/webhooks/1181066194053234789/wGz4fQsJiHwYUF2XwwMu6PeZmJCuyX3-KePnk2a39oFru24w4EJDgOFnXJSOIUiwwPFY"





def generate_4_to_5_character_username():

    while True:

        # Choose a random 4-5 character word from the English dictionary

        import random

        import requests

        from time import sleep



        # Function to get a list of English words from a remote source

        def get_english_words():

            response = requests.get('https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt')



            if response.status_code == 200:

                words = response.text.split()

                return set(word.lower() for word in words)

            else:

                print(f"Failed to fetch English words. Status code: {response.status_code}")

                return set()



        # Load the English words set

        english_words = get_english_words()



        # Discord webhook URL

        discord_webhook_url = "https://discord.com/api/webhooks/1181066194053234789/wGz4fQsJiHwYUF2XwwMu6PeZmJCuyX3-KePnk2a39oFru24w4EJDgOFnXJSOIUiwwPFY"



        def generate_4_to_5_character_username():

            while True:

                # Choose a random 4-5 character word from the English dictionary

                word = random.choice([w for w in english_words if 4 <= len(w) <= 5])



                if word:

                    return word.lower()



        def generate_any_english_word_username():

            # Choose a random word from the English dictionary without character limits

            return random.choice(list(english_words)).lower()



        def check_tiktok_username_availability(username):

            url = f'https://www.tiktok.com/@{username}'

            response = requests.get(url)



            if response.status_code == 200:

                # The username is not available

                return False

            elif response.status_code == 404:

                # The username is available

                return True

            else:

                # Handle other status codes as needed

                print(f"Unexpected status code: {response.status_code}")

                return False



        def send_to_discord_webhook(username):

            discord_data = {

                "content": f"New Available TikTok Username: {username}"

            }

            response = requests.post(discord_webhook_url, json=discord_data)



            if response.status_code != 204:

                print(f"Failed to send message to Discord. Status code: {response.status_code}")



        if __name__ == "__main__":

            print("Generating available usernames on TikTok:")



            while True:

                max_iterations = 20  # You can change this to control the number of iterations

                unique_usernames = set()



                for _ in range(max_iterations):

                    # Generate a 4-5 character username

                    username_4_to_5 = generate_4_to_5_character_username()

                    if username_4_to_5 not in unique_usernames:

                        if check_tiktok_username_availability(username_4_to_5):

                            unique_usernames.add(username_4_to_5)

                            print(f"Generated and Available 4-5 Character Username: {username_4_to_5}")



                            # Send the available username to Discord webhook

                            send_to_discord_webhook(username_4_to_5)



                        else:

                            print(f"Generated but Taken 4-5 Character Username: {username_4_to_5}")

                    else:

                        print(f"Duplicate 4-5 Character Username: {username_4_to_5}")



                    # Generate a username with any English word without character limits

                    username_any_word = generate_any_english_word_username()

                    if username_any_word not in unique_usernames:

                        if check_tiktok_username_availability(username_any_word):

                            unique_usernames.add(username_any_word)

                            print(f"Generated and Available Any English Word Username: {username_any_word}")



                            # Send the available username to Discord webhook

                            send_to_discord_webhook(username_any_word)



                        else:

                            print(f"Generated but Taken Any English Word Username: {username_any_word}")

                    else:

                        print(f"Duplicate Any English Word Username: {username_any_word}")



                    sleep(1)  # Be respectful, add a delay to avoid overloading the server



                print("\nGenerated Usernames:")

                for username in unique_usernames:

                    print(username)

        word = random.choice([w for w in english_words if 4 <= len(w) <= 5])



        if word:

            return word.lower()





def generate_any_english_word_username():

    # Choose a random word from the English dictionary without character limits

    return random.choice(list(english_words)).lower()





def check_tiktok_username_availability(username):

    url = f'https://www.tiktok.com/@{username}'

    response = requests.get(url)



    if response.status_code == 200:

        # The username is not available

        return False

    elif response.status_code == 404:

        # The username is available

        return True

    else:

        # Handle other status codes as needed

        print(f"Unexpected status code: {response.status_code}")

        return False





def send_to_discord_webhook(username):

    discord_data = {

        "content": f"New Available TikTok Username: {username}"

    }

    response = requests.post(discord_webhook_url, json=discord_data)



    if response.status_code != 204:

        print(f"Failed to send message to Discord. Status code: {response.status_code}")





if __name__ == "__main__":

    print("Generating available usernames on TikTok:")



    while True:

        max_iterations = 20  # You can change this to control the number of iterations

        unique_usernames = set()



        for _ in range(max_iterations):

            # Generate a 4-5 character username

            username_4_to_5 = generate_4_to_5_character_username()

            if username_4_to_5 not in unique_usernames:

                if check_tiktok_username_availability(username_4_to_5):

                    unique_usernames.add(username_4_to_5)

                    print(f"Generated and Available 4-5 Character Username: {username_4_to_5}")



                    # Send the available username to Discord webhook

                    send_to_discord_webhook(username_4_to_5)



                else:

                    print(f"Generated but Taken 4-5 Character Username: {username_4_to_5}")

            else:

                print(f"Duplicate 4-5 Character Username: {username_4_to_5}")



            # Generate a username with any English word without character limits

            username_any_word = generate_any_english_word_username()

            if username_any_word not in unique_usernames:

                if check_tiktok_username_availability(username_any_word):

                    unique_usernames.add(username_any_word)

                    print(f"Generated and Available Any English Word Username: {username_any_word}")



                    # Send the available username to Discord webhook

                    send_to_discord_webhook(username_any_word)



                else:

                    print(f"Generated but Taken Any English Word Username: {username_any_word}")

            else:

                print(f"Duplicate Any English Word Username: {username_any_word}")



            sleep(1)  # Be respectful, add a delay to avoid overloading the server



        print("\nGenerated Usernames:")

        for username in unique_usernames:

            print(username)