

# #printing in python--------------------------------------------------
print ("Hello World by python!")
print (3*4)
print ("Boopathy!")

# ##-------------------------------------------------------------------


# #list in python------------------------------------------------------

# print (areas)

areas = ["boopathy", 24, "Teja", 76]
print ("teja")
print (areas[-1])

# ##-------------------------------------------------------------------


# #Function in python -------------------------------------------------
def add(a,b):
	c = a + b
	return c
	print (c)

result = add(2,3)
print (result)

# ##-------------------------------------------------------------------

# #If statement in python--------------------------------------------------

def ifstatement():
	areas = [1, 24, 4, 76, "Stalin"]
	if "Stalin" in areas:
		return ("Yes stalin is in the list")
firstif = ifstatement()
print (firstif)

def ifstatement2():
	areas = ["Name", "Madhu", "Siva", "Teja"]
	if "Madhu" in areas:
		return ("Yes Madhu is in the list")
secondif = ifstatement2()
print (secondif)

# ##-------------------------------------------------------------------

# #Writing a file using python------------------------------------------

fo = open("E:\\fileForSearch.html", "w")
fo.write( "<html> <body> <h1> Python is a great language.\nYeah its great!!\n  Madhu Madhu Madhu</h1></body></html>Madhu Madhu ");

# ##-------------------------------------------------------------------

# #Finding in how many line a word occur in given file:----------------
count=0
f=open('E:\\fileForSearch1.txt','r')
lines_in_file =f.readlines()
for line in lines_in_file:
    if "Madhu" in line:
        count=count+1
print(count)
f.close()

# ##-------------------------------------------------------------------

# #Finding how many times a word occus in the whole file---------------

f = open('E:\\fileForSearch1.txt').read()
count = f.count('Madhu')
print(count)

# ##-------------------------------------------------------------------


# #Opening a file and outputting its content into sublime text console-
f=open('E:\\fileForSearch1.txt','r')
print(f.read())

# ##-------------------------------------------------------------------

# #file.seek() and file.tell()-----------------------------------------

f.seek(7)
print(f.tell())
f.close()

#     # this seek function moved the cursor
# 	# to the mentioned position and whereas 
# 	# the tell function actually tells where the cursor 
# 	# is on the file right now.
# ##-------------------------------------------------------------------


# #To find number of words in a file and printing it-------------------
file=open('E:\\bigText.txt','r')
wordcount=0
for word in file.read().split():
    wordcount = wordcount + 1
print (wordcount)
file.close();

# ##-------------------------------------------------------------------
# #Printing what word occured how many times---------------------------
file=open('E:\\bigText.txt','r')
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
file.close();

# ##-------------------------------------------------------------------

# # Checking the commit to github after adding this text

# Python histogram:

import matplotlib.pyplot as plt 

fig = plt.figure("Histogram")
ax = fig.add_subplot(1,1,1)
ax.hist([21,12,23,23,45,65,23,12,56,32], bins = 7, facecolor = 'g', normed = "True")
plt.title("Distribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()



------------------------------------------------------------------------------------------------------


fig2 = plt.figure('Box-plot')
ax1 = fig2.add_subplot(1,1,1)
ax1.boxplot([21,23,45,43,67,43,24,67,54])
plt.show()


fig3 = plt.figure('Bar')
ax2 = fig3.add_subplot(1,1,1)
ax2.set_xlabel('X')
ax2.set_xlabel('Y')
ax2.bar([0,1,2,3],[5,10,15,5],[0.5,1,1.3,1], color = ['b', 'r'])
plt.show()