# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Mr.......
# Student ID:
import pytest
MINIMUM = 500
MIDRANGE: int = 700
MAXIMUM = 1200
FREE_ICECREAM = "Free ice cream cone = "
FREE_CAKE = "Free chocolate cake = "
NO_GIFT = "Thank you and see you next time"

def print_promotion(total_cost):
    temp_cost = total_cost
    num_icecream = 0
    num_cake = 0

    # Check if total_cost is more than minimum requirement
    if total_cost >= MINIMUM:
        while temp_cost != 0:
            if temp_cost // MAXIMUM >= 1:
                num_icecream += temp_cost // MAXIMUM
                num_cake += temp_cost // MAXIMUM
                temp_cost = temp_cost - (num_icecream * MAXIMUM)
            elif temp_cost // MIDRANGE >= 1:
                num_cake += temp_cost // MIDRANGE
                temp_cost = temp_cost - (num_cake * MIDRANGE)
            elif temp_cost // MINIMUM >= 1:
                num_icecream += temp_cost // MINIMUM
                temp_cost = temp_cost - (num_icecream * MAXIMUM)
            else:
                temp_cost = 0
    else:
        # no gift
        print(NO_GIFT)

    if total_cost >= MAXIMUM:
        print(FREE_ICECREAM + str(num_icecream) + " and " + FREE_CAKE + str(num_cake))
    elif total_cost >= MIDRANGE:
        print(FREE_CAKE + str(num_cake))
    else:
        print(FREE_ICECREAM + str(num_icecream))

#Test
print("TS001")
print_promotion(499) #แสดง Thank you and see you next time

print("TS002")
print_promotion(699) #แสดงFree ice cream cone = 1
print_promotion(505) #แสดงFree ice cream cone = 1

print("TS003")
print_promotion(701) #แสดง Free chocolate cake = 1
print_promotion(1120) #แสดง Free chocolate cake = 1
print_promotion(1199) #แสดง Free chocolate cake = 1

print("TS004")
print_promotion(1200) #แสดง Free ice cream cone = 1 and Free chocolate cake = 1

print("TS005")
print_promotion(1400) #แสดง Free ice cream cone = 1 and Free chocolate cake = 1
print_promotion(2400) #แสดง Free ice cream cone = 2 and Free chocolate cake = 2
print_promotion(3505) #แสดง ice cream cone = 2 and Free chocolate cake = 3