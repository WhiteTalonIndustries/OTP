import os


text_file = open("otp.txt", "a")
text_file.write("------------"+ '\n')
text_file.close()  

os.system('python3 ./namegen.py')
text_file = open("otp.txt", "a")
text_file.write("------------"+ '\n')
text_file.close()  

text_file = open("otp.txt", "a")
text_file.write("-------------------------------------------------"+ '\n')
text_file.close()  
x=30
for i in range(0,x):
    os.system('python3 ./otp.py')
text_file = open("otp.txt", "a")
text_file.write("-------------------------------------------------"+ '\n')
text_file.close()  