Feistel_Indexes = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]
Feistel_Indexes = list(map(lambda x:x-1, Feistel_Indexes))

Ri = input("Enter Ri-1:")
Ki = input("Enter Ki  :")

if (len(Ri)!=32) or (len(Ki)!=48):
	print("!!! Key or Ri-1 have inapropriate lenght")
	exit()
RiNew = [Ri[index] for index in Feistel_Indexes]


xor_out = ""
for i in range(len(RiNew)):
	xor_out += "1" if (RiNew[i] != Ki[i]) else "0"

for i in range(8):
	print(f"B{i+1}:", xor_out[6*i:6+6*i])

	111111111111111110000000000000000