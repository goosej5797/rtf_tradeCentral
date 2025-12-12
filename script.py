import httpx

def fetch_data(url: str) -> dict:
    """Fetch JSON data from a given URL."""
    try:
        response = httpx.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except httpx.HTTPError as e:
        print(f"An error occurred while fetching data: {e}")
        return {}
    
def display_trade(trade_data: dict):
    """Display trade data in a readable format."""
    for key, value in trade_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    leagueId = '1283366654155177984'
    y = 1
    while y < 15:
        url = f"https://api.sleeper.app/v1/league/{leagueId}/transactions/{y}"
        data = fetch_data(url)
        for x in data:
            if x['type'] == 'trade':
                display_trade(x)
                break
        y += 1
    
    print(data)