import uuid

text_file = open("otp.txt", "a")

def title(string_length=10):
    """Returns a random string of length string_length."""
    random = str(uuid.uuid4()) 
    random = random.upper() 
    random = random.replace("-","")
    return random[0:string_length]

text_file.write('|' + str(title(10)) + '|' + '\n')

text_file.close()  
print(title(10))
