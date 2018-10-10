#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the detector function below.
def detector(tweets):

    for tweet in tweets:

        cardinality = 0
        suffix = tweet[-3:]
        tweet = tweet[:-3]
        length = len(tweet)
        palindrome_count = 0

        if length > 240 or length < 1:
            print(suffix + " Ignore")
            return

        if tweet.isalnum() is False:
            print(suffix + " Ignore")
            return

        for i in range(3, length+1):
            for j in range(0, length-i+1):
                if palindrome_check(tweet[j:j+i]) is True:
                    palindrome_count += 1
                    cardinality += len(tweet[j:j+i])

        if palindrome_count >= 2:
            if cardinality in range(1, 11):
                print(suffix + " Possible")
            elif cardinality in range(11, 41):
                print(suffix + " Probable")
            elif cardinality in range(41, 151):
                print(suffix + " Escalate")
            else:
                print(suffix + " Ignore")

        else:
            print(suffix + " Ignore")
    return

def palindrome_check(substring):
    return (substring == substring[::-1])


if __name__ == '__main__':
    tweets_count = int(input().strip())

    tweets = []

    for _ in range(tweets_count):
        tweets_item = input()
        tweets.append(tweets_item)

    detector(tweets)
