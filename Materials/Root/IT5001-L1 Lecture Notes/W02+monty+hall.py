import random

def Monty_Hall_Experiment(switch):
    num_trials = 100000
    strike = 0
    trial_no = 0
    print('Run the experiement {} times.'.format(num_trials))
    if switch:
        print('The player WILL change his mind')
    else:
        print('The player WONT change his mind')
    while trial_no < num_trials:
        trial_no += 1
        car_door = random.randint(0,2)
        originl_guess = random.randint(0,2)
        if switch:
            # You win if your original guess is NOT the car
            if originl_guess != car_door: 
                strike += 1
        else:
            # You win if your original guess IS the car
            if originl_guess == car_door:
                strike += 1

    print('The number of times you win a car is {}.'.format(strike))
    print('The chance of winning is about {}%.'.format(strike*100.0/num_trials))



Monty_Hall_Experiment(False)

print('Run another time')
print()

Monty_Hall_Experiment(True)
