mport urllib
import requests
from bs4 import BeautifulSoup


url = "http://www.usacycling.org/clubs/members.php?club="
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

prefix = "http://www.usacycling.org/"

homeArticleBodies = soup.find_all("td", class_="homearticlebody")
firstHomeArticleBody = homeArticleBodies[0::2]

usacMembers = {}

from lxml import html
import datetime

for element in firstHomeArticleBody:
	memberName = unicode(element.get_text()).replace(u'\xa0','')
	memberName = str(memberName)[1::]
	print memberName
	usacMembers[memberName] = {}
	usacMembers[memberName]["link"] = prefix + element.a["href"]
	page = requests.get(usacMembers[memberName]['link'])
	tree = html.fromstring(page.text)
	raceDates = tree.xpath('//span[@class="homearticleheader"]/text()')
	races14 = 0
	races15 = 0
	for i, date in enumerate(raceDates):
		raceDates[i] = date[0:10:]
		if raceDates[i][6:10:] == '2015':
			races15 += 1
		if raceDates[i][6:10:] == '2014':
			races14 += 1
	print '2015 races ', races15
	print '2014 races ', races14
