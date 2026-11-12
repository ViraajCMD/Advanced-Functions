num = int(input("Enter a number: "))

odd_under = [i for i in range(num) if i % 2 != 0]
odd_copy = [i for i in odd_under]

print("Odd numbers under input:", odd_under)
print("Another list of odd numbers:", odd_copy)

fruits = ['apple', 'banana', 'mango', 'orange', 'grapes']
capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Updated fruits list:", capitalized_fruits)
