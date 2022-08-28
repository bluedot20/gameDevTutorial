#2 Factorial 

# def factorial(number): 
# 	answer = 1 
# 	for i in range(1, number + 1): 
# 		answer *= i  
# 	return answer 

# # print(factorial(4))

# import math
# # print(math.factorial(20))


# #3 
# # # Syntax Errors (Compile-Time Errors)
# # # print("Uh oh!) # ERROR!  missing close-quote

# # # Runtime Errors ("Crash")
# # # print(1/0) # ERROR!  Division by zero!

# # # Logical Errors (Compiles and Runs, but is Wrong!)
# # # print("2+2=5") # ERROR!  Untrue!!!








# # print("Some basic types in Python:")
# # print(type(2))           # int
# # print(type(2.2))         # float
# # print(type(2 < 2.2))     # bool (boolean)
# # print(type(type(42)))    # type

# # print("#####################################################")

# # print("And some other types we may see later in the course...")
# # print(type("2.2"))       # str (string or text)
# # print(type([1,2,3]))     # list
# # print(type((1,2,3)))     # tuple
# # print(type({1,2}))       # set
# # print(type({1:42}))      # dict (dictionary or map)
# # print(type(2+3j))        # complex  (complex number)

# # print(10 / 3) 	# exact val (float)
# # print(10 // 3) # quotient

# # def isPrime(n): 
# # 	for i in range(2, n): 
# # 		if n % i == 0: 
# # 			return False 
# # 		print(i)
# # 	return True 
# # 	# print("Hello")

# # print(isPrime(9))



# x = [1,2,3]
# # x = x.append(4) 
# x.append(4)
# print(x)


# print(ord("A"))
# print(ord("a"))
# # print(chr(97))
# # print(chr(ord("a") + 1))

# print("a" < "A")



a = [1,2,3,4,5,6]
x = a.remove(2)		# element
print(a)
print(x)
a = [1,2,3,4,5,6]
number = a.pop(2)  			# index, stores popped # in number 
print(a, number)


listA = [("cow", 5), ("dog", 98)]
dictA = dict(listA)
print(listA)







# def friendsOfFriends(d):
#     #this function returns a dictionary that tells one's friends of friends
#     finalDictionary=dict()
#     for values in d:
#         newset=set() #creates the set for the friends of friends 
#         friendValues=d[values] #friends        
#         for friend in friendValues: 
#             fof=d[friend]
#             for name in fof: 
#                 if name != values and name not in d[values]: 
#                 #excludes friends and oneself 
#                     newset.add(name) 
#         finalDictionary[values] = newset 
#     return finalDictionary


# d = { }
# d["jon"] = set(["arya", "tyrion"])
# d["tyrion"] = set(["jon", "jaime", "pod"])
# d["arya"] = set(["jon"])
# d["jaime"] = set(["tyrion", "brienne"])
# d["brienne"] = set(["jaime", "pod"])
# d["pod"] = set(["tyrion", "brienne", "jaime"])
# d["ramsay"] = set()

# print(friendsOfFriends(d))