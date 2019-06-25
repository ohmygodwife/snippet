'''
Usage: python base-pin.py ~/Downloads/pin-3.7-97619-g0d0c92f4f-gcc-linux /mnt/hgfs/matches/91ctf/180121/plz_re_me 8 [GRANULARITY: 0/1/2] [guess_length]
Known password length, collision test password byte by byte with pin
'''
import sys
import os
import subprocess

GRANULARITY_ARRAY = ('rtncount', # not reliable, never use!
                     'tracecount',  #fast but not accurate
                     'inscount2',  #instruction level calculated by trace
                     'inscount0',  #real instruction level#
                    )
GRANULARITY_RTN = 0
GRANULARITY_TRACE = 1
GRANULARITY_INS_2 = 2
GRANULARITY_INS_0 = 3

pin_root = sys.argv[1]
app_path = sys.argv[2]
passwd_len = int(sys.argv[3])

if len(sys.argv) > 4:
  gran = int(sys.argv[4])
else:
  gran = GRANULARITY_INS_2

sample_dir = os.path.join(pin_root, 'source', 'tools', 'ManualExamples')
out_file = GRANULARITY_ARRAY[gran] + '.out'
os.chdir(sample_dir)
# pin -t obj-intel64/rtncount.so -- app_path
# ~/Downloads/pin-3.7-97619-g0d0c92f4f-gcc-linux/pin -t obj-intel64/tracecount.so -o tracecount.out -- /mnt/hgfs/matches/91ctf/180121/plz_re_me
cmd = [os.path.join(pin_root, 'pin'),
       '-t',
       os.path.join('obj-intel64', GRANULARITY_ARRAY[gran] + '.so'),
       '-o',
       out_file,
       '--',
       app_path]
print cmd

result_file = open('passwd.txt', 'w')

def call_pin(passwd):
  p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  # https://stackoverflow.com/questions/28616018/multiple-inputs-and-outputs-in-python-subprocess-communicate
  # Popen.communicate() is a helper method that does a one-time write of data to stdin and creates threads to pull data from stdout and stderr
#  print p.stdout.readline()
#  p.stdin.write(passwd)
#  p.stdin.close() # Must call close, otherwise would hang for python 2.* https://docs.python.org/2/library/subprocess.html
  (stdoutdata, stderrdata) = p.communicate(passwd)
  if 'Congratulations' in stdoutdata:
    print "Found: ", passwd
    exit()
    result_file.write(passwd + '\n')


def get_count():
  with open(out_file) as f:
    line = f.readline()
  return int(line.split(' ')[1])

def guess_passwd(known):
  junk = chr(31) # use one non-printable char as padding
  array = []
  max_count = 0
  for j in range(32, 127):  # iterate all printable chars
    ch = chr(j)
    passwd = known + ch + junk * (passwd_len - len(known) - 1)
    call_pin(passwd)
    count = get_count()
    print 'trying: {}, count: {}'.format(passwd, count)
    if count == max_count:
      array.append(ch)
    elif count > max_count:
      array = []
      array.append(ch)
      max_count = count
  known_len = len(known)
  if len(array) > 1:
    print str(known_len) + " might be more than 1 possibility: " + ','.join(array)
    #      exit(-1)
  if known_len < passwd_len - 1:
    for i in array:
      guess_passwd(known + i)

def guess_length():
  max_count = 0
  array = []
  for i in range(1, passwd_len + 1):
    passwd = 'a' * i + '\n' #depends on how app read. If using fgets, MUST be '\n' at the end
    call_pin(passwd)
    count = get_count()
    print 'trying length: {}, count: {}'.format(i, count)
    if count == max_count:
      array.append(i)
    elif count > max_count:
      array = []
      array.append(i)
      max_count = count
  print 'password length should be:' , array

#call_pin('#/F&@(20')

if len(sys.argv) > 5:
  guess_length()
else:
  guess_passwd('')

result_file.close()
