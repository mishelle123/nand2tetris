//StackTest
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt0
D;JGT
@cmp_lt0
0;JMP
(cmp_gt0)
@SP
A=M-1
A=A-1
D=M
@gt_lt0
D;JLT
@reg_cmp0
0;JMP
(gt_lt0)
D=-1
@cmp0
0;JMP
(cmp_lt0)
@SP
A=M-1
A=A-1
D=M
@lt_gt0
D;JGT
@reg_cmp0
0;JMP
(lt_gt0)
D=1
@cmp0
0;JMP
(reg_cmp0)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp0)
@true0
D;JEQ
@false0
0;JMP
(true0)
D=-1
@end0
0;JMP
(false0)
D=0
@end0
0;JMP
(end0)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt1
D;JGT
@cmp_lt1
0;JMP
(cmp_gt1)
@SP
A=M-1
A=A-1
D=M
@gt_lt1
D;JLT
@reg_cmp1
0;JMP
(gt_lt1)
D=-1
@cmp1
0;JMP
(cmp_lt1)
@SP
A=M-1
A=A-1
D=M
@lt_gt1
D;JGT
@reg_cmp1
0;JMP
(lt_gt1)
D=1
@cmp1
0;JMP
(reg_cmp1)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp1)
@true1
D;JEQ
@false1
0;JMP
(true1)
D=-1
@end1
0;JMP
(false1)
D=0
@end1
0;JMP
(end1)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt2
D;JGT
@cmp_lt2
0;JMP
(cmp_gt2)
@SP
A=M-1
A=A-1
D=M
@gt_lt2
D;JLT
@reg_cmp2
0;JMP
(gt_lt2)
D=-1
@cmp2
0;JMP
(cmp_lt2)
@SP
A=M-1
A=A-1
D=M
@lt_gt2
D;JGT
@reg_cmp2
0;JMP
(lt_gt2)
D=1
@cmp2
0;JMP
(reg_cmp2)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp2)
@true2
D;JEQ
@false2
0;JMP
(true2)
D=-1
@end2
0;JMP
(false2)
D=0
@end2
0;JMP
(end2)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt3
D;JGT
@cmp_lt3
0;JMP
(cmp_gt3)
@SP
A=M-1
A=A-1
D=M
@gt_lt3
D;JLT
@reg_cmp3
0;JMP
(gt_lt3)
D=-1
@cmp3
0;JMP
(cmp_lt3)
@SP
A=M-1
A=A-1
D=M
@lt_gt3
D;JGT
@reg_cmp3
0;JMP
(lt_gt3)
D=1
@cmp3
0;JMP
(reg_cmp3)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp3)
@true3
D;JLT
@false3
0;JMP
(true3)
D=-1
@end3
0;JMP
(false3)
D=0
@end3
0;JMP
(end3)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt4
D;JGT
@cmp_lt4
0;JMP
(cmp_gt4)
@SP
A=M-1
A=A-1
D=M
@gt_lt4
D;JLT
@reg_cmp4
0;JMP
(gt_lt4)
D=-1
@cmp4
0;JMP
(cmp_lt4)
@SP
A=M-1
A=A-1
D=M
@lt_gt4
D;JGT
@reg_cmp4
0;JMP
(lt_gt4)
D=1
@cmp4
0;JMP
(reg_cmp4)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp4)
@true4
D;JLT
@false4
0;JMP
(true4)
D=-1
@end4
0;JMP
(false4)
D=0
@end4
0;JMP
(end4)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt5
D;JGT
@cmp_lt5
0;JMP
(cmp_gt5)
@SP
A=M-1
A=A-1
D=M
@gt_lt5
D;JLT
@reg_cmp5
0;JMP
(gt_lt5)
D=-1
@cmp5
0;JMP
(cmp_lt5)
@SP
A=M-1
A=A-1
D=M
@lt_gt5
D;JGT
@reg_cmp5
0;JMP
(lt_gt5)
D=1
@cmp5
0;JMP
(reg_cmp5)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp5)
@true5
D;JLT
@false5
0;JMP
(true5)
D=-1
@end5
0;JMP
(false5)
D=0
@end5
0;JMP
(end5)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt6
D;JGT
@cmp_lt6
0;JMP
(cmp_gt6)
@SP
A=M-1
A=A-1
D=M
@gt_lt6
D;JLT
@reg_cmp6
0;JMP
(gt_lt6)
D=-1
@cmp6
0;JMP
(cmp_lt6)
@SP
A=M-1
A=A-1
D=M
@lt_gt6
D;JGT
@reg_cmp6
0;JMP
(lt_gt6)
D=1
@cmp6
0;JMP
(reg_cmp6)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp6)
@true6
D;JGT
@false6
0;JMP
(true6)
D=-1
@end6
0;JMP
(false6)
D=0
@end6
0;JMP
(end6)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt7
D;JGT
@cmp_lt7
0;JMP
(cmp_gt7)
@SP
A=M-1
A=A-1
D=M
@gt_lt7
D;JLT
@reg_cmp7
0;JMP
(gt_lt7)
D=-1
@cmp7
0;JMP
(cmp_lt7)
@SP
A=M-1
A=A-1
D=M
@lt_gt7
D;JGT
@reg_cmp7
0;JMP
(lt_gt7)
D=1
@cmp7
0;JMP
(reg_cmp7)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp7)
@true7
D;JGT
@false7
0;JMP
(true7)
D=-1
@end7
0;JMP
(false7)
D=0
@end7
0;JMP
(end7)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M-1
D=M
@cmp_gt8
D;JGT
@cmp_lt8
0;JMP
(cmp_gt8)
@SP
A=M-1
A=A-1
D=M
@gt_lt8
D;JLT
@reg_cmp8
0;JMP
(gt_lt8)
D=-1
@cmp8
0;JMP
(cmp_lt8)
@SP
A=M-1
A=A-1
D=M
@lt_gt8
D;JGT
@reg_cmp8
0;JMP
(lt_gt8)
D=1
@cmp8
0;JMP
(reg_cmp8)
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
D=M-D
(cmp8)
@true8
D;JGT
@false8
0;JMP
(true8)
D=-1
@end8
0;JMP
(false8)
D=0
@end8
0;JMP
(end8)
@SP
A=M-1
A=A-1
M=D
@SP
M=M-1
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
@53
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
@112
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
M=-M
@SP
A=M-1
D=M
@SP
A=M-1
A=A-1
M=M&D
@SP
M=M-1
@82
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
M=M|D
@SP
M=M-1
@SP
A=M-1
M=!M
