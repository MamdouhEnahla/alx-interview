#!/usr/bin/python3
""" Prime Game module"""


def generatePrimeNumbers(limit):
    """Create a list of primes until the limit"""
    primeNums = []
    sieveList = [True] * (limit + 1)
    for potentialPrime in range(2, limit + 1):
        if sieveList[potentialPrime]:
            primeNums.append(potentialPrime)
            for multiple in range(potentialPrime, limit + 1, potentialPrime):
                sieveList[multiple] = False
    return primeNums


def isWinner(nRounds, roundVal):
    """
    Get the winner of the game
    """
    if not nRounds or not roundVal:
        return None
    mariaScore = benScore = 0
    for i in range(nRounds):
        primes = generatePrimeNumbers(roundVal[i])
        if len(primes) % 2 == 0:
            benScore += 1
        else:
            mariaScore += 1
    if mariaScore > benScore:
        return "Maria"
    elif benScore > mariaScore:
        return "Ben"
    return None
