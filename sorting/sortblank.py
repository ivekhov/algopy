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

