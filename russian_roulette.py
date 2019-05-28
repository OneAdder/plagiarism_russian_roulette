import random
import os
from odf.opendocument import load
from odf.text import *

with open('wals_intro', 'r', encoding='utf-8') as f:
    pl = f.read()
    
filename = [f for f in os.listdir() if f.endswith('.odt')][0]

doc = load(filename)

h = H(outlinelevel=1, text="Plagiarism")
doc.text.addElement(h)

p = P(text=pl)
doc.text.addElement(p)

pool = range(6)
if random.choice(pool) == 4:
    doc.save(filename)
