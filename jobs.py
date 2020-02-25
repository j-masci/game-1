

# jobs, a.k.a. systems, processes, actions etc.
# want to make a system for executing a very large number of
# requirements:
# - jobs need to run in a particular order and need to be able to be added and removed
# - need to run them efficiently
# - want to add tons of profiling to know exactly how long each job took.
# - all of this will mean using an enormous amount of mutable state

class Jobs:

    def __init__(self):
        self.jobs = []


    def register(self, *args):
        self.jobs.append('')
        return len(self.jobs) - 1



    def process(self):
        self.jobs = []
        pass



