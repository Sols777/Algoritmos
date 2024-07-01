num = 0
count = 0
maxCount = 50


while True:
    if count == maxCount:
        break
    if num % 2 == 0:
        count +=1
        num +=2
        print (f'\n{count}- {num-2}\n')
        
        
# for i in range(0,100,2):
#     if i %2 == 0:
#         count +=1
#         num +=2
#         print (f'\n{count}- {num-2}\n') 
#     else:
#         break

