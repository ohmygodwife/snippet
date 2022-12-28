#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"xxtea.h"
int main(int argc,char*argv[]){
	FILE*fp;
	char*key;
	char*sign;
	char*infile;
	char*outfile;
	char*buf,*data;
	unsigned long size;
	int keylen,signlen,retlen;
	if(argc<5){
		printf("usage:lua_decrypt infile outfile sign key\n");
		return -1;
	}
	else{
		infile=argv[1];
		outfile=argv[2];
		sign=argv[3];
		key=argv[4];
		keylen=strlen(key);
		signlen=strlen(sign);
	}

	if((fp=fopen(infile,"rb"))==NULL){
			perror("can't open the input file");
			return -1;
	}
	fseek(fp, 0L, SEEK_END);
	size=ftell(fp);
	rewind(fp);
	buf=(char*)malloc(size);
	fread(buf,size,1,fp);
	fclose(fp);
	data=xxtea_decrypt(buf+signlen,size-signlen,key,keylen,&retlen);
	if(data==NULL){
		printf("%s decrypt fail\n",infile);
		return -1;
	}
	if((fp=fopen(outfile,"wb+"))==NULL){
		    perror("can't open the output file");
			return -1;
	}
	fwrite(data,retlen,1,fp);
	fclose(fp);
	free(data);
	printf("%s decrypt successful\n",infile);
	return 0;

}

	
