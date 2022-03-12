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

    # Connect to Twitter API and retrieve friend network

    try:
        client = tweepy.Client(bearer_token=settings.bearer_token, 
                                wait_on_rate_limit=True)
    except tweepy.Unauthorized:
        print('Error 401. Could not authorize.')

    _edges = {
        'source': [],
        'source_label': [],
        'target': [],
        'target_label': []
    }

    edges = process.get_friends(client, uniqueData, _edges)

    # TODO: Write information to csv (edges and nodes)

    print('Writing to file...')
    process.node_edge_transform(edges)
