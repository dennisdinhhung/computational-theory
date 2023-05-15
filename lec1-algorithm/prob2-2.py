#insertion sort
def main():
    compare_count = 0
    input_list = input("Input a list: ")

    for j in range(1, len(input_list) - 1):
        i = 0
        while input_list[j] > input_list[i]:
            i += 1
        m = input_list[j]
        for k in range(j - i - 1):
            pass


    for i in range(len(input_list) - 1):
        for j in range(len(input_list) - i):
            if input_list[j] > input_list[j+1]:
                compare_count += 1
                temp = input_list[i]
                input_list[i] = input_list[i+1]
                input_list[i+1] = temp

main()