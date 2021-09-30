import tweepy
import random
from authorization_tokens import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
message = ""
api = tweepy.API(auth)
x = " "

# atmosphere = (🌞    )( 🌞   )(  🌞  )(   🌞 )(    🌞)(⭐ ⭐ ⭐)(⭐⭐⭐⭐⭐)

space = [" ",
         "\U0001FA90",
         "   \U0001FA90",
         "\U0001F47D",
         "     \U0001F47D",
         "\U0001F6F8",
         "  \U0001F6F8",
         "    \U0001F6F8"]

atmosphere = ["\U0001F31E",
              " ""\U0001F31E",
              " "" ""\U0001F31E",
              " "" "" ""\U0001F31E",
              " "" "" "" "" ""\U0001F31E",
              "\U00002600",
              " "" "" ""\U00002600",
              " "" "" "" ""\U0001F975",
              " "" ""\U0001F975",
              " "" "" ""\U0001F976",
              " "" ""\U0001F31D",
              " "" "" ""\U0001F31C",
              " ""\U0001F31C",
              " "" "" "" ""\U0001F31C",
              "\U00002B50 \U00002B50 \U00002B50",
              "\U00002B50 \U00002B50\U00002B50\U00002B50\U00002B50",
              "\U00002728""\U00002728"" ""\U00002728""\U00002728""\U00002728",
              "\U00002728""\U00002728""\U0001F318""\U00002728""\U00002728",
              "\U00002728"" ""\U00002728""\U00002728""\U0001F319""\U00002728",
              "\U00002728"" "" ""\U00002728",
              "\U00002728""\U00002728"  "\U00002728""\U00002728"]

sky = ["\U00002601",
       " ""\U00002601",
       " "" ""\U00002601",
       " "" "" ""\U00002601",
       " "" "" "" ""\U00002601",
       "\U00002601"" ""\U00002601\U00002601\U00002601\U00002601",
       " ",
       " ",
       " ",
       " ",
       " "" "" ""\U0001F327",
       "\U00002601"" ""\U0001F327"" ""U00002601",
       "\U00002601"" ""\U0001F327\U00002601\U0001F327\U00002601"]

air = [" ",
       " ",
       " "," "," "," "," "," "," "," "," "," "," "," "," "," ",
       "\U0001F987",
       "\U0001F985",
       "\U0001F409",
       "\U00002744",
       "\U0001F343",
       "\U0001F342",
       "\U0001F99F",
       "\U0001F98B",
       "\U0001F41D",
       "\U0001F409",
       "\U0001F985",
       "\U0001F987",
       ]

ground = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",
       "\U0000F6B6",
       "\U0001F43F",
       "\U0001F98F",
       "\U0001F998",
       "\U0001F9A3",
       "\U0001F412",
       "\U0001F411",
       "\U0001F994",
       "\U0001F99D",
       "\U0001F416",
       "\U0001F98C",
       "\U0001F407",
       "\U0001F408"
       "\U0001F9A1",
       "\U0001F9A6",
       "\U0001F9A4",
       "\U0001F40A",
       "\U0001F995",
       "\U0001F996",
       "\U0001F333",
       "\000U1F335",
       "\U0001F332",
       "\U0001F3D4",
       "\U0001F30B",
       "\U0001F5FB",
       "\U0001F3D5",
       "\U0001F3DD",
       "\U0001FAA8",
       "\U0001FAB5" ]

earth = ["\U0001F40C",
         "\U0001F41B",
         "\U0001F41C",
         "\U0001F41E",
         "\U0001FAB1",
         "\U0001F339",
         "\U0001F33B",
          "\U0001F331",
          "\U0001F33E",
          "\U0001F33F",
          "\U0001F340",
           "\U0001F331",
           "\U0001F33E",
           "\U0001F33F",
           "\U0001F340",
            "\U0001F331",
            "\U0001F33E",
            "\U0001F33F",
            "\U0001F340",
             "\U0001F331",
             "\U0001F33E",
             "\U0001F33F",
             "\U0001F340",
              "\U0001F331",
              "\U0001F33E",
              "\U0001F33F",
              "\U0001F340",
         "\U0001F331",
         "\U0001F33E",
         "\U0001F33F",
         "\U0001F340",
]


#       Objective: print emoji using CLDR code

# Test 1: print 😀
#print ("\U0001F600")
#   run in terminal - produces emoji

# Test 2: print 😃          😃
#   using x as space
#     note I guess I don't actually need x either I can just use space
#print ("\U0001F600"+10*x+"\U0001F600")


# Test 3: print:
# 😃
# 😃
#print ("\U0001F600\n\U0001F600")

# Test 4: print them together
#print ("\U0001F600\n\U0001F600")
#print ("\U0001F600"+10*x+"\U0001F600")

# Test 5: make a landscape out of emojis
#  🌥 🌞 🌧
#
#  🧚🏻‍♂️
#     🧍‍♀️
#  🌱🌱🌱🌱
#print ("\U00026C5"+1*x+"\U0001F31E"+1*x+"\U00026C5")
#print ("\U00002601")
#print ("\U0001F31E")
#print ("\U0001F9DA")
#print ("\U0001F9CD")
#print ("\U0001F331")
#   for some reason the emoji wasn't working...tried adding a zero and it worked? I might need to test the emoji codes before I use them
#   I may not need to use \n\ if I can just use return - check how it looks on twitter
#   I can use (x) as empty line
#print ("\U000026C5"+x+"\U0001F31E"+x+"\U000026C5")
#print (x)
#print ("\U0001F9DA")
#print (3*x+"\U0001F9CD")
#print ("\U0001F331" "\U0001F331" "\U0001F331" "\U0001F331")


# Note: so I'll need to assign a space set, an atmosphere set, a sky set, an air set, a ground set, and an earth set
#           These sets should include spaces. Then I'll have it randomly choose from within each set to create an image
#               I will make a 6x6 square (1 row for each set with 5 random choices per row)

#   test:

#print ("\U0001F327")

#  Actual Code Starts Here! Write Tests Above

#message = random.choice(atmosphere)
#message = random.choice(space)

string_template = "{}\n{}\n{}\n{}\n{}\n{}"
string_air = "{} {} {} "
string_ground = "{}{}{}{}{}{}"
string_earth = "{}{}{}{}{}{}"

randomair1 = random.choice(air)
randomair2 = random.choice(air)
randomair3 = random.choice(air)

randomground1 = random.choice(ground)
randomground2 = random.choice(ground)
randomground3 = random.choice(ground)
randomground4 = random.choice(ground)
randomground5 = random.choice(ground)
randomground6 = random.choice(ground)

randomearth1 = random.choice(earth)
randomearth2 = random.choice(earth)
randomearth3 = random.choice(earth)
randomearth4 = random.choice(earth)
randomearth5 = random.choice(earth)
randomearth6 = random.choice(earth)

field1 = random.choice(space)
field2 = random.choice(atmosphere)
field3 = random.choice(sky)
field4 = string_air.format(randomair1,randomair2,randomair3)
field5 = string_ground.format(randomground1,randomground2,randomground3,randomground4,randomground5,randomground6)
field6 = string_earth.format(randomearth1,randomearth2,randomearth3,randomearth4,randomearth5,randomearth6)


message = string_template.format(field1,field2,field3,field4,field5,field6)


#print(message)

api.update_status(message)
print("Done.")
