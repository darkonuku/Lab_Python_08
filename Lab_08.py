
print'Lab 08'
print'-------------------------- QUE 3 -------------------------------'
print

import re

inp = raw_input('Enter your email: ')
isEmail(inp)

def isEmail(inp):
    
    output = re.compile(r'\w+@\w+\.[a-z|A-Z]{2,4}', re.IGNORECASE)
    mail = output.match(inp)

    if mail:
        print 'True'
    else:
        print 'False'

print
print'-------------------------- QUE 4 -------------------------------'
print

def getTxts(files):

    txt = re.compile(r'\w+\.txt\b')
    output = txt.findall(files)

    if txt:
        print output
    else:
        pass

getTxts('yo.html blah.txt woah.txt he ')


print
print'-------------------------- QUE 5 -------------------------------'
print

def percAwesome(inp):

    found_count = 0
    per = re.compile(r"\w+[ |\n||\w]",re.IGNORECASE)
    per_list = per.findall(inp)
    
    for words in per_list:
        if (re.search('\w*awes[o,0]me\w*', words)):
            found_count +=1
        else:
            pass
    print'the level of awsomeness is:',int((found_count/float(len(per_list)))*100),'%'

percAwesome('iamawesomeblah and awes0me is as awesomeo does')


print
print'-------------------------- QUE 6 -------------------------------'
print

