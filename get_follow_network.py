# Gets the following and friend networks for users

import csv
import tweepy
import constants

# Not used right now, factorize later
# def load_data(filename: str) -> csv.reader:
#     """Loads csv data from Hydrated Tweet set"""
#     with open(filename, newline='') as csvfile:
#         data = csv.reader(csvfile)
#         return data

# Testing 
filename = 'Unite-the-Right_Full-set.csv'

users = {
    'user_id': [],
    'user_screen_name': [],
}

with open(filename, newline='', encoding='utf-8') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        users['user_id'].append(row[21])   # user_id column
        users['user_screen_name'].append(row[30])   # user_screen_name

# Create new lists for user ids and lables (names) from csv dataset

user_ids = []
for user in users['user_id']:
    if user not in user_ids:
        user_ids.append(user)

user_labels = []
for user_label in users['user_screen_name']:
    if user not in user_labels: 
        user_labels.append(user_label)

print(user_ids[:100])
print(user_labels[:100])
print(len(user_ids))

# Get followers of unique users from dataset

edges = {
    'source': [],
    'source_label': [],
    'target': [],       
    'target_label': []
}  

def get_friends(ids: list, labels: list, edges: dict) -> dict:
    """Returns list of followers for each user id"""
    for id, label in zip(ids, labels):
        print(f'Retrieving data for {label}.')
        friends = tweepy.API.get_friends(user_id=id)  # Returns list of class User
        for friend in friends:
            edges['source'].append(id)
            edges['source_label'].append(label)
            edges['target'].append(friend.id)
            edges['target_label'].append(friend.screen_name)

        return edges

def node_edge_transform(edges: dict, path='export',filenameEdges=R'export\edges.csv',
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
