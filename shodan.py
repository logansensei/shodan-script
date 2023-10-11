import shodan
import random

def get_random_user_agent():
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
        'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        # Add more user agents as needed
    ]
    return random.choice(user_agents)

def search_with_api_key(query, api_key, user_agent):
    api = shodan.Shodan(api_key)

    try:
        results = api.search(query, headers={'User-Agent': user_agent})

        for result in results['matches']:
            print(f"IP: {result['ip_str']}")
            print(f"Port: {result['port']}")
            print(f"Organization: {result['org']}")
            print(f"Product: {result['product']}")
            print(f"-----------------------------")

    except shodan.APIError as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Shodan Search Script!")
    query = input("Enter your search query (e.g., 'apache', 'nginx', 'Microsoft IIS'): ")
    api_keys = []
    user_agent = get_random_user_agent()

    while True:
        api_key = input("Enter your Shodan API key (press Enter to finish): ")

        if not api_key:
            break

        api_keys.append(api_key)

    if not api_keys:
        print("No API keys provided. Exiting...")
        return

    print(f"\nUsing user agent: {user_agent}\n")
    print("Searching...\n")

    for api_key in api_keys:
        search_with_api_key(query, api_key, user_agent)

if __name__ == "__main__":
    main()
