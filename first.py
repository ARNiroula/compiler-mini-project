import pprint

f=open('grammar.txt','r')

def is_terminal(str):
    if str.islower() or str=='#':
        return True
    return False

def is_nonterminal(str):
    if str.isupper() and str != '#':
        return True
    return False
    
rules={}
for x in f:
    lhs,rhs=x.split('=')
    lhs=str(lhs).strip()
    rhs=str(rhs).strip()
    if '/' in rhs:
        rhs=rhs.split('/')
        rhs[0]=rhs[0].strip()
        rhs[-1]=rhs[-1].strip()
    rules[lhs]=[rhs]


# pprint.pprint(rules)

first={}
def first(rules):
    keys=rules.keys()
    # print(keys)
    for keys,values in rules.items():
        print(values)
first(rules)

