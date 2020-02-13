import time, json

class Debugger:

    def __init__(self):
        self.data = []

    def print(self):
        print("debugger...", self.data)

    def log(self):
        filename = "Debugger_" + str(int(time.time())) + ".txt"
        file = open(filename, "w")
        print(self.data, file=file)
        file.close()
