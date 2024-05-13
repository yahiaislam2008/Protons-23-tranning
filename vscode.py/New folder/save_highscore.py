import turtle
import random
import time
import winsound
import json

# Function to load player data from JSON file
def load_players_data():
    try:
        with open("players.json", "r") as file:
            players_data = json.load(file)
    except FileNotFoundError:
        players_data = {}
    
    return players_data

# Function to save player data to JSON file
def save_players_data(players_data):
    with open("players.json", "w") as file:
        json.dump(players_data, file)

# Function to get player name and retrieve existing player data or create a new player entry
def get_player_data(players_data):
    player_name = input("Enter your name: ")
    
    if player_name not in players_data:
        players_data[player_name] = {"highscore": 0}
    
    return players_data[player_name]

# Function to display the leaderboard
def display_leaderboard(players_data):
    sorted_players = sorted(players_data.items(), key=lambda x: x[1]["highscore"], reverse=True)
    
    print("Leaderboard:")
    for player, data in sorted_players:
        print(player, "- Highscore:", data["highscore"])

# Load players data from JSON file
players_data = load_players_data()

# Get or create player data
player_data = get_player_data(players_data)

# Set the high score from player data
high_score = player_data["highscore"]

# Update the player's highscore if a new highscore is achieved
def update_highscore(score):
    if score > player_data["highscore"]:
        player_data["highscore"] = score
score=0
# Rest of your code...

# Update highscore if necessary
update_highscore(score)

# Save players data to JSON file
save_players_data(players_data)

# Display the leaderboard
display_leaderboard(players_data)