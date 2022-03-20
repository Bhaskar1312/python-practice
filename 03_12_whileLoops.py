number =23

while 0 < number <=100:
    print(number)
    number //=2

command =""
# while(command !='quit' and command != "QUIT"):
while(command.lower() != "quit"):
    command = input(">")
    print("ECHO", command)

# run using python 03_12_whileLoops.py