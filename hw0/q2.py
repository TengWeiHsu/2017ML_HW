from PIL import Image
from numpy import *
 
pil_im = Image.open("C:/Users/USER/Documents/GitHub/2017ML_HW/Given/Lena.png")   
pil_im = pil_im.rotate(180)     
pil_im.save("C:/Users/USER/Documents/GitHub/2017ML_HW/Given/ans.png", 'png')