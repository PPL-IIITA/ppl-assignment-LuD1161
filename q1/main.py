import csv

from boys import Boys
from girls import Girls

from utilities import create_log
from utilities import test_cases

# Generate Test Cases
test_cases()

boys = open('./boys_list.csv')
getBoy = csv.reader(boys, delimiter=',')

girls = open('./girls_list.csv')
getGirls = csv.reader(girls, delimiter=',')

boy_list = []
girl_list = []
gift_list = []

for i in getBoy:
    boy_list += [Boys(i[0], int(i[1]), int(i[2]), int(i[3]), int(i[4]), i[5])]

for i in getGirls:
    girl_list += [Girls(i[0], int(i[1]), int(i[2]), int(i[3]), i[4])]


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

            text = girl.name + ' is in a relationship with ' + boy.name
            print text
            # Create Log
            create_log(text)
            break
