from IPython.display import HTML

import PIL
import base64
from PIL import Image
import io


with open("1_Introduction/images/vgg16.png", "rb") as f:
    data = f.read()
    print data.encode("base64")

im = data.encode("base64")






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
<img src="data:image/gif;base64,

""" 

bla = bla + im +'" width="650">'


HTML(bla)