print('Welcome to my first task!')
#loop thats prints GCI is great:
x = 0
while x < 10:
    x += 1
    #I think the x can make an index number for the text :|
    print(str(x)+'. GCI is great')
#input and answer for name:
userName = input('Please enter your name:\n')
print('Hello '+str(userName)+', please to meet you!')
#reverse name:
#learned from: https://www.w3schools.com/python/python_howto_reverse_string.asp
def func():
    return userName[::-1]
revName = func()
print('Did you know that your name backwards is '+str(revName)+'?')
