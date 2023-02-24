############Generating lists with While loop###########
#L = []

#num = 1

#while num<=100:
    #L.append(num)
    #num = num + 1

############Generating lists with For loop###########
#print (L)

#L = []

#num = 1

#for num in range(100):
    #L.append(num + 1)
#print (L)

############Generating lists with List Comprehension, i.e without looping###########
####This is where the computer generates the list, in a more faster and optimized fashion###

##declare the variable within the list, and loop using the variable with the range function of 50###

l = [number for number in range(50)]
evennumb = [num*4 for num in range(20)]

print(evennumb)

## to get the 7th item within a list
print(evennumb[7])

## to get the last item within a list
print(evennumb[-1])

## to get a specific portion within a list
print(evennumb[1:5])

## to get a specific portion within a list from the beginning of the list
print(evennumb[:10])

## to get a specific portion within a list from a particular number to the end of the list 
print(evennumb[10:])