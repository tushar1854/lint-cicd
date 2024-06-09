import pandas as pd
import random
from api_conf import polarity_api
import requests
from datetime import datetime

def process_comments(comments_list):
  updated_comments_list = []
  for comment in comments_list:
    params = {'text': comment['text']}
    response = requests.get(polarity_api, params)
    response = response.json()
    comment['polarity_score'] = response['polarity_score']
    comment['polarity'] = response['polarity']
    updated_comments_list.append(comment)
  return updated_comments_list


def convert_dict2list(data):
	comment_list = []
	for comment in data:
		comment_list.append([comment['id'], comment['username'], comment['text'], 
			datetime.utcfromtimestamp(comment['created_at']).strftime('%Y-%m-%d %H:%M:%S'), 
			comment['polarity_score'], comment['polarity']])

	return pd.DataFrame(comment_list, columns=['user_id', 'username', 'comment', 
		'created_at', 'polarity_score', 'polarity'], index=None)
if __name__ == "__main__":
	data = {
  "subfeddit_id": 2,
  "limit": 25,
  "skip": 0,
  "comments": [
    {
      "id": 33787,
      "username": "user_56",
      "text": "Well done! Good work.",
      "created_at": 1717490719
    },
    {
      "id": 33788,
      "username": "user_57",
      "text": "Well done! Luckily you did it.",
      "created_at": 1717487119
    },
    {
      "id": 33789,
      "username": "user_58",
      "text": "Well done! Proud of you.",
      "created_at": 1717483519
    },
    {
      "id": 33790,
      "username": "user_59",
      "text": "Well done! Enjoy!",
      "created_at": 1717479919
    },
    {
      "id": 33791,
      "username": "user_60",
      "text": "Looks decent. It looks great!",
      "created_at": 1717476319
    },
    {
      "id": 33792,
      "username": "user_61",
      "text": "Looks decent. Love it.",
      "created_at": 1717472719
    },
    {
      "id": 33793,
      "username": "user_62",
      "text": "Looks decent. Awesome.",
      "created_at": 1717469119
    },
    {
      "id": 33794,
      "username": "user_63",
      "text": "Looks decent. Well done!",
      "created_at": 1717465519
    },
    {
      "id": 33795,
      "username": "user_64",
      "text": "Looks decent. Looks decent.",
      "created_at": 1717461919
    },
    {
      "id": 33731,
      "username": "user_0",
      "text": "It looks great!",
      "created_at": 1717692319
    },
    {
      "id": 33732,
      "username": "user_1",
      "text": "Love it.",
      "created_at": 1717688719
    },
    {
      "id": 33733,
      "username": "user_2",
      "text": "Awesome.",
      "created_at": 1717685119
    },
    {
      "id": 33734,
      "username": "user_3",
      "text": "Well done!",
      "created_at": 1717681519
    },
    {
      "id": 33735,
      "username": "user_4",
      "text": "Looks decent.",
      "created_at": 1717677919
    },
    {
      "id": 33736,
      "username": "user_5",
      "text": "What you did was right.",
      "created_at": 1717674319
    },
    {
      "id": 33737,
      "username": "user_6",
      "text": "Thumbs up.",
      "created_at": 1717670719
    },
    {
      "id": 33738,
      "username": "user_7",
      "text": "Like it a lot!",
      "created_at": 1717667119
    },
    {
      "id": 33739,
      "username": "user_8",
      "text": "Good work.",
      "created_at": 1717663519
    },
    {
      "id": 33740,
      "username": "user_9",
      "text": "Luckily you did it.",
      "created_at": 1717659919
    },
    {
      "id": 33741,
      "username": "user_10",
      "text": "Proud of you.",
      "created_at": 1717656319
    },
    {
      "id": 33742,
      "username": "user_11",
      "text": "Enjoy!",
      "created_at": 1717652719
    },
    {
      "id": 33743,
      "username": "user_12",
      "text": "It looks great! It looks great!",
      "created_at": 1717649119
    },
    {
      "id": 33744,
      "username": "user_13",
      "text": "It looks great! Love it.",
      "created_at": 1717645519
    },
    {
      "id": 33745,
      "username": "user_14",
      "text": "It looks great! Awesome.",
      "created_at": 1717641919
    },
    {
      "id": 33746,
      "username": "user_15",
      "text": "It looks great! Well done!",
      "created_at": 1717638319
    }
  ]
}
	df = process_comments(data['comments'])
	import pdb; pdb.set_trace()