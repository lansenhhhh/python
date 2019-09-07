#!/usr/bin/env python
# coding: utf-8

# In[3]:


from numpy import *
import matplotlib.pyplot as plt
def Generate_Img(img):
    m=img.shape[0]
    n=img.shape[1]
    k=img.shape[2]
    conv_img=zeros((m,n,k))
    return conv_img 
def _conv_each(img_block,kernel):
    conv_sum=0
    img_block=img_block.flatten()
    kernel=kernel.flatten()
    pixel_count=kernel.size
    for i in arange(pixel_count):
        conv_sum=conv_sum+img_block[pixel_count-1-i]*kernel[i]
    pixel_value=conv_sum
    if  pixel_value<0:
        pixel_value=0
    elif pixel_value>255:
        pixel_value=255
    else:
        pixel_value=pixel_value
    return pixel_value
def conv(img,kernel):
    conv_img=Generate_Img(img)
    k_size=kernel.shape[0]
    for i in arange(img.shape[0]-k_size):
        for j in arange(img.shape[1]-k_size):
            for k in arange(img.shape[2]):
                conv_img[i,j,k]=_conv_each(img[i:i+k_size,j:j+k_size,k],kernel)
    
    return conv_img

def test(SrcImg,kernel):
    SrcImg=plt.imread('lena512color.tiff')
    kernel=array([[-1,-1,-1],
                  [-1,9,-1],
                  [-1,-1,-1]])
    New_img=conv(SrcImg,kernel)
    fig=plt.figure(figsize=(10,20))
    ax1=fig.add_subplot(121)
    ax1.imshow(SrcImg)
    ax2=fig.add_subplot(122)
    ax2.imshow(New_img)


# In[6]:


from conv import *


# In[ ]:





# In[ ]:





# In[ ]:




