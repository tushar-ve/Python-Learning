import os
# if(not os.path.exists("data")):
#     os.mkdir("data")
# for i in range(0, 30): 
#     os.mkdir(f"data/Day{i+1}")


# Rename the directories 

# for i in range(0,30):
#     os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")


# folders = os.listdir("data")

# print(folders)
# print(os.getcwd())
# print folder inside the repository 
# for folder in folders:
#     print(folder)

# create file inside the file 
# for folder in folders
#     folders=os.open(f"data/{folder}/filename.txt",os.O_RDONLY|os.O_CREAT)
#     print(folder)
#     print(os.listdir(f"data/{folder}"))


# Read a File
try:
    file=os.open("data/Tutorial2/filename.txt",os.O_RDONLY)
    myData=os.read(file,105)
    myStr=myData.decode("UTF-8")
    print(myStr)
except Exception as e:
    print(str(e))
finally:
    os.close(file)


# How to write a file

# try:
#     file=os.open("data/Tutorial2/filename.txt",os.O_WRONLY | os.O_APPEND)
#     myStr="Hi This is Pythonforbeginners.com"
#     myData=myStr.encode("UTF-8")
#     os.write(file,myData)
# except Exception as e:
#     print(str(e))
# finally:
#     os.close(file)