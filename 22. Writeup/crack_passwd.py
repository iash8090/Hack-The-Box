
#62def4866937f08cc13bab43bb14e6f7:5a599ef579066807
import hashlib

password='62def4866937f08cc13bab43bb14e6f7'
salt='5a599ef579066807'
output=''
wordlist='/usr/share/wordlists/rockyou.txt'

def crack_password():
    global password
    global output
    global wordlist
    global salt
    dict = open(wordlist)
    for line in dict.readlines():
        line = line.replace("\n", "")
        if hashlib.md5(str(salt) + line).hexdigest() == password:
            output += "\n[+] Password cracked: " + line
            print output
            break
    dict.close()

crack_password()
