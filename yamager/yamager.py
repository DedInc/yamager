from lxml import html, etree
from requests import get
from json import loads
from re import findall

agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
headers = {'User-Agent': agent}

def getBestImage(previews):
	sizes = []
	urls = []
	for preview in previews:
		sizes.append(preview['w'] + preview['h'])
		url = preview['url']
		if url.startswith('//'):
			url = 'https:' + url
		urls.append(url)
	return urls[sizes.index(max(sizes))]

def searchYandexImages(search):
	previews = []

	tree = html.fromstring(get(f'https://yandex.net/images/search?text={search}', headers=headers).content)

	images = tree.xpath('//div[contains(@class, \'serp-item\')]')
	for image in images:
		try:
			previews.append(loads(image.attrib['data-bem'])['serp-item']['preview'])
		except:
			pass
	return previews

def searchGoogleImages(search):
	images = []
	tree = html.fromstring(get(f'https://google.com/search?q={search}&tbm=isch', headers=headers).content)
	scripts = tree.xpath('//script/text()')
	for script in scripts:
		if 'Size' in script:
			trash = findall("https?://\S+?\.(?:jpg|jpeg|gif|png|webp)", script)
			for arg in trash:
				dem = arg.split(',["')
				images.append(dem[len(dem) - 1])
			break
	return images