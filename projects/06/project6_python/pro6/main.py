__author__ = 'mishelle123'
import  Parser as P
import Code as C
import  sys
import assembler as A
import os

if __name__ == '__main__':
  a = A.assembler()

  path = sys.argv[1]
  #open files in a folder
  if os.path.isdir(path):
    files_in_dir = os.listdir(path)
    for file_in_dir in files_in_dir:
      if file_in_dir.endswith("asm"):
        a.assemble(path+"/"+file_in_dir)
  #open one file
  elif path.endswith("asm"):
    a.assemble(path)


