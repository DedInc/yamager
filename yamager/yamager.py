from lxml import html, etree
from requests import get
from json import loads

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

def searchImages(search):
	previews = []

	tree = html.fromstring(get(f'https://yandex.net/images/search?text={search}').content)

	images = tree.xpath('//div[contains(@class, \'serp-item\')]')
	for image in images:
		try:
			previews.append(loads(image.attrib['data-bem'])['serp-item']['preview'])
		except:
			pass
	return previews