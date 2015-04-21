# -*- coding: utf-8 -*-

from jinja2 import Template
from bs4 import BeautifulSoup
import urllib.request


HOST_URL = "http://ba.wikipedia.org"
NEXT_PAGE = "Киләһе бит"

url_start = 'https://ba.wikipedia.org/wiki/%D0%9C%D0%B0%D1%85%D1%81%D1%83%D1%81:%D0%91%D0%B0%D1%80%D0%BB%D1%8B%D2%A1_%D0%B1%D0%B8%D1%82%D3%99%D1%80'
out_html = open("results_best.html", "w", encoding='utf-8')


max_ref = 0
results = ("None", "None", 0)

# start of reading Wiki
next_page_link = url_start


while next_page_link != "":

    to_parse = []

    request = urllib.request.Request(next_page_link)
    request.add_header("Content-Type", "application/x-www-form-urlencoded;charset=utf-8")
    html = urllib.request.urlopen(request).read().decode('utf-8')

    soup = BeautifulSoup(html)
    body = soup.find('ul')

    # fetching all URL's on the page
    for i in range(0, len(body.contents), 2):
        to_parse.append(HOST_URL + body.contents[i].contents[0].get('href'))

    # finding next page
    next_page_link = ""
    navigation = soup.find_all("div", class_="mw-allpages-nav")
    for nav_tag in navigation[0].contents:
        if NEXT_PAGE in nav_tag.string:
            next_page_link = HOST_URL + nav_tag.get('href')

    # getting info from found pages
    for link in to_parse:
        webpage = urllib.request.urlopen(link)
        soup = BeautifulSoup(webpage)
        link.encode('utf-8')
        name = soup.find('title').string
        for tag_refl in soup.find_all('ol', class_="references"):
            amount_l = 0
            for tag_link in tag_refl.contents:
                if tag_link.name == 'li':
                    amount_l += 1

            if amount_l > max_ref:
                max_ref = amount_l
                results = (name, link, amount_l)
        soup.clear()        
        """
        We search <li> tags through the tag_refl.contents
        """

# end of reading Wiki

# Jinja code interpretating results
result_page = Template(u'''\
<html>
<head><title>Results of searching</title></head>
<body>
<table border>
<tr>
<th>Name of page</th>
<th>URL of page</th>
<th>Amount of external references</th>
</tr>
<tr>
   <td>{{ result[0] }}</td>
   <td><a href="{{ result[1] }}">{{ result[1] }}</td>
   <td align="middle">{{ result[2] }}</td>
</tr>
</table>
</body>
</html>''')
# Jinja code ended

print(result_page.render(result=results), file=out_html)
out_html.close()
# creating output file and closing it
