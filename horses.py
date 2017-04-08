import random

class Horse:
    def __init__(self, name, count = 0):
        self.name = name
        self.count = count

    def go_steps(self, step):
        self.count += step

    def get_name(self):
        return self.name

#haciendo una prueba de git hub