#Modules

import time as t

t.localtime()

time_now = t.localtime()

print("Transaction completed at ", str(time_now.tm_hour) + "h" + str(time_now.tm_min) + "m")


print(t.time())

t.time()

print("Lets  pause, then resume")

print(t.time())

time_now = t.time()

delivery_time = time_now + (86400 * 7)

print(delivery_time)

print(t.localtime(delivery_time))

#slow terminal response down by 5 seconds
t.sleep(5)
