import requests
token = "441258fb34be47d7d23a10dc113b900642b109ae3fa35b2e0840747dfd93baa0551fc801b8c783932b329"

url = "http://www.vktops.com/statusy-pro-zhizn/"
r = requests.get(url)
html = r.text
from bs4 import BeautifulSoup 
soup = BeautifulSoup(html, "html.parser")
status_list = soup.select(".statusesList .statusesList-item div.text")
statuses = []
for item in status_list:
	statuses.append(item.text)
import random
p = random.randrange(0, len(statuses))
text = statuses[p]
print(text)
