twitter_users = [
    {
        'name': 'Oneh Amos',
        'username': '@amosoneh',
        'age': 32,
        'is_verified': True,
        'number_of_tweet': 45,
        'followers': 100,
        'following': 40,
        'tweets': [
            {
                'content': 'I love you so much honour',
                'likes': 5,
                'comments': 20
            },
            {
                'content': 'We are OBIdiently waiting',
                'likes': 5,
                'comments': 20
            },
        ]
    },

    {
        'name': 'Oneh Monday',
        'username': '@monday',
        'age': 31,
        'is_verified': True,
        'number_of_tweet': 75,
        'followers': 1000,
        'following': 110,
        'tweets': [
            {
                'content': 'God is good',
                'likes': 45,
                'comments': 120
            },
            {
                'content': 'Jesus is coming soon',
                'likes': 50,
                'comments': 80
            },
            {
                'content': 'Jesus is Lord',
                'likes': 150,
                'comments': 110
            },
        ]
    },

    {
        'name': 'Diego Khaled',
        'username': '@diego',
        'age': 30,
        'is_verified': True,
        'number_of_tweet': 75,
        'followers': 10000,
        'following': 70,
        'tweets': [
            {
                'content': 'God is good',
                'likes': 95,
                'comments': 65
            },
            {
                'content': 'No space for Tinubu',
                'likes': 500,
                'comments': 80
            },
            {
                'content': 'We need change',
                'likes': 150,
                'comments': 110
            },
            {
                'content': 'Naija will be great again',
                'likes': 15,
                'comments': 10
            },
            {
                'content': 'We are tired of corruption',
                'likes': 95,
                'comments': 40
            },
        ]
    },

    {
        'name': 'Khaled Malam',
        'username': '@khaled',
        'age': 30,
        'is_verified': False,
        'number_of_tweet': 75,
        'followers': 10000,
        'following': 70,
        'tweets': [
            {
                'content': 'God is love',
                'likes': 85,
                'comments': 115
            },
            {
                'content': 'No space for Tinubu as presido',
                'likes': 700,
                'comments': 80
            },
            {
                'content': 'We need change in naija',
                'likes': 150,
                'comments': 110
            },
            {
                'content': 'Naija is doom',
                'likes': 153,
                'comments': 40
            },
            {
                'content': 'We are tired of corruption',
                'likes': 25,
                'comments': 140
            },
            {
                'content': 'No old cargo',
                'likes': 1700,
                'comments': 800
            },
            {
                'content': 'Python is fun to write',
                'likes': 1700,
                'comments': 800
            }
        ]
    }
]


def get_tweet(dict_: dict):
    return dict_['tweets']


list_of_verified_users = [user for user in twitter_users if user['is_verified'] == True]
list_of_users_names = [user['name'] for user in twitter_users]
list_of_non_verified_users = [user for user in twitter_users if user['is_verified'] == False]
avg_user_age = sum(user['age'] for user in twitter_users) / len(twitter_users)
user_with_most_tweet = [user for user in twitter_users for tweet in 'tweets' if max(tweet)]
lst = max([[len(a["tweets"]), a["username"]] for a in twitter_users])
# print(lst)
# # user = max(twitter_users, key='tweets')
# print(user_with_most_tweet)
# print(list_of_verified_users)
# print(list_of_users_names)