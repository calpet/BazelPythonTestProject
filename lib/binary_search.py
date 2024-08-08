class BinarySearchEngine:
    def __init__(self, nums: list):
        self.nums = nums
    
    def binary_search(self, choice):
        min = 0
        max = len(self.nums) - 1
        guess = 0
        attempts = 0
        while (guess != choice):
            index = int((min + max) / 2)
            guess = self.nums[index]
            if guess == choice:
                return attempts
            elif guess < choice:
                attempts += 1
                min = index + 1
            else:
                attempts += 1
                max = index - 1
                
        # not found:
        return -1