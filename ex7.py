#Make a two-player Rock-Paper-Scissors game.
#(Hint: Ask for player plays (using input)
#compare them
#print out a message of congratulations to the winner
#and ask if the players want to start a new game)

#Remember the rules:

#Rock beats scissors
#Scissors beats paper
#Paper beats rock

a = 0
b = 0

choices = ['rock', 'paper', 'scissors']
while a == 0:
    u1_choice = input('Player1: Rock.. Paper.. Scissors!: ')
    if u1_choice.lower() in choices:
        a = a + 1
    else: print("This isnt one of the choices")

while b == 0:
    u2_choice = input('Player1: Rock.. Paper.. Scissors!: ')
    if u2_choice.lower() in choices:
        b = b + 1
    else: print("This isnt one of the choices")

print(f"p1: " + u1_choice)
print(f"p2: " + u2_choice)

if u1_choice.lower() == 'rock' and u2_choice.lower() == 'scissors':
    print("User1 Wins!")
elif u1_choice.lower() == 'scissors' and u2_choice.lower() == 'rock':
    print("User2 Wins!")
elif u1_choice.lower() == 'paper' and u2_choice.lower() == 'scissors':
    print("User2 Wins!")
elif u1_choice.lower() == 'scissors' and u2_choice.lower() == 'paper':
    print("User1 Wins!")
elif u1_choice.lower() == 'rock' and u2_choice.lower() == 'paper':
    print("User2 Wins!")
elif u1_choice.lower() == 'paper' and u2_choice.lower() == 'rock':
    print("User1 Wins!")
