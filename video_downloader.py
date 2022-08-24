#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


pip install pytube


# In[ ]:





# In[39]:


import tkinter


# In[ ]:





# In[40]:


from tkinter import *
from pytube import YouTube


# In[41]:


root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("DataFlair-youtube video downloader")


# In[42]:


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()


# In[43]:


link = StringVar()

Label(root, text = 'https://youtu.be/Uw_otLQoqNw', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)


# In[44]:


def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




