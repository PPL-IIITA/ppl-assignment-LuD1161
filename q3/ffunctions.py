import math
from random import randint

from utils import create_log

text = ''


def typeOfBoy(type, gifts, c):
    b1 = 0
    b2 = 0
    for g in gifts:
        if (c.boy.budget >= 0) and (
                    (g.cost - c.girl.maintenance_budget <= 100) or (g.cost == c.girl.maintenance_budget)) and (
                        c.boy.budget - g.cost > 0):
            if g.type_of_gift == 'Luxury':
                b2 += 2 * g.cost
            else:
                b2 = b2 + g.cost
            b1 = b1 + g.cost
            c.gifts += [g]
            c.boy.budget = c.boy.budget - g.cost
            create_log(c.boy.name + '  gave ' + c.girl.name + ' a  Gift:| ' + g.name + '| of price =Rs. ' + str(
                g.cost) + '\-.')
    if type == 'geek':
        for i in gifts:
            if (i not in c.gifts) and (i.type_of_gift == 'Luxury') and (i.cost <= c.boy.budget):
                b2 += 2 * i.cost
                b1 = b1 + i.cost
                c.gifts += [i]
                c.boy.budget = c.boy.budget - i.cost
                create_log(c.boy.name + '  gave  ' + c.girl.name + ' a  Gift:| ' + i.name + '| of price =Rs. ' + str(
                    i.cost) + '\-.')
                break
    if c.girl.type_of_gf == 'Choosy' and b2 > 0:
        c.girl.happiness = math.log10(b2)
    elif c.girl.type_of_gf == 'Normal':
        c.girl.happiness = b1
    else:
        c.girl.happiness = math.exp(b1)

    if type == 'Geek':
        c.boy.happiness = c.girl.intelligence
    elif type == 'Miser':
        c.boy.happiness = c.boy.budget
    elif type == 'Generous':
        c.boy.happiness = c.girl.happiness
    c.set_happiness()
    c.set_compatibility()


def calc_happiness(H, gifts):
    create_log('\n\nDetails of Gifts:\n')
    for i in H:
        typeOfBoy(i.boy.type_of, gifts, i)

    return gifts_details(H)


def happy_couple(H, k):
    global text
    A = sorted(H, key=lambda item: item.happiness, reverse=True)
    B = sorted(H, key=lambda item: item.compatibility_status, reverse=True)
    text += '\n\n' + str(k) + ' most Compatible couples are as follows:'
    print ('\n\n' + str(k) + ' most Compatible couples are as follows:')
    for i in range(k):
        text += B[i].boy.name + ' & ' + B[i].girl.name
        print B[i].boy.name + ' & ' + B[i].girl.name
    text += '***Still Single***\n'
    print '***Still Single***\n'
    text += '\n\n' + str(k) + ' most happy couples are as follows:'
    print ('\n\n' + str(k) + ' most happy couples are as follows:')
    for i in range(k):
        text += A[i].boy.name + ' & ' + A[i].girl.name
        print (A[i].boy.name + ' & ' + A[i].girl.name)
    text += '***Still Single***\n'
    print('***Still Single***\n')
    return text


def gifts_details(H):
    global text
    for couple in H:
        text += 'Gifts given from : ' + couple.boy.name + ' to : ' + couple.girl.name + ':\n'
        print ('Gifts given from : ' + couple.boy.name + ' to : ' + couple.girl.name + ':\n')
        for gift in couple.gifts:
            text += gift.name + '\tType: ' + gift.type_of_gift
            print (gift.name + '\tType: ' + gift.type_of_gift)
        text += '\n'
        print ('\n')
        k = randint(1, len(H))
    return happy_couple(H, k)
