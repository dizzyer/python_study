Aup = 0.01
B = 37.78
A = 1

while A < B:
    A = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            A = A*(1-0.01)
        else:
            A = A*(1+Aup)
    Aup = Aup + 0.001

print(Aup)

# for i in range(365):
#     if i % 7 in [0, 6]:
#         A = A*(1-0.01)
#     else:
#         A = A*(1+0.1)
# print(A)
