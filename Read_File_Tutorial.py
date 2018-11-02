# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 14:32:03 2018

@author: imcco



This will be test code for rassberry pi's. The goal is to spin a stepper motor at some constant speed, 
save files to a USB or otherwise, 
This specific script will just be for reading in data, be sure to download the txt files that are mentioned...
... in here and keep them in the same folder that you have this python file in, otherwise you'll have to...
... redirect python "in-line" to where those files are now

"""

### This is pulling the file and seperating it into sub arrays within and larger array ###

text_file = open("tsi_model.txt", "r")#opens up the txt file tsi_model so python can read through it
#lines = text_file.read()#feel free to play with this code, some of this works in different ways and you can get similar results
#print (lines)
lines = text_file.read().splitlines()#this is how python will seperate all of the information in the file, in this case line by line
array = []#here we define an empty array so we can throw stuff into it later
for line in lines:#simple 'for' loop that goes through each line that we split up in the data and 'appends' it to the array
  array.append(line.split(','))#in this case we'll be using the comma simble to seperate each set in our array
  #line = line.split(',')

text_file.close()#after we're done reading in the data we close the file, since we're done with it and all

text_file2 = open("sorce_tsi_L3_c24h_latest_set.txt", "r")#next we open up our second file
lines2 = text_file2.read().splitlines()#again pre-splitting our data line by line
array2 = []#here's a new array we can start adding this data to
for line in lines2:#another 'for' loop that accomplishes the same goal as the first
  array2.append(line.split(' '))#in this case the data read in is not seperated by a comma but a simple space so we use that as our 'symbol' to seperate by
  
#lines = text_file.readlines()

text_file2.close()#again, since we're done with the file and don't need it anymore, we close it up

"""
Below is showing how you might find particular sets within the data, you could print the WHOLE array but...
... sometimes you only need one point of data or maybe just a smaller subset of it so feel free to play around with...
... what you want to see from the data or other wise
"""

print (array[45000])#this syntax allows you to see a particular set of data like the date, time, temperature, etc. in one line
print (array[49763][0])#however this is if you just want to, say, look at the date only

print (array[45000:49763])#this is if you would like to look at a subset of the data, like alot of the line for instance











