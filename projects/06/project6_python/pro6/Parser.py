__author__ = 'mishelle123'

import sys
import  os

class Parser:

  def __init__(self, file):
    self.file = open(file, "r")
    self.num_lines = sum(1 for line in self.file)
    self.file.seek(0)
    self.line = ""
    self.lineCount = 0
    self.advance()

  def hasMoreCommand(self):
    return self.lineCount <= self.num_lines

  def advance(self):
    if self.hasMoreCommand():
      self.line = self.file.readline()
      self.line = self.line.split("//")[0]
      self.lineCount += 1
      self.line = "".join(self.line.split())
      if self.line == "" :
       self.advance()




  def commandType(self):
    if self.line.startswith("@"):
      return "A_COMMAND"
    if "=" in self.line or ";" in self.line:
      return "C_COMMAND"
    if "(" in self.line and ")" in self.line:
      return "L_COMMAND"


  # return symbol or decimal of the command
  def symbol(self):
    if self.line.startswith("@"):
      return self.line[1:]
    if "(" in self.line and ")" in self.line:
      return self.line[1:-1]


  def dest(self):
    if "=" in self.line:
      dest = self.line.split("=")[0]
      return dest
    else:
      return None

  def comp(self):
    if "=" in self.line:
      return (self.line.split("=")[1]).split(";")[0]
    if ";" in self.line:
      return self.line.split(";")[0]

  def jump(self):
    if ";" in self.line:
      return self.line.split(";")[1]



