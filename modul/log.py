import os, sys

print ("\033[1;31mAnda Harus Login Terlebih Dahulu")
print ("\033[1;32mMasukan Username & Password")
username = 'mr.joker'
password = 'joker'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:
                        print"\n\033[1;34mWelcome To Tools Joker",
                        sys.exit()

                else:
                        print "\n\033[1;36mSorry Invalid password !!!\033[00m"
                        print "Back Login/n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()
