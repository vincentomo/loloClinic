dataset = []
count=0
with open("gdp.txt") as fin:
    for line in fin:
        dataset.append(line.strip())

while count < 4:
    data = dataset[count].strip().split('|')
    date = data[1]
    level_current = float(data[2].strip())
    level_chained = float(data[3].strip())
    change_current = float(data[4].strip())
    change_chained = float(data[5].strip())
    print (f"Date: {date}")
    print (f"Level_Current:  {level_current}")
    print (f"Level_Chained: {level_chained}")
    print (f"Change_Change: {change_current}")
    print (f"Change_Chained: {change_chained}")

    print(f"======= END {count} ==========")
    count += 1


