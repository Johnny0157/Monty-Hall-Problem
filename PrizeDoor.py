from random import randint
i = 1
wins = 0
losses = 0
trials = 10000

while i <= trials:
    doors = [1,2,3]
    car = randint(1,3) # for car location

    guess = randint(1,3) # for players guess

    doors.remove(guess) # for possible door reveals
    if guess != car:
        doors.remove(car)
    reveal = randint(0,len(doors)-1)
    reveal = doors[reveal]
    doors.remove(reveal)

    if guess != car: # special case where guess != car
        doors.append(car)

    guess = doors[0] # reassign guess to element remaining in list

    if guess == car: # keep score
        wins += 1
    else:
        losses += 1

    i += 1

success_rt = round(float(((wins/(wins+losses))*100)),2) # find success rate

print(f"Had success {wins} times.")
print(f"Failed {losses} times.")
print(f"Finished {trials} trials with a success rate of {success_rt} %.")