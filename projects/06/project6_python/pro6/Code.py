__author__ = 'mishelle123'


class Code:


  def dest(self, mnemo):
    dest = [0, 0, 0]
    if mnemo != None:
      if "M" in mnemo:
        dest[2] = 1
      if "D" in mnemo:
        dest[1] = 1
      if "A" in mnemo:
        dest[0] = 1
    return str(dest[0]) + str(dest[1]) + str(dest[2])

  def comp(self, mnemo):
    comp = [0, 0, 0, 0, 0, 0, 0]
    if mnemo != None:

      if "D" in mnemo:
        comp = [0, 0, 0, 1, 1, 0, 0]
        if "+" in mnemo:
          if "1" in mnemo:
            comp = [0, 0, 1, 1, 1, 1, 1]
          else:
            comp = [0, 0, 0, 0, 0, 1, 0]

        elif "-" in mnemo:
          comp = [0, 0, 0, 1, 1, 1, 1]
          if mnemo[0] == "D":
            comp = [0, 0, 1, 0, 0, 1, 1]
            if "1" in mnemo:
              comp = [0, 0, 0, 1, 1, 1, 0]
          if "D" != mnemo[0] and "-" != mnemo[0] :
            comp = [0, 0, 0, 0, 1, 1, 1]

        elif "&" in mnemo:
          comp = [0, 0, 0, 0, 0, 0, 0]

        elif "|" in mnemo:
          comp = [0, 0, 1, 0, 1, 0, 1]

        elif "!" in mnemo:
          comp = [0, 0, 0, 1, 1, 0, 1]

      else:
        comp = [0, 1, 1, 0, 0, 0, 0]
        if "+" in mnemo:
          if "1" in mnemo:
            comp = [0, 1, 1, 0, 1, 1, 1]
          else:
            comp = [0, 0, 0, 0, 0, 1, 0]

        elif "-" in mnemo:
          comp = [0, 1, 1, 0, 0, 1, 1]
          if "1" in mnemo:
            comp = [0, 1, 1, 0, 0, 1, 0]
        elif "!" in mnemo:
          comp = [0, 1, 1, 0, 0, 0, 1]

      if mnemo == "0":
        comp = [0, 1, 0, 1, 0, 1, 0]
      if mnemo == "1":
        comp = [0, 1, 1, 1, 1, 1, 1]
      if mnemo == "-1":
        comp = [0, 1, 1, 1, 0, 1, 0]
      if "M" in mnemo:
        comp[0] = 1
    return str(comp[0]) + str(comp[1]) + str(comp[2]) + str(comp[3]) + str(comp[4]) + str(comp[5]) + str(comp[6])

  def jump(self, mnemo):
    jump = [0, 0, 0]
    if mnemo != None:
      if "E" in mnemo:
        if "N" in mnemo:
          jump = [1, 0, 1]
        else:
          jump[1] = 1
      if "G" in mnemo:
        jump[2] = 1
      if "L" in mnemo:
        jump[0] = 1
      if "JMP" == mnemo:
        jump = [1, 1, 1]

    return str(jump[0]) + str(jump[1]) + str(jump[2])

  def shift(self, mnemo):
    shift = [1, 0, 1, 0, 0, 0]
    if "<<" in mnemo or ">>" in mnemo:
      if "<<" in mnemo:
        shift[4] = 1
      if "D" in mnemo:
        shift[5] = 1
      if "M" in mnemo:
        shift[3] = 1
      return str(shift[0]) + str(shift[1]) + str(shift[2]) + str(shift[3]) + str(shift[4]) + str(shift[5])
    else:
      return False