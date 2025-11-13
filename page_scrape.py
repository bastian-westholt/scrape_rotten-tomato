from bs4 import BeautifulSoup

with open('page.html', 'r') as page_obj:
    content = page_obj.read()

soup = BeautifulSoup(content, 'html.parser')

title = soup.find('media-hero')
print(title.find('rt-text', {'slot': 'title'}).text)
print()

critics_consensus = soup.find('div', {'id': 'critics-consensus'})
print(critics_consensus.find('rt-text').text.strip())
print(critics_consensus.find('p').text.strip())
print()

media_infos = soup.find('section', {'class': 'media-info'})
media_infos = media_infos.find_all('div', {'class': 'category-wrap'})
for element in media_infos:
    text = element.text.strip()
    if text:
        # Ersetze mehrfache Leerzeilen mit einer einzigen Leerzeile
        print(text.split())
        text = ' '.join(text.split())
        print(text)

print()