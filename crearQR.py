# Importamos las librerías pyqrcode y png
import pyqrcode
import png 

# 'version' especifica el tamaño y capacidad de datos , va del 1 al 40 --> del mas chico al mas grande
# 'error' establece el nivel de correción de errores del código:
# 'L' -> 7%, 'M'-> 15%, 'Q'-> 25%, 'H'-> 30%
# 'mode' indica como se codificará el contenido: 'numeric', 'alphanumeric', 'kanji', 'binary'
# Dentro de create() indicamos la url 
url = pyqrcode.create('https://www.brightlabs.com.mx/', error='H', version=10, mode='binary')
# Dentro de png() indicamos el nombre de la imagen
url.png('brightlabsQR.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])