__author__ = 'mishelle123'
import  Parser as P

class SymbolTable:

  def __init__(self, file_name):
    self.memory = dict()
    self.initialize_predefined()
    self.parse_table(file_name)

  # add item to dictionary
  def addEntry(self, symbol, address):
    self.memory[symbol] = address

  # check if value is in the table
  def contains(self, symbol):
    return symbol in self.memory.keys()

  #return the address
  def addressof(self, symbol):
    return self.memory[symbol]


  def parse_table(self, file_name):
    parse = P.Parser(file_name)
    linecount = 0;

    while(parse.hasMoreCommand()):
      if parse.commandType() is "L_COMMAND":
        s = parse.symbol()
        self.addEntry(s, linecount)
        linecount -= 1

      linecount += 1
      parse.advance()

    parse = P.Parser(file_name)
    varCount = 16;
    while(parse.hasMoreCommand()):

      if parse.commandType() is "A_COMMAND":
        s = parse.symbol()
        if s.isdigit():
          self.addEntry(s, s)

        elif not self.contains(s) :
          self.addEntry(s, varCount)
          varCount += 1

      parse.advance()

  #initialize the constant addresses
  def initialize_predefined(self):
    self.addEntry("SP", 0)
    self.addEntry("LCL", 1)
    self.addEntry("ARG", 2)
    self.addEntry("THIS", 3)
    self.addEntry("THAT", 4)
    self.addEntry("SCREEN", 16384)
    self.addEntry("KBD", 24576)
    for i in range(16):
      self.addEntry("R"+str(i), i)