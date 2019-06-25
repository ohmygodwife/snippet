'''
https://www.usb.org/sites/default/files/documents/hut1_12v2.pdf
https://furutsuki.hatenablog.com/entry/2018/11/11/220733
tshark.exe -r usb1.pcap -T fields -e usb.capdata > usbdata.txt
tshark.exe -r usb2.pcap -T fields -e usb.capdata > usbdata.txt
'''
keymap = {  0x04: ('a','A'), 0x05: ('b','B'),0x06: ('c','C'),
        0x07: ('d','D'), 0x08: ('e','E'),0x09: ('f','F'),
        0x0a: ('g','G'), 0x0b: ('h','H'),0x0c: ('i','I'),
        0x0d: ('j','J'), 0x0e: ('k','K'),0x0f: ('l','L'),
        0x10: ('m','M'), 0x11: ('n','N'),0x12: ('o','O'),
        0x13: ('p','P'), 0x14: ('q','Q'),0x15: ('r','R'),
        0x16: ('s','S'), 0x17: ('t','T'),0x18: ('u','U'),
        0x19: ('v','V'), 0x1a: ('w','W'),0x1b: ('x','X'),
        0x1c: ('y','Y'), 0x1d: ('z','Z'),0x1e: ('1','!'),
        0x1f: ('2','@'), 0x20: ('3','#'),0x21: ('4','$'),
        0x22: ('5','%'), 0x23: ('6','^'),0x24: ('7','&'),
        0x25: ('8','*'), 0x26: ('9','('),0x27: ('0',')'),
        0x28: ('\n','\n'), 0x29: (' [esc] ',' [esc] '),
        0x2a: (' [del] ',' [del] '), 0x2b: ('\x09','\x09'),
        0x2c: ('\x20','\x20'), 0x2d: ('-','_'),
        0x2e: ('=','+'), 0x2f: ('[','{'),0x30: (']','}'),
        0x31: ('\\','|'), 0x32: (' [Non-US] ', ' [Non-US] '), 0x33: (';',':'),0x34: ('\'','\"'),
        0x35: ('`','~'), 0x36: (',','<'),0x37: ('.','>'),
        0x38: ('/','?'),
         57: 'Caps', 58: 'F1', 59: 'F2', 60: 'F3', 61: 'F4', 62: 'F5', 63: 'F6', 64: 'F7', 65: 'F8', 66: 'F9', 67: 'F10', 68: 'F11', 69: 'F12', 70: 'PrintScreen1', 71: 'Scroll', 72: 'Pause1', 73: 'Insert1', 74: 'Home1', 75: 'PageUp1', 76: 'Delete', 77: 'End1', 78: 'PageDown1', 79: 'RightArrow1', 80: 'LeftArrow1', 81: 'DownArrow1', 82: 'UpArrow1', 100: 'Non-US', 101: 'Application10', 102: 'Power9', 104: 'F13', 105: 'F14', 106: 'F15', 107: 'F16', 108: 'F17', 109: 'F18', 110: 'F19', 111: 'F20', 112: 'F21', 113: 'F22', 114: 'F23', 115: 'F24', 116: 'Execute', 117: 'Help', 118: 'Menu', 119: 'Select', 120: 'Stop', 121: 'Again', 122: 'Undo', 123: 'Cut', 124: 'Copy', 125: 'Paste', 126: 'Find', 127: 'Mute', 128: 'Volume', 129: 'Volume', 130: 'Locking', 131: 'Locking', 132: 'Locking', 135: 'International115,28', 136: 'International216', 137: 'International317', 138: 'International418', 139: 'International519', 140: 'International620', 141: 'International721', 142: 'International822', 143: 'International922', 144: 'LANG125', 145: 'LANG226', 146: 'LANG330', 147: 'LANG431', 148: 'LANG532', 149: 'LANG68', 150: 'LANG78', 151: 'LANG88', 152: 'LANG98', 153: 'Alternate', 154: 'SysReq/Attention1', 155: 'Cancel', 156: 'Clear', 157: 'Prior', 158: 'Return', 159: 'Separator', 160: 'Out', 161: 'Oper', 162: 'Clear/Again', 163: 'CrSel/Props', 164: 'ExSel'
        }

def analyze_usb_data(usb_data):
    flag = ""
    for d in usb_data:
        if d[2] == 0 or not(0 in d[3:8]):
            #No Event
            continue
        if d[0] == 0x02:
            #press shift
            flag += keymap[d[2]][1]
        elif d[0] == 0x00 or d[0] == 0x01:
            c = keymap[d[2]][0]
            if d[0] == 0x01:
              #press ctrl
              flag += ' [ctr] '
            flag += c
        else:
            print "ERROR: ", d[0]
    print flag

import collections
def main():
    data = list(map(lambda x: list(map(lambda y: int(y, 16), x.split(":"))), open("usbdata.txt").read().splitlines()))
    array = [ hex(line[2]) for line in data]
    print collections.Counter(array)
    analyze_usb_data(data)

if __name__ == '__main__':
    main()