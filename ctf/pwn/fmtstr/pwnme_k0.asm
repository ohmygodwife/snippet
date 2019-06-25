
pwnme_k0:     file format elf64-x86-64


Disassembly of section .init:

0000000000400708 <.init>:
  400708:	48 83 ec 08          	sub    $0x8,%rsp
  40070c:	48 8b 05 cd 18 20 00 	mov    0x2018cd(%rip),%rax        # 601fe0 <atol@plt+0x201838>
  400713:	48 85 c0             	test   %rax,%rax
  400716:	74 05                	je     40071d <putchar@plt-0x23>
  400718:	e8 73 00 00 00       	callq  400790 <__gmon_start__@plt>
  40071d:	48 83 c4 08          	add    $0x8,%rsp
  400721:	c3                   	retq   

Disassembly of section .plt:

0000000000400730 <.plt>:
  400730:	ff 35 4a 18 20 00    	pushq  0x20184a(%rip)        # 601f80 <atol@plt+0x2017d8>
  400736:	ff 25 4c 18 20 00    	jmpq   *0x20184c(%rip)        # 601f88 <atol@plt+0x2017e0>
  40073c:	0f 1f 40 00          	nopl   0x0(%rax)

Disassembly of section .plt.got:

0000000000400740 <putchar@plt>:
  400740:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601f90 <atol@plt+0x2017e8>
  400746:	66 90                	xchg   %ax,%ax

0000000000400748 <strcpy@plt>:
  400748:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601f98 <atol@plt+0x2017f0>
  40074e:	66 90                	xchg   %ax,%ax

0000000000400750 <puts@plt>:
  400750:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fa0 <atol@plt+0x2017f8>
  400756:	66 90                	xchg   %ax,%ax

0000000000400758 <write@plt>:
  400758:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fa8 <atol@plt+0x201800>
  40075e:	66 90                	xchg   %ax,%ax

0000000000400760 <setbuf@plt>:
  400760:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fb0 <atol@plt+0x201808>
  400766:	66 90                	xchg   %ax,%ax

0000000000400768 <system@plt>:
  400768:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fb8 <atol@plt+0x201810>
  40076e:	66 90                	xchg   %ax,%ax

0000000000400770 <printf@plt>:
  400770:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fc0 <atol@plt+0x201818>
  400776:	66 90                	xchg   %ax,%ax

0000000000400778 <memset@plt>:
  400778:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fc8 <atol@plt+0x201820>
  40077e:	66 90                	xchg   %ax,%ax

0000000000400780 <read@plt>:
  400780:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fd0 <atol@plt+0x201828>
  400786:	66 90                	xchg   %ax,%ax

0000000000400788 <__libc_start_main@plt>:
  400788:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fd8 <atol@plt+0x201830>
  40078e:	66 90                	xchg   %ax,%ax

0000000000400790 <__gmon_start__@plt>:
  400790:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fe0 <atol@plt+0x201838>
  400796:	66 90                	xchg   %ax,%ax

0000000000400798 <memcpy@plt>:
  400798:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601fe8 <atol@plt+0x201840>
  40079e:	66 90                	xchg   %ax,%ax

00000000004007a0 <fflush@plt>:
  4007a0:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601ff0 <atol@plt+0x201848>
  4007a6:	66 90                	xchg   %ax,%ax

00000000004007a8 <atol@plt>:
  4007a8:	ff 25 4a 18 20 00    	jmpq   *0x20184a(%rip)        # 601ff8 <atol@plt+0x201850>
  4007ae:	66 90                	xchg   %ax,%ax

Disassembly of section .text:

00000000004007b0 <.text>:
  4007b0:	31 ed                	xor    %ebp,%ebp
  4007b2:	49 89 d1             	mov    %rdx,%r9
  4007b5:	5e                   	pop    %rsi
  4007b6:	48 89 e2             	mov    %rsp,%rdx
  4007b9:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  4007bd:	50                   	push   %rax
  4007be:	54                   	push   %rsp
  4007bf:	49 c7 c0 20 0f 40 00 	mov    $0x400f20,%r8
  4007c6:	48 c7 c1 b0 0e 40 00 	mov    $0x400eb0,%rcx
  4007cd:	48 c7 c7 d8 0d 40 00 	mov    $0x400dd8,%rdi
  4007d4:	e8 af ff ff ff       	callq  400788 <__libc_start_main@plt>
  4007d9:	f4                   	hlt    
  4007da:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  4007e0:	b8 17 20 60 00       	mov    $0x602017,%eax
  4007e5:	55                   	push   %rbp
  4007e6:	48 2d 10 20 60 00    	sub    $0x602010,%rax
  4007ec:	48 83 f8 0e          	cmp    $0xe,%rax
  4007f0:	48 89 e5             	mov    %rsp,%rbp
  4007f3:	76 1b                	jbe    400810 <atol@plt+0x68>
  4007f5:	b8 00 00 00 00       	mov    $0x0,%eax
  4007fa:	48 85 c0             	test   %rax,%rax
  4007fd:	74 11                	je     400810 <atol@plt+0x68>
  4007ff:	5d                   	pop    %rbp
  400800:	bf 10 20 60 00       	mov    $0x602010,%edi
  400805:	ff e0                	jmpq   *%rax
  400807:	66 0f 1f 84 00 00 00 	nopw   0x0(%rax,%rax,1)
  40080e:	00 00 
  400810:	5d                   	pop    %rbp
  400811:	c3                   	retq   
  400812:	0f 1f 40 00          	nopl   0x0(%rax)
  400816:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40081d:	00 00 00 
  400820:	be 10 20 60 00       	mov    $0x602010,%esi
  400825:	55                   	push   %rbp
  400826:	48 81 ee 10 20 60 00 	sub    $0x602010,%rsi
  40082d:	48 c1 fe 03          	sar    $0x3,%rsi
  400831:	48 89 e5             	mov    %rsp,%rbp
  400834:	48 89 f0             	mov    %rsi,%rax
  400837:	48 c1 e8 3f          	shr    $0x3f,%rax
  40083b:	48 01 c6             	add    %rax,%rsi
  40083e:	48 d1 fe             	sar    %rsi
  400841:	74 15                	je     400858 <atol@plt+0xb0>
  400843:	b8 00 00 00 00       	mov    $0x0,%eax
  400848:	48 85 c0             	test   %rax,%rax
  40084b:	74 0b                	je     400858 <atol@plt+0xb0>
  40084d:	5d                   	pop    %rbp
  40084e:	bf 10 20 60 00       	mov    $0x602010,%edi
  400853:	ff e0                	jmpq   *%rax
  400855:	0f 1f 00             	nopl   (%rax)
  400858:	5d                   	pop    %rbp
  400859:	c3                   	retq   
  40085a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)
  400860:	80 3d c1 17 20 00 00 	cmpb   $0x0,0x2017c1(%rip)        # 602028 <stdin@@GLIBC_2.2.5+0x8>
  400867:	75 11                	jne    40087a <atol@plt+0xd2>
  400869:	55                   	push   %rbp
  40086a:	48 89 e5             	mov    %rsp,%rbp
  40086d:	e8 6e ff ff ff       	callq  4007e0 <atol@plt+0x38>
  400872:	5d                   	pop    %rbp
  400873:	c6 05 ae 17 20 00 01 	movb   $0x1,0x2017ae(%rip)        # 602028 <stdin@@GLIBC_2.2.5+0x8>
  40087a:	f3 c3                	repz retq 
  40087c:	0f 1f 40 00          	nopl   0x0(%rax)
  400880:	bf b0 1d 60 00       	mov    $0x601db0,%edi
  400885:	48 83 3f 00          	cmpq   $0x0,(%rdi)
  400889:	75 05                	jne    400890 <atol@plt+0xe8>
  40088b:	eb 93                	jmp    400820 <atol@plt+0x78>
  40088d:	0f 1f 00             	nopl   (%rax)
  400890:	b8 00 00 00 00       	mov    $0x0,%eax
  400895:	48 85 c0             	test   %rax,%rax
  400898:	74 f1                	je     40088b <atol@plt+0xe3>
  40089a:	55                   	push   %rbp
  40089b:	48 89 e5             	mov    %rsp,%rbp
  40089e:	ff d0                	callq  *%rax
  4008a0:	5d                   	pop    %rbp
  4008a1:	e9 7a ff ff ff       	jmpq   400820 <atol@plt+0x78>
  4008a6:	55                   	push   %rbp
  4008a7:	48 89 e5             	mov    %rsp,%rbp
  4008aa:	bf 38 0f 40 00       	mov    $0x400f38,%edi
  4008af:	e8 b4 fe ff ff       	callq  400768 <system@plt>
  4008b4:	5f                   	pop    %rdi
  4008b5:	5e                   	pop    %rsi
  4008b6:	5a                   	pop    %rdx
  4008b7:	c3                   	retq   
  4008b8:	90                   	nop
  4008b9:	5d                   	pop    %rbp
  4008ba:	c3                   	retq   
  4008bb:	55                   	push   %rbp
  4008bc:	48 89 e5             	mov    %rsp,%rbp
  4008bf:	bf 40 0f 40 00       	mov    $0x400f40,%edi
  4008c4:	e8 87 fe ff ff       	callq  400750 <puts@plt>
  4008c9:	bf 70 0f 40 00       	mov    $0x400f70,%edi
  4008ce:	e8 7d fe ff ff       	callq  400750 <puts@plt>
  4008d3:	bf a0 0f 40 00       	mov    $0x400fa0,%edi
  4008d8:	e8 73 fe ff ff       	callq  400750 <puts@plt>
  4008dd:	bf 70 0f 40 00       	mov    $0x400f70,%edi
  4008e2:	e8 69 fe ff ff       	callq  400750 <puts@plt>
  4008e7:	bf 40 0f 40 00       	mov    $0x400f40,%edi
  4008ec:	e8 5f fe ff ff       	callq  400750 <puts@plt>
  4008f1:	48 8b 05 18 17 20 00 	mov    0x201718(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  4008f8:	48 89 c7             	mov    %rax,%rdi
  4008fb:	e8 a0 fe ff ff       	callq  4007a0 <fflush@plt>
  400900:	90                   	nop
  400901:	5d                   	pop    %rbp
  400902:	c3                   	retq   
  400903:	55                   	push   %rbp
  400904:	48 89 e5             	mov    %rsp,%rbp
  400907:	48 83 ec 20          	sub    $0x20,%rsp
  40090b:	48 89 7d e8          	mov    %rdi,-0x18(%rbp)
  40090f:	bf cf 0f 40 00       	mov    $0x400fcf,%edi
  400914:	e8 37 fe ff ff       	callq  400750 <puts@plt>
  400919:	bf e8 0f 40 00       	mov    $0x400fe8,%edi
  40091e:	e8 2d fe ff ff       	callq  400750 <puts@plt>
  400923:	48 8b 05 e6 16 20 00 	mov    0x2016e6(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  40092a:	48 89 c7             	mov    %rax,%rdi
  40092d:	e8 6e fe ff ff       	callq  4007a0 <fflush@plt>
  400932:	ba 14 00 00 00       	mov    $0x14,%edx
  400937:	48 8d 75 10          	lea    0x10(%rbp),%rsi
  40093b:	bf 00 00 00 00       	mov    $0x0,%edi
  400940:	e8 3b fe ff ff       	callq  400780 <read@plt>
  400945:	88 45 ff             	mov    %al,-0x1(%rbp)
  400948:	80 7d ff 00          	cmpb   $0x0,-0x1(%rbp)
  40094c:	74 06                	je     400954 <atol@plt+0x1ac>
  40094e:	80 7d ff 14          	cmpb   $0x14,-0x1(%rbp)
  400952:	76 53                	jbe    4009a7 <atol@plt+0x1ff>
  400954:	0f b6 05 b1 06 00 00 	movzbl 0x6b1(%rip),%eax        # 40100c <atol@plt+0x864>
  40095b:	88 45 10             	mov    %al,0x10(%rbp)
  40095e:	bf 10 10 40 00       	mov    $0x401010,%edi
  400963:	e8 e8 fd ff ff       	callq  400750 <puts@plt>
  400968:	48 8b 05 a1 16 20 00 	mov    0x2016a1(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  40096f:	48 89 c7             	mov    %rax,%rdi
  400972:	e8 29 fe ff ff       	callq  4007a0 <fflush@plt>
  400977:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  40097b:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  40097f:	48 89 10             	mov    %rdx,(%rax)
  400982:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400986:	48 89 50 08          	mov    %rdx,0x8(%rax)
  40098a:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  40098e:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400992:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400996:	48 89 50 18          	mov    %rdx,0x18(%rax)
  40099a:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  40099e:	48 89 50 20          	mov    %rdx,0x20(%rax)
  4009a2:	e9 c8 00 00 00       	jmpq   400a6f <atol@plt+0x2c7>
  4009a7:	bf 30 10 40 00       	mov    $0x401030,%edi
  4009ac:	e8 9f fd ff ff       	callq  400750 <puts@plt>
  4009b1:	48 8b 05 58 16 20 00 	mov    0x201658(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  4009b8:	48 89 c7             	mov    %rax,%rdi
  4009bb:	e8 e0 fd ff ff       	callq  4007a0 <fflush@plt>
  4009c0:	48 8d 45 24          	lea    0x24(%rbp),%rax
  4009c4:	ba 14 00 00 00       	mov    $0x14,%edx
  4009c9:	48 89 c6             	mov    %rax,%rsi
  4009cc:	bf 00 00 00 00       	mov    $0x0,%edi
  4009d1:	e8 aa fd ff ff       	callq  400780 <read@plt>
  4009d6:	88 45 fe             	mov    %al,-0x2(%rbp)
  4009d9:	80 7d fe 00          	cmpb   $0x0,-0x2(%rbp)
  4009dd:	75 56                	jne    400a35 <atol@plt+0x28d>
  4009df:	80 7d fe 14          	cmpb   $0x14,-0x2(%rbp)
  4009e3:	76 50                	jbe    400a35 <atol@plt+0x28d>
  4009e5:	0f b6 05 20 06 00 00 	movzbl 0x620(%rip),%eax        # 40100c <atol@plt+0x864>
  4009ec:	88 45 10             	mov    %al,0x10(%rbp)
  4009ef:	bf 58 10 40 00       	mov    $0x401058,%edi
  4009f4:	e8 57 fd ff ff       	callq  400750 <puts@plt>
  4009f9:	48 8b 05 10 16 20 00 	mov    0x201610(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400a00:	48 89 c7             	mov    %rax,%rdi
  400a03:	e8 98 fd ff ff       	callq  4007a0 <fflush@plt>
  400a08:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  400a0c:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  400a10:	48 89 10             	mov    %rdx,(%rax)
  400a13:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400a17:	48 89 50 08          	mov    %rdx,0x8(%rax)
  400a1b:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  400a1f:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400a23:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400a27:	48 89 50 18          	mov    %rdx,0x18(%rax)
  400a2b:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  400a2f:	48 89 50 20          	mov    %rdx,0x20(%rax)
  400a33:	eb 3a                	jmp    400a6f <atol@plt+0x2c7>
  400a35:	48 8b 05 d4 15 20 00 	mov    0x2015d4(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400a3c:	48 89 c7             	mov    %rax,%rdi
  400a3f:	e8 5c fd ff ff       	callq  4007a0 <fflush@plt>
  400a44:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  400a48:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  400a4c:	48 89 10             	mov    %rdx,(%rax)
  400a4f:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400a53:	48 89 50 08          	mov    %rdx,0x8(%rax)
  400a57:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  400a5b:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400a5f:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400a63:	48 89 50 18          	mov    %rdx,0x18(%rax)
  400a67:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  400a6b:	48 89 50 20          	mov    %rdx,0x20(%rax)
  400a6f:	48 8b 45 e8          	mov    -0x18(%rbp),%rax
  400a73:	c9                   	leaveq 
  400a74:	c3                   	retq   
  400a75:	55                   	push   %rbp
  400a76:	48 89 e5             	mov    %rsp,%rbp
  400a79:	48 83 ec 10          	sub    $0x10,%rsp
  400a7d:	c7 45 f8 00 00 00 00 	movl   $0x0,-0x8(%rbp)
  400a84:	bf 78 10 40 00       	mov    $0x401078,%edi
  400a89:	e8 c2 fc ff ff       	callq  400750 <puts@plt>
  400a8e:	bf 93 10 40 00       	mov    $0x401093,%edi
  400a93:	e8 b8 fc ff ff       	callq  400750 <puts@plt>
  400a98:	bf ae 10 40 00       	mov    $0x4010ae,%edi
  400a9d:	e8 ae fc ff ff       	callq  400750 <puts@plt>
  400aa2:	bf 3e 00 00 00       	mov    $0x3e,%edi
  400aa7:	e8 94 fc ff ff       	callq  400740 <putchar@plt>
  400aac:	48 8b 05 5d 15 20 00 	mov    0x20155d(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400ab3:	48 89 c7             	mov    %rax,%rdi
  400ab6:	e8 e5 fc ff ff       	callq  4007a0 <fflush@plt>
  400abb:	48 8d 45 f8          	lea    -0x8(%rbp),%rax
  400abf:	ba 05 00 00 00       	mov    $0x5,%edx
  400ac4:	48 89 c6             	mov    %rax,%rsi
  400ac7:	bf 00 00 00 00       	mov    $0x0,%edi
  400acc:	e8 af fc ff ff       	callq  400780 <read@plt>
  400ad1:	48 8d 45 f8          	lea    -0x8(%rbp),%rax
  400ad5:	48 89 c7             	mov    %rax,%rdi
  400ad8:	e8 cb fc ff ff       	callq  4007a8 <atol@plt>
  400add:	89 45 fc             	mov    %eax,-0x4(%rbp)
  400ae0:	8b 45 fc             	mov    -0x4(%rbp),%eax
  400ae3:	c9                   	leaveq 
  400ae4:	c3                   	retq   
  400ae5:	55                   	push   %rbp
  400ae6:	48 89 e5             	mov    %rsp,%rbp
  400ae9:	48 83 ec 30          	sub    $0x30,%rsp
  400aed:	48 89 7d d8          	mov    %rdi,-0x28(%rbp)
  400af1:	48 8b 55 d8          	mov    -0x28(%rbp),%rdx
  400af5:	48 8d 45 e0          	lea    -0x20(%rbp),%rax
  400af9:	48 89 d6             	mov    %rdx,%rsi
  400afc:	48 89 c7             	mov    %rax,%rdi
  400aff:	e8 44 fc ff ff       	callq  400748 <strcpy@plt>
  400b04:	90                   	nop
  400b05:	c9                   	leaveq 
  400b06:	c3                   	retq   
  400b07:	55                   	push   %rbp
  400b08:	48 89 e5             	mov    %rsp,%rbp
  400b0b:	ba 1a 00 00 00       	mov    $0x1a,%edx
  400b10:	be c3 10 40 00       	mov    $0x4010c3,%esi
  400b15:	bf 00 00 00 00       	mov    $0x0,%edi
  400b1a:	e8 39 fc ff ff       	callq  400758 <write@plt>
  400b1f:	48 8d 7d 10          	lea    0x10(%rbp),%rdi
  400b23:	b8 00 00 00 00       	mov    $0x0,%eax
  400b28:	e8 43 fc ff ff       	callq  400770 <printf@plt>
  400b2d:	48 8d 45 24          	lea    0x24(%rbp),%rax
  400b31:	48 89 c7             	mov    %rax,%rdi
  400b34:	b8 00 00 00 00       	mov    $0x0,%eax
  400b39:	e8 32 fc ff ff       	callq  400770 <printf@plt>
  400b3e:	90                   	nop
  400b3f:	5d                   	pop    %rbp
  400b40:	c3                   	retq   
  400b41:	55                   	push   %rbp
  400b42:	48 89 e5             	mov    %rsp,%rbp
  400b45:	48 81 ec 70 02 00 00 	sub    $0x270,%rsp
  400b4c:	48 89 bd 98 fd ff ff 	mov    %rdi,-0x268(%rbp)
  400b53:	bf e0 10 40 00       	mov    $0x4010e0,%edi
  400b58:	e8 f3 fb ff ff       	callq  400750 <puts@plt>
  400b5d:	48 8b 05 ac 14 20 00 	mov    0x2014ac(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400b64:	48 89 c7             	mov    %rax,%rdi
  400b67:	e8 34 fc ff ff       	callq  4007a0 <fflush@plt>
  400b6c:	48 8d 85 a0 fd ff ff 	lea    -0x260(%rbp),%rax
  400b73:	ba 2c 01 00 00       	mov    $0x12c,%edx
  400b78:	48 89 c6             	mov    %rax,%rsi
  400b7b:	bf 00 00 00 00       	mov    $0x0,%edi
  400b80:	e8 fb fb ff ff       	callq  400780 <read@plt>
  400b85:	88 45 ff             	mov    %al,-0x1(%rbp)
  400b88:	80 7d ff 00          	cmpb   $0x0,-0x1(%rbp)
  400b8c:	7e 6c                	jle    400bfa <atol@plt+0x452>
  400b8e:	80 7d ff 14          	cmpb   $0x14,-0x1(%rbp)
  400b92:	7f 66                	jg     400bfa <atol@plt+0x452>
  400b94:	ba 14 00 00 00       	mov    $0x14,%edx
  400b99:	be 00 00 00 00       	mov    $0x0,%esi
  400b9e:	48 8d 7d 10          	lea    0x10(%rbp),%rdi
  400ba2:	e8 d1 fb ff ff       	callq  400778 <memset@plt>
  400ba7:	48 8d 85 a0 fd ff ff 	lea    -0x260(%rbp),%rax
  400bae:	48 89 c6             	mov    %rax,%rsi
  400bb1:	48 8d 7d 10          	lea    0x10(%rbp),%rdi
  400bb5:	e8 8e fb ff ff       	callq  400748 <strcpy@plt>
  400bba:	bf 10 11 40 00       	mov    $0x401110,%edi
  400bbf:	e8 8c fb ff ff       	callq  400750 <puts@plt>
  400bc4:	48 8b 05 45 14 20 00 	mov    0x201445(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400bcb:	48 89 c7             	mov    %rax,%rdi
  400bce:	e8 cd fb ff ff       	callq  4007a0 <fflush@plt>
  400bd3:	48 8d 85 d0 fe ff ff 	lea    -0x130(%rbp),%rax
  400bda:	ba 2c 01 00 00       	mov    $0x12c,%edx
  400bdf:	48 89 c6             	mov    %rax,%rsi
  400be2:	bf 00 00 00 00       	mov    $0x0,%edi
  400be7:	e8 94 fb ff ff       	callq  400780 <read@plt>
  400bec:	88 45 fe             	mov    %al,-0x2(%rbp)
  400bef:	80 7d fe 00          	cmpb   $0x0,-0x2(%rbp)
  400bf3:	75 51                	jne    400c46 <atol@plt+0x49e>
  400bf5:	e9 d0 00 00 00       	jmpq   400cca <atol@plt+0x522>
  400bfa:	bf 40 11 40 00       	mov    $0x401140,%edi
  400bff:	e8 4c fb ff ff       	callq  400750 <puts@plt>
  400c04:	48 8b 05 05 14 20 00 	mov    0x201405(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400c0b:	48 89 c7             	mov    %rax,%rdi
  400c0e:	e8 8d fb ff ff       	callq  4007a0 <fflush@plt>
  400c13:	48 8b 85 98 fd ff ff 	mov    -0x268(%rbp),%rax
  400c1a:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  400c1e:	48 89 10             	mov    %rdx,(%rax)
  400c21:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400c25:	48 89 50 08          	mov    %rdx,0x8(%rax)
  400c29:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  400c2d:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400c31:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400c35:	48 89 50 18          	mov    %rdx,0x18(%rax)
  400c39:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  400c3d:	48 89 50 20          	mov    %rdx,0x20(%rax)
  400c41:	e9 cb 00 00 00       	jmpq   400d11 <atol@plt+0x569>
  400c46:	80 7d fe 14          	cmpb   $0x14,-0x2(%rbp)
  400c4a:	77 7e                	ja     400cca <atol@plt+0x522>
  400c4c:	48 8d 45 24          	lea    0x24(%rbp),%rax
  400c50:	ba 14 00 00 00       	mov    $0x14,%edx
  400c55:	be 00 00 00 00       	mov    $0x0,%esi
  400c5a:	48 89 c7             	mov    %rax,%rdi
  400c5d:	e8 16 fb ff ff       	callq  400778 <memset@plt>
  400c62:	48 8d 85 d0 fe ff ff 	lea    -0x130(%rbp),%rax
  400c69:	48 89 c7             	mov    %rax,%rdi
  400c6c:	e8 74 fe ff ff       	callq  400ae5 <atol@plt+0x33d>
  400c71:	0f b6 55 fe          	movzbl -0x2(%rbp),%edx
  400c75:	48 8d 8d d0 fe ff ff 	lea    -0x130(%rbp),%rcx
  400c7c:	48 8d 45 24          	lea    0x24(%rbp),%rax
  400c80:	48 89 ce             	mov    %rcx,%rsi
  400c83:	48 89 c7             	mov    %rax,%rdi
  400c86:	e8 0d fb ff ff       	callq  400798 <memcpy@plt>
  400c8b:	48 8b 05 7e 13 20 00 	mov    0x20137e(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400c92:	48 89 c7             	mov    %rax,%rdi
  400c95:	e8 06 fb ff ff       	callq  4007a0 <fflush@plt>
  400c9a:	48 8b 85 98 fd ff ff 	mov    -0x268(%rbp),%rax
  400ca1:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  400ca5:	48 89 10             	mov    %rdx,(%rax)
  400ca8:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400cac:	48 89 50 08          	mov    %rdx,0x8(%rax)
  400cb0:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  400cb4:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400cb8:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400cbc:	48 89 50 18          	mov    %rdx,0x18(%rax)
  400cc0:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  400cc4:	48 89 50 20          	mov    %rdx,0x20(%rax)
  400cc8:	eb 47                	jmp    400d11 <atol@plt+0x569>
  400cca:	bf 68 11 40 00       	mov    $0x401168,%edi
  400ccf:	e8 7c fa ff ff       	callq  400750 <puts@plt>
  400cd4:	48 8b 05 35 13 20 00 	mov    0x201335(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400cdb:	48 89 c7             	mov    %rax,%rdi
  400cde:	e8 bd fa ff ff       	callq  4007a0 <fflush@plt>
  400ce3:	48 8b 85 98 fd ff ff 	mov    -0x268(%rbp),%rax
  400cea:	48 8b 55 10          	mov    0x10(%rbp),%rdx
  400cee:	48 89 10             	mov    %rdx,(%rax)
  400cf1:	48 8b 55 18          	mov    0x18(%rbp),%rdx
  400cf5:	48 89 50 08          	mov    %rdx,0x8(%rax)
  400cf9:	48 8b 55 20          	mov    0x20(%rbp),%rdx
  400cfd:	48 89 50 10          	mov    %rdx,0x10(%rax)
  400d01:	48 8b 55 28          	mov    0x28(%rbp),%rdx
  400d05:	48 89 50 18          	mov    %rdx,0x18(%rax)
  400d09:	48 8b 55 30          	mov    0x30(%rbp),%rdx
  400d0d:	48 89 50 20          	mov    %rdx,0x20(%rax)
  400d11:	48 8b 85 98 fd ff ff 	mov    -0x268(%rbp),%rax
  400d18:	c9                   	leaveq 
  400d19:	c3                   	retq   
  400d1a:	55                   	push   %rbp
  400d1b:	48 89 e5             	mov    %rsp,%rbp
  400d1e:	bf 8c 11 40 00       	mov    $0x40118c,%edi
  400d23:	e8 28 fa ff ff       	callq  400750 <puts@plt>
  400d28:	90                   	nop
  400d29:	5d                   	pop    %rbp
  400d2a:	c3                   	retq   
  400d2b:	55                   	push   %rbp
  400d2c:	48 89 e5             	mov    %rsp,%rbp
  400d2f:	48 8b 05 ea 12 20 00 	mov    0x2012ea(%rip),%rax        # 602020 <stdin@@GLIBC_2.2.5>
  400d36:	be 00 00 00 00       	mov    $0x0,%esi
  400d3b:	48 89 c7             	mov    %rax,%rdi
  400d3e:	e8 1d fa ff ff       	callq  400760 <setbuf@plt>
  400d43:	b8 00 00 00 00       	mov    $0x0,%eax
  400d48:	e8 28 fd ff ff       	callq  400a75 <atol@plt+0x2cd>
  400d4d:	83 f8 02             	cmp    $0x2,%eax
  400d50:	74 28                	je     400d7a <atol@plt+0x5d2>
  400d52:	83 f8 03             	cmp    $0x3,%eax
  400d55:	74 45                	je     400d9c <atol@plt+0x5f4>
  400d57:	83 f8 01             	cmp    $0x1,%eax
  400d5a:	75 4c                	jne    400da8 <atol@plt+0x600>
  400d5c:	48 83 ec 08          	sub    $0x8,%rsp
  400d60:	ff 75 30             	pushq  0x30(%rbp)
  400d63:	ff 75 28             	pushq  0x28(%rbp)
  400d66:	ff 75 20             	pushq  0x20(%rbp)
  400d69:	ff 75 18             	pushq  0x18(%rbp)
  400d6c:	ff 75 10             	pushq  0x10(%rbp)
  400d6f:	e8 93 fd ff ff       	callq  400b07 <atol@plt+0x35f>
  400d74:	48 83 c4 30          	add    $0x30,%rsp
  400d78:	eb 48                	jmp    400dc2 <atol@plt+0x61a>
  400d7a:	48 83 ec 08          	sub    $0x8,%rsp
  400d7e:	ff 75 30             	pushq  0x30(%rbp)
  400d81:	ff 75 28             	pushq  0x28(%rbp)
  400d84:	ff 75 20             	pushq  0x20(%rbp)
  400d87:	ff 75 18             	pushq  0x18(%rbp)
  400d8a:	ff 75 10             	pushq  0x10(%rbp)
  400d8d:	48 8d 7d 10          	lea    0x10(%rbp),%rdi
  400d91:	e8 ab fd ff ff       	callq  400b41 <atol@plt+0x399>
  400d96:	48 83 c4 30          	add    $0x30,%rsp
  400d9a:	eb 26                	jmp    400dc2 <atol@plt+0x61a>
  400d9c:	b8 00 00 00 00       	mov    $0x0,%eax
  400da1:	e8 74 ff ff ff       	callq  400d1a <atol@plt+0x572>
  400da6:	eb 2e                	jmp    400dd6 <atol@plt+0x62e>
  400da8:	bf 96 11 40 00       	mov    $0x401196,%edi
  400dad:	e8 9e f9 ff ff       	callq  400750 <puts@plt>
  400db2:	48 8b 05 57 12 20 00 	mov    0x201257(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400db9:	48 89 c7             	mov    %rax,%rdi
  400dbc:	e8 df f9 ff ff       	callq  4007a0 <fflush@plt>
  400dc1:	90                   	nop
  400dc2:	48 8b 05 47 12 20 00 	mov    0x201247(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400dc9:	48 89 c7             	mov    %rax,%rdi
  400dcc:	e8 cf f9 ff ff       	callq  4007a0 <fflush@plt>
  400dd1:	e9 6d ff ff ff       	jmpq   400d43 <atol@plt+0x59b>
  400dd6:	c9                   	leaveq 
  400dd7:	c3                   	retq   
  400dd8:	55                   	push   %rbp
  400dd9:	48 89 e5             	mov    %rsp,%rbp
  400ddc:	48 83 ec 70          	sub    $0x70,%rsp
  400de0:	89 7d 9c             	mov    %edi,-0x64(%rbp)
  400de3:	48 89 75 90          	mov    %rsi,-0x70(%rbp)
  400de7:	48 c7 45 d0 30 00 00 	movq   $0x30,-0x30(%rbp)
  400dee:	00 
  400def:	48 c7 45 d8 00 00 00 	movq   $0x0,-0x28(%rbp)
  400df6:	00 
  400df7:	c7 45 e0 00 00 00 00 	movl   $0x0,-0x20(%rbp)
  400dfe:	48 c7 45 e4 30 00 00 	movq   $0x30,-0x1c(%rbp)
  400e05:	00 
  400e06:	48 c7 45 ec 00 00 00 	movq   $0x0,-0x14(%rbp)
  400e0d:	00 
  400e0e:	c7 45 f4 00 00 00 00 	movl   $0x0,-0xc(%rbp)
  400e15:	b8 00 00 00 00       	mov    $0x0,%eax
  400e1a:	e8 9c fa ff ff       	callq  4008bb <atol@plt+0x113>
  400e1f:	48 8d 45 a0          	lea    -0x60(%rbp),%rax
  400e23:	48 83 ec 08          	sub    $0x8,%rsp
  400e27:	ff 75 f0             	pushq  -0x10(%rbp)
  400e2a:	ff 75 e8             	pushq  -0x18(%rbp)
  400e2d:	ff 75 e0             	pushq  -0x20(%rbp)
  400e30:	ff 75 d8             	pushq  -0x28(%rbp)
  400e33:	ff 75 d0             	pushq  -0x30(%rbp)
  400e36:	48 89 c7             	mov    %rax,%rdi
  400e39:	e8 c5 fa ff ff       	callq  400903 <atol@plt+0x15b>
  400e3e:	48 83 c4 30          	add    $0x30,%rsp
  400e42:	0f b6 45 a0          	movzbl -0x60(%rbp),%eax
  400e46:	3c 30                	cmp    $0x30,%al
  400e48:	74 1b                	je     400e65 <atol@plt+0x6bd>
  400e4a:	bf a4 11 40 00       	mov    $0x4011a4,%edi
  400e4f:	e8 fc f8 ff ff       	callq  400750 <puts@plt>
  400e54:	48 8b 05 b5 11 20 00 	mov    0x2011b5(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400e5b:	48 89 c7             	mov    %rax,%rdi
  400e5e:	e8 3d f9 ff ff       	callq  4007a0 <fflush@plt>
  400e63:	eb 1b                	jmp    400e80 <atol@plt+0x6d8>
  400e65:	bf b7 11 40 00       	mov    $0x4011b7,%edi
  400e6a:	e8 e1 f8 ff ff       	callq  400750 <puts@plt>
  400e6f:	48 8b 05 9a 11 20 00 	mov    0x20119a(%rip),%rax        # 602010 <stdout@@GLIBC_2.2.5>
  400e76:	48 89 c7             	mov    %rax,%rdi
  400e79:	e8 22 f9 ff ff       	callq  4007a0 <fflush@plt>
  400e7e:	eb 9f                	jmp    400e1f <atol@plt+0x677>
  400e80:	48 83 ec 08          	sub    $0x8,%rsp
  400e84:	ff 75 c0             	pushq  -0x40(%rbp)
  400e87:	ff 75 b8             	pushq  -0x48(%rbp)
  400e8a:	ff 75 b0             	pushq  -0x50(%rbp)
  400e8d:	ff 75 a8             	pushq  -0x58(%rbp)
  400e90:	ff 75 a0             	pushq  -0x60(%rbp)
  400e93:	e8 93 fe ff ff       	callq  400d2b <atol@plt+0x583>
  400e98:	48 83 c4 30          	add    $0x30,%rsp
  400e9c:	b8 00 00 00 00       	mov    $0x0,%eax
  400ea1:	c9                   	leaveq 
  400ea2:	c3                   	retq   
  400ea3:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  400eaa:	00 00 00 
  400ead:	0f 1f 00             	nopl   (%rax)
  400eb0:	41 57                	push   %r15
  400eb2:	41 56                	push   %r14
  400eb4:	41 89 ff             	mov    %edi,%r15d
  400eb7:	41 55                	push   %r13
  400eb9:	41 54                	push   %r12
  400ebb:	4c 8d 25 de 0e 20 00 	lea    0x200ede(%rip),%r12        # 601da0 <atol@plt+0x2015f8>
  400ec2:	55                   	push   %rbp
  400ec3:	48 8d 2d de 0e 20 00 	lea    0x200ede(%rip),%rbp        # 601da8 <atol@plt+0x201600>
  400eca:	53                   	push   %rbx
  400ecb:	49 89 f6             	mov    %rsi,%r14
  400ece:	49 89 d5             	mov    %rdx,%r13
  400ed1:	31 db                	xor    %ebx,%ebx
  400ed3:	4c 29 e5             	sub    %r12,%rbp
  400ed6:	48 83 ec 08          	sub    $0x8,%rsp
  400eda:	48 c1 fd 03          	sar    $0x3,%rbp
  400ede:	e8 25 f8 ff ff       	callq  400708 <putchar@plt-0x38>
  400ee3:	48 85 ed             	test   %rbp,%rbp
  400ee6:	74 1e                	je     400f06 <atol@plt+0x75e>
  400ee8:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  400eef:	00 
  400ef0:	4c 89 ea             	mov    %r13,%rdx
  400ef3:	4c 89 f6             	mov    %r14,%rsi
  400ef6:	44 89 ff             	mov    %r15d,%edi
  400ef9:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  400efd:	48 83 c3 01          	add    $0x1,%rbx
  400f01:	48 39 eb             	cmp    %rbp,%rbx
  400f04:	75 ea                	jne    400ef0 <atol@plt+0x748>
  400f06:	48 83 c4 08          	add    $0x8,%rsp
  400f0a:	5b                   	pop    %rbx
  400f0b:	5d                   	pop    %rbp
  400f0c:	41 5c                	pop    %r12
  400f0e:	41 5d                	pop    %r13
  400f10:	41 5e                	pop    %r14
  400f12:	41 5f                	pop    %r15
  400f14:	c3                   	retq   
  400f15:	90                   	nop
  400f16:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  400f1d:	00 00 00 
  400f20:	f3 c3                	repz retq 

Disassembly of section .fini:

0000000000400f24 <.fini>:
  400f24:	48 83 ec 08          	sub    $0x8,%rsp
  400f28:	48 83 c4 08          	add    $0x8,%rsp
  400f2c:	c3                   	retq   
