import requests
from bs4 import BeautifulSoup

# Fetch the HTML source of the page
response = requests.get('https://www.kernel.org')

# Parse the HTML source with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the 'td' element containing 'stable:'
stable_td = soup.find('td', string='stable:')

# Find the next 'td' element, which contains the version number
version_td = stable_td.find_next('td')

# Extract the version number
stable_version = version_td.text.strip()

print(f'The current stable version is: {stable_version}')
