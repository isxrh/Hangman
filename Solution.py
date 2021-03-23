# -*- coding: utf-8 -*-

import random


class Solution(object):
    def __init__(self, theme):
        # print("[Test] Solution class called")
        print(theme)
        self.ListOfWords = []
        self.loadWordList(theme)
        self.x = 0
        self.hiddenSolution = []
        self.LettersIn = []
        self.RandomiseSolution()
        self.FirstDisplay()

    def loadWordList(self, theme):
        fpath = './words/' + theme + '.txt'
        print(fpath)
        with open(fpath, 'r', encoding='UTF-8') as f:
            for line in f.readlines():
                line = line.strip('\n').upper()
                # print(line)
                self.ListOfWords.append(line)
        print(self.ListOfWords)

    def resetSolution(self):
        self.x = 0
        self.hiddenSolution = []
        self.LettersIn = []
        self.RandomiseSolution()
        self.FirstDisplay()

    def RandomiseSolution(self):
        # print("[Test] Randomise Solution here")
        self.x = random.randint(0, len(self.ListOfWords) - 1)
        # print(self.x)
        self.Solution = self.ListOfWords[self.x]
        print(self.Solution)

    def FirstDisplay(self):
        self.hiddenSolution = "-" * len(self.Solution)
        # print(len(self.Solution))
        # print(self.hiddenSolution)

    def CheckIfInWord(self, UserInput):
        # print("[Test]")
        self.LettersIn = [i for i, e in enumerate(self.Solution) if e == UserInput]
        for i in self.LettersIn:
            self.hiddenSolution = self.hiddenSolution[:i] + UserInput + self.hiddenSolution[i + 1:]
        # print(self.LettersIn)
        # print(self.hiddenSolution)


