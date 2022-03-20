
def fn(x):
  if 0 < x <= 9:
    return x
  x -= 9
  if 0 < x <= 90*2:
    num = ((x+1)//2+9)
    return [num, str(num)[(x+1)%2]]
  x -= 90*2
  if 0 < x <= 900*3:
    num = ((x-1)//3+100)
    # print(num)
    return [num, str(num)[(x+2)%3] ]

def fn2(x):
    if x <=0:
        return -1
    digit =1
    pow10 =1
    while(x >0):
        if 0 < x <= 9*pow10*digit:
            num = ((x+digit-1)//digit + pow10-1)
            # print(num)
            return [num, str(num)[(x+digit-1)%digit]]
        x -= 9*pow10*digit
        pow10 *= 10
        digit +=1

# x = int(input())
for i in range(1, 200):
  print(i, fn2(i))
  # print(i, fn(i))