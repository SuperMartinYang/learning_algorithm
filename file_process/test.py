# include <stdio.h>

int
IP[64] = {58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40,
          32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63,
          55, 47, 39, 31, 23, 15, 7};
int
Key_Permutation[56] = {57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60,
                       52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21,
                       13, 5, 28, 20, 12, 4};
int
Key_shift_num[16] = {1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1};
int
Key_compress_substitution[48] = {14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
                                 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36,
                                 29, 32};
int
R_expansion[48] = {32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19,
                   20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1};
int
s_box_1[4][16] = {14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7, 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5,
                  3, 8, 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0, 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14,
                  10, 0, 6, 13};
int
s_box_2[4][16] = {15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10, 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9,
                  11, 5, 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15, 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12,
                  0, 5, 14, 9};
int
s_box_3[4][16] = {10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8, 13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11,
                  15, 1, 13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7, 1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3,
                  11, 5, 2, 12};
int
s_box_4[4][16] = {7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15, 13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10,
                  14, 19, 10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4, 3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11,
                  12, 7, 2, 14};
int
s_box_5[4][16] = {2, 12, 4, 1, 7, 10, 11, 6, 5, 8, 3, 15, 13, 0, 14, 9, 14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 13, 3, 9,
                  8, 6, 4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14, 11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9,
                  10, 4, 5, 3};
int
s_box_6[4][16] = {12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11, 10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11,
                  3, 8, 9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6, 4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7,
                  6, 0, 8, 13};
int
s_box_7[4][16] = {4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1, 13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15,
                  8, 6, 1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2, 6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15,
                  14, 2, 3, 12};
int
s_box_8[4][16] = {13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7, 1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14,
                  9, 2, 7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8, 2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0,
                  3, 5, 6, 11};
int ** s_boxes[8] = {s_box_1, s_box_2, s_box_3, s_box_4, s_box_5, s_box_6, s_box_7, s_box_8};

int
P_BOX[32] = {16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22,
             11, 4, 25};
int
IN_P[64] = {40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13,
            53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26,
            33, 1, 41, 9, 49, 17, 57, 25};

# define BIT 0x8000000000000000
# define LEFT 0xFFFFFFFF00000000
# define RIGHT 0x00000000FFFFFFFF
# define KEY_LEFT 0x00FFFFFFF0000000
# define KEY_RIGHT 0x000000000FFFFFFF
# define INIT 1
# define INVERSE 0

# define B1 0xFC0000000000
# define B2 0x3F000000000
# define B3 0xFC0000000
# define B4 0x3F000000
# define B5 0xFC0000
# define B6 0x3F000
# define B7 0xFC0
# define B8 0x3F
int
Bs[8] = {B1, B2, B3, B4, B5, B6, B7, B8};
/ *macro
function * /
# define GET16(x) ((((x) & 0x20) >> 4) | ((x) & 0x1))
# define GET2345(x) ((x) << 1 >> 2)

# define LAST_1 0x1
# define LAST_2 0x11




int
times = 0;

/ *left
shift * /
long
long
ls(long
long
key_half){
    int
shift_num = 0;
shift_num = Key_shift_num[times];
int
last_bits = (shift_num == 1) ? LAST_1: LAST_2;
return ((key_half & last_bits) << (28 - shift_num)) | (key_half >> shift_num);
}

/ *key
divid and shift * /
          long
long
key_generate(long
long
key){
long
long
key_left, key_right;
// left and right
shift
1 or 2
bits
respectively
key_left = KEY_LEFT & key >> 27;
key_right = KEY_RIGHT & key;
return (ls(key_left) << 27) | ls(key_right);
}

/ *key
permutation * /
long
long
init_key(long
long
key){
int
i;
long
long
key_init = 0x0;
for (i = 0; i < 56; i++){
key_init |= (key & (BIT >> (Key_Permutation[i] - 1))) << (Key_Permutation[i] - 9 - i);
}
return key_init;
}

/ *compress & substitution
48
b -> 32 * /
     long
long
pc(long
long
key_curr){
int
i;
long
long
sub_key = 0x0;
for (i = 0; i < 48; i++){
sub_key |= (key_curr & (BIT >> 8 >> (Key_compress_substitution[i] - 1))) << (Key_compress_substitution[i] - 9 - i);
}
return sub_key;
}

/ *init
permutation * /
long
long
init_inverse_permutation(long
long
plaintext, int
flag){
int
i, *P;
long
long
init_inverse_p = 0x0;
P = (flag == INIT) ? IP: IN_P;
for (i = 0; i < 64; i++){
init_inverse_p |= (plaintext & (BIT >> (P[i] - 1))) << (P[i] - 1 - i);
}
return init_inverse_p;
}





long
long
expansion(long
long
right){
int
i;
long
long
expanded_right = 0x0;
for (i = 0; i < 48; i ++){
expanded_right |= (right & (BIT >> 32 >> (R_expansion[i] -1))) << (R_expansion[i] + 15 - i);
}
return expanded_right;
}

/ *use
s_box
to
compress(48
b -> 32
b) * /
long
long
subsitution(long
long
expanded_xor_right){
int
i, tmp, row_no = 0, col_no = 0;
long
long
cipherred_right = 0x0;
for (i = 0; i < 8; i ++){
tmp = (expanded_xor_right & Bs[i]) >> ((7 - i) * 6);
row_no = GET16(tmp);
col_no = GET2345(tmp);
cipherred_right |= (s_boxes[i][row_no][col_no]) << ((7 - i) * 4);
}
return cipherred_right;
}
/ *P
box
permutation * /
long
long
p_permutation(long
long
cipherred_right){
long
long
right_end;
int
i;
for (i = 0; i < 32; i ++){
right_end |= (cipherred_right & (BIT >> 32 >> (P_BOX[i] - 1))) << (P_BOX[i] - 1 -i);
}
return right_end;
}

/ *function
f -> Ri
expand and key
xor and compress * /
        long
long
func(long
long
right, long
long
key_curr){
long
long
expanded_right = 0, cipherred_right = 0, right_end = 0;
expanded_right = expansion(right);
cipherred_right = substitution(expanded_right ^ key_curr);
right_end = p_permutation(cipherred_right);
return right_end;
}

/ *round
16
times
recursively * /
long
long
round_16_times(long
long
curr, long
long
C_D){
if (times == 16)
    return curr;
int
i;
long
long
left, right, tmp;
left = LEFT & curr;
right = RIGHT & curr;
tmp = left; // Li = Ri
left = right << 31;

right = (tmp >> 31) ^ func(right, pc(C_D)); // Ri = Li0(f(Ri, ki))
C_D = key_generate(C_D);
curr = left | right;
times + +; // count
times
round_16_times(curr, C_D);
}

/ *encrypt * /
   long
long
encrypt(long
long
plaintext, long
long
key){
// long
long
has
64
bits
long
long
curr = 0, key_init = 0, C_D = 0, p_end = 0, ciphertext = 0;
curr = init_inverse_permutation(plaintext, INIT);
key_init = init_key(key);
C_D = key_generate(key_init);
p_end = round_16_times(curr, C_D);
ciphertext = init_inverse_permutation(p_end, INVERSE);
return ciphertext;
}

/ *main * /
   int
main()
{
long
long
plaintext, key, ciphertext;
printf("Please input plaintext(8 chars):");
scanf("%ll", & plaintext);
printf("Please input key:");
scanf("%ll", & key);
ciphertext = encrypt(plaintext, key);
printf("Cipher text is : %ll", ciphertext);
return 0;
}