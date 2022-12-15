
#multiplying two numbers
# number1=20
# number2=30
# a='The result is {}'
# print(a.format(number1*number2))

#finding the missing integer
# n=5
# a={1,2,3,5}
# b=[]
# for i in range(1,n):
#     if i not in a:
#         b.append(i)
# for j in b:
#     c=str(j)
# print(c)

#list comprihension for finding between the range which is divicible by 3
# a=[i for i in range(1,50) if i%3==0]
# print(a)

#finding numbers with even number digits
# nums=[12,345,26,6,7896,7895,56]
# b=[]
# n=0
# for i in nums:
#     str_nums=str(i)
#     b.append(str_nums)
# print(b)
# for j in b:
#    len_b=len(j)
#    if len(j)%2==0:
#       n+=1
# print(n)
#using simple method
# count=0
# for i in nums:
#    if len(str(i))%2==0:
#       count+=1
# print(count)


#finding how many times substring is appears
# str='emma is a good developer. emma is a writer'
# a=str.split()
# count=0
# print(str.split())
# for i in a:
#     if i == 'emma':
#         count+=1
# print('emma appeared {} times'.format(count))

#
# nums=[1,1,1,2,2,3]
# a=[]
# b=[]
# c=[]
# count=0
# count1=0
# for i in nums:
#    str_c=str(i)
#    c.append(str_c)
# print(c)
# for j in range(0,len(c)):
#    if j not in a:
#          a.append(j)
#          count+=1
#    elif j in a:
#          b.append(j)
#          count1+=1
# print(count)
# print(count1)
# #
# print(a)
# print(b)

#

#
a=[1,1,1,2,2,3]
k=2
b=[]
c=[]
count=0
for j in range(0,k):
    num=a[0]
    for i in a:
        frequent= a.count(i)
        if (frequent>count):
            count=frequent
            num=i
    c.append(num)
    if num in a:
        for i in a:
            a.remove(num)
        b=a
        a=b
print(c)


#program to sort the elements in odd positions in descending order and elements in ascendind order
# a=[1,2,3,4,5,6,7,8,9]
# b=[]
# c=[]
# d=0
# e=0
# for i in range(0,len(a)):
#         if (i%2==0) :
#             b.append(a[i])
#         else:
#             c.append(a[i])
# b.sort(reverse=True)
# c.sort()
# for i in range(0,len(a)):
#     if (i%2==0):
#         a[i]=b[d]
#         d+=1
#     else:
#         a[i]=c[e]
#         e+=1
# print(a)


# print(b)
# print(c)
# print(len(a))a

#using slicing method

# a=[1,2,3,4,5,6,7,8,9]
# c=a[1::2]
# b=a[::-2]
# # b.sort(reverse=True)
# # print(b)
# d=0
# e=0

#
#
# for i in range(0,len(a)):
#     if(i%2==0):
#         a[i]=b[d]
#         d+=1
#     else:
#         a[i]=c[e]
#         e+=1
# print(a)

#sum of square of first n natural numbers
# n=4
# a=0
# for i in range(0,n+1):
#    a+=(i*i)
# print(a)

#finding sum of integer in given sentence
# string='200 plus 500 is equal to'
#
# b=string.split()
# print(b)
# d=0
# n=1
# for i in b:
#    if i.isdigit():
#       d+=int(i)
# print(d)


#finding numbers of vowels and consonents in the substring
# a=input('enter the input:')
# vowels=""
# consonants=""
# for i in a:
#     if i.lower() in ('a','e','i','o','u'):
#         vowels+=i
#     else:
#         consonants+=i
# print('total numbers of vowels:',len(vowels))
# print('total numbers of consonants:',len(consonants))

# BLACKJACK: Given three integers between 1 and 11,
# if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# blackjack(5,6,7) --> 18
# blackjack(9,9,9) --> 'BUST'
# blackjack(9,9,11)-->19

# def blackjack(a,b,c):
#     sum=a+b+c
#     if (sum<=21):
#         return sum
#     elif (sum>21)and (a==11 or b==11 or c==11):
#         return (sum-10)
#     else:
#         return('Bust')
# a=int(input('a'))
# b=int(input('b'))
# c=int(input('c'))
# print(blackjack(a,b,c))

#Longest Substring Without Repeating Characters
s=str(input('s:'))
i=0
j=0
output=0
a=set()
while j< len(s):
    if (s[j]) not in a:
        a.add(s[j])
        j+=1
        output=max(output,len(a))
    else:
        a.remove(s[i])
        i+=1
print(output)

#print list in reverse order using a loop
# list=[10,20,30,40,50]
# rev=list[::-1]
# for i in rev:
#     print(i)



# n=int(input('enter the number:'))
# dict={}
# for i in range(1,n+1):
#         a={i:(i*i)}
#         dict.update(a)
# print(dict)




