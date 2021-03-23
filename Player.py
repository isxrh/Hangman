# -*- coding: utf-8 -*-

class Player(object):
    def __init__(self):
        self.lifeMax = 6
        self.currentLife = self.lifeMax
        self.userInput = []
        self.lostGame = False

    def loosingLife(self):
        self.currentLife -= 1
        self.Lost()

    def Lost(self):
        if self.currentLife == 0:
            self.lostGame = True

    def resetPlayer(self):
        self.currentLife = self.lifeMax
        self.userInput = []
        self.lostGame = False
