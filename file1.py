#!/usr/bin/env python
# coding: utf-8

# In[6]:


f = open("hi.txt",'w')
f.write("WELCOME")
f.write("new\n")
f.write("file")
f.close()
print(f.read)


# In[18]:


f = open("hi.txt",'a')
f.writelines(["hi\n","hello\n","python\n"])
f.close()


# In[39]:


f = open("sample.txt")
f.readline()
f.readline()
f.readline()
f.close()


# In[25]:


f = open("sample.txt",'r')
f.readlines(3)
f.close()


# In[31]:


f =open("sample.txt")
f.tell()
f.read(2)
f.tell()
f.read(2)
f.tell()
f.close()


# In[34]:


get_ipython().run_cell_magic('writef+3', '', '-27ile newfile.txt\nhello\nhi\nhow are u\niam fine')


# In[5]:


f = open("newfile.txt")
f.seek(0,2)
f.read()
f.close()


# In[7]:


with open("new.txt",'w') as f:
    f.write("Hello World")
print(f.closed)


# In[16]:


f = open("untitled1.txt")
cw =0
cs=0
for i in f.readlines():
    for j in i :
        if j.isalpha():
            cw = cw+1
        elif j==' ':
            cs = cs+1
print(cw,cs)            

