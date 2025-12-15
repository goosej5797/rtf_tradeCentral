import httpx
import json

#Trade Helpers - CACHE TBD
def fetch_player_from_cache(playerId: str) -> dict:
    """Fetch player data from a local cache or database."""
    # Placeholder for cache fetching logic
    # In a real implementation, this would query a local database or cache
    with open('player_cache.json', 'r') as f:
        player_cache = json.load(f)
        if playerId in player_cache:
            return player_cache[playerId]
        return {}
    

def fetch_player_from_db(playerIdList: dict) -> dict:
    player_db_list = {}
    with open('player_db_filtered.json', 'r') as f:
        player_db = json.load(f)
        for playerId in playerIdList:
            try:
                player_db_list[playerId] = player_db[playerId]
            except KeyError:
                playerIdList[playerId] = {}
    return player_db_list

def find_players_in_trade(trade_data: dict) -> list:
    """Extract player IDs involved in a trade."""
    player_ids = []
    for team in trade_data.get('roster_ids', []):
        for player_id in trade_data.get('players', []):
            player_ids.append(player_id)
    return player_ids

def display_trade(trade_data: dict):
    """Display trade data in a readable format."""
    print(type(trade_data))
    for key, value in trade_data.items():
        print(f"{key}: {value}")


#API Calls
def fetch_data(url: str) -> dict:
    """Fetch JSON data from a given URL."""
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except httpx.HTTPError as e:
        print(f"An error occurred while fetching data: {e}")
        return {}

if __name__ == "__main__":
    #Read example_trade / replace with API call
    with open('example_trade.json', 'r') as f:
        example_trade = json.load(f)
    
    player_id_list = example_trade['adds'].keys()
    player_db_list = fetch_player_from_db(player_id_list)

    print(player_db_list["2133"]['full_name'])
    # leagueId = '1259632689275744256'
    # y = 1
    # while y < 15:
    #     url = f"https://api.sleeper.app/v1/league/{leagueId}/transactions/{y}"
    #     data = fetch_data(url)
    #     for x in data:
    #         if x['type'] == 'trade':
    #             display_trade(x)
    #             print('y: ' + str(y))
    #             break
    #     y += 1
    # print(data)
