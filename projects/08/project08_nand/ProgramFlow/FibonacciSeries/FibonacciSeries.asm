//FibonacciSeries
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@13
M=D
@1
D=A
@THIS
A=A+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@13
M=D
@0
D=A
@THAT
A=M+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@13
M=D
@1
D=A
@THAT
A=M+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1
@SP
A=M-1
D=M
@13
M=D
@0
D=A
@ARG
A=M+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
(:MAIN_LOOP_START)
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
M=M-1
@:COMPUTE_ELEMENT
D;JNE
@:END_PROGRAM
0;JMP
(:COMPUTE_ELEMENT)
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M-1
D=M
@13
M=D
@2
D=A
@THAT
A=M+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@1
D=A
@THIS
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M+D
@SP
M=M-1
@SP
A=M-1
D=M
@13
M=D
@1
D=A
@THIS
A=A+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M-D
@SP
M=M-1
@SP
A=M-1
D=M
@13
M=D
@0
D=A
@ARG
A=M+D
D=A
@14
M=D
@13
D=M
@14
A=M
M=D
@SP
M=M-1
@:MAIN_LOOP_START
0;JMP
(:END_PROGRAM)
