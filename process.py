
# #opens the txt file and saves it to a variable called log_file
log_file = open("um-server-01.txt")

# #defining a function called sales_reports that takes in our open txt file, which we named log_file above
# def sales_reports(log_file):
# #looping over each line in our txt file
#     for line in log_file:
# #stripping each line of the white space between lines
#         line = line.rstrip()
# #telling the for loop which index from the txt file we want to access, and saving it to a variable named day
#         day = line[0:3]
# #telling the for loop which value we want to access in the index we set above
#         if day == "Mon":
# #if the index we requested equals our day variable, we're printing the line variable we set above
#             print(line)

# #invoking our sales_reports function and passing in our open txt file as an argument
# sales_reports(log_file)

def melon_orders (log_file):
   for order in log_file:
        order = order.rstrip().split(' ')
        count = int(order[2])
        if count > 10:
                        print(count)

melon_orders(log_file)