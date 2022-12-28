import pyshark
import binascii
def flag():
    try:
        captures = pyshark.FileCapture("tmflag.pcapng")
        flag_frsm = False
        flag_frsm_id = None
        flag_read = False
        for capture in captures:
            for pkt in capture:
                if pkt.layer_name == "mms":
                    # file open
                    if hasattr(pkt, "confirmedservicerequest") and int(pkt.confirmedservicerequest) == 72:
                        if hasattr(pkt, "filename_item"):
                            filename_items = pkt.filename_item.fields
                            for f in filename_items:
                                file_name = str(f.get_default_value())
                                if file_name == "flag.7z":
                                    flag_frsm = True
                    if hasattr(pkt, "confirmedserviceresponse") and int(pkt.confirmedserviceresponse) == 72 and flag_frsm:
                        if hasattr(pkt, "frsmid"):
                            flag_frsm_id = pkt.frsmid
                        flag_frsm = False
                    if hasattr(pkt, "confirmedservicerequest") and int(pkt.confirmedservicerequest) == 73 and flag_frsm_id:
                        if hasattr(pkt, "fileread"):
                            if str(pkt.fileread) == str(flag_frsm_id):
                                flag_read = True
                        flag_frsm_id = None
                    if hasattr(pkt, "confirmedserviceresponse") and int(pkt.confirmedserviceresponse) == 73 and flag_read:
                        if hasattr(pkt, "filedata"):
                            data = str(pkt.filedata).replace(":", "")
                            hex2char(data)
                        flag_read = False
    except Exception as e:
        print(e)


def hex2char(data):
#    binascii.a2b_hex(hexstr) 
    output = binascii.unhexlify(data)
    print(output)

if __name__ == '__main__':
flag()