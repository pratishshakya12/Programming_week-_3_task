# Create a Python program that greets the user with the message "Welcome to the
# Magic Forest". Then, ask the user whether they want to go "north" or "south". If
# they choose "south", print "Game Over". If they choose "north", ask if they want to
# "cross the river" or "follow the path". If they choose "cross the river", print "Game
# Over". If they choose "follow the path", ask them to choose between "fairy","ogre",
# or "elf". If they choose "ogre" or "fairy", print "Game Over". If they choose "elf",
# print
print('Welcome to the Magic Forest')
ans1=input('Do you want to go north or south')
if ans1=='south':
    ans2=input('Do you want to go cross the river or follow the path')
    if ans2=='follow the path':
        ans3=input('Choose between fairy ogre or elf')
        if ans3=='elf':
            print('You Win')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')