import random
from lib import binary_search, recursive_binary_search

def main():
    nums = [random.randint(1, 100000) for _ in range(100000)]
    nums.sort()
    engine = binary_search.BinarySearchEngine(nums)
    min = 0
    max = len(nums) - 1
    choice  = nums[random.randint(min, max)]
    answer = engine.binary_search(choice)
    print(f'Non recursive binary search: {answer}')

    r_engine = recursive_binary_search.RecursiveBinarySearchEngine(nums)
    r_answer = r_engine.binary_search(min, max, choice, 0)
    print(f'Recursive binary search: {r_answer}')

if __name__ == '__main__':
    main()