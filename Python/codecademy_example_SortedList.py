class SortedList(list):

    def __init__(self, lst):
        super().__init__(lst)
        self.sort()

    def append(self, value):
        super().append(value)
        self.sort()

new_list = SortedList([4, 1, 5])
print(new_list)
new_list.append(0)
print(new_list)