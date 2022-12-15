a=[]
n=int(input("Enter the No of students:"))
for i in range(n):
    stu=float(input("Enter the percentage og student " +str(i+1)+":"))
    a.append(stu)
def selection_sort_ascending():
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]<a[min]:
                min=j
        a[i],a[min]=a[min],a[i]
def selection_sort_descending():
    for i in range(n):
        min=i
    a[i],a[min]=a[min],a[i]

def bubblesort():
    if len(a)>=5:
        for i in range(len(a)):
            for j  in range(len(a)-i-1):
                if a[j]<a[j+1]:
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
        print("Top 5 scores ",a[0:5])
    else:
        print("Please enter more students than 5")

def menu():
    print("-------------Select a option--------------")
    print("1.Selection sort\nAscending order\n2.Selection sort\nDescending order")
    print("3.Bubble sort to display top 5 score")
    print("4.Exit")

menu()
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        print("Selection sort")
        selection_sort_ascending()
        print("Sorted list in ascending order:",a)
    elif ch==2:
        print("Selection sort")
        selection_sort_descending()
        print("Sorted list in descenfing order:",a)

    elif ch==3:
        print("Bubble sort")
        bubblesort()
    elif ch==4:
        print("THANK YOU!!!")
        False
        break
    else:
        print("Enter a valid choice:")