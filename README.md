# Python Grammer Cheatsheets

## While

```py
cur = 1
while cur < 3:
    print(cur)
    cur += 1
    
'''
Output:
1
2
'''
```

## While-Else 

```py
cur = 1
while cur < 3:
    print(cur)
    cur += 1
else:
    print(cur)

'''
Output:
1
2
3
'''
```

## While with Break

```py
cur = 1
while True:
    if cur > 3:
        break
    print(cur)
    cur += 1

'''
Output:
1
2
3
'''
```
