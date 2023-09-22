##contais duplicate - solução 1
class Solution(object):
    def containsDuplicate(self, nums):
        n = len(nums)
        contains = False
        for i in range(n):
            for j in range(i + 1, n):
                if(nums[i] == nums[j]):
                    return True
        return False

## contains duplicate - solução 2
class Solution(object):
  def containsDuplicate(self, nums):
      hashset = set()

      for n in nums:
          if n in hashset:
              return True
          hashset.add(n)


## https://leetcode.com/problems/contains-duplicate/