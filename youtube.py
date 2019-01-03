import requests
from bs4 import BeautifulSoup
import subprocess

scrape_url="https://www.youtube.com"
search_url="/results?search_query="
search_hardcode = "OPPO"
mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}

def bstheurl(video_links):
        sb_get = requests.get(video_links, headers = mozhdr)
        soupeddata = BeautifulSoup(sb_get.content, "html.parser")
        yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
        for x in yt_links:
            yt_href =  x.get("href")
            yt_title = x.get("title")
            yt_final = scrape_url + yt_href

            cmd=['youtube-dl',yt_final]
            subprocess.Popen(cmd)
            

video_links = scrape_url + search_url + search_hardcode
bstheurl(video_links)
