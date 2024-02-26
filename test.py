# chapter two

# is and ==
a = 3; o = 3
print(a == o)  # true
print(a is o)  # true

aa = [3, 2, 3]
oo = [3, 2, 3]
print(aa == oo)  # true
print(aa is oo)  # false cuz their restoration is different

# change two variables values without using a third one
c = 8; b = 0
c , b = b , c;

print(b , c)

