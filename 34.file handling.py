
import  os
f  = open("MyFile","w")
f.write("Hello i am Pratik \n i am a web developer \n i am learning things which help me to improve")

f  = open("MyFile","r")
print(f.read())
f.close()
# to rempve a file
os.remove("MyFile")
