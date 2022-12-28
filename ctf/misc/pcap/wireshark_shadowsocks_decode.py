#misc_chall-nctf-2019, http://ctf.njupt.edu.cn/298.html
#run in python3
import pyshark
from binascii import unhexlify
from shadowsocks.crypto.openssl import OpenSSLCrypto
from shadowsocks.encrypt import EVP_BytesToKey

streams = set()
decrypted_stream = set()

password, _ = EVP_BytesToKey(b'5e77b05530b30283e24c120d8cc13fb5', 32, 16)
server = '25565'
send = b''
recv = b''

def stream_callback(pkt):
    if hasattr(pkt, 'data'):
        streams.add(pkt.tcp.stream)

def decrypt_callback(pkt):
    global send
    global recv

    if hasattr(pkt, 'data'):
        if pkt.tcp.dstport == server:
            send += unhexlify(pkt.data.data)
        else:
            recv += unhexlify(pkt.data.data)

shark = pyshark.FileCapture('misc_chall.pcapng', display_filter="tcp.port == 25565 and ip.addr == 123.207.121.32")
shark.apply_on_packets(stream_callback)

print(streams)

for i in streams:
    send = b''
    recv = b''

    shark = pyshark.FileCapture('misc_chall.pcapng', display_filter=f"tcp.stream eq {i}")
    shark.apply_on_packets(decrypt_callback)

    decryptor = OpenSSLCrypto('aes-256-cfb', password, recv[:16], 0)
    data = decryptor.update(recv[16:])
    if b'NCTF' in data:
        print(data)