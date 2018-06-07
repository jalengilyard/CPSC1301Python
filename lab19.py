# Jalen Gilyard
# Lab 19
# 24 April 2018

def replace_word(list1, target, replacement):
    total_replaced = 0
    for i in range(len(list1)):
        if list1[i] == target:
            list1[i] = replacement
            total_replaced += 1
    output = "%s was replaced %d times and the new list is %s " % (target,total_replaced, list1)
    return output

def main():
    stored_list = []
    value = input("Enter the first value: ")
    while value != "q":
        stored_list.append(value)
        value = input("Next value: ")
        if value == "q":
            value = "q"
    original = stored_list.copy()
    target = input("Enter a target word: ")
    replacement = input("Enter replacement word: ")
    print(replace_word(stored_list, target, replacement))
    print(original)
main()
