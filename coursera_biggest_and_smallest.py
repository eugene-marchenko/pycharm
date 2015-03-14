largest = None
smallest = None
while True:

    number = raw_input('Enter number')
    if number == 'done':
        break
    else:
        try:
            number = int(number)

        except:
            print "Invalid input"
            continue

    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
    elif number > largest:
        largest = number





print "Maximum is", largest
print "Minimum is", smallest




