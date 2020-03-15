class Sort:

    def __init__(self, arr):
        self.array = arr

    def swap(self, a, b):
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def myprint(self):
        for item in self.array:
            print(item, end=' ')
        print("\n")

    def myprint_first(self, num):
        for item in self.array[0 : num]:
            print(item, end=' ')
        print("\n")


    def myprint_last(self, num):
        for item in self.array[ len(self.array) - num  : len(self.array) - 1]:
            print(item, end=' ')
        print("\n")

