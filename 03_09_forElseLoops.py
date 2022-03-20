successFul = False
# successFul = True

for number in range(1, 4):
    print("Try ", number)
    if successFul:
        print("successful")
        break
else:
    print("Attempted 3 times failed")