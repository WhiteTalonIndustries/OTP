# generates a 4 column 30 row text for shared encryption to fit madgear.shop formating
# options write to file with --filename

import uuid, re, os, secrets

print('Defaults listed in ()')

try:
    title_length = int(input('Title Length (10): '))
except:
    title_length = 10
try:
    number_columns = int(input('Number of columns (4): '))
except:
    number_columns = 4 
try:
    number_rows = int(input('Number of rows: (30)'))
except:
    number_rows = 30


print('')
print('For security reasons, writing this info to a file is not recommended')
print('')
try:
    filename = str(input('Enter a file name to write to: '))
except:
    pass


def title(length: int = 10):
    """Returns a random string of length title_length."""
    random = str(uuid.uuid4())
    random = random.upper()
    random = random.replace("-","")
    return str(random[0:title_length])


def build(columns):
    matrix = [[secrets.randbelow(10) for i in range (5)] for i in range (columns)]
    otp = [(str(matrix).strip("[]"))]
    otp = re.sub(r"[\([{})\]]", "|", (str(otp)))
    otp = re.sub(r",", "", (str(otp)))
    otp = re.sub(r"'", "",(str(otp)))

    yield otp


def write_file(filename):
    with open(filename, 'w') as file:
        file.write("------------" + "\n")
        file.write("|"+title(title_length)+"|" + "\n")
        file.write("------------" + "\n")
        file.write("-----------------------------------------------" + "\n")
        for i in range(0,number_rows):
            for x in build(number_columns):
                file.write(x + "\n")
        file.write("-----------------------------------------------" + "\n")                


if __name__ == "__main__":
    if filename:
        # write to file
        write_file(filename)
        # print out file
        with open(filename, 'r') as file:
            for line in file:
                print(line.strip())
    else:
        print("------------")
        print("|"+title(title_length)+"|")
        print("------------")
        print("-----------------------------------------------")
        for i in range(0,number_rows):
            for x in build(number_columns):
                print(x)
        print("-----------------------------------------------")                