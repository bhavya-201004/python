#f = open("Bhavya_text1.txt","r")
#Data = f.readline()
#data1 = f.readline()
#data2 = f.readline()
#print(Data)
##print(data2)
#f.close()



#we can use read directly but it reads all the lines in one go and if we use read and readline simultaneously
#then it will only show read command
#write(w) command erase all the previous data and add new data given 
#append(a) command all new data to the previous one 
#f = open("Bhavya_text1.txt","a")
#f.write("\nBhavya Bhaskar Kanth")
#f.close()


#append and write command can create a file just by open and close function if we havent created it


#with open("Bhavya_text1.txt","a+") as f:
    #data = f.write("\n Bhavya Bhaskar")
   # print(data)
    
#with command is generally used to open read and append files because it dont  need close command


#deleting a file as shown below
#import os
#os.remove("sample_text.py")


#replace a word as given
with open("sample.txt","a") as f:
    f.write("bhavya is smart \n he is intelligent")
    f.write("\nbhavya is smart \n he is cute")
    
with open("sample.txt","r") as f:
    old_data = f.read()
new_data = old_data.replace("smart","dumb")
print(new_data)   

with open("sample.txt","w") as f:
    f.write(new_data)