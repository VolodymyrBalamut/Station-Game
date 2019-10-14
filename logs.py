from datetime import datetime

class Logs:
    def __init__(self, file="logo.txt"):
        self.__file = open(file, "a")
        self.__file.write("Station logs! " + str(datetime.now().strftime("%x - %X")) + "\n")
    def write(self, text):
        self.__file.write("\t" + text + "\n")
        print(text)
    def close(self):
        self.write("Good Bye!")
        self.__file.close()