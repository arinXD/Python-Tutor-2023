file = "re.txt"
try:
    fruits = {}
    total = 0
    with open(file, "r") as f:
        data = f.readlines()
    for (index,line) in enumerate(data):
        if(index==0):
            continue
        order = line.strip().split(",")
        fruit = order[1]
        price = order[-1] 
        if not price.isnumeric():
            print("Cannot read the data line {}: {}".format(index, line))
            continue
        total += int(price)
        fruits.setdefault(fruit, 0)
        if fruit in fruits:
            fruits[fruit] += 1
    fruits = dict(sorted(fruits.items(), key=lambda item: item[1], reverse=True))
    f = open('output.txt', 'w')
    print("========== Fruir Report ==========")
    print("Quantity\t\tFruit")
    print("==================================")

    f.write("========== Fruir Report ==========\n")
    f.write("Quantity\t\tFruit\n")
    f.write("==================================\n")
    for (k,v) in fruits.items():
        print("{}\t\t\t{}".format(v,k))
        f.write("{}\t\t\t\t{}\n".format(v,k))
    f.close()

except FileNotFoundError:
    print("Cannot open {}".format(file))