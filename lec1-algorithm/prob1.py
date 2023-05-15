def search_recurse_binary(list, search_item, low_index, high_index):
    #search the right side (aka middle index + 1)
    while(low_index != high_index):
        middle_index = round(len(list)/2) 
        middle = list[middle_index]

        if search_item == middle:
            print("The index of the number is: " + str(middle_index))
        elif search_item > middle:
            low_index = middle_index + 1
        else: 
            high_index = middle_index -1

def main():
    list = input("Input a list of n intergers: ")
    search_item = input("Input the searching number: ")

    search_recurse_binary(list, search_item, 0, len(list)) 

main()