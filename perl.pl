fc
Casefolding is the process of mapping strings to a form where case differences are erased; comparing two strings in their casefolded form is effectively a way of asking if two strings are equal, regardless of case.

sort() returns aliases into the original list, much as a for loop's index variable aliases the list elements. That is, modifying an element of a list returned by sort() (for example, in a foreach , map or grep) actually modifies the element in the original list. This is usually something to be avoided when writing clear code.

use Data::Dumper;
print Dumper(\@arr);
print Dumper(\%hash);

#Perl lib version (5.10.0) doesn't match executable version (v5.16.3)
export PERL5LIB=/home/wzhzhou/software/ActivePerl-5.16/lib/

If the script is running as root you can change your UID and or EUID. There are special variables $< and $> that hold them. 

open (FILE, "<", $filename) or print "Error: $!\n";

$# 记录数组的下标最大值
$@ 记录eval捕获的错误


#check Perl module
perl -MDigest -e'print $_ . " => " . $INC{$_} . "\n" for keys %INC'

#check module version
perl -MDigest -e 'print $Digest::VERSION . "\n"';
perl -MLWP::Protocol::https -e 'print $LWP::Protocol::https::VERSION . "\n"';

#update cpan mirror
1. search available mirror from: http://mirrors.cpan.org/
2. perl -MCPAN -eshell
cpan[7]> o conf urllist push http://search.cpan.org/CPAN
Please use 'o conf commit' to make the config permanent!


cpan[8]> o conf commit
commit: wrote '/home/talai/.cpan/CPAN/MyConfig.pm'

cpan[8]> o conf urllist shift


#install module
(1) From span   (http://www.wanglianghome.org/blog/2006/01/install-perl-module-from-cpan.html)
perl -MCPAN -eshell
配置过程会询问一些问题，其中CPAN的镜像可以选择http://cpan.linuxforum.net/。
cpan> install Protocol::WebSocket
(2) From tar
tar -zxvf [module].tar.gz
perl Makefile.PL prefix=/scratch/talai/view_storage/talai_1226/perl/lib/site_perl/5.10.0 LIB=/scratch/talai/view_storage/talai_1226/perl/lib/site_perl/5.10.0 
make
make test
make install

# SSL support
1. Try::Tiny
2. Crypt-SSLeay