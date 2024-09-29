import secrets

text_file = open("otp.txt", "a")

number = [[secrets.randbelow(10) for i in range (5)] for i in range (4)]

text_file.write(str(number)+ '\n')

text_file.close()  
print(number)
print("OTP Generated")  