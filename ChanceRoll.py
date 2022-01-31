import argparse

from numpy import random

def main():
    descStr = "Chance and success rate calculator"
    parser = argparse.ArgumentParser(description=descStr)

    parser.add_argument('-c', '--chance', dest='chance', required=True)
    parser.add_argument('-r', '--rolls', dest='rolls', required=False)
    parser.add_argument('-o', '--odds', action='store_true', required=False, help="Calculate odds")
    parser.add_argument('-l', '--roll', action='store_true', required=False, help="Roll")

    args = parser.parse_args()

    chance = float(args.chance)
    rolls = 1
    if args.rolls:
        rolls = int(args.rolls)

    if rolls == 1:
        print("Rolling %d time with a chance of %.3f%% succeeds %.3f%% of the time" % (rolls, chance, chanceInXRolls(chance, rolls)))
    else:
        print("Rolling %d times with a chance of %.3f%% succeeds %.3f%% of the time" % (rolls, chance, chanceInXRolls(chance, rolls)))

    if args.odds:
        c = chanceInXRolls(chance, rolls)
        print("Odds of success are 1 in %.3f" % (oneInX(c)))

    if args.roll:
        if args.odds:
            print("Rolling %d times with %.3f%% chance succeeded %d times" % (rolls, chance, rollWithChance(chance)))

def rollWithChance(chance):
    """
    Rolls a % chance once and returns whether the roll succeeded or not
    :param chance: % chance of success
    :return: Whether roll succeeded or not
    """
    x = random.randint(oneInX(chance))
    return True if x==1 else False

def oneInX(chance : float):
    """
    Converts a percent chance into a "one out of X" chance
    :param chance: % chance of success
    :return: One in X chance
    """
    return 100/chance

def chanceInXRolls(chance : float, n : int):
    """
    Calculates chance based on number of rolls n with success rate percentChance
    :param chance: % chance of success
    :param n: number of rolls
    :return: % chance
    """
    x = chance/100.0
    x = 1 - x
    y = 1.0

    for i in range(n):
        y *= x

    return (1-y)*100

def rollXTimes(chance, n):
    """
    Rolls n times and returns total number of successes
    :param chance: % chance of success
    :param n: number of rolls
    :return: Number of succesful rolls
    """
    successCount = 0
    for i in range(n):
        if rollWithChance(chance):
            successCount += 1
    return successCount



if __name__ == "__main__":
    main()