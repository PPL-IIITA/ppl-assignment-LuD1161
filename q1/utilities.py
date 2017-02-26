from random import randint
import csv
import logging


def test_cases():
    Gifts = []
    Boys = []
    Girls = []

    gift_types = ['Essential', 'Luxury', 'Utility']
    boy_types = ['Miser', 'Generous', 'Geek']
    girl_types = ['Choosy', 'Normal', 'Desperate']

    for i in range(0, 100, 1):
        Boys += [('Boy' + str(i), randint(0, 100), randint(0, 100),
                  randint(0, 100), randint(0, 100), boy_types[randint(0, 2)])]

    for i in range(0, 40, 1):
        Girls += [('Girl' + str(i), randint(0, 100), randint(0, 100),
                   randint(0, 100), randint(0, 100), girl_types[randint(0, 2)])]

    make_csv('./boys_list.csv', Boys)
    make_csv('./girls_list.csv', Girls)


def make_csv(filename, listname):
    fp = open(filename, 'w')
    writer = csv.writer(fp, delimiter=',')

    for list_row in listname:
        writer.writerow(list_row)


def create_log(data):
    logging.basicConfig(filename='question_1_log.txt', filemode='w',
                        datefmt='%d/%m/%Y %I:%M:%S %p',
                        format='%(asctime)s %(name)-6s %(levelname) s: %(message)s',
                        level=logging.DEBUG)
    logging.info(data)
