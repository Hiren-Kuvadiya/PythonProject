class ListMapping:

    def map_and_iterate(self):
        # Define the lists within the method
        a = [1, 2, 3, 4]
        b = ['a', 'b', 'c', 'd']

        # Create a dictionary using zip
        mapped_dict = dict(zip(b, a))

        # Iterate over the dictionary
        for key, value in mapped_dict.items():
            print(f"Key: {key}, Value: {value}")