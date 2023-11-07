# Facecompare.py
from functools import reduce
from PIL import Image
import math, operator
def compare(face, newface):
    h1 = Image.open(face).histogram()
    h2 = Image.open(newface).histogram()
    RMS = math.sqrt(reduce(operator.add, list(map(lambda a,b:
                (a-b)**2, h1, h2)))/len(h1))
    return RMS



