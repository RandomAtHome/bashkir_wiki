from bs4 import BeautifulSoup
import urllib.request

webpage = urllib.request.urlopen('https://en.wikipedia.org/wiki/Multinational_corporation')
soup = BeautifulSoup(webpage)
for tag_refl in soup.find_all('ol'):
    print((len(tag_refl.contents) - 1) // 2)
    """ tag_refl.contents resembles a list of tags inside tag <ol>
        there are N external references, each 
        closed between 2 tags - <li> and </li>
        and there is a closing tag </ol>
        in summary we have 2 * N + 1 elements in tag_refl.contents, where N is number of ext. ref
    """