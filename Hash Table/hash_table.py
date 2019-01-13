# Hash table implementation in Python without using dicts


class HashTable():

    def __init__(self, n=10):
        self.hash_table = self.create_hash_table(n)

    def create_hash_table(self, n):
        """Function to create hash table with 'n' values"""
        hash_table = [[] for _ in range(n)]
        return hash_table

    def hashing_func(self, key):
        return hash(key) % len(self.hash_table)

    def insert(self, key, value):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = ((key, value))
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = self.hashing_func(key)
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v

    def delete(self, key):
        hash_key = self.hashing_func(key)
        key_exists = False
        bucket = self.hash_table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print ('Key {} deleted'.format(key))
        else:
            print ('Key {} not found'.format(key))
