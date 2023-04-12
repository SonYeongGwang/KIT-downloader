import requests
from bs4 import BeautifulSoup
import io
import zipfile

'''
REFERENCE

------------------------------------------------------------------------------
https://beomi.github.io/gb-crawling/posts/2017-01-20-HowToMakeWebCrawler.html
------------------------------------------------------------------------------
#listAll > table > tbody > tr:nth-child(3) > td:nth-child(5) > a --> 1
#listAll > table > tbody > tr:nth-child(5) > td:nth-child(5) > a
#listAll > table > tbody > tr:nth-child(7) > td:nth-child(5) > a
#listAll > table > tbody > tr:nth-child(291) > td:nth-child(5) > a --> 180
'''

#listAll > table > tbody > tr:nth-child(3) > td:nth-child(5) > a
# https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/tmp.php?id=1&kat=DCMeshes&dp=Objects/OrangeMarmelade/meshes.zip
# https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/tmp.php?id=2&kat=DCMeshes&dp=Objects/BlueSaltCube/meshes.zip

base_url = 'https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/index.php?section=listAll'
download_base_url = 'https://h2t-projects.webarchiv.kit.edu/Projects/ObjectModelsWebUI/'
req = requests.get(base_url)
print(req.ok)
# print(res.headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')

for i, x in enumerate(soup.find_all('a', attrs={'title':'Triangulated meshes'})):
    d_url = download_base_url+x.get('href')
    r = requests.get(d_url)
    print(req.ok)

    z = zipfile.ZipFile(io.BytesIO(r.content))
    # z.extractall("/home/robot/Downloads/kit_models/{}".format(i))
    z.extractall("destination/for/your/environment/kit_models/{}".format(i))

    # requests.get(download_base_url+x.get('href'))
