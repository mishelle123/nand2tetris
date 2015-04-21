__author__ = 'mishelle123'

import Parser as P
import CodeWriter as C
import os
import ntpath

class Translator:

  def Translate(self, path):



    #open files in a folder
    if os.path.isdir(path):
      fileName = ntpath.basename(path)
      new_file_name = path +"/"+fileName+ ".asm"
      self.codeWriter = C.CodeWriter(new_file_name)
      files_in_dir = os.listdir(path)
      for file_in_dir in files_in_dir:
        if file_in_dir.endswith("vm"):
          self.translateFile(path+"/"+file_in_dir)
    #open one file
    elif path.endswith("vm"):
      new_file_name = path[:-2] + "asm"
      self.codeWriter = C.CodeWriter(new_file_name)
      self.translateFile(path)

    self.codeWriter.close()

  def translateFile(self, path):
    parser = P.Parser(path)
    fileName = ntpath.basename(path)[:-3]
    self.codeWriter.setFileName(fileName)
    while parser.hasMoreCommand():
      codeType = parser.commandType()
      if codeType == "C_ARITHMETIC":
        self.codeWriter.writeArithmetic(parser.arg1())
      if codeType == "C_PUSH" or codeType == "C_POP":
        self.codeWriter.writePushPop(codeType,parser.arg1(),parser.arg2())

      parser.advance()