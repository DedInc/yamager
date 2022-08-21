<h1 align="center">Yamager - Simple module for parsing images from Yandex.</h1>

<br>

<h1 align="center"> -How to use?- </h1>

```python
import yamager as yimg
from random import choice

images = yimg.searchImages('anime') #get image previews
previews = choice(images) #get previews of random image
print(yimg.getBestImage(previews)) #get best image of previews with high resolution
```