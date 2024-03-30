text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = text.replace(",", "").replace(".", "")
result = (list(map(len, text.split())))
#resultを文字列のリストに変換し、結合
result = list(map(str, result))
print("".join(result))