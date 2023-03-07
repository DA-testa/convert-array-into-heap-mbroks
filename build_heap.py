# python3
import math

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(len(data)-1,-1,-1):
        while i>=0 and data[i]<data[int((i-1)/2)]:
            data[int((i-1)/2)], data[i] = data[i], data[int((i-1)/2)]
            swaps.append(str(str(int((i-1)/2))+ " "+str(i)))
            i = int((i-1)/2)
            

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    txt = input()
    if 'I' in txt:
        n = int(input())
        arr = input()
        data = map(int,arr.split())
        data = list(data)
        
    elif 'F' in txt:
        path = input()
        if '.a' not in path:
            path = "tests/"+path
            with open(path,'r') as file:
                n = int(file.readline())
                data = file.read()
                data = map(int,data.split())
                data = list(data)
    else:
        print("wrong input")
        

    # input from keyboard
    #n = int(input())
    #data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print(len(swaps))

    # output all swaps
    #print(len(swaps))
    #swaps = []
    for i in range(len(swaps)):
        print(swaps[i])
    #print(*data)
    
if __name__ == "__main__":
    main()
