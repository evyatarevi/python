
# Remove: remove, pop, clear
# Insert: append, insert, replace
# List: slice, sum, min, max

print(len("Hello, World!"))

# Output:  13  - כולל רווחים וסימנים, אך לא כולל גרשיים סוגורת משני הצדדים



print("Hello, World"[0:5]) # slice: [start index : end index : jump number]

# Output: Hello   




text = "Hello, World, Hellow!"
print(text.replace("Hello", "Hi"))  #Return a copy with *all* occurrences of substring old replaced by new.

# Output: Hi, World, Hi!



text = "Hello, World!"
print(text.isdigit())  #Return True if the *string* is a digit string, False otherwise.
                       #A string is a digit string if *all* characters in the string are digits and there is at least one character in the string.
                       # פועל רק על מחרוזת ולא על מספרים. אפשר גם לבחור אינדקס ספציפי ועליו לבדוק
# Output: False

text = "h3"
print(text[1].isdigit()) 
# output: True



numbers = [1, 2, 3, 4, 5]
print(sum(numbers))

# Output: 15





numbers = [1, 2, 3, 4, 5]
print(min(numbers))

# Output: 1 (אפשר גם מס' שלילי)




numbers = [1, 2, 3, 4, 5]
print(max(numbers))

# Output: 5




numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

# Output: [5, 4, 3, 2, 1] return array



numbers = [1, 2, 3, 4, 5]
print(numbers[0:3])

# Output: [1, 2, 3]



numbers = [1, 2, 3, 4, 5]
numbers.append(6)  #Append object to the end of the list.
print(numbers)

# Output: [1, 2, 3, 4, 5, 6]



numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 22)  #Insert object before index.
print(numbers)

# Output:[22, 1, 2, 3, 4, 5]  שים לב שהוא לא מחליף אלא דוחף,לפי האינדקס




numbers = [1, 2, 3, 4, 5]
numbers.remove(3)  #Remove first occurrence of value. Raises ValueError if the value is not presen
print(numbers)

# Output: [1, 2, 4, 5] - מחליף את הערך המספרי ולא לפי אינדקס

# Remove - by value, pop - by index

numbers = [1, 2, 3, 4, 5]
numbers.pop()  #Remove and return item at index (default last)
print(numbers)

#Output: [1, 2, 3, 4]



numbers = [1, 2, 3, 4, 5]
numbers.clear()  #reset list
print(numbers)

#Output: []


numbers = [1, 2, 3, 4, 5]
print(len(numbers))

#Output: 5


