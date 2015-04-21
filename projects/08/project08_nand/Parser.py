
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
      self.line = self.line.strip()
      if self.line == "" :
       self.advance()




  def commandType(self):
    # print(self.line)
    command = self.line.split()
    if len(command) is 1 and command[0] != "return":
      return "C_ARITHMETIC"
    if "push" in self.line:
      return "C_PUSH"
    if "pop" in self.line:
      return "C_POP"
    if "label" in self.line:
      return "C_LABEL"
    if "if" in self.line:
      return "C_IF"
    if "goto" in self.line:
      return "C_GOTO"
    if "function" in self.line:
      return "C_FUNCTION"
    if "return" in self.line:
      return "C_RETURN"
    if "call" in self.line:
      return "C_CALL"


  #return first argument in the current command
  def arg1(self):
    if self.commandType() != "C_RETURN":
      command = self.line.split()
      if self.commandType() == "C_ARITHMETIC":
        return command[0]
      else:
        return  command[1]


  #return second argument in the current command
  def arg2(self):
    type = self.commandType()
    if (type is "C_PUSH" or type is "C_POP") or (type is "C_FUNCTION" or type is "C_CALL"):
      command = self.line.split()
      return int(command[2])





