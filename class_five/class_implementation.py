from class_interface import ListInterface

class List(ListInterface):
    def __init__(self):
        self._internal_list = []

    def sort(self):
        self._internal_list.sort()

    def append(self, data):
        self._internal_list.append(data)

    def remove(self, data):
        self._internal_list.remove(data)
