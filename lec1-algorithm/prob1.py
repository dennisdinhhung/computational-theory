list = input("Input a list of n intergers: ")
search = input("Input the searching number: ")
lowest = list[0]
highest = list[len(list)]
middle_index = round(len(list)/2) 
middle = list[middle_index]

if search == middle:
    print("The index of the number is: " + str(middle_index))

