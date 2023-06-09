from bs4 import BeautifulSoup
import requests
from proxy_config import login, password, proxy

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
proxies = {
    'http': f'https://{login}:{password}@{proxy}'
}

def get_data(url):
    response = requests.get(url=url, headers=headers, proxies=proxies)
    print(response)

def main():
    get_data(url='https://www.bls.gov/regions/midwest/data/AverageEnergyPrices_SelectedAreas_Table.htm')

if __name__ == "__main__":
    main()
