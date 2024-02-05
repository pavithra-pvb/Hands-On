#Write your function here
def divisible_by_ten(nums):
  count = 0
  for x in nums:
    if (x % 10 == 0):
      count += 1
  return count


#Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))