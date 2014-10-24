__author__ = 'Ayla'

#1
def whileloop(n):
    i=1

    while i <= n:
        print(i)
        i=i+1



n=10
whileloop(n)

#2
def whileloop(n):
        while True:
            userschoice=input('q. Exit:')
            if userschoice=="q":
                return userschoice








whileloop(10)

#3
def whileloop(m):
    sum=0
    i=1

    while sum <= m:
        sum+=i**2
        i=1+i
    print(i)
    return sum


m=10
print(whileloop(m))

