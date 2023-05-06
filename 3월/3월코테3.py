s=input()
stack=[]
isCorrect =True
gdict={
    '(':')',
    '{':'}',
    '[':']'
}

for i in s:
    if i in ['(','[','{']:
        stack.append(i)
    else:
        if len(stack)==0:
            isCorrect=False
            break
        t= stack.pop()
        if i==gdict[t]:
            continue
        else:
            isCorrect=False
            break

if len(stack) !=0:
    isCorrect=False

if isCorrect:
    print('YES')
else:
    print('NO')