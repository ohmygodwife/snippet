#!/bin/sh
process_file(){
	for file in `ls -a $1`
	do
		if [ x"$file" != x"." -a x"$file" != x".." ];then
		 if [ -d "$1/$file" ];then
		 	process_file "$1/$file" $2 $3
		 else
		 	#You should backup your file
		 	if [ x"${file##*.}" = x"luac" ];then
		 	  ./lua_decrypt "$1/$file" "$1/$file" $2 $3
		 	fi
		 fi
		fi
	done
}
if [ $# != 3 ]; then
   echo "error..  example:\ndecode.sh srcdir sign key"
   exit 1
fi
process_file $1 $2 $3
