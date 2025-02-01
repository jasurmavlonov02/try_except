# file = open('data.txt', 'r')
# data = file.read()
# print(data)
# file.close()

# file = None
# try:
#     file = open("data.txt", "r")
# except FileNotFoundError as e:
#     print(e)
# else:
#     data = file.readlines()
#     for line in data:
#         print(line.rstrip('\n'))
# finally:
#     if file and not file.closed:
#         file.close()

#
# file = None
# try:
#     file = open("data.txt", "r")
# except FileNotFoundError as e:
#     print(e)
# else:
#     data1 = file.readline()
#     data2 = file.readline()
#     data3 = file.readline()
#     print(data3)
#
# finally:
#     if file and not file.closed:
#         file.close()


# 'r' , 'w' , 'a'
