import secrets
import re

text_file = open("otp.txt", "a")

matrix = [[secrets.randbelow(10) for i in range (5)] for i in range (4)]

otp = [(str(matrix).strip("[]"))]

otp = re.sub(r"[\([{})\]]", "|", (str(otp)))
otp = re.sub(r",", "", (str(otp)))

text_file.write(str(otp) + '\n')

text_file.close()  
print(otp)
print("OTP Generated")  