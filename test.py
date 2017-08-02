def move_zeros(array):
    #your code here
    for item in array:
        try:
            if int(item) == 0:
                array.remove(0)
                array.append(0)
        except:
            pass
    return array

if __name__ == '__main__':
    print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))