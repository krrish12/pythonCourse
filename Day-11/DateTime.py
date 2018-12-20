import time

print("Expression value is:",time.time())
#output: Expression value is: 1545302015.9695518

print("Expression value is:",time.altzone)
#output: Expression value is: -23400

print("Expression value is:",time.asctime())
#output: Expression value is: Thu Dec 20 16:13:38 2018

print("Expression value is:",time.localtime())
#output: Expression value is: time.struct_time(tm_year=2018, tm_mon=12, tm_mday=20, tm_hour=16, tm_min=41, tm_sec=58, tm_wday=3, tm_yday=354, tm_isdst=0)

print("Expression value is:",time.asctime(time.localtime()))
#output: Expression value is: Thu Dec 20 16:13:38 2018

print("Expression value is:",time.process_time())
#output: Expression value is: 0.03125

print("Expression value is:",time.perf_counter())
#output: Expression value is: 0.0186701

print("Expression value is:",time.ctime())
#output: Expression value is: Thu Dec 20 16:32:06 2018

print("Expression value is:",time.gmtime())
#output: Expression value is: time.struct_time(tm_year=2018, tm_mon=12, tm_mday=20, tm_hour=11, tm_min=2, tm_sec=35, tm_wday=3, tm_yday=354, tm_isdst=0)

t = (2018, 12, 20, 22, 30, 00, 1, 18, 0)
secs = time.mktime( t )
print("time.mktime(t) : %f" %  secs)
#output: time.mktime(t) : 1545304418.000000

print("asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs)))
#output: asctime(localtime(secs)): Thu Dec 20 16:43:38 2018

c=time.ctime()
print("Expression value is:",c)
#output: Expression value is: Thu Dec 20 16:46:59 2018

time.sleep(5)

print("Expression value is:",c)
#output: Expression value is: Thu Dec 20 16:46:59 2018

print("Expression value is:",time.strftime("%b %d %Y %H:%M:%S", time.gmtime(secs)))
#output: Expression value is: Dec 20 2018 11:13:38

#print("Expression value is:",time.strftime("%B %D %Y %H:%M:%S", time.gmtime(secs)))
#output: Expression value is: December  12/20/18 2018 11:13:38

print("Expression value is:",time.strftime("%b %d %Y %H:%M:%S %p", time.gmtime(secs)))
#output: Expression value is: Dec 20 2018 17:00:00 PM

print("Expression value is:",time.strftime("%B %d %Y %r", time.gmtime(secs)))
#output: Expression value is: December 20 2018 05:00:00 PM

struct_time = time.strptime("30 Nov 00", "%d %b %y")
print("returned tuple:",struct_time)
#output: returned tuple: time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

