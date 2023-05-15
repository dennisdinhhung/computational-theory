#Given a list of integers, determine the number of comparisons used by the bubble sort and by the insertion sort to sort this list.

#Bubble sort
def main():
    compare_count = 0
    input_list = input("Input a list: ")
    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i):
            if input_list[j] > input_list[j+1]:
                compare_count += 1
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp

main()