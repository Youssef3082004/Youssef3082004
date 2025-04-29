import openai
import tweepy
import tweepy.client
import re
from re import sub

class GPT_x:
    @staticmethod
    def generate_response(prompt):
        openai.api_key = "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"
        response = openai.completions.create(
            model="gpt-3.5-turbo-instruct",  
            prompt=prompt,
            max_tokens=2000 -len(prompt) ,               #500 - len(prompt)
            # temperature=0.5
        )

        text = response.choices[0].text.strip()
        text = sub(r'["".,!:\n]','', text)
        return text
    
    @staticmethod
    def Upload_in_Twitter(tweet_text:str,media_path:str): 
        baerer_token = "AAAAAAAAAAAAAAAAAAAAALHWtwEAAAAAPkAlYa69XGNznMN8qlppHRLOe6A%3DPN5CzyjsPnpcqCdbjxNPnlHYzSdXksjvSe6OuoZpJ8KIHRdjsb"
        consumer_key = 'UDZAlp3W1IQIAATxFaZeIlChF'
        consumer_secret = 's3U4nvM6Ba4F9On3ru306KOb2zPbRx1cDY6wlcFtemCiLeAJTL'
        access_token = '2398251728-7UNlwSXdVY6YpMTlydLjDtePq8UdQeR8x2q6GbV'
        access_token_secret = 'cZrPSu6JnUr1CVJbzGXusqoYNOukI0UR0psk2mL1C23ko'
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        client = tweepy.Client(
                    bearer_token= baerer_token,
                    consumer_key=consumer_key,
                    consumer_secret= consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret,      
                )
        try:
            media_id = api.media_upload(filename=media_path).media_id_string
            client.create_tweet(text=tweet_text,media_ids=[media_id])
        except: 
            pass
            

        