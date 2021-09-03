
with open('chicken.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line.strip())

#strip

print(" aa  def  ".strip())

my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split(". "))