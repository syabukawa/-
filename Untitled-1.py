print("   ", end="")
for i in range(1, 13):
    print(f"{i:4}", end="")
print()

print("   ", end="")
for i in range(1, 13):
    print("----", end="")
print()

for i in range(1, 13):
    print(f"{i:2}|", end="") 
    for j in range(1, 13):
        print(f"{i * j:4}", end="") 
    print()