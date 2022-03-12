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
        'user_label': []
    }

    filenameData = 'Unite-the-Right_Full-set.csv'
    process.createUserList(filenameData, users)
    



    # Connect to Twitter API and retrieve friend network

    try:
        client = tweepy.Client(bearer_token=settings.bearer_token, 
                                wait_on_rate_limit=True)
    except tweepy.Unauthorized:
        print('Error 401. Could not authorize.')

    # TODO: Write information to csv (edges and nodes)
