string_num='14'
int_num=14
float_num=1.22

#implicit type conversion
sum=int_num+float_num
print(sum)
print(type(sum))

print(type(string_num))
print(type(int_num))

# Explicit type conversion
string_num=int(string_num)
num_sum=int_num+string_num

print(num_sum)
print(type(num_sum))
