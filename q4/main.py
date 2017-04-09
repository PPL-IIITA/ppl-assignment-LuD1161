import csv

from boys import Boys
from girls import Girls
from gifts import Gift
from couple import Couple
from ffunctions import calc_happiness

from utils import create_log
from utils import test_cases

# Generate Test Cases
test_cases()


def main():
    boys = open('./boys_list.csv')
    getBoy = csv.reader(boys, delimiter=',')

    girls = open('./girls_list.csv')
    getGirls = csv.reader(girls, delimiter=',')

    boy_list = []
    girl_list = []
    couple_list = []
    virtual_couple_list = []

    after_breakup_girl_list = []

    for i in getBoy:
        boy_list += [Boys(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]

    for i in getGirls:
        girl_list += [Girls(i[0], int(i[1]), int(i[2]), int(i[3]), i[4])]

    # Create gift list to be sent to happiness calculator
    with open('./gift_list.csv', 'r') as gift_file:
        gift_list = csv.reader(gift_file, delimiter=',')
        for row in gift_list:
            gifts = [Gift(row[0], int(row[1]), int(row[2]), row[3])]
        gift_file.close()

    gifts = sorted(gifts, key=lambda item: item.cost)

    for girl in girl_list:
        for boy in boy_list:
            # Create Log
            create_log(boy.name + ' is trying for ' + girl.name)
            if boy.status == 'Single' and girl.status == 'Single' and \
                    boy.check_eligibility(girl.maintenance_budget, girl.attractiveness):
                boy.gf = girl.name
                girl.bf = boy.name

                # Update relationship status
                boy.status = 'Committed'
                girl.status = 'Committed'

                text = girl.name + ' is in relationship with ' + boy.name
                print(text)
                # Create Log
                create_log(text)
                couple_list += [(girl, boy)]
                break

    for i in couple_list:
        # Create couples first to be sent to happiness calculator
        virtual_couple_list += [Couple(i[0], i[1])]

    print("Couples in relationship are : ")
    for couple in virtual_couple_list:
        print(couple.girl.name + " is in a relationship with " + couple.boy.name)

    calc_happiness(virtual_couple_list, gifts)

    for girl in girl_list:
        for i in range(0, 10):
            if girl == virtual_couple_list[i].girl:
                # Add the boy to girl's blacklist , thus removing any chance
                # of their matching up again
                girl.blacklist = virtual_couple_list[i].boy.name

                # Create the new list of girls after breakup
                after_breakup_girl_list.append(girl)

                # Remove them from couple list
                virtual_couple_list.remove(virtual_couple_list[i])

    # Now rerun the matchup loop after breakup
    for girl in after_breakup_girl_list:
        for boy in boy_list:
            # Create Log
            create_log(boy.name + ' is trying for ' + girl.name)
            if boy.status == 'Single' and girl.status == 'Single' and \
                    boy.check_eligibility(girl.maintenance_budget, girl.attractiveness):
                boy.gf = girl.name
                girl.bf = boy.name

                # Update relationship status
                boy.status = 'Committed'
                girl.status = 'Committed'

                text = girl.name + ' is in relationship with ' + boy.name
                print(text)
                # Create Log
                create_log(text)
                virtual_couple_list.append(Couple(girl, boy))
                break

main()
