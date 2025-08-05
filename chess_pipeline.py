"""
This module provides functionality for managing and processing chess game data.
It includes functions to load chess game data from an api into a duckdb database and 
display it into a streamlit interface using dlt package.
"""

from datetime import date

import dlt
import requests
#from dlt.sources.helpers import requests

today_date = date.today()

# Create a dlt pipeline that will load
# chess player data to the DuckDB destination
pipeline = dlt.pipeline(
    pipeline_name='chess_pipeline',
    destination='duckdb',
    dataset_name='player_data'
)

structured_data = []

for player in ['dede0610', 'Fred3337']:
    URL = f'https://api.chess.com/pub/player/{player}'
    try:
         # Récupération du profil
        profile_response = requests.get(URL)
        profile_response.raise_for_status()
        player_profile = profile_response.json()

        # Récupération des stats
        stats_response = requests.get(URL + '/stats')
        stats_response.raise_for_status()
        player_stats = stats_response.json()

        # Combine les données pour ce joueur
        player_record = {
            "username": player_profile["username"],
            "date_extraction" : today_date,
            "country": player_profile["country"],
            "last_online": player_profile["last_online"],

            "chess_rapid_rating": player_stats["chess_rapid"]["last"]["rating"],
            "chess_rapid_best_rating": player_stats["chess_rapid"]["best"]["rating"],
            "chess_rapid_best_rating_date": player_stats["chess_rapid"]["best"]["date"],
            "chess_rapid_stats": player_stats["chess_rapid"]["record"],

            "chess_blitz_rating": player_stats["chess_blitz"]["last"]["rating"],
            "chess_blitz_best_rating": player_stats["chess_blitz"]["best"]["rating"],
            "chess_blitz_best_rating_date": player_stats["chess_blitz"]["best"]["date"],
            "chess_blitz_stats": player_stats["chess_blitz"]["record"],   
        }
        # Ajoute les données structurées
        structured_data.append(player_record)
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch data for {player}: {e}")



# Extract, normalize, and load the data
pipeline.run(structured_data, table_name='player_stats')

# CLI command to run
# dlt pipeline chess_pipeline show
