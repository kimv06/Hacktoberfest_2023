# Title: 442. Find All Duplicates in an Array
# Difficulty: Medium
# Problem: https://leetcode.com/problems/find-all-duplicates-in-an-array/

def findDuplicates(nums: list[int]) -> list[int]:
        #testcase for this function
        """
        >>> findDuplicates([2,4,52,4,6,2,5,6,3,5])
        [2, 4, 5, 6]
        """

        nums= sorted(nums)
        duplicates=[]
        # Iterate through the sorted list.
        for i in range(1,len(nums)):
            # Check if the current element is equal to the previous element.
            if nums[i]==nums[i-1]:
                # If equal, it's a duplicate, add it to the 'duplicates' list
                duplicates.append(nums[i])
        return duplicates

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    result = findDuplicates([2,4,52,4,6,2,5,6,3,5])
    print(result)


