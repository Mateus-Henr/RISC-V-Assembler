add x2, x0, x1 #00000000000100000000000100110011
add x6, x0, x2 #00000000001000000000001100110011
sub x3, x6, x2 #01000000001000110000000110110011
xor x4, x2, x3 #00000000001100010100001000110011
srl x0, x2, x2 #00000000001000010101000000110011
sh x5, 40(x6)
lui  x5, 40(x6)

