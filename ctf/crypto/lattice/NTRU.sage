from Crypto.Util.number import *
import gmpy2
 
h = 70851272226599856513658616506718804769182611213413854493145253337330709939355936692154199813179587933065165812259913249917314725765898812249062834111179900151466610356207921771928832591335738750053453046857602342378475278876652263044722419918958361163645152112020971804267503129035439011008349349624213734004
p = 125796773654949906956757901514929172896506715196511121353157781851652093811702246079116208920427110231653664239838444378725001877052652056537732732266407477191221775698956008368755461680533430353707546171814962217736494341129233572423073286387554056407408816555382448824610216634458550949715062229816683685469
c = 4691517945653877981376957637565364382959972087952249273292897076221178958350355396910942555879426136128610896883898318646711419768716904972164508407035668258209226498292327845169861395205212789741065517685193351416871631112431257858097798333893494180621728198734264288028849543413123321402664789239712408700

A=matrix([[1,h],[0,p]])
lll=A.LLL()
F,G=lll[0]
F,G=abs(F),abs(G)
 
M=F*c %p
m=gmpy2.invert(F,G)*M %G
 
print(long_to_bytes(m))