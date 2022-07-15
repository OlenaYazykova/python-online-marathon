def priority(y):
    if y in ['*', '/', '%']:
        return 2
    elif y in ['+', '-']:
        return 1

def toPostFixExpression(e):
    stack = []
    post = []
    for y in e:
        if y not in ['*', '/', '+', '-', '%', '(', ')']:
            post.append(y)
        else:
            if y != ')' and (not stack or y == '(' or stack[-1] == '('or priority(y) > priority(stack[-1])):
                stack.append(y)
            elif y == ')':
                while True:
                    x = stack.pop()
                    if x != '(':
                        post.append(x)
                    else:
                        break
            else:
                while True:
                    if stack and stack[-1] != '(' and priority(y) <= priority(stack[-1]):
                        post.append(stack.pop())
                    else:
                        stack.append(y)
                        break
    while stack:
        post.append(stack.pop())
    return post

e=["20","+","3","*","(","5","*","4",")"]
print(toPostFixExpression(e))
