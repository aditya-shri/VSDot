data = {}
lst = []
for it in range(0,84):
    first = input().replace('-', '').split(" ")
    lst.append(first[-1])
data = {"crops" : lst}
print(data)