word1 = 'Hello'
word2 = "Welcome"
word3 = """to Python class"""
print(f"{word1} {word2} {word3}")

sentence = ("Python is fun to learn!")
print(sentence)

print("""Python is powerful\nIt is easy to learn\nIt is loved by developers""")

txt = "PYTHON"

print(txt[0])
print(txt[2])
print(txt[5])

language = ("PYTHON")
for language in language:
    print(language)

fruit = ("Banana")
print(len(fruit))

word = ("Learning Python is cool")
print("Python" in word)

word = ("Learning Python and Java is cool")
if ("Python" in word):
 print("Yes! 'Python' is found")
 word = ("Learning python and Jva is cool")
if ("Java" in word):
    print("Yes")
else:
    print("No! Java is unavailable")

message = "Coding  is fun"
count = 0
for n in message:
    if n == "n":
        count += 1

print(count)

poem = '''Ten green bottles standing on the wall
it's ten green bottles and one accidentally
down, nine green bottles standing on the wall...'''
print(poem.upper())