#Paguio, Jarred
#42762868

#Documentation of Variables
string = raw_input("Convert binary into decimal: ")
sum = 0

#Length of string/Number of bits
N = len(string)

#Converts binary into decimal
for n in range(N):
    i = N-1-n
    ans = int(string[i]) * (2**n)
    sum = sum + ans
print(sum)
