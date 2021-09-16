import tweepy

from authorization_tokens import *

import random

message = " "
# Option 1: Select a message randomly from a list of messages phrase_list = []
# phrase_list = ["Hi my name is floopy.",
# "I am a floop.",
# "I am flippy and flop."]
#
# message = random.choice(phrase_list)

# Option 2: A simple mad lib

# string_template = "Some people eat {} but a eat {}"
#
# word_list = ["apples", "bannanas", "shorts", "computers", "hamsters"]
#
# # string template subbstitutes words from word_list into word1 and word2
#
# word1 = random.choice (word_list)
# word2 = random.choice (word_list)
#
# message = string_template.format(word1,word2)

# Option 3 = list of possible mad libs

# template_list = ["I ate a {} and I am a {}.",
# "I found a {} and ate {}.",
# "I walked a {} and kicked a {}."]
#
# word_list1 = [ "car", "dog", "hamster", "apples", "oranges"]
# word_list2 = ["key", "bug", "computer"]
#
# template = random.choice(template_list)
#
# word1 = random.choice(word_list1)
# word2 = random.choice(word_list2)
#
# message = template.format(word1,word2)
#
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# api.update_status(message)
# print("Done.")

# Option 4: using if statements

string_template = "hi there, im {}, eater of {}"

word_list1 = ["human", "computer"]

word_list2_a = ["hamsters", "flowers", "koolaid", "coffee"]
word_list2_b = ["people", "keys", "chargers", "words"]

word1 = random.choice(word_list1)

if word1 == "human":
    word2 = random.choice(word_list2_a)
elif word1 == "computer":
    word2 = random.choice(word_list2_b)

message = string_template.format(word1,word2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print("Done.")
