INSTALLATION:
Create a directory where you wish to generate the Onetime Pad.
Save the three python files im that directory.

HOW TO USE:
In Linux & MacOS open a terminal window and navigagte to the installation directory you chose.
In Windows open a Powershell window and navigate to the installation directory you chose.
Type "python3 cryptogen.py" press the enter key.
A textfile called otp.txt will be generated with the UUID for the One Time Pad and then the 4 column 30 row pad.
Once the pad has been written down, delete the text file.

UNINSTALL:
Delete the folder that has the python files in it.


Program was developed in Linux, should work in Windows. Some people say that Windows cryptgenrandom is not as secure as the urandom found in Linux. Not sure about MacOS, I assume it uses urandom as it is unix based.
