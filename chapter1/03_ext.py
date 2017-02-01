s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

count = []

for i in s.split():
    count += [len(i.strip(",."))]

print(count)
