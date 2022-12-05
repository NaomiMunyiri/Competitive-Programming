def bubble_sort(elements,key='name'):
    size=len(elements)

    for i in range(size-1):
        for j in range(size-1):
            if elements[key]>elements[key+1]:
                tmp=elements[key]
                elements[key]=elements[key+1]
                elements[key+1]=tmp
                swapped=True
            if not swapped:
                break

if __name__=='__main__':
    elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
    bubble_sort(elements)
    print(elements)