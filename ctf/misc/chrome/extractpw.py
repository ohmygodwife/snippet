import sqlite3
import binascii
conn = sqlite3.connect("Login Data")
cursor = conn.cursor()
cursor.execute('SELECT action_url, username_value, password_value FROM logins')
for result in cursor.fetchall():
    print (binascii.b2a_hex(result[2]))
    f = open('test.txt', 'wb')
    f.write(result[2])
    f.close()