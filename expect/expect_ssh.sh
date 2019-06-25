#!/usr/bin/expect -f  

#aime
set user [lindex $argv 0]

#2cool
set password [lindex $argv 1]

#scl58212.us.oracle.com/localhost
set host [lindex $argv 2]

set timeout 15 

spawn ssh $user@$host  

expect "no)?" {
send "yes\r" }

#Send Wrong password
expect "*assword:*" {
send "wrongpw\r" }

#Send right password
expect "*assword:*" { 
send "$password\r" }

expect {
  "*$*" {send "exit\r"}
  "*#*" {send "exit\r"}
}

expect eof
exit
