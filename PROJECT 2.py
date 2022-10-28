code = str(input('Enter the customer\'s code:'))
first = int(input('Enter the customer\'s beginning meter reading: '))
sec = int(input('The customer\'s ending meter reading: '))

print('Customer\'s code:', code)
print("Beginning meter reading: {:0>9}".format(first))
print("Ending meter reading: {:0>9}".format(sec))

if (0 < first <= 999999999) and (0 < sec <= 999999999):
        if first < sec:
            gal = (sec - first) / 10.0
        else:
            gal = ((1000000000 - first) + sec) / 10.0
else:
    gal=0
    code = 'q'
    print('Invalid meter reading')

print("Gallons of water used: {:.1f}".format(gal))

if code == 'R' or code == 'r':
    price = float(5 + (0.0005*gal))

    print("Amount billed: ${:.2f}".format(price))

elif code == 'C' or code == 'c':
    if gal <= 4000000:
        price = float(1000)

        print("Amount billed: ${:.2f}".format(price))
    else:
        price = float(1000 + ((gal-4000000)*0.00025))

        print("Amount billed: ${:.2f}".format(price))

elif code == 'I' or code == 'i':
    if gal <=4000000:
        price = float(1000)
        print("Amount billed: ${:.2f}".format(price))
    elif 4000000 <gal <= 10000000:
        price = float(2000)
        print("Amount billed: ${:.2f}".format(price))
    else:
        price = float(2000 + ((gal-10000000)*0.00025))
        print("Amount billed: ${:.2f}".format(price))

else:
    print('Invalid Entry')
