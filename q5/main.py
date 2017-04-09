import csv

from q3.boys import Boys
from q3.girls import Girls
from q3.gifts import Gift
from q3.couple import Couple
from q3.ffunctions import calc_happiness

from q3.utils import create_log
from q3.utils import test_cases

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
    girl_list = sorted(girl_list, key=lambda x: x.attractiveness, reverse=True)

    i = 0
    j = 0
    while i < 20:
        girl = girl_list[i]
        for boy in boy_list:
            create_log(girl.name + ' is trying for ' + boy.name)
            if boy.status == girl.status and boy.status == "single" and boy.check_eligibility(girl.maintenance_budget,
                                                                                           girl.attractiveness) and girl.is_eligible(
                boy.budget):

                boy.gf = girl.name
                girl.bf = boy.name

                # Update relationship status
                boy.status = 'Committed'
                girl.status = 'Committed'
                text = girl.name + ' is in relationship with ' + boy.name
                print(text)

                # Create Log
                create_log(text)
                virtual_couple_list.append(Couple(boy, girl))
                break

        i += 1
        boy = boy_list[j]
        for girl in girl_list:
            create_log(boy.name + ' is trying for ' + girl.name)
            if boy.status == girl.status and boy.status == 'Single' and boy.check_eligibility(girl.maintenance_budget,
                                                                                           girl.attractiveness) and girl.is_eligible(
                boy.budget):

                boy.gf = girl.name
                girl.bf = boy.name

                # Update relationship status
                boy.status = 'Committed'
                girl.status = 'Committed'
                text = girl.name + ' is in relationship with ' + boy.name
                print(text)

                # Create Log
                create_log(text)
                virtual_couple_list.append(Couple(boy, girl))
                break
        j += 1

    print("Couples in relationship are : ")
    for couple in virtual_couple_list:
        print(couple.girl.name + " is in a relationship with " + couple.boy.name)

    calc_happiness(virtual_couple_list, gifts)

    virtual_couple_list = sorted(virtual_couple_list, key=lambda x: x.happiness, reverse=True)
    print("\n")
    print("10 most happy couple : ")
    for i in range(0, 10):
        print(virtual_couple_list[i].boy.name + " and " + virtual_couple_list[i].girl.name)
    print("\n")
    # print(virtual_couple_list[i].happiness)
    print("10 most compatible couple : ")

    virtual_couple_list = sorted(virtual_couple_list, key=lambda x: x.compatibility, reverse=True)
    for i in range(0, 10):
        print(virtual_couple_list[i].boy.name + " and " + virtual_couple_list[i].girl.name)


main()
