import urllib.request
import http.client
from bs4 import BeautifulSoup

def get_leaderboard_honor():
    #f = codecs.open("https://www.codewars.com/users/leaderboard", 'r', 'utf-8')
    #tables = pd.read_html("https://www.codewars.com/users/leaderboard")
    f = urllib.request.urlopen("https://www.codewars.com/users/leaderboard")
    data = http.client.HTTPResponse.read(f)
    soup = BeautifulSoup(data, 'html.parser')
    print(soup.body)
