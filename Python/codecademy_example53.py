#Write your function here
def max_num(nums):
  max = nums[0]
  for num in nums:
    if num > max:
      max = num
  return max

#Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))