strings = "  fly me   to   the moon  "
i = len(strings) - 1
while i >= 0 and strings[i] == " ":
    i -= 1
    
end = i

while i >= 0 and strings[i] != " ":
    i -= 1
    
start = i + 1

last_word = strings[start:end + 1]
print(last_word)
print(len(last_word))
