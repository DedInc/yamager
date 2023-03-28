from lxml import html
import requests
import re
import json

class Yamager:

    def __init__(self):
        self.agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
        self.headers = {'User-Agent': self.agent, 'Cookie': 'yp=1711521583.sp.bhtt:0:brl:0:family:0:pgtr:0'}

    @staticmethod
    def get_best_image(previews):
        max_size = 0
        best_url = ''
        for preview in previews:
            size = preview['w'] + preview['h']
            url = preview['url']

            if url.startswith('//'):
                url = 'https:' + url

            if max_size < size:
                max_size = size
                best_url = url
        return best_url

    def search_yandex_images(self, search, page=1, zenrows=None):
        previews = []

        if zenrows is None:
            response = requests.get(f'https://yandex.ru/images/search?text={search}&p={page}', headers=self.headers).content
        else:
            response = requests.get(f'https://api.zenrows.com/v1/?apikey={zenrows}&url=https://yandex.ru/images/search?text={search}&p={page}&js_render=true&window_width=1920&window_height=1080&custom_headers=true', headers=self.headers).content

        tree = html.fromstring(response)
        images = tree.xpath('//div[contains(@class, \'serp-item\')]')

        for image in images:
            try:
                previews.append(json.loads(image.attrib['data-bem'])['serp-item']['preview'])
            except:
                pass

        return previews

    def search_google_images(self, search):
        images = []
        tree = html.fromstring(requests.get(f'https://google.com/search?q={search}&tbm=isch&tbs=isz:l', headers=self.headers).content)
        scripts = tree.xpath('//script/text()')

        for script in scripts:
            trash = re.findall("https?://\S+?\.(?:jpg|jpeg|gif|png|webp|tiff|tif|svg|ico|eps|raw|cr2|nef|orf|sr2|kdc|dng|arw|rw2|x3f|raf|mos|mrw|fff|3fr|cin|dpx|exr|hdr|jxr|wdp)", script)
            for arg in trash:
                dem = arg.split(',["')
                images.append(dem[len(dem) - 1])
            if len(trash) > 0:
                break

        return images