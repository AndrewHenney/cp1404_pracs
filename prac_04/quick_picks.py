from random import randint
quick_pick_selection = []
number_of_picks = int(input('How many quick picks?'))
for i in range(number_of_picks):
    quick_pick_selection = []
    for pick_number in range(6):
        quick_pick_selection.append(randint(0, 45))


    print('{:2} {:2} {:2} {:2} {:2} {:2}'.format(quick_pick_selection[0],quick_pick_selection[1],quick_pick_selection[2],quick_pick_selection[3],quick_pick_selection[4],quick_pick_selection[5]))


