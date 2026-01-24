def armstrong(num):
    a=num
    sum_of_cube=0
    while a>0:
        rem=a%10
        sum_of_cube=sum_of_cube+rem**3
        a=a//10
    return sum_of_cube==num
    print("number is armstrong")

print(armstrong(153))

s="swapnil patil"

dict_dup={}

for i in s:
    if i in dict_dup:
        dict_dup[i]+=1
    else:
        dict_dup[i]=1
for i,count in dict_dup.items():
    if count>1:
        print(f"{i} appers {count} times")

d="sadhana"
print(d[::-1])

rev=""

for j in d:
    rev=j+rev
print(rev)

b= "shree ram"
list_b=b.split()
rev_words=[]
for i in list_b:
    rev=i[::-1]
    rev_words.append(rev)
result=" ".join(rev_words)

print(result)

print(b[::-1])
