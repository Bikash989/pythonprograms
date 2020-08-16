"""Use a stack ds to convert int to binary

Example: 242

242 / 2 = 121 -> 0
121 / 2 = 60  -> 1
60 / 2  = 30  -> 0
30 /2   = 15  -> 0
15 / 2  = 7   -> 0
7  / 2  = 3   -> 1
3 / 2   = 1   -> 1
1  / 2  = 0   -> 1

 verify: int('11110010', 2) = 242
"""

from stack import Stack
from math import floor
def div_by_2 (dec_num):
	if dec_num <= 0:
		raise ValueError("Number must be postive")
	s = Stack()
	
	while dec_num > 0:
		remainder = dec_num % 2
		s.push(remainder)
		dec_num  = int(floor(dec_num/2))
		# or dec_num = dec_num // 2  # integer division
	bin_num = ""
	while not s.is_empty():
		bin_num += str(s.pop())
	return bin_num
try:
	print(div_by_2(-10))
except Exception as e:
	print(e)
print(div_by_2(242))

