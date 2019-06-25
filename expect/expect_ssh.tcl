#!/usr/bin/expect -f  

variable machine "[lindex $argv 0]"
variable user "[lindex $argv 1]"
variable passwd "[lindex $argv 2]"
variable cmd "[lindex $argv 3]"

set timeout 600

spawn ssh -o StrictHostKeyChecking=no -o PubkeyAuthentication=no -o BatchMode=no $user@$machine "$cmd"
expect {
        -re   "Are you sure you want to continue connecting (yes/no)?" {
                exp_send "yes\r"
                exp_continue
        }
        -nocase "password: " {
                exp_send "$passwd\r"
                puts "\n----------------------"
        }
}

expect eof

