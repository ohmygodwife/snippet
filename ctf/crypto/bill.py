'''
with open('Bill.txt') as f:
  contents = f.read()
'''
contents = '''You can't spend any amount of time with Canadians, listen to them, actually hear them, and walk away thinking those feelings don't matter. < They matter a lot to me, and to our government.
 
The level of confidence that Canadians have in their economic future is important, especially when it comes to getting a new job, - making an offer on a house or buying a new car. _ As we celebrate our successes, we must also recognize that there are still many Canadians who are concerned about losing ground rather than getting ahead. > Budget 2017 is focused on people, what they need to feel confident about their future. It gives Canadians the tools they need to build a better life for themselves, for their children and for their grandchildren.'''

array = contents.split(' ')
print len(array)

keys = [34, 6, 13, 43, 68, 21, 43, 1, 77, 100, 6, 41, 5, 54, 68, 100, 3, 6, 13, 68, 41, 2, 34, 23, 56, 56, 56, 56, 56, 56, 56, 56, 5, 5, 23, 56, 34, 56, 94, 5, 5, 56, 56, 56, 56, 94, 5, 5, 56, 94, 34, 23, 56, 5, 5, 23, 56, 56, 56, 56, 5, 5, 23, 56, 34, 56, 94, 5, 5, 56, 56, 56, 56, 94, 5, 5, 56, 94, 34, 23, 56, 5, 5, 23, 56, 56, 56, 56, 56, 56, 23, 56, 34]

flag = ''
for i in keys:
    flag += array[i][0]
    
print flag
'''
the_decrption_path_is
<--------oo<- (start)
->oo---->oo->
<-oo<----oo<-
->oo---->oo->
<-oo<------<-

lf1e7f05}ba83909764e2686e{7a7fsi_galfagb8d004

flag_isfl
ag{7a7f1e
8be6862f7
d09764e05
400938ab}
'''
