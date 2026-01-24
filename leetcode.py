
'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.'''


nums=[2,7,5,6,3]
target=9
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# call the function and print the result
result=two_sum(nums, target)
print(result)

nums1=[2,7,5,6,3]
target1=9
'''
def two_sum(nums1,target1):
    num1_map={}
    for i,nums in enumerate(nums1):
        compon=target1-nums
        if compon in num1_map:
           return [num1_map[compon],i]
        num1_map[nums] = i
        
resu=two_sum(nums1,target1)
print(resu)'''


list1=[7,8,5,8,5,7,9]
resu=[]
for i in list1:
    if i>1:
        count = 0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            resu.append(i)
print(resu)


tup1=(4,7,1,8,21,23,29,13)
fact1=[]
for i in tup1:
    fact=1
    for j in range(2,i+1):
        fact=fact*j
    fact1.append(fact)

print(fact1)

########find index position of pivot number from list i.e left sum =right sum
li=[1,2,4,5,6,1]
#li=[1,2,3]
n=len(li)
print(n)
total=sum(li)
print(total)
left=0
def find_pivot(li):
    total = sum(li)
    left = 0
    for i,element in enumerate(li):
        right=total-left-element
        if left==right:
            return i
        left +=element
    return - 1

re=find_pivot(li)
print(re)


















