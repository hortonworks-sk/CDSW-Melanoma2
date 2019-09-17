from IPython.display import HTML

import PIL
import base64
from PIL import Image
import io


i = PIL.Image.open('1_Introduction/images/add_classifier.jpg')

i.show()

im = Image.open('1_Introduction/images/vgg16.png')

im.show() 


with open("1_Introduction/images/vgg16.png", "rb") as file:
    img = base64.b64encode(file.read())

img = Image.open(io.BytesIO(img))
img.show() 




bla = """<center>
<p><br><br><br><br><br>

<H1> Using deep learning to classify Melanoma </H1>
<H2> skiaie@cloudera.com </H2>


<br><br><br><br>

<h2>Goal </h2>
<!--<p align="left"> -->
<b> To build a classifier that can  <br><br> 1) take an image of skin <br> <br> 2) determine whether the patient needs critical attention form a physician.  
<br><br><br><br><br><br>
<!--
<p align="left">

We will build a classifier which takes an image of skin, and tells us if the patient associated with that image, needs critical attention from a physician. 
-->
<p align="center">
<img src="

""" 

bla = bla + im +">"

print(bla)

HTML(bla)