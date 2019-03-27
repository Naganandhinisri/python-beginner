def almostSorted(arr):
    sorted_array = arr.copy()
    sorted_array.sort()
    non_matching_index_list = []
    count = 0
    for i in range(0, len(arr)):
        if arr[i] != sorted_array[i]:
            count = count + 1
            non_matching_index_list.append(i)
    if count == 2 :
        print("yes")
        print("swap", non_matching_index_list[0] + 1, non_matching_index_list[1] + 1,    end='')
    else:
        is_consecutive = True
        # for i in range(0,(len(non_matching_index_list)-1)):
        #     array_index = non_matching_index_list
        #     if array_index[i]+1 != array_index[i+1]:
        #         is_consecutive = False
        #         break

        if is_consecutive == True:
            start_index = non_matching_index_list[0]
            end_index = non_matching_index_list[len(non_matching_index_list)-1]
            segment = arr[start_index:end_index+1]
            segment.reverse()
            index_to_replace = start_index
            # print(segment)
            for i in range(0,len(segment)):
                value = segment[i]
                # index = non_matching_index_list[i]
                arr[index_to_replace] = value
                index_to_replace+=1

            if arr == sorted_array:
                print("yes")
                print("reverse",start_index+1,end_index+1,end='')
            else:
                print("no")
        else:
            print("no")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
