import requests

def brute_force_folders(ip,path):
    with open(path, 'r') as f:
        wordlist = f.read().splitlines()

    for word in wordlist:
        url = f'http://{ip}/{word}/'
        response = requests.get(url)

        if response.status_code != 404:
            print(f'Found: {url}')

# Replace 'your_server_ip' with your actual server IP
ip = '196.203.79.217'
# Replace 'wordlist.txt' with the path to your wordlist file
path = './wordlist.txt'

brute_force_folders(ip, path)