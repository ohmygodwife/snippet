#Press F5 to run
# -*- coding: UTF-8 -*-
import frida,sys

js_code = '''
Java.perform(function(){
  var check = Java.use("com.example.test.ctf02.Check");
  check.checkPassword.implementation = function(arg1){
    var obj = check.$new();
    //obj.attribute.value = "hello"; //get/set value
    console.log("hook arg1:",arg1);
    send(arguments[0]);
    return true; //this.checkPassword(arg1), call the origial implementation
  }
  
  check.$init.implementation = function() {} // construction
  
//  check.fun1.overload("int", "java.lang.String", "com.example.test.ctf02.Check").implementation = function() {}
});
'''

appPacknName = "com.example.test.ctf02"

def on_message(message, data):
  if message['type'] == 'send':
    print("[*] {0}".format(message['payload']))
  else:
    print(message)

#https://blog.csdn.net/u014139511/article/details/127063795
#set port as 12345 instead of the default 27042/27043
host = '127.0.0.1:12345'
manager = frida.get_device_manager() #instead of get_remote_device() which use the default port
device= manager.add_remote_device(host)
# spawn
pid = device.spawn([appPacknName])
session = device.attach(pid)
#https://www.jianshu.com/p/b833fba1bffe
device.resume(pid)

script = session.create_script(js_code)
script.on('message', on_message)
script.load()
sys.stdin.read()
