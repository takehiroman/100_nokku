#str.split(sep)でsepを区切り文字として文字列を分割してリストにします。区切り文字が指定されていない場合、スペース、タブ、改行文字列などで区切られます。

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

count = [len(i.strip(",.")) for i in str.split()]
print(count)

