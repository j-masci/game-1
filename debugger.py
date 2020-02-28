import time, json, pprint


class Debugger:

    def __init__(self):
        self.data = []
        self.pp = pprint.PrettyPrinter()

    def print(self):
        print("debugger...", self.data)

    def log(self):
        filename = "./logs/Debugger_" + str(int(time.time())) + ".txt"
        file = open(filename, "w")
        output = self.pp.pformat(self.data)
        file.write(output)
        file.close()
