start = int(input("number you want to start the sum? "))
end = int(input("Number till you want sum? "))
sum = 0
for i in range(start , end+1):
    sum = sum + i

print(sum)