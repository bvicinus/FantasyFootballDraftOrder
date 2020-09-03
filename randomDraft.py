import random
import datetime


members = [
    'brandon',
    'matt',
    'seth',  # chi daddy chi sauce
    'bryce',
    'din',
    'rico',
    'nick',
    'peck',
    'nigel',
    'casey',
    'donny',
    'joey',
]
order = []

def main():
    print('main')
    for i in range(12):
        order.append(pick())
    print('the draft order is: %s' % order)

def pick():
    rng = random.Random()
    rng.seed(datetime.datetime.utcnow())
    choice = rng.choice(members)
    if choice not in order:
        return choice
    return pick()


if __name__ == '__main__':
    main()
