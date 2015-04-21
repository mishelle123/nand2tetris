
class CodeWriter:

  def __init__(self, output_file):
    self.output_file = open(output_file, 'w+')
    self.fileName = ''
    self.functionName = ''
    self.call_id = 0
    self.label_id = 0
    self.binary_op = ["add", "sub", "and", "or"]
    self.unary_op = ["not", "neg"]
    self.bool_op = ["eq", "gt", "lt"]

  def setFileName(self, file_name):
    self.output_file.write("//"+file_name+"\n")
    self.fileName = file_name

  def writeArithmetic(self, command):
    if command in self.binary_op:
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("A=A-1\n")

      if command == "add":
        self.output_file.write("M=M+D\n")
      if command == "sub":
        self.output_file.write("M=M-D\n")
      if command == "and":
        self.output_file.write("M=M&D\n")
      if command == "or":
        self.output_file.write("M=M|D\n")
      self.output_file.write("@SP\n")
      self.output_file.write("M=M-1\n")

    if command in self.unary_op:
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      if command == "not":
        self.output_file.write("M=!M\n")
      if command == "neg":
        self.output_file.write("M=-M\n")
      # self.output_file.write("@SP\n")
      # self.output_file.write("M=M-1\n")

    if command in self.bool_op:
      true_label = "true"+str(self.label_id)
      false_label = "false"+str(self.label_id)
      end_label = "end"+str(self.label_id)
      cmp_gt_label = "cmp_gt"+str(self.label_id)
      cmp_lt_label = "cmp_lt"+str(self.label_id)
      gt_lt_label = "gt_lt"+str(self.label_id)
      lt_gt_label = "lt_gt"+str(self.label_id)
      reg_cmp_label = "reg_cmp"+str(self.label_id)
      cmp_label = "cmp"+str(self.label_id)


      #update the label id
      self.label_id = self.label_id + 1
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("D=M\n")
      #checks if the first number is greater than 0
      self.output_file.write("@"+cmp_gt_label+ "\n")
      self.output_file.write("D;JGT\n")
      #checks if the first number is lower than 0
      self.output_file.write("@"+cmp_lt_label+ "\n")
      self.output_file.write("0;JMP\n")

      #the first number is greater than 0
      self.output_file.write("(" + cmp_gt_label + ")"+"\n")
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("A=A-1\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@"+gt_lt_label+ "\n")
      self.output_file.write("D;JLT\n")
      self.output_file.write("@"+reg_cmp_label+ "\n")
      self.output_file.write("0;JMP\n")

      #the second number is lower than 0
      self.output_file.write("(" + gt_lt_label + ")"+"\n")
      self.output_file.write("D=-1\n")
      self.output_file.write("@"+cmp_label+ "\n")
      self.output_file.write("0;JMP\n")

      #the first number is lower than 0
      self.output_file.write("(" + cmp_lt_label + ")"+"\n")
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("A=A-1\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@"+lt_gt_label+ "\n")
      self.output_file.write("D;JGT\n")
      self.output_file.write("@"+reg_cmp_label+ "\n")
      self.output_file.write("0;JMP\n")

      #the second number is greater than 0
      self.output_file.write("(" + lt_gt_label + ")"+"\n")
      self.output_file.write("D=1\n")
      self.output_file.write("@"+cmp_label+ "\n")
      self.output_file.write("0;JMP\n")

      self.output_file.write("(" + reg_cmp_label + ")"+"\n")

      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("A=A-1\n")
      self.output_file.write("D=M-D\n")

      self.output_file.write("(" + cmp_label + ")"+"\n")

      self.output_file.write("@"+true_label+ "\n")
      if command == "eq":
        self.output_file.write("D;JEQ\n")
      if command == "gt":
        self.output_file.write("D;JGT\n")
      if command == "lt":
        self.output_file.write("D;JLT\n")
      self.output_file.write("@"+false_label+ "\n")
      self.output_file.write("0;JMP\n")
      self.output_file.write("(" + true_label + ")"+"\n")
      self.output_file.write("D=-1\n")
      self.output_file.write("@"+end_label+ "\n")
      self.output_file.write("0;JMP\n")
      self.output_file.write("(" + false_label + ")"+"\n")
      self.output_file.write("D=0\n")
      self.output_file.write("@"+end_label+ "\n")
      self.output_file.write("0;JMP\n")
      self.output_file.write("(" + end_label + ")"+"\n")
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("A=A-1\n")
      self.output_file.write("M=D\n")
      self.output_file.write("@SP\n")
      self.output_file.write("M=M-1\n")



  def writePushPop(self, command, segment, index):
    if command == "C_PUSH":
      #constant
      if segment == "constant":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")

      if segment == "local":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("A=M+D\n")
        self.output_file.write("D=M\n")


      if segment == "argument":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("A=M+D\n")
        self.output_file.write("D=M\n")

      if segment == "this":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("A=M+D\n")
        self.output_file.write("D=M\n")

      if segment == "that":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("A=M+D\n")
        self.output_file.write("D=M\n")

      if segment == "pointer":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("A=A+D\n")
        self.output_file.write("D=M\n")

      if segment == "temp":

        self.output_file.write("@"+str(5+index)+"\n")
        self.output_file.write("D=M\n")

      if segment == "static":
        self.output_file.write("@"+self.fileName+"."+str(index)+"\n")
        self.output_file.write("D=M\n")

      self.output_file.write("@SP\n")
      self.output_file.write("A=M\n")
      self.output_file.write("M=D\n")
      self.output_file.write("@SP\n")
      self.output_file.write("M=M+1\n")
    #pop command
    else:
      self.output_file.write("@SP\n")
      self.output_file.write("A=M-1\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@13\n")
      self.output_file.write("M=D\n")

      if segment == "local":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@LCL\n")
        self.output_file.write("A=M+D\n")

      if segment == "argument":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@ARG\n")
        self.output_file.write("A=M+D\n")

      if segment == "this":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("A=M+D\n")

      if segment == "that":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THAT\n")
        self.output_file.write("A=M+D\n")

      if segment == "pointer":
        self.output_file.write("@"+str(index)+"\n")
        self.output_file.write("D=A\n")
        self.output_file.write("@THIS\n")
        self.output_file.write("A=A+D\n")


      if segment == "temp":
        self.output_file.write("@"+str(5+index)+"\n")

      if segment == "static":
        self.output_file.write("@"+self.fileName+"."+str(index)+"\n")


      self.output_file.write("D=A\n")
      self.output_file.write("@14\n")
      self.output_file.write("M=D\n")

      self.output_file.write("@13\n")
      self.output_file.write("D=M\n")


      self.output_file.write("@14\n")
      self.output_file.write("A=M\n")
      self.output_file.write("M=D\n")

      self.output_file.write("@SP\n")
      self.output_file.write("M=M-1\n")

  def writeInit(self):
    self.output_file.write("@256\n")
    self.output_file.write("D=A\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=D\n")
    self.writeCall("Sys.init", 0)


  def writeLabel(self, label):
    self.output_file.write("(" + self.functionName +":"+ label + ")"+"\n")

  def writeGoto(self, label):
    self.output_file.write("@" + self.functionName + ":" + label + "\n")
    self.output_file.write("0;JMP\n")

  def writeIf(self, label):
    self.output_file.write("@SP\n")
    self.output_file.write("A=M-1\n")
    self.output_file.write("D=M\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=M-1\n")
    self.output_file.write("@" + self.functionName + ":" + label + "\n")
    self.output_file.write("D;JNE\n")

  #push address to stack
  def pushStackAddress(self, address):
    self.output_file.write("@" + address +"\n")
    self.output_file.write("D=A\n")
    self.output_file.write("@SP\n")
    self.output_file.write("A=M\n")
    self.output_file.write("M=D\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=M+1\n")

  #push data to stack
  def pushStackData(self):
    self.output_file.write("@SP\n")
    self.output_file.write("A=M\n")
    self.output_file.write("M=D\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=M+1\n")

  def writeCall(self, functionName, numArgs):
    return_address = self.functionName +"_"+ str(self.call_id)
    self.call_id += 1
    self.pushStackAddress(return_address)

    self.output_file.write("@LCL\n")
    self.output_file.write("D=M\n")
    self.pushStackData()
    self.output_file.write("@ARG\n")
    self.output_file.write("D=M\n")
    self.pushStackData()
    self.output_file.write("@THIS\n")
    self.output_file.write("D=M\n")
    self.pushStackData()
    self.output_file.write("@THAT\n")
    self.output_file.write("D=M\n")
    self.pushStackData()
    # self.pushStackAddress("ARG")
    # self.pushStackAddress("THIS")
    # self.pushStackAddress("THAT")
    self.output_file.write("@5\n")
    self.output_file.write("D=A\n")
    self.output_file.write("@" + str(numArgs) + "\n")
    self.output_file.write("D=D+A\n")
    self.output_file.write("@SP\n")
    self.output_file.write("D=M-D\n")
    self.output_file.write("@ARG\n")
    self.output_file.write("M=D\n")
    self.output_file.write("@SP\n")
    self.output_file.write("D=M\n")
    self.output_file.write("@LCL\n")
    self.output_file.write("M=D\n")
    self.output_file.write("@" + functionName+ "\n")
    self.output_file.write("0;JMP\n")
    self.output_file.write("(" + return_address + ")\n")

  def writeReturn(self):

    self.output_file.write("@LCL\n")
    self.output_file.write("D=M\n")
    self.output_file.write("@13\n")
    self.output_file.write("M=D\n")
    self.output_file.write("@5\n")
    self.output_file.write("D=D-A\n")

    self.output_file.write("A=D\n")
    self.output_file.write("D=M\n")
    self.output_file.write("@14\n")
    self.output_file.write("M=D\n")
    #pop
    self.output_file.write("@SP\n")
    self.output_file.write("A=M-1\n")
    self.output_file.write("D=M\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=M-1\n")
    #put in arg
    self.output_file.write("@ARG\n")
    self.output_file.write("A=M\n")
    self.output_file.write("M=D\n")

    self.output_file.write("D=A\n")
    self.output_file.write("@SP\n")
    self.output_file.write("M=D+1\n")

    for i in range(1,5):
      self.output_file.write("@"+str(i)+"\n")
      self.output_file.write("D=A\n")
      self.output_file.write("@13\n")
      self.output_file.write("D=M-D\n")
      self.output_file.write("A=D\n")
      self.output_file.write("D=M\n")
      self.output_file.write("@"+str(5-i)+"\n")
      self.output_file.write("M=D\n")

    self.output_file.write("@14\n")
    self.output_file.write("A=M\n")
    self.output_file.write("0;JMP\n")

  def writeFunction(self, functionName, numLocals):
    self.functionName = functionName
    self.output_file.write("(" + functionName + ")\n")
    #put 0's in D
    self.output_file.write("@0\n")
    self.output_file.write("D=A\n")
    for i in range(numLocals):
      self.pushStackData()



  def close(self):
    self.output_file.close()


