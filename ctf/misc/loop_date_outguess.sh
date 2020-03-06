#genius_abc-anheng-200101
#!/bin/sh

cur=20140101
end=20151231
while [ $cur -le $end ]
do
  echo $cur
  outguess -r Ziggs.jpg -t flag.txt -k $cur
  grep "flag" flag.txt > /dev/null
  if [ $? -eq 0 ]; then
    echo "key is: $cur"
    exit
  fi
  cur=`date -d "+1 day $cur" +%Y%m%d`
done

