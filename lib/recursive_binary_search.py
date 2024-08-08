class RecursiveBinarySearchEngine:
    def __init__(self, nums):
        self.nums = nums
        
    def binary_search(self, min, max, choice, attempts):
        print(f'Attempt: #{attempts} \tPossible range in array: [{min} - {max}]')
        # Start at the middle of the array:
        index = int((min + max) / 2)
            
        value = self.nums[index]

        # If the value is higher than the chosen number, it will know it needs to look lower in the array.
        # Grab index of value and set it as new maximum, narrowing down the range in which the chosen number hides in.
        if value > choice:
            attempts += 1
            return self.binary_search(min, index, choice, attempts)
        elif value < choice:
            attempts += 1
            return self.binary_search(index, max, choice, attempts)
        else:
            return attempts