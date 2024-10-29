# nums = map(int, input("Enter your scores (separated by space): ").split())
#
# print(nums)
#
# for num in nums:
#     print(num)



whole_input = input("Enter your scores (separated by space): ").split()
print(whole_input)
print(type(whole_input))
nums = list(map(int, whole_input))

print(nums)

for num in nums:
    print(num)

