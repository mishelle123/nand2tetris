// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, the
// program clears the screen, i.e. writes "white" in every pixel.

// Put your code here.

(LOOP)
    @SCREEN
    D=A
    @i
    M=D
    @KBD
    D=M
    @WHITE_SCREEN
    D;JEQ
    @BLACK_SCREEN
    0;JMP

(WHITE_SCREEN)
    @i
    D=M
    @KBD
    D=D-A
    @LOOP
    D;JGE
    @i
    A=M
    M=0
    @i
    M=M+1
    @WHITE_SCREEN
    0;JMP
    
(BLACK_SCREEN)
    @i
    D=M
    @KBD
    D=D-A
    @LOOP
    D;JGE
    @i
    A=M
    M=-1
    @i
    M=M+1
    @BLACK_SCREEN
    0;JMP
    

