import requests
import json

filename = "brawlStats.json"

# Define the API endpoint and your API token
player_tag = '#'

player_tag = player_tag+ input("input your player code: ")

player_stats = None

player_tag = player_tag.replace('#', "%23")

url = f'https://api.brawlstars.com/v1/players/{player_tag}'
api_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImFkMjUzYjkyLTE0ZDUtNGIwYS04YjI2LTc3N2M2MDI1YTU5NCIsImlhdCI6MTcwODEwMzcyNCwic3ViIjoiZGV2ZWxvcGVyLzYwZWJhYjdkLTA0NGQtZmJlYy0zZTg1LTdjYWFjYWM4NjA0YyIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzMuMTY0LjIzMi41MiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.r4dnGv5GrH66AJjZtNqn7lCgOnToFjK-ECQ7K1MClOw1sWm1ZF7AYkBmliq06_L9SkIrzZHuvnrj3HEEx0DrzQ'

# Create headers with the API token
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Make the GET request
response = requests.get(url, headers=headers)

data = response.json()

with open(filename, 'w') as file:  
    json.dump(data, file, indent=4)

with open(filename, 'r') as file:
    json.load(file)

if 'name' in data:
        name = data['name']
        print(f"\n This player's name is: {name}\n here are some of their stats")

if '3vs3Victories' in data:
        wins3v3 = data['3vs3Victories']
        print(f"\n3 v 3 Victories: {wins3v3}\n")
        
if 'trophies' in data:
        trophies = data['trophies']
        print(f"trophies: {trophies}\n")
        
if 'soloVictories' in data:
        soloVictories = data['soloVictories']
        print(f"solo Victories: {soloVictories}\n")
