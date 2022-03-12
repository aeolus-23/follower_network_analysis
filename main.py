#! - python3

import tweepy
import constants
import get_follow_network as process

if __name__ == '__main__':
    # Do stuff 
    settings = constants.Constants

    # Set variables for data

    users = {
        'user_id': [],
        'user_screen_name': []
    }

    filenameData = 'Unite-the-Right_Full-set.csv'
    userData = process.createUserList(filenameData, users)
    print(len(userData['user_id']))
    print(len(userData['user_screen_name']))

    # Get only unique names from userData
    uniqueData = process.uniqueUsers(zip(*userData.values()))
    print(uniqueData[:10])
    # _something = process.uniqueUsers(zip(*userData.values()))
    # ids, labels = process.uniqueUsers(userData)
    # print(len(ids))
    # print(len(labels))
    



    # Connect to Twitter API and retrieve friend network

    # try:
    #     client = tweepy.Client(bearer_token=settings.bearer_token, 
    #                             wait_on_rate_limit=True)
    # except tweepy.Unauthorized:
    #     print('Error 401. Could not authorize.')

    # TODO: Write information to csv (edges and nodes)
