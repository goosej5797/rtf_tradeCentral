import json
from pathlib import Path

def filter_player_db(input_file: str, output_file: str = None) -> None:
    """
    Filter player database to keep only QB, RB, WR, and TE positions.
    
    Args:
        input_file: Path to input JSON file
        output_file: Path to output JSON file (defaults to input_file with _filtered suffix)
    """
    if output_file is None:
        input_path = Path(input_file)
        output_file = input_path.parent / f"{input_path.stem}_filtered.json"
    
    valid_positions = {"QB", "RB", "WR", "TE"}
    
    try:
        # Read the JSON file
        with open(input_file, "r", encoding="utf-8") as f:
            players = json.load(f)
        
        # Filter players
        filtered_players = {
            player_id: player for player_id, player in players.items()
            if player.get("fantasy_positions") and 
            any(pos in valid_positions for pos in player["fantasy_positions"])
        }
        
        # Write filtered results
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(filtered_players, f, indent=2)
        
        print(f"Filtered {len(players)} players down to {len(filtered_players)}")
        print(f"Results saved to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: {input_file} not found")
    except json.JSONDecodeError:
        print(f"Error: {input_file} is not valid JSON")


if __name__ == "__main__":
    filter_player_db("player_db.json")