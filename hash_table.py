class Contact:
    def __init__(self,name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'{self.name} : {self.number}'


class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        current = self.data[index]

        if self.data[index] is None:
            self.data[index] = Node(key, value)
            return

        while current:
            if current.key == key:
                current.value = value
                return

            if current.next is None:
                break
            current = current.next

        current.next = Node(key, value)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        return None

    def print_table(self):
        for index, bucket in enumerate(self.data):
            current = bucket

            if current is None:
                print(f'Index {index}: Empty')
                continue

            peices = []

            while current is not None:
                peices.append(str(current.value))
                current = current.next

            print(f'{index} : {peices}')

  