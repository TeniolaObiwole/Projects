'''
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.


example
imput: nums = [2,7,11,15], target = 9
output: [0,1]


psuedocode
find a integer  that is the outcome of subtracting another integer from target. 
create a hashmap to store the index and integers as a key-value pair. 
for loop(integer, index) with enumerate function to get a tuple of integer and index
subtract integer (intger from the for loop above) from target and check if the result(pair) is in the hashmap 
if pair in hashmap return it's index and integer's index as a list 
else add integer and it's index as a key-value pair in hashmap
'''

nums = [2,7,11,15]
target = 9

def two_sums(nums, target):

    index_map = {}

    for index,integer in enumerate(nums):
        pair = target - integer 
        if pair in index_map:
            return list((index_map[pair], index))
        else:
            index_map[integer] = index 

output = two_sums(nums, target)

print(output)