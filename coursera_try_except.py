def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
        error_co = 0
    except:
        error_co = -1
        if error_co <= -1:
            return 'Incorrect input!'
    if hours < 0:
        return 'Incorrect hours'
    elif hours <= 40 and hours >= 0:
        return hours * rate
    elif hours > 40:
        limit = 40
        return rate * ((hours - limit) * 1.5 + limit)



print computepay(raw_input('Enter hours:'),raw_input('Enter rate:'))