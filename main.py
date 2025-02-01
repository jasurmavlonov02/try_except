# from project import get_user_by_username as get_user
# print(get_user())
# Try , except => exception

# age = int(input("Enter your name: "))

# print(5 / 0)  # cheksizlik

# arr = [10, 20, 30, 40]
#
# print(arr[10])

'''
try:
    pass

except ZeroDivisionError:
    pass
'''

# try:
#     number = int(input('Enter a number: '))
#     result = 100 / number
#     print(result)
#
# except ValueError as e: # error
#     print(e)
# except ZeroDivisionError as e:
#     print(e)

#
# cars = ['bmw', 'audi', 'toyota', 'subaru', 'ferrari']
#
# try:
#     index = int(input('index => '))
#     car = cars[index]
#     print(car)
#
# except (ValueError, IndexError, ZeroDivisionError) as e:
#     print(e)
#
# except IndexError as e:
#     print(e)


# dict => KeyError
# ModuleNotFoundError
# import sherali


user_db = {
    'username': 'john',
    'password': 'admin123',
    'is_active': True
}

# print(user_db['email'])
# try:
#     key = input('key => ')
#     print(user_db[key])
#
# except KeyError:
#     print('invalid key')


'''
try:
    pass
    
except ZeroDivisionError:
    pass
else:
    pass
    
finally:
    pass

'''

# arr = [10, 20, 30]
#
# try:
#     index = int(input('index : '))
#     get_item = arr[index]
#
# except (ValueError, IndexError) as e:
#     print(e)
# else:
#     print(get_item)
#
# finally:
#     print('This Finally BLock')

# if try success => try , else , finally
# if exception success => except , finally

# raise => Exception
#
# x = -24
#
# if x < 0:
#     raise IndexError('x must be positive')
#
# print('------------')


arr = [100, 200, 300, 400]

target = 12324

if target not in arr:
    raise Exception('Your target is not found')
