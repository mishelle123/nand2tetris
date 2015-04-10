//The program input will be at R14(starting address),R15(length of array).
//The program should sort the array starting at the address in R14 with length specified in R15.
//The sort is in descending order - the largest number at the head of the array.
//The array is allocated in the heap address 2048-16383.

    
    @i
    M=-1
    
(OUTER_LOOP)
    @i
    M=M+1
    @R15
    D=M
    @i
    D=D-M
    @END
    D;JLT
    @j
    M=0
    @INNER_LOOP
    0;JMP


(INNER_LOOP)
    @j
    M=M+1
    @i
    D=M
    @R15
    D=M-D
    @j
    D=D-M
    @OUTER_LOOP
    D;JLE
    @R14
    D=M
    @j
    D=D+M
    @ptr1
    M=D
    @ptr2
    M=D-1
    A=M
    D=M
    @ptr1
    A=M
    D=D-M
    
    @SWAP
    D;JLT
    @INNER_LOOP
    0;JMP

(SWAP)
    @ptr1
    A=M
    D=M
    @temp
    M=D
    @ptr2
    A=M
    D=M
    @ptr1
    A=M
    M=D
    @temp
    D=M
    @ptr2
    A=M
    M=D
    @INNER_LOOP
    0;JMP
    
(END)
    @END
    0;JMP  
