'''
Created on Oct 26, 2020

@author: dragoscorleanca
'''
from BST import *
import re
class Scanner:
    def __init__(self, fileName):
        self.tokens = []
        self.pif = []
        self.st = BST()
        self.fileName = fileName
        self.pifout = open("pif.txt", 'w')
        self.stout = open("st.txt", 'w')
    def readTokens(self):
        f = open("tokens")
        f.readline()
        f.readline()
        for line in f:
            line = line.split()
            self.tokens.append(line[0])
    def isIdentifier(self, token):
        x = re.findall("^[a-z]+[0-9]*$", token)
        if len(x):
            return True
        return False
    def isReservedWord(self, token):
        try:
            idx = self.tokens.index(token)
        except ValueError:
            return False
        if idx >= 22:
            return True
        return False
    def isOperator(self, token):
        try:
            idx = self.tokens.index(token)
        except ValueError:
            return False
        idx = self.tokens.index(token)
        if idx >= 0 and idx <= 12:
            return True
        return False
    
    def isSeparator(self, token):
        if token == ' ' or token == '\n':
            return True
        try:
            idx = self.tokens.index(token)
        except ValueError:
            return False
        idx = self.tokens.index(token)
        if idx >= 13 and idx <= 21:
            return True
        return False
    def isConstant(self, token):
        x = re.findall("^[\+-]?[0-9]*$", token)
        if len(x):
            return True
        return False
    def genPif(self, token, val):
        self.pifout.write(token + " " + str(val) + '\n')
    def run(self):
        f = open(self.fileName)
        self.readTokens()
        file = f.read()
        lastSep = -1
#         for i in range(len(file)):
#             if not file[i].isalpha() and not file[i].isdigit():
#                 token = file[lastSep + 1 : i]
#                 lastSep = i
        file.replace('\n', ' ')
        file = file.split()
        
        for token in file:
            print(token)
            if token == '#':
                token = '#'
            if self.isReservedWord(token) or self.isOperator(token) or self.isSeparator(token):
                self.genPif(token, 0)
            elif self.isConstant(token) or self.isIdentifier(token):
                self.st.add(token)
                idx = self.st.contains(token)
                self.genPif(token, idx)
            else:
                print('Lexical error')
        
        self.stout.write(str(self.st))
                
                
        #print(file)
            