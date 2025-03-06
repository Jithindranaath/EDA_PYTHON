import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x1=np.linspace(0,10,100)

#create a plot figure
fig=plt.figure()

# plt.plot(x1, np.sin(x1), '*')  #in plot we get ony one graph
# plt.plot(x1, np.cos(x1), '--')
# plt.plot(x1, np.tan(x1), '-')
# plt.show()

# plt.subplot(2,1,1) #(rows,columns,panel num) in subplot we get more than one graph
# plt.plot(x1,np.sin(x1))
# plt.subplot(2,2,1)
# plt.plot(x1,np.cos(x1))
# plt.show()

# print(plt.gcf())  #get current figure info

# print(plt.gca())  #get current

plt.plot([1,2,3,4]) #linear
plt.ylabel('Numbers')
plt.show()

plt.plot([1,2,3,4], [54,79,36,9]) #non-linear
plt.ylabel('Numbers')
plt.show()

x=np.linspace(0,2,100)
plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')
plt.legend()
plt.show()

txt='jithu hehe'
print(txt.split())  #uses to split the string with ','


import streamlit as st
st.write('dfjgvfsgfgy')