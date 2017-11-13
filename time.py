import datetime as dt

a = dt.datetime.now()

print (a)
a = str(a)
# a= a[11:16]

time=a[11:13]+a[14:16]


print (time)

#time=int(input("Please enter the time: "))
#string=str(time)

string=a[11:13]+a[14:16]
time = int(string)
finished=False
word = "You entered a wrong time"
while word == 'You entered a wrong time':
        if word == 'You entered a wrong time':
                word = '.'
                if len(string) == 3:
                        string = string[0:1]+string[1:]
                        a = int(string[1:])
                        if a>59:
                            word = 'You entered a wrong time'
                            time = int(input("You entered a wrong time \n Please enter the time: "))
                        elif time > 400 and time < 1000:
                            word = ","
                                                  
                            print('Good morning!')
                            
                             
                elif len(string)==4:
                        string=string[0:2]+string[2:]
                        a=int(string[2:])
                        if a>59:
                            word='You entered a wrong time'
                            time=int(input("you entered a wrong time \n Please enter the time: "))
                        elif time>=1000 and time<1100:
                            print('Good morning!')
                        elif time>=1100 and time<1300:
                            print('Good day!')
                        elif time>=1300 and time<1800:
                            print('Good afternoon!')
                        elif time>=1800 and time<2300:
                            print('Good evening!')
                        else:
                            print('Good night!')
                elif len(string)==2 and time>0:
                    
                        a=int(string)
                        if a>59:
                            print('You entered a wrong time')
                        else:    
                            print('Good night!')
                elif len(string)==1 and time>0:
                        a=int(string)
                        print('Good night!')
                else:
                        time=int(input('You entered a wrong time'))





