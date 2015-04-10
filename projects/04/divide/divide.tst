// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/divide/Divide.tst

load Divide.asm,
output-file Divide.out,
compare-to Divide.cmp,
output-list RAM[13]%D2.7.2 RAM[14]%D2.7.2 RAM[15]%D2.7.2;

set RAM[13] 0,   // Set test arguments
set RAM[14] 1,
set RAM[15] -1;  // Test that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 1,   // Set test arguments
set RAM[14] 1,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 4,   // Set test arguments
set RAM[14] 4,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 3,   // Set test arguments
set RAM[14] 1,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 4,   // Set test arguments
set RAM[14] 2,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 5,   // Set test arguments
set RAM[14] 2,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;

set PC 0,
set RAM[13] 2,   // Set test arguments
set RAM[14] 4,
set RAM[15] -1;  // Ensure that program initialized product to 0
repeat 300 {
  ticktock;
}
output;
