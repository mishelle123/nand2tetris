__author__ = 'mishelle123'

import  Parser as P
import Code as C
import SymbolTable as S
class assembler:

  def assemble(self, file_name):
    self.parser = P.Parser(file_name)
    self.code = C.Code()
    self.symbolTable = S.SymbolTable(file_name)
    #open new file
    new_file_name = file_name[:-3] + "hack"
    new_file = open(new_file_name, "w")
    binary_line = ""
    while(self.parser.hasMoreCommand()):
      binary_line = ""
      if self.parser.commandType() is "A_COMMAND":
        binary_line = self.a_line()
        new_file.write(binary_line + "\n")

      if self.parser.commandType() is "C_COMMAND":
        binary_line = self.c_line()
        new_file.write(binary_line + "\n")

      # if self.parser.commandType() is "L_COMMAND":
      #
      #   continue
      self.parser.advance()
    new_file.close()

  def a_line(self):
    symbol = self.parser.symbol()
    binar = str(bin(int(self.symbolTable.addressof(symbol)))).split("b")[1]
    bin_len = 16 - len(binar)
    line = ""
    for i in range (bin_len):
      line += "0"

    line += binar

    return line


  def c_line(self):
    shift = self.code.shift(self.parser.comp())
    if shift:
      line = shift
      line += "0000"
    else:
      line = "111"
      line += self.code.comp(self.parser.comp())
    line += self.code.dest(self.parser.dest())
    line += self.code.jump(self.parser.jump())

    return line

  # def l_line(self):
  #   return 0