#!/usr/bin/env python3
import json

def extract_followers_usernames(data):
    return [
        item.get('value')
        for entry in data
        for item in entry.get('string_list_data', [])
        if item.get('value')
    ]

def extract_following_usernames(data):
    return [
        entry.get('title')
        for entry in data
        if entry.get('title')
    ]

# Open and load follower & following data files
with open('followers_1.json', 'r', encoding='utf-8') as followers_file:
    followers_data = json.load(followers_file)

if isinstance(followers_data, list) and len(followers_data) == 1:
    followers_data = followers_data[0]

with open('following.json', 'r', encoding='utf-8') as following_file:
    following_data = json.load(following_file).get('relationships_following', [])

cnt = 0
followers = extract_followers_usernames(followers_data)
followers_set = set(followers)
following = extract_following_usernames(following_data)

print('not followed back by:\n')

for user in following:
    if user not in followers_set:
        cnt += 1
        print(user)

print('\ntotal not followed by:', cnt)
print('\nfollowers:', len(followers))
print('following:', len(following))
