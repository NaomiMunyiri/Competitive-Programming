def bubble_sort(elements):
    size=len(elements)

    swapped=False
    for i in range (size-1):
        for j in range(size-1):
            if elements[j]>elements[j+1]:
                tmp=elements[j]
                elements[j]=elements[j+1]
                elements[j+1]=tmp
                swapped=True         
        if not swapped:
            break

if __name__=='__main__':
    elements=[5,9,2,1,67,34,88,34]
    bubble_sort(elements)
    print(elements)