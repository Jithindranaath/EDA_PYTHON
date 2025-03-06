import numpy as np
# ones_arr=np.ones((5,5),dtype=int)
# print(ones_arr)
# print(ones_arr*255)  #it just multiplies the value of ones_arr to 255

import matplotlib.pyplot as plt  #matplotlib is used for visualisation
# %matplotlib inline
# pip install pillow
from PIL import Image
horse_img=Image.open(r'c:\Users\ADMIN\OneDrive\Pictures\Saved Pictures\varsha.jpg')
plt.imshow(horse_img)
plt.show()
print(type(horse_img))
horse_arr=np.asarray(horse_img)
print(horse_arr)
print(type(horse_arr))
plt.imshow(horse_arr)
plt.show()
horse_red=horse_arr.copy()
print(horse_red.shape)  #height,width,rgb
plt.imshow(horse_red[:,:,0])
plt.show()
print(horse_red==horse_arr)
plt.imshow(horse_red[:,:,0],cmap='Greys')
plt.axis('off')   #it wont show axis
plt.show()
plt.imshow(horse_red[:,:,0],cmap='Purples')
plt.axis('off')
plt.show()
plt.imshow(horse_red[:,:,0],cmap='Blues')
plt.axis('off')
plt.show()
plt.imshow(horse_red[:,:,0],cmap='Reds')
plt.axis('off')
plt.show()
plt.imshow(horse_red[:,:,0],cmap='YlOrBr')
plt.axis('off')
plt.show()
plt.imshow(horse_red[:,:,0],cmap='BuPu')
plt.axis('off')
plt.show()