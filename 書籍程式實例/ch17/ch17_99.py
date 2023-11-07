# ch17_99.py
from PIL import Image

pict = Image.open("jkhung.jpg")           # 建立Pillow物件
width, height = pict.size
newPict1 = pict.resize((100,100))   # 寬度是2倍
newPict1.save("jhung.jpg")




