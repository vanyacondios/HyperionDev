# sum = 0 before user has entered anything the total sum is 0
# num = 57 initial num value is irrelevant as long as not -1, it only serves to start the loop, num is then immediately redefined
# i = 0   using i as a counter to help calculate the average later

sum, num, i = 0, 57, 0 
while num != -1: # as long as entered value is not -1
    num = float(input("Please enter a random number: ")) # user will be asked to input a number
    i += 1 # total number of entries increases by 1
    sum = sum + num # sum increases by the number the user has entered
    continue # loop starts again
    # if num == -1: 
    #     break       # these two lines appear redundant
    
average = round(((sum+1)/(i-1)),2) # because we ask the user for input only after the while condition
                                   # the -1 is counted towards the final sum and i values
                                   # we do not want to count the -1 entry, therefore subtract -1 from the sum 
                                   # and subtract 1 from i so total number of entries is reduced by 1
print(f"The average (not counting -1) is {average}.") 