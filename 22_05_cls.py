
class Myineterator:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == len(self.obj):
            raise StopIteration
        current_item = self.obj[self._index]
        current_index = self._index
        self._index += 1
        return (current_index, current_item)



for item, index in Myineterator(['один', 'два', 'три']):
    print(item, index)