//BasicLoop
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
@LCL
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
(:LOOP_START)
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
@0
D=A
@LCL
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
@0
D=A
@LCL
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
@:LOOP_START
D;JNE
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1