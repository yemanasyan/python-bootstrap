import random


class RandomizedSet:

    def __init__(self):
        self._items_dict = dict()
        self._items_list = list()

    def insert(self, val: int) -> bool:
        if val in self._items_dict:
            return False

        self._items_dict[val] = len(self._items_list)
        self._items_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self._items_dict:
            return False

        index = self._items_dict.pop(val)
        # check to see whether it was the last element
        if index < len(self._items_list) - 1:
            self._items_list[index], self._items_list[-1] = self._items_list[-1], self._items_list[index]
            self._items_dict[self._items_list[index]] = index

        self._items_list.pop()

        return True

    def getRandom(self) -> int:
        index = random.randint(0, len(self._items_list) - 1)
        return self._items_list[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
