'''Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190'''

'''expense=[2200,2350,2600,2130,2190]

#1. In Feb, how many dollars you spent extra compare to January?

print("In Feb, we expect ", expense[1]-expense[0])

# Find out your total expense in first quarter (first three months) of the year.

print("Total of the quarter is", expense[0]+expense[1]+expense[2])

for i in expense:
    if i == 2000:
        print("Yes")
    else:
        print("No")

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.insert(5,1980)

print(expense)

#You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this

expense[3]=expense[3]+200
print(expense)



#2. You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

#Length of the list
print (len(heros))

#Add 'black panther' at the end of this list
heros.append('blackpanther')
print(heros)

#You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('blackpanther')
heros.insert(3,'blackpanther')
print(heros)

#Now you don't like thor and hulk because they get angry easily :) So you want to remove thor and hulk from list and 
# replace them with doctor strange (because he is cool).Do that with one line of code.

heros[1:3]=['doctor strange']
print(heros)

#Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)'''

# 3. Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
x= int(input("Insert a number: "))

odd=[]

for i in range (1,x):
    if i % 2 == 1:
        odd.append(i)
print("They are :", odd)