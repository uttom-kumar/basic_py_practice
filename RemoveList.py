# remove() = the remove() method removes the specified them.

thisList = ['apple', 'banana', 'mango', 20, 50]
thisList.remove(20)
thisList.remove("apple")
print(thisList)


# pop () = The pop() method removes specified index
thisList2 = ['apple', 'banana', 'mango', 20, 50]
thisList2.pop(0) #remove specified index items
thisList2.pop() #remove the last items
print(thisList2)

#clear () = the clear() method removes all items
thisList3 = ['apple', 'banana', 'mango', 20, 50]
thisList3.clear()
print(thisList3)

# del = The del keyword also removes the specified index
thisList4 = ['apple', 'banana', 'mango', 20, 50]
del thisList4[4]
print(thisList4)
#del thisList4 #NameError: name 'thisList4' is not defined. Did you mean: 'thisList'?