from jinja2 import Template
from bs4 import BeautifulSoup
import urllib.request


out_html = open("results.html", "w")
results = []

# start of reading Wiki
url = 'https://en.wikipedia.org/wiki/Multinational_corporation'
webpage = urllib.request.urlopen(url)
soup = BeautifulSoup(webpage)

name = soup.find('h1').string
# gets the title of the article (not the webpage)

for tag_refl in soup.find_all('ol'):
    results.append((name, url, (len(tag_refl.contents) - 1) // 2))
    """ tag_refl.contents resembles a list of tags inside tag <ol>
        there are N external references, each
        closed between 2 tags - <li> and </li>
        and there is a closing tag </ol>
        in summary we have 2 * N + 1 elements in tag_refl.contents,
        where N is number of ext. ref.
    """
results.sort(key=lambda x: x[2])
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
{% for result in item_list -%}
<tr>
   <td>{{ result[0] }}</td>
   <td><a href="{{ result[1] }}">{{ result[1] }}</td>
   <td align="middle">{{ result[2] }}</td>
</tr>
{% endfor %}
</table>
</body>
</html>''')
# Jinja code ended

print(result_page.render(item_list=results), file=out_html)
out_html.close()
# creating output file and closing it
