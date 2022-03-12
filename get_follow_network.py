# Gets the following and friend networks for users

import csv
import tweepy

# Get relevant user data 
def createUserList(filename: str, users: dict):
    """Creates list of users of interest from csv file"""
    with open(filename, newline='', encoding='utf-8') as csvfile:
        data = csv.reader(csvfile)
        for row in data:
            users['user_id'].append(row[21])   # user_id column
            users['user_screen_name'].append(row[30])   # user_screen_name

        return users
    
def uniqueUsers(usersData: zip) -> list:
    """Removes duplicate user ids, returns list of tuples (user_id, label)"""
    return list(set([i for i in usersData]))

# Get follower networks 

def get_friends(client: tweepy.Client, userData: list, edges: dict) -> dict:
    """Returns list of followers for each user id"""
    for id, label in userData:
        print(f'Retrieving data for {label}.')
        friends = client.get_users_following(id) 
        print(f'Found {len(friends)} friends for{label}. Collecting data...')
        for friend in friends.data:
            edges['source'].append(id)
            edges['source_label'].append(label)
            edges['target'].append(friend.id)
            edges['target_label'].append(friend.username)

    return edges

# Transform to Gephi data

def node_edge_transform(edges: dict, filenameEdges=R'export\edges.csv',
                        filenameNodes=R'export\nodes.csv'):
    """Transforms dictionary of friend network into Gephi node + edge sheets
    Exports these sheets as csv file to default 'export' folder, unless specified"""
    with open(filenameEdges, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        # Write header row, then each row by iterating thru dict
        csvwriter.writerow(edges.keys())
        csvwriter.writerows(zip(*edges.values()))

    with open(filenameNodes, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['id', 'label'])
        csvwriter.writerows(zip(edges['source'], edges['source_label']))
















# Write csv files for edges

# filename_edges_write = 'edges_followNetwork'
# filename_nodes_write = 'nodes_followNetwork'

# with open(filename_edges_write, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow(list(edges.keys()))
#     csvwriter.writerow(edges['source'])
#     csvwriter.writerow(edges['target'])
#     csvwriter.writerow(edges['target_label'])

# # Retrieve nodes from edges 
# # TODO: Update to include label (from first user list --> dic)
# nodes = {
#     'user_id': [user for user in edges['source']],
# }
