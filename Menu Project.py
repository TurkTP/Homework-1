__author__ = 'Luke'
def whereis(s,letter):
    position = ''
    for i in range(len(s)):
        if position == "":
            position+=str(i+1)
        else:
            position +=","+str(i+1)
    return position

def count(s, letter):
    c=0
    for i in range(len(s)):
        if s[i].upper() == letter.upper():
            c+=1
    return c

def formatname(name):
    #makes first letters capitals and rest lower case

def firstname():
    fname=str(input('Enter employee(s) name'))
    return fname

def lastname():
    lname=str(input('Enter employee(s) name'))
    return lname

def DOB():
    mon=str(input('Enter month of birth'))
    if mon == 'January':
        mon == '01'
    elif mon == 'February':
        mon == '02'
    elif mon == 'March':
        mon == '03'
    elif mon == 'April':
        mon == '04'
    elif mon == 'May':
        mon == '05'
    elif mon == 'June':
        mon == '06'
    elif mon == 'July':
        mon == '07'
    elif mon == 'August':
        mon == '08'
    elif mon == 'September':
        mon == '09'
    elif mon == 'October':
        mon == '10'
    elif mon == 'November':
        mon == '11'
    elif mon == 'December':
        mon == '12'
    day=str(input('Enter day of Birth'))
    if day not in range(30):
        day=str(input('You need to enter a day 1-31'))
    yr=str(input('Enter year of birth'))
    dob=mon+'/'+day+'/'+yr
    return dob
def SS():
    ss=str(input('Enter your social security number (no spaces): '))
    first=ss.strip(1)
    ss.seek(2)
    second=ss.strip(2)
    ss.seek(5)
    third=ss.strip(4)
    ss=(first+'-'+second+'-'+third)
    return ss
def street():
    #Input the street address. Have them put in the number first, and the street name. Return this as one string.
    # Make sure to strip of any whitespace characters from the user input.
    num=str(input('Enter employee(s) Street Address: \n Number: '))
    name=str(input('Name: '))
    city=str(input('\n City: '))
    zip=str(input('\n Zip: '))
    state=str(input('\n State: '))
    street=(num+' '+name+','+city+' '+state+' '+zip+'.')
    return street



def menu():
    print('1. Input employee first name. \n2. Input employee last name. \n3. Input employee DOB \n4. Input employee SS#'
          '\n5. Input employee \n6. Print out employee information.\n7. Quit')
    opt=str(input('Which option would you like to chose'))
    while opt != '7' :
        opt=str(input('Enter a menu option'))
        if opt == '1':
            print(formatname(firstname()))
        elif opt == '2':
            print(formatname(lastname()))
        elif opt == '3':
            print(DOB())
        elif opt == '4':
            print(SS())
        elif opt == '5':
            print(street())
        elif opt == '6':
            print(fname+','+lname+','+DOB()+','+SS()+','+street()+'.')
    else:
        print('Goodbye!')
        exit()

menu()