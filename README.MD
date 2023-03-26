<h1 align="center">Yamager - Simple module for parsing images from Yandex and Google.</h1>

<br>

<h1 align="center"> -How to use?- </h1>

```python
from yamager import Yamager
import random

yamager = Yamager()

############Yandex Images############
images = yamager.search_yandex_images('anime') #get image previews
previews = random.choice(images) #get previews of random image
print(yamager.get_best_image(previews)) #get best image of previews with high resolution
#####################################

############Yandex Images with ZenRows bypasser############
images = yamager.search_yandex_images('anime', zenrows='API_KEY')
previews = random.choice(images)
print(yamager.get_best_image(previews))
#####################################

############Yandex Images pages############
images = yamager.search_yandex_images('anime', page=30)
previews = random.choice(images)
print(yamager.get_best_image(previews))
#####################################

############Google Images############
images = yamager.search_google_images('anime')
print(random.choice(images)) #get random image from search
#####################################
```