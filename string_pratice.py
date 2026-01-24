#######String##########

Name="Swapnil"
Age=25
City="Mumbai"

print("I am " +Name+ " age is "+str(Age)+ " City is "+City)
print("I am {} ,age is {},city is {}".format(Name,Age,City))
print(f"I am {Name} ,age is {Age},city is {City}")

'''print(dir(str))
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__.py', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
'''

str1="We are learning Python Programming"
#upper() and lower() method:
print("upper case:",str1.upper()) #upper case: WE ARE LEARNING PYTHON PROGRAMMING
print("lower case:",str1.lower()) #lower case: we are learning python programming
print("swapcase result:",str1.swapcase()) #swapcase result: wE ARE LEARNING pYTHON pROGRAMMING
#Ex.
str2="Python"
print(str2[2].upper())#T
print(str2[:3].upper()) #PYT

#isupper() and islower method
#isupper method:This method return true if all character are in upper case.
#islower method:This method return true if all character are in lower case

str_a="PYTHON"
str_b='python'
print("str_a:",str_a.isupper(),str_a.islower()) #str_a: True False
print("str_b:",str_a.isupper(),str_a.islower()) #str_b: True False

#title method():This method convert first character each word in string to upper case.
str_c="Hello good morning"
print("title case:",str_c.title()) #title case: Hello Good Morning
#istitle method(0:This method check the given string is in title case or not.
str_d="Python  Learning Is Fun"
str_e="Programmimg language"
print("str_d :",str_d.istitle()) #str_d : True
print("str_e:",str_e.istitle()) #str_e: False

#split method :Split method,split the string in list of string from given delimeters.
str_f="Python is Easy to learn"
str_g="Python,is,Easy,to,Learn"
str_h="Good#Morning@Hope@You@are@good"

#split from space
print("space split result :",str_f.split(" "))#space split result : ['Python', 'is', 'Easy', 'to', 'learn']

#split from comma
print("comma split result",str_g.split(",")) #comma split result ['Python', 'is', 'Easy', 'to', 'Learn']
#splitfrom special character
print("space from special characters :",str_h.split("@"))#space from special characters : ['Good#Morning', 'Hope', 'You', 'are', 'good']

result=str_h.split("@")[0].split("#")[1]#Morning
print(result)

#replace method:This Method replace any given string from target string

str_j="Good#Morning@Hope@You@are@good"
result=str_j.replace("@"," ") #Good#Morning Hope You are good
print(result)
result1=result.replace("#"," ") #Good Morning Hope You are good
print(result1)
result3=str_j.replace("@"," ").replace("#"," ")#Good Morning Hope You are good
print(result3)

#join () method :The method join any given string with delimeters

str_1="Python"
result="-".join(str_1)
print(result)#P-y-t-h-o-n

str_z="Hello%good%morning%hope%you%enjoy%learning"
word_list=str_z.split("%")
print(word_list)
str_result=" ".join(word_list)
print(str_result) #Hello good morning hope you enjoy learning

list2=["a","b","c"]
print("".join(list2)) #abc

#write a python program to get longest word in the given string
str_x="Dipwali is best holyfestival"
word_list=str_x.split( " ")
max_length =word_list[0]
for word in word_list:

   if len(word) >len(max_length):
       max_lengh = word
   else:
        continue
print("lonest_word:",max_lengh) #lonest_word: holyfestival

#write a program to remove duplicateword from given string

str_y="Akash Manish Akshay Manish Akshay Rahul"
#output=Akash Manish Rahul Akshay
print(" ".join((list(set(str_y.split(" ")))))) #Akash Manish Rahul Akshay

result=""
word_list=str_y.split(" ")
for word in word_list:
    if word  not in result:
        result=result+word+" "
    else:
        continue
print(result) #Akash Manish Akshay Rahul

#strip() method: thismethod remove traling spaces from given string
str1="  Python Programming  "
print("strip:",str1.strip()) #Python Programming
str2=" good morning"
print(str2.strip()) #good morning
#lstip() method: this will remove  the left side space from given string

str_d="  good evening "
print(str_d.lstrip()) #good evening

#rstip() method: this will remove  the right side space from given string

print(str_d.rstrip()) #  good evening

str_b=" g o o d morning"
result2=str_b.strip()
print(result2)
word1=str_b[:8]
word2=str_b[8:]
print(" ".join([word1.replace(" ",""),word2])) #good  morning

########
#count method:this method return the right side space from string
str_c="Hello we are learning python programming"
print("count of o:",str_c.count("o")) #count of o: 3
temp=""
for char in str_c:
    if char not in temp:
        print(char,str_c.count(char))
        temp+= char
    else:
        continue
print(temp)
#index method :this method return the index position of any char/string
str_d="Today is rainy day"
print("index position of r:",str_d.index("r")) #index position of r: 9
#check the char,which does not exist in the string
#print(str_d.index("w")) #ValueError: substring not found



#find() method: This method return the index position of any char or substring,if it is available in the
# given string.if it is not available,then it will return -1.
str_e=" India is best cricket team"
print("index of b:",str_e.find("b")) #index of b: 10
print("index position of rindex of a",str_e.rindex("a"))#index position of rindex of a 25

print("index of w :",str_e.find("w")) #index of w : -1,as character is not available in the target string.

#get indexposition of all
for i in range(len(str_e)):
    print(i,":",str_e[i])

##############################
#str.isalnum:this method return true ifstringcontains alphate and numbers
str_j="Good 567"
str_k="Good567"
print("check is alphanum():",str_j.isalnum())#check is alphanum(): False
print("check is alphanum():",str_k.isalnum())#check is alphanum(): True

#############
#str.isalpha() method :this method check the given string is only contains alphabets

str_l="Program"
print("check of isalpha:",str_l.isalpha()) #check of isalpha: True
#str.isnumberic mehod:this method check the given string is only contains numberic
str_w="456777788"
print("check of isnumeric:",str_w.isnumeric()) #check of isalpha: True

#######
#str.isspace():this method return if given string only contains space
str_r="Hello Good Morning"
print("check of isspace:",str_r.isspace()) #check of isspace: False
str_p="   "
print("check of isspace:",str_p.isspace()) #check of isspace: True

for char in str_r:
    print(char,char.isspace())

# write python program to find odd and even length words and arrange them
str3="Good Morning,Hope you are doing good"

even_word=""
odd_word=""

word_list=str3.replace(",","  ").split()


for word in word_list:
    if len(word)%2==0:
        even_word=even_word+word+" "
    else:
        odd_word = odd_word +word + " "

print(even_word+odd_word)

#write a python to getall the word whose length is 5

str2="Hello Good rning , Weare earning Pytho Programming"

#output="Hello rning Weare Pytho"
result=""
word_list = str2.split(" ")

for word1 in word_list:
    if len(word1)== 5:
        result=result + word1+" "
    else:
        continue
print(result) #Hello rning Weare Pytho











