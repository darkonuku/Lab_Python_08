import re

print
print'Lab 08, REGULAR EXPRESSIONS'
print
output = ''
inp = raw_input('Enter Email: ')
def isEmail(inp):
    output = re.match(r'(\w)+@(\w)+\.[..|....]',inp ,re.IGNORECASE)
    return output

if (output != None):
    print'True'
    
else:
    print 'False'
    
