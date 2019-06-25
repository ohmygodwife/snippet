
fuckup:     file format elf32-i386


Disassembly of section .text:

08048094 <.text>:
 8048094:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 8048098:	83 e4 f0             	and    $0xfffffff0,%esp
 804809b:	ff 71 fc             	pushl  -0x4(%ecx)
 804809e:	55                   	push   %ebp
 804809f:	89 e5                	mov    %esp,%ebp
 80480a1:	56                   	push   %esi
 80480a2:	53                   	push   %ebx
 80480a3:	e8 24 05 00 00       	call   0x80485cc
 80480a8:	81 c3 c4 49 00 00    	add    $0x49c4,%ebx
 80480ae:	51                   	push   %ecx
 80480af:	8d 75 a8             	lea    -0x58(%ebp),%esi
 80480b2:	8d 83 21 b7 ff ff    	lea    -0x48df(%ebx),%eax
 80480b8:	83 ec 64             	sub    $0x64,%esp
 80480bb:	50                   	push   %eax
 80480bc:	6a 0e                	push   $0xe
 80480be:	e8 01 16 00 00       	call   0x80496c4
 80480c3:	c7 04 24 1e 00 00 00 	movl   $0x1e,(%esp)
 80480ca:	e8 a0 06 00 00       	call   0x804876f
 80480cf:	5a                   	pop    %edx
 80480d0:	8d 83 c0 de ff ff    	lea    -0x2140(%ebx),%eax
 80480d6:	59                   	pop    %ecx
 80480d7:	6a 00                	push   $0x0
 80480d9:	50                   	push   %eax
 80480da:	e8 90 07 00 00       	call   0x804886f
 80480df:	89 45 a4             	mov    %eax,-0x5c(%ebp)
 80480e2:	8b 45 a4             	mov    -0x5c(%ebp),%eax
 80480e5:	83 c4 0c             	add    $0xc,%esp
 80480e8:	6a 40                	push   $0x40
 80480ea:	56                   	push   %esi
 80480eb:	50                   	push   %eax
 80480ec:	e8 be 07 00 00       	call   0x80488af
 80480f1:	8b 45 a4             	mov    -0x5c(%ebp),%eax
 80480f4:	89 04 24             	mov    %eax,(%esp)
 80480f7:	e8 a6 06 00 00       	call   0x80487a2
 80480fc:	8b 83 f4 ff ff ff    	mov    -0xc(%ebx),%eax
 8048102:	c7 00 00 80 04 08    	movl   $0x8048000,(%eax)
 8048108:	8b 83 f8 ff ff ff    	mov    -0x8(%ebx),%eax
 804810e:	c7 00 00 00 00 00    	movl   $0x0,(%eax)
 8048114:	89 34 24             	mov    %esi,(%esp)
 8048117:	8d b3 cd de ff ff    	lea    -0x2133(%ebx),%esi
 804811d:	e8 ae 04 00 00       	call   0x80485d0
 8048122:	e8 99 02 00 00       	call   0x80483c0
 8048127:	e8 7a 00 00 00       	call   0x80481a6
 804812c:	83 c4 10             	add    $0x10,%esp
 804812f:	e8 19 03 00 00       	call   0x804844d
 8048134:	83 ec 0c             	sub    $0xc,%esp
 8048137:	89 45 a4             	mov    %eax,-0x5c(%ebp)
 804813a:	6a 1e                	push   $0x1e
 804813c:	e8 2e 06 00 00       	call   0x804876f
 8048141:	8b 45 a4             	mov    -0x5c(%ebp),%eax
 8048144:	83 c4 10             	add    $0x10,%esp
 8048147:	83 f8 04             	cmp    $0x4,%eax
 804814a:	77 31                	ja     0x804817d
 804814c:	8b 94 83 e0 de ff ff 	mov    -0x2120(%ebx,%eax,4),%edx
 8048153:	01 da                	add    %ebx,%edx
 8048155:	ff e2                	jmp    *%edx
 8048157:	e8 a1 02 00 00       	call   0x80483fd
 804815c:	eb d1                	jmp    0x804812f
 804815e:	e8 0d 04 00 00       	call   0x8048570
 8048163:	eb ca                	jmp    0x804812f
 8048165:	e8 34 04 00 00       	call   0x804859e
 804816a:	eb c3                	jmp    0x804812f
 804816c:	e8 b0 03 00 00       	call   0x8048521
 8048171:	eb bc                	jmp    0x804812f
 8048173:	83 ec 0c             	sub    $0xc,%esp
 8048176:	6a 00                	push   $0x0
 8048178:	e8 54 06 00 00       	call   0x80487d1
 804817d:	50                   	push   %eax
 804817e:	6a 10                	push   $0x10
 8048180:	56                   	push   %esi
 8048181:	6a 01                	push   $0x1
 8048183:	e8 60 07 00 00       	call   0x80488e8
 8048188:	83 c4 10             	add    $0x10,%esp
 804818b:	eb a2                	jmp    0x804812f
 804818d:	55                   	push   %ebp
 804818e:	89 e5                	mov    %esp,%ebp
 8048190:	53                   	push   %ebx
 8048191:	e8 36 04 00 00       	call   0x80485cc
 8048196:	81 c3 d6 48 00 00    	add    $0x48d6,%ebx
 804819c:	83 ec 10             	sub    $0x10,%esp
 804819f:	6a 00                	push   $0x0
 80481a1:	e8 2b 06 00 00       	call   0x80487d1
 80481a6:	55                   	push   %ebp
 80481a7:	89 e5                	mov    %esp,%ebp
 80481a9:	57                   	push   %edi
 80481aa:	56                   	push   %esi
 80481ab:	53                   	push   %ebx
 80481ac:	e8 1b 04 00 00       	call   0x80485cc
 80481b1:	81 c3 bb 48 00 00    	add    $0x48bb,%ebx
 80481b7:	83 ec 3c             	sub    $0x3c,%esp
 80481ba:	e8 64 04 00 00       	call   0x8048623
 80481bf:	d9 7d c6             	fnstcw -0x3a(%ebp)
 80481c2:	dc 8b f4 de ff ff    	fmull  -0x210c(%ebx)
 80481c8:	66 8b 45 c6          	mov    -0x3a(%ebp),%ax
 80481cc:	51                   	push   %ecx
 80481cd:	51                   	push   %ecx
 80481ce:	6a 00                	push   $0x0
 80481d0:	6a ff                	push   $0xffffffff
 80481d2:	80 cc 0c             	or     $0xc,%ah
 80481d5:	6a 22                	push   $0x22
 80481d7:	6a 03                	push   $0x3
 80481d9:	66 89 45 c4          	mov    %ax,-0x3c(%ebp)
 80481dd:	68 00 70 00 00       	push   $0x7000
 80481e2:	dd 5d e0             	fstpl  -0x20(%ebp)
 80481e5:	dd 45 e0             	fldl   -0x20(%ebp)
 80481e8:	d9 6d c4             	fldcw  -0x3c(%ebp)
 80481eb:	df 7d b8             	fistpll -0x48(%ebp)
 80481ee:	d9 6d c6             	fldcw  -0x3a(%ebp)
 80481f1:	8b 45 b8             	mov    -0x48(%ebp),%eax
 80481f4:	89 45 dc             	mov    %eax,-0x24(%ebp)
 80481f7:	8b 45 dc             	mov    -0x24(%ebp),%eax
 80481fa:	25 00 f0 ff ff       	and    $0xfffff000,%eax
 80481ff:	89 45 d4             	mov    %eax,-0x2c(%ebp)
 8048202:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048205:	50                   	push   %eax
 8048206:	e8 49 05 00 00       	call   0x8048754
 804820b:	89 45 d8             	mov    %eax,-0x28(%ebp)
 804820e:	8b 55 d4             	mov    -0x2c(%ebp),%edx
 8048211:	83 c4 20             	add    $0x20,%esp
 8048214:	8b 45 d8             	mov    -0x28(%ebp),%eax
 8048217:	39 c2                	cmp    %eax,%edx
 8048219:	75 9f                	jne    0x80481ba
 804821b:	8b 8b f4 ff ff ff    	mov    -0xc(%ebx),%ecx
 8048221:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048224:	8b 31                	mov    (%ecx),%esi
 8048226:	89 4d c0             	mov    %ecx,-0x40(%ebp)
 8048229:	89 c7                	mov    %eax,%edi
 804822b:	b9 00 1c 00 00       	mov    $0x1c00,%ecx
 8048230:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 8048233:	f3 a5                	rep movsl %ds:(%esi),%es:(%edi)
 8048235:	52                   	push   %edx
 8048236:	6a 05                	push   $0x5
 8048238:	68 00 40 00 00       	push   $0x4000
 804823d:	50                   	push   %eax
 804823e:	e8 be 05 00 00       	call   0x8048801
 8048243:	8b 45 c0             	mov    -0x40(%ebp),%eax
 8048246:	8b 7d d4             	mov    -0x2c(%ebp),%edi
 8048249:	8b 30                	mov    (%eax),%esi
 804824b:	eb 07                	jmp    0x8048254
 804824d:	58                   	pop    %eax
 804824e:	29 f0                	sub    %esi,%eax
 8048250:	01 f8                	add    %edi,%eax
 8048252:	ff e0                	jmp    *%eax
 8048254:	e8 f4 ff ff ff       	call   0x804824d
 8048259:	89 e2                	mov    %esp,%edx
 804825b:	c1 ea 0c             	shr    $0xc,%edx
 804825e:	42                   	inc    %edx
 804825f:	c1 e2 0c             	shl    $0xc,%edx
 8048262:	89 e1                	mov    %esp,%ecx
 8048264:	8b 01                	mov    (%ecx),%eax
 8048266:	29 f0                	sub    %esi,%eax
 8048268:	3d 00 70 00 00       	cmp    $0x7000,%eax
 804826d:	77 04                	ja     0x8048273
 804826f:	01 f8                	add    %edi,%eax
 8048271:	89 01                	mov    %eax,(%ecx)
 8048273:	83 c1 04             	add    $0x4,%ecx
 8048276:	39 d1                	cmp    %edx,%ecx
 8048278:	72 ea                	jb     0x8048264
 804827a:	29 f3                	sub    %esi,%ebx
 804827c:	01 fb                	add    %edi,%ebx
 804827e:	89 da                	mov    %ebx,%edx
 8048280:	83 ea 0c             	sub    $0xc,%edx
 8048283:	31 c9                	xor    %ecx,%ecx
 8048285:	8b 04 11             	mov    (%ecx,%edx,1),%eax
 8048288:	29 f0                	sub    %esi,%eax
 804828a:	3d 00 70 00 00       	cmp    $0x7000,%eax
 804828f:	77 05                	ja     0x8048296
 8048291:	01 f8                	add    %edi,%eax
 8048293:	89 04 11             	mov    %eax,(%ecx,%edx,1)
 8048296:	83 c1 04             	add    $0x4,%ecx
 8048299:	81 f9 d0 00 00 00    	cmp    $0xd0,%ecx
 804829f:	75 e4                	jne    0x8048285
 80482a1:	59                   	pop    %ecx
 80482a2:	5f                   	pop    %edi
 80482a3:	68 00 70 00 00       	push   $0x7000
 80482a8:	56                   	push   %esi
 80482a9:	e8 8c 05 00 00       	call   0x804883a
 80482ae:	8b 45 d4             	mov    -0x2c(%ebp),%eax
 80482b1:	8b 4d c0             	mov    -0x40(%ebp),%ecx
 80482b4:	8b 55 dc             	mov    -0x24(%ebp),%edx
 80482b7:	89 01                	mov    %eax,(%ecx)
 80482b9:	8b 83 f8 ff ff ff    	mov    -0x8(%ebx),%eax
 80482bf:	89 10                	mov    %edx,(%eax)
 80482c1:	58                   	pop    %eax
 80482c2:	8d 83 21 b7 ff ff    	lea    -0x48df(%ebx),%eax
 80482c8:	5a                   	pop    %edx
 80482c9:	50                   	push   %eax
 80482ca:	6a 0e                	push   $0xe
 80482cc:	e8 f3 13 00 00       	call   0x80496c4
 80482d1:	83 c4 10             	add    $0x10,%esp
 80482d4:	8d 65 f4             	lea    -0xc(%ebp),%esp
 80482d7:	5b                   	pop    %ebx
 80482d8:	5e                   	pop    %esi
 80482d9:	5f                   	pop    %edi
 80482da:	5d                   	pop    %ebp
 80482db:	c3                   	ret    
 80482dc:	55                   	push   %ebp
 80482dd:	89 e5                	mov    %esp,%ebp
 80482df:	57                   	push   %edi
 80482e0:	56                   	push   %esi
 80482e1:	53                   	push   %ebx
 80482e2:	8d 7d e7             	lea    -0x19(%ebp),%edi
 80482e5:	31 f6                	xor    %esi,%esi
 80482e7:	e8 e0 02 00 00       	call   0x80485cc
 80482ec:	81 c3 80 47 00 00    	add    $0x4780,%ebx
 80482f2:	83 ec 2c             	sub    $0x2c,%esp
 80482f5:	8a 55 10             	mov    0x10(%ebp),%dl
 80482f8:	c6 45 e7 00          	movb   $0x0,-0x19(%ebp)
 80482fc:	50                   	push   %eax
 80482fd:	6a 01                	push   $0x1
 80482ff:	57                   	push   %edi
 8048300:	6a 00                	push   $0x0
 8048302:	88 55 d4             	mov    %dl,-0x2c(%ebp)
 8048305:	e8 a5 05 00 00       	call   0x80488af
 804830a:	83 c4 10             	add    $0x10,%esp
 804830d:	40                   	inc    %eax
 804830e:	8a 55 d4             	mov    -0x2c(%ebp),%dl
 8048311:	74 15                	je     0x8048328
 8048313:	8a 45 e7             	mov    -0x19(%ebp),%al
 8048316:	38 c2                	cmp    %al,%dl
 8048318:	74 18                	je     0x8048332
 804831a:	8b 4d 08             	mov    0x8(%ebp),%ecx
 804831d:	88 04 31             	mov    %al,(%ecx,%esi,1)
 8048320:	46                   	inc    %esi
 8048321:	39 75 0c             	cmp    %esi,0xc(%ebp)
 8048324:	7f d6                	jg     0x80482fc
 8048326:	eb 0a                	jmp    0x8048332
 8048328:	3b 75 0c             	cmp    0xc(%ebp),%esi
 804832b:	7d 05                	jge    0x8048332
 804832d:	38 55 e7             	cmp    %dl,-0x19(%ebp)
 8048330:	75 ca                	jne    0x80482fc
 8048332:	8d 46 ff             	lea    -0x1(%esi),%eax
 8048335:	31 ff                	xor    %edi,%edi
 8048337:	89 45 d4             	mov    %eax,-0x2c(%ebp)
 804833a:	3b 7d d4             	cmp    -0x2c(%ebp),%edi
 804833d:	7d 0a                	jge    0x8048349
 804833f:	e8 df 02 00 00       	call   0x8048623
 8048344:	dd d8                	fstp   %st(0)
 8048346:	47                   	inc    %edi
 8048347:	eb f1                	jmp    0x804833a
 8048349:	8b 45 08             	mov    0x8(%ebp),%eax
 804834c:	80 38 34             	cmpb   $0x34,(%eax)
 804834f:	74 05                	je     0x8048356
 8048351:	e8 50 fe ff ff       	call   0x80481a6
 8048356:	8d 65 f4             	lea    -0xc(%ebp),%esp
 8048359:	89 f0                	mov    %esi,%eax
 804835b:	5b                   	pop    %ebx
 804835c:	5e                   	pop    %esi
 804835d:	5f                   	pop    %edi
 804835e:	5d                   	pop    %ebp
 804835f:	c3                   	ret    
 8048360:	55                   	push   %ebp
 8048361:	89 e5                	mov    %esp,%ebp
 8048363:	57                   	push   %edi
 8048364:	56                   	push   %esi
 8048365:	53                   	push   %ebx
 8048366:	31 f6                	xor    %esi,%esi
 8048368:	e8 5f 02 00 00       	call   0x80485cc
 804836d:	81 c3 ff 46 00 00    	add    $0x46ff,%ebx
 8048373:	83 ec 1c             	sub    $0x1c,%esp
 8048376:	50                   	push   %eax
 8048377:	8b 45 0c             	mov    0xc(%ebp),%eax
 804837a:	29 f0                	sub    %esi,%eax
 804837c:	50                   	push   %eax
 804837d:	ff 75 08             	pushl  0x8(%ebp)
 8048380:	6a 00                	push   $0x0
 8048382:	e8 28 05 00 00       	call   0x80488af
 8048387:	89 c7                	mov    %eax,%edi
 8048389:	8d 04 06             	lea    (%esi,%eax,1),%eax
 804838c:	83 c4 10             	add    $0x10,%esp
 804838f:	83 ff ff             	cmp    $0xffffffff,%edi
 8048392:	0f 45 f0             	cmovne %eax,%esi
 8048395:	3b 75 0c             	cmp    0xc(%ebp),%esi
 8048398:	7c dc                	jl     0x8048376
 804839a:	8d 47 ff             	lea    -0x1(%edi),%eax
 804839d:	31 f6                	xor    %esi,%esi
 804839f:	89 45 e4             	mov    %eax,-0x1c(%ebp)
 80483a2:	3b 75 e4             	cmp    -0x1c(%ebp),%esi
 80483a5:	7d 0a                	jge    0x80483b1
 80483a7:	e8 77 02 00 00       	call   0x8048623
 80483ac:	dd d8                	fstp   %st(0)
 80483ae:	46                   	inc    %esi
 80483af:	eb f1                	jmp    0x80483a2
 80483b1:	e8 f0 fd ff ff       	call   0x80481a6
 80483b6:	8d 65 f4             	lea    -0xc(%ebp),%esp
 80483b9:	89 f8                	mov    %edi,%eax
 80483bb:	5b                   	pop    %ebx
 80483bc:	5e                   	pop    %esi
 80483bd:	5f                   	pop    %edi
 80483be:	5d                   	pop    %ebp
 80483bf:	c3                   	ret    
 80483c0:	55                   	push   %ebp
 80483c1:	89 e5                	mov    %esp,%ebp
 80483c3:	53                   	push   %ebx
 80483c4:	e8 03 02 00 00       	call   0x80485cc
 80483c9:	81 c3 a3 46 00 00    	add    $0x46a3,%ebx
 80483cf:	83 ec 08             	sub    $0x8,%esp
 80483d2:	8d 83 d4 db ff ff    	lea    -0x242c(%ebx),%eax
 80483d8:	6a 6e                	push   $0x6e
 80483da:	50                   	push   %eax
 80483db:	6a 01                	push   $0x1
 80483dd:	e8 06 05 00 00       	call   0x80488e8
 80483e2:	8d 83 43 dc ff ff    	lea    -0x23bd(%ebx),%eax
 80483e8:	83 c4 0c             	add    $0xc,%esp
 80483eb:	6a 37                	push   $0x37
 80483ed:	50                   	push   %eax
 80483ee:	6a 01                	push   $0x1
 80483f0:	e8 f3 04 00 00       	call   0x80488e8
 80483f5:	83 c4 10             	add    $0x10,%esp
 80483f8:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 80483fb:	c9                   	leave  
 80483fc:	c3                   	ret    
 80483fd:	55                   	push   %ebp
 80483fe:	89 e5                	mov    %esp,%ebp
 8048400:	53                   	push   %ebx
 8048401:	e8 c6 01 00 00       	call   0x80485cc
 8048406:	81 c3 66 46 00 00    	add    $0x4666,%ebx
 804840c:	83 ec 08             	sub    $0x8,%esp
 804840f:	8d 83 7b dc ff ff    	lea    -0x2385(%ebx),%eax
 8048415:	6a 68                	push   $0x68
 8048417:	50                   	push   %eax
 8048418:	6a 01                	push   $0x1
 804841a:	e8 c9 04 00 00       	call   0x80488e8
 804841f:	8d 83 e4 dc ff ff    	lea    -0x231c(%ebx),%eax
 8048425:	83 c4 0c             	add    $0xc,%esp
 8048428:	6a 27                	push   $0x27
 804842a:	50                   	push   %eax
 804842b:	6a 01                	push   $0x1
 804842d:	e8 b6 04 00 00       	call   0x80488e8
 8048432:	8d 83 0c dd ff ff    	lea    -0x22f4(%ebx),%eax
 8048438:	83 c4 0c             	add    $0xc,%esp
 804843b:	6a 6f                	push   $0x6f
 804843d:	50                   	push   %eax
 804843e:	6a 01                	push   $0x1
 8048440:	e8 a3 04 00 00       	call   0x80488e8
 8048445:	83 c4 10             	add    $0x10,%esp
 8048448:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 804844b:	c9                   	leave  
 804844c:	c3                   	ret    
 804844d:	55                   	push   %ebp
 804844e:	89 e5                	mov    %esp,%ebp
 8048450:	57                   	push   %edi
 8048451:	56                   	push   %esi
 8048452:	53                   	push   %ebx
 8048453:	8d 75 e3             	lea    -0x1d(%ebp),%esi
 8048456:	e8 71 01 00 00       	call   0x80485cc
 804845b:	81 c3 11 46 00 00    	add    $0x4611,%ebx
 8048461:	83 ec 20             	sub    $0x20,%esp
 8048464:	89 f7                	mov    %esi,%edi
 8048466:	8d 83 7c dd ff ff    	lea    -0x2284(%ebx),%eax
 804846c:	6a 0a                	push   $0xa
 804846e:	50                   	push   %eax
 804846f:	6a 01                	push   $0x1
 8048471:	e8 72 04 00 00       	call   0x80488e8
 8048476:	8d 83 87 dd ff ff    	lea    -0x2279(%ebx),%eax
 804847c:	83 c4 0c             	add    $0xc,%esp
 804847f:	6a 0a                	push   $0xa
 8048481:	50                   	push   %eax
 8048482:	6a 01                	push   $0x1
 8048484:	e8 5f 04 00 00       	call   0x80488e8
 8048489:	8d 83 92 dd ff ff    	lea    -0x226e(%ebx),%eax
 804848f:	83 c4 0c             	add    $0xc,%esp
 8048492:	6a 10                	push   $0x10
 8048494:	50                   	push   %eax
 8048495:	6a 01                	push   $0x1
 8048497:	e8 4c 04 00 00       	call   0x80488e8
 804849c:	8d 83 a3 dd ff ff    	lea    -0x225d(%ebx),%eax
 80484a2:	83 c4 0c             	add    $0xc,%esp
 80484a5:	6a 11                	push   $0x11
 80484a7:	50                   	push   %eax
 80484a8:	6a 01                	push   $0x1
 80484aa:	e8 39 04 00 00       	call   0x80488e8
 80484af:	8d 83 b5 dd ff ff    	lea    -0x224b(%ebx),%eax
 80484b5:	83 c4 0c             	add    $0xc,%esp
 80484b8:	6a 13                	push   $0x13
 80484ba:	50                   	push   %eax
 80484bb:	6a 01                	push   $0x1
 80484bd:	e8 26 04 00 00       	call   0x80488e8
 80484c2:	8d 83 c9 dd ff ff    	lea    -0x2237(%ebx),%eax
 80484c8:	83 c4 0c             	add    $0xc,%esp
 80484cb:	6a 14                	push   $0x14
 80484cd:	50                   	push   %eax
 80484ce:	6a 01                	push   $0x1
 80484d0:	e8 13 04 00 00       	call   0x80488e8
 80484d5:	8d 83 89 dd ff ff    	lea    -0x2277(%ebx),%eax
 80484db:	83 c4 0c             	add    $0xc,%esp
 80484de:	6a 08                	push   $0x8
 80484e0:	50                   	push   %eax
 80484e1:	6a 01                	push   $0x1
 80484e3:	e8 00 04 00 00       	call   0x80488e8
 80484e8:	8d 83 de dd ff ff    	lea    -0x2222(%ebx),%eax
 80484ee:	83 c4 0c             	add    $0xc,%esp
 80484f1:	6a 08                	push   $0x8
 80484f3:	50                   	push   %eax
 80484f4:	6a 01                	push   $0x1
 80484f6:	e8 ed 03 00 00       	call   0x80488e8
 80484fb:	31 c0                	xor    %eax,%eax
 80484fd:	b9 05 00 00 00       	mov    $0x5,%ecx
 8048502:	83 c4 0c             	add    $0xc,%esp
 8048505:	f3 aa                	rep stos %al,%es:(%edi)
 8048507:	6a 0a                	push   $0xa
 8048509:	6a 03                	push   $0x3
 804850b:	56                   	push   %esi
 804850c:	e8 cb fd ff ff       	call   0x80482dc
 8048511:	89 34 24             	mov    %esi,(%esp)
 8048514:	e8 a6 12 00 00       	call   0x80497bf
 8048519:	8d 65 f4             	lea    -0xc(%ebp),%esp
 804851c:	5b                   	pop    %ebx
 804851d:	5e                   	pop    %esi
 804851e:	5f                   	pop    %edi
 804851f:	5d                   	pop    %ebp
 8048520:	c3                   	ret    
 8048521:	55                   	push   %ebp
 8048522:	89 e5                	mov    %esp,%ebp
 8048524:	53                   	push   %ebx
 8048525:	e8 a2 00 00 00       	call   0x80485cc
 804852a:	81 c3 42 45 00 00    	add    $0x4542,%ebx
 8048530:	83 ec 18             	sub    $0x18,%esp
 8048533:	8d 83 e7 dd ff ff    	lea    -0x2219(%ebx),%eax
 8048539:	6a 3f                	push   $0x3f
 804853b:	50                   	push   %eax
 804853c:	6a 01                	push   $0x1
 804853e:	e8 a5 03 00 00       	call   0x80488e8
 8048543:	8d 83 27 de ff ff    	lea    -0x21d9(%ebx),%eax
 8048549:	83 c4 0c             	add    $0xc,%esp
 804854c:	6a 60                	push   $0x60
 804854e:	50                   	push   %eax
 804854f:	6a 01                	push   $0x1
 8048551:	e8 92 03 00 00       	call   0x80488e8
 8048556:	e8 4b fc ff ff       	call   0x80481a6
 804855b:	58                   	pop    %eax
 804855c:	8d 45 ee             	lea    -0x12(%ebp),%eax
 804855f:	5a                   	pop    %edx
 8048560:	6a 64                	push   $0x64
 8048562:	50                   	push   %eax
 8048563:	e8 f8 fd ff ff       	call   0x8048360
 8048568:	83 c4 10             	add    $0x10,%esp
 804856b:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 804856e:	c9                   	leave  
 804856f:	c3                   	ret    
 8048570:	55                   	push   %ebp
 8048571:	89 e5                	mov    %esp,%ebp
 8048573:	53                   	push   %ebx
 8048574:	50                   	push   %eax
 8048575:	e8 52 00 00 00       	call   0x80485cc
 804857a:	81 c3 f2 44 00 00    	add    $0x44f2,%ebx
 8048580:	e8 21 fc ff ff       	call   0x80481a6
 8048585:	8d 83 88 de ff ff    	lea    -0x2178(%ebx),%eax
 804858b:	52                   	push   %edx
 804858c:	6a 21                	push   $0x21
 804858e:	50                   	push   %eax
 804858f:	6a 01                	push   $0x1
 8048591:	e8 52 03 00 00       	call   0x80488e8
 8048596:	83 c4 10             	add    $0x10,%esp
 8048599:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 804859c:	c9                   	leave  
 804859d:	c3                   	ret    
 804859e:	55                   	push   %ebp
 804859f:	89 e5                	mov    %esp,%ebp
 80485a1:	53                   	push   %ebx
 80485a2:	e8 25 00 00 00       	call   0x80485cc
 80485a7:	81 c3 c5 44 00 00    	add    $0x44c5,%ebx
 80485ad:	83 ec 0c             	sub    $0xc,%esp
 80485b0:	8b 83 f8 ff ff ff    	mov    -0x8(%ebx),%eax
 80485b6:	ff 30                	pushl  (%eax)
 80485b8:	8d 83 aa de ff ff    	lea    -0x2156(%ebx),%eax
 80485be:	50                   	push   %eax
 80485bf:	e8 5d 03 00 00       	call   0x8048921
 80485c4:	83 c4 10             	add    $0x10,%esp
 80485c7:	8b 5d fc             	mov    -0x4(%ebp),%ebx
 80485ca:	c9                   	leave  
 80485cb:	c3                   	ret    
 80485cc:	8b 1c 24             	mov    (%esp),%ebx
 80485cf:	c3                   	ret    
 80485d0:	55                   	push   %ebp
 80485d1:	89 e5                	mov    %esp,%ebp
 80485d3:	56                   	push   %esi
 80485d4:	53                   	push   %ebx
 80485d5:	e8 f2 ff ff ff       	call   0x80485cc
 80485da:	81 c3 92 44 00 00    	add    $0x4492,%ebx
 80485e0:	50                   	push   %eax
 80485e1:	50                   	push   %eax
 80485e2:	6a 00                	push   $0x0
 80485e4:	6a ff                	push   $0xffffffff
 80485e6:	6a 22                	push   $0x22
 80485e8:	6a 03                	push   $0x3
 80485ea:	68 00 10 00 00       	push   $0x1000
 80485ef:	6a 00                	push   $0x0
 80485f1:	8b 75 08             	mov    0x8(%ebp),%esi
 80485f4:	c7 83 b4 00 00 00 00 	movl   $0x0,0xb4(%ebx)
 80485fb:	00 00 00 
 80485fe:	e8 51 01 00 00       	call   0x8048754
 8048603:	8b 93 fc ff ff ff    	mov    -0x4(%ebx),%edx
 8048609:	83 c4 20             	add    $0x20,%esp
 804860c:	89 02                	mov    %eax,(%edx)
 804860e:	31 d2                	xor    %edx,%edx
 8048610:	8b 0c 96             	mov    (%esi,%edx,4),%ecx
 8048613:	89 0c 90             	mov    %ecx,(%eax,%edx,4)
 8048616:	42                   	inc    %edx
 8048617:	83 fa 10             	cmp    $0x10,%edx
 804861a:	75 f4                	jne    0x8048610
 804861c:	8d 65 f8             	lea    -0x8(%ebp),%esp
 804861f:	5b                   	pop    %ebx
 8048620:	5e                   	pop    %esi
 8048621:	5d                   	pop    %ebp
 8048622:	c3                   	ret    
 8048623:	55                   	push   %ebp
 8048624:	89 e5                	mov    %esp,%ebp
 8048626:	57                   	push   %edi
 8048627:	56                   	push   %esi
 8048628:	e8 23 01 00 00       	call   0x8048750
 804862d:	81 c7 3f 44 00 00    	add    $0x443f,%edi
 8048633:	53                   	push   %ebx
 8048634:	83 ec 1c             	sub    $0x1c,%esp
 8048637:	8b 9f b4 00 00 00    	mov    0xb4(%edi),%ebx
 804863d:	8b 87 fc ff ff ff    	mov    -0x4(%edi),%eax
 8048643:	c7 45 e4 00 00 00 00 	movl   $0x0,-0x1c(%ebp)
 804864a:	8b 30                	mov    (%eax),%esi
 804864c:	8d 43 0f             	lea    0xf(%ebx),%eax
 804864f:	83 e0 0f             	and    $0xf,%eax
 8048652:	89 45 e0             	mov    %eax,-0x20(%ebp)
 8048655:	8d 04 86             	lea    (%esi,%eax,4),%eax
 8048658:	8b 14 9e             	mov    (%esi,%ebx,4),%edx
 804865b:	89 45 dc             	mov    %eax,-0x24(%ebp)
 804865e:	8b 00                	mov    (%eax),%eax
 8048660:	89 45 d8             	mov    %eax,-0x28(%ebp)
 8048663:	8d 43 0d             	lea    0xd(%ebx),%eax
 8048666:	83 e0 0f             	and    $0xf,%eax
 8048669:	8b 0c 86             	mov    (%esi,%eax,4),%ecx
 804866c:	89 d0                	mov    %edx,%eax
 804866e:	c1 e0 10             	shl    $0x10,%eax
 8048671:	31 d0                	xor    %edx,%eax
 8048673:	31 c8                	xor    %ecx,%eax
 8048675:	89 c2                	mov    %eax,%edx
 8048677:	89 c8                	mov    %ecx,%eax
 8048679:	c1 e0 0f             	shl    $0xf,%eax
 804867c:	31 d0                	xor    %edx,%eax
 804867e:	8d 53 09             	lea    0x9(%ebx),%edx
 8048681:	83 c3 0a             	add    $0xa,%ebx
 8048684:	83 e3 0f             	and    $0xf,%ebx
 8048687:	83 e2 0f             	and    $0xf,%edx
 804868a:	8b 14 96             	mov    (%esi,%edx,4),%edx
 804868d:	89 d1                	mov    %edx,%ecx
 804868f:	c1 e9 0b             	shr    $0xb,%ecx
 8048692:	31 d1                	xor    %edx,%ecx
 8048694:	89 c2                	mov    %eax,%edx
 8048696:	31 ca                	xor    %ecx,%edx
 8048698:	c1 e1 1c             	shl    $0x1c,%ecx
 804869b:	89 14 9e             	mov    %edx,(%esi,%ebx,4)
 804869e:	8b 75 d8             	mov    -0x28(%ebp),%esi
 80486a1:	8d 1c b5 00 00 00 00 	lea    0x0(,%esi,4),%ebx
 80486a8:	31 f3                	xor    %esi,%ebx
 80486aa:	8b 75 dc             	mov    -0x24(%ebp),%esi
 80486ad:	31 c3                	xor    %eax,%ebx
 80486af:	c1 e0 12             	shl    $0x12,%eax
 80486b2:	31 d3                	xor    %edx,%ebx
 80486b4:	c1 e2 05             	shl    $0x5,%edx
 80486b7:	31 d8                	xor    %ebx,%eax
 80486b9:	89 cb                	mov    %ecx,%ebx
 80486bb:	81 e2 24 2d 44 da    	and    $0xda442d24,%edx
 80486c1:	31 c3                	xor    %eax,%ebx
 80486c3:	89 d8                	mov    %ebx,%eax
 80486c5:	31 d0                	xor    %edx,%eax
 80486c7:	89 06                	mov    %eax,(%esi)
 80486c9:	8b 75 e0             	mov    -0x20(%ebp),%esi
 80486cc:	89 45 e0             	mov    %eax,-0x20(%ebp)
 80486cf:	df 6d e0             	fildll -0x20(%ebp)
 80486d2:	89 b7 b4 00 00 00    	mov    %esi,0xb4(%edi)
 80486d8:	d8 8f 10 df ff ff    	fmuls  -0x20f0(%edi)
 80486de:	83 c4 1c             	add    $0x1c,%esp
 80486e1:	5b                   	pop    %ebx
 80486e2:	5e                   	pop    %esi
 80486e3:	5f                   	pop    %edi
 80486e4:	5d                   	pop    %ebp
 80486e5:	c3                   	ret    
 80486e6:	55                   	push   %ebp
 80486e7:	89 e5                	mov    %esp,%ebp
 80486e9:	57                   	push   %edi
 80486ea:	56                   	push   %esi
 80486eb:	53                   	push   %ebx
 80486ec:	31 ff                	xor    %edi,%edi
 80486ee:	e8 d9 fe ff ff       	call   0x80485cc
 80486f3:	81 c3 79 43 00 00    	add    $0x4379,%ebx
 80486f9:	83 ec 1c             	sub    $0x1c,%esp
 80486fc:	8b 83 fc ff ff ff    	mov    -0x4(%ebx),%eax
 8048702:	8d b3 fc de ff ff    	lea    -0x2104(%ebx),%esi
 8048708:	89 45 e4             	mov    %eax,-0x1c(%ebp)
 804870b:	50                   	push   %eax
 804870c:	8b 45 e4             	mov    -0x1c(%ebp),%eax
 804870f:	8b 00                	mov    (%eax),%eax
 8048711:	ff 34 b8             	pushl  (%eax,%edi,4)
 8048714:	57                   	push   %edi
 8048715:	47                   	inc    %edi
 8048716:	56                   	push   %esi
 8048717:	e8 05 02 00 00       	call   0x8048921
 804871c:	83 c4 10             	add    $0x10,%esp
 804871f:	83 ff 10             	cmp    $0x10,%edi
 8048722:	74 17                	je     0x804873b
 8048724:	f7 c7 03 00 00 00    	test   $0x3,%edi
 804872a:	75 df                	jne    0x804870b
 804872c:	83 ec 0c             	sub    $0xc,%esp
 804872f:	6a 0a                	push   $0xa
 8048731:	e8 b0 0e 00 00       	call   0x80495e6
 8048736:	83 c4 10             	add    $0x10,%esp
 8048739:	eb d0                	jmp    0x804870b
 804873b:	83 ec 0c             	sub    $0xc,%esp
 804873e:	6a 0a                	push   $0xa
 8048740:	e8 a1 0e 00 00       	call   0x80495e6
 8048745:	83 c4 10             	add    $0x10,%esp
 8048748:	8d 65 f4             	lea    -0xc(%ebp),%esp
 804874b:	5b                   	pop    %ebx
 804874c:	5e                   	pop    %esi
 804874d:	5f                   	pop    %edi
 804874e:	5d                   	pop    %ebp
 804874f:	c3                   	ret    
 8048750:	8b 3c 24             	mov    (%esp),%edi
 8048753:	c3                   	ret    
 8048754:	89 da                	mov    %ebx,%edx
 8048756:	b8 5a 00 00 00       	mov    $0x5a,%eax
 804875b:	8d 5c 24 04          	lea    0x4(%esp),%ebx
 804875f:	cd 80                	int    $0x80
 8048761:	89 d3                	mov    %edx,%ebx
 8048763:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 8048768:	0f 87 d7 11 00 00    	ja     0x8049945
 804876e:	c3                   	ret    
 804876f:	e8 2a 00 00 00       	call   0x804879e
 8048774:	81 c1 f8 42 00 00    	add    $0x42f8,%ecx
 804877a:	8b 54 24 04          	mov    0x4(%esp),%edx
 804877e:	87 d3                	xchg   %edx,%ebx
 8048780:	b8 1b 00 00 00       	mov    $0x1b,%eax
 8048785:	cd 80                	int    $0x80
 8048787:	87 d3                	xchg   %edx,%ebx
 8048789:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 804878e:	76 0d                	jbe    0x804879d
 8048790:	f7 d8                	neg    %eax
 8048792:	8d 91 bc 00 00 00    	lea    0xbc(%ecx),%edx
 8048798:	89 02                	mov    %eax,(%edx)
 804879a:	83 c8 ff             	or     $0xffffffff,%eax
 804879d:	c3                   	ret    
 804879e:	8b 0c 24             	mov    (%esp),%ecx
 80487a1:	c3                   	ret    
 80487a2:	e8 f7 ff ff ff       	call   0x804879e
 80487a7:	81 c1 c5 42 00 00    	add    $0x42c5,%ecx
 80487ad:	8b 54 24 04          	mov    0x4(%esp),%edx
 80487b1:	87 d3                	xchg   %edx,%ebx
 80487b3:	b8 06 00 00 00       	mov    $0x6,%eax
 80487b8:	cd 80                	int    $0x80
 80487ba:	87 d3                	xchg   %edx,%ebx
 80487bc:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 80487c1:	76 0d                	jbe    0x80487d0
 80487c3:	f7 d8                	neg    %eax
 80487c5:	8d 91 bc 00 00 00    	lea    0xbc(%ecx),%edx
 80487cb:	89 02                	mov    %eax,(%edx)
 80487cd:	83 c8 ff             	or     $0xffffffff,%eax
 80487d0:	c3                   	ret    
 80487d1:	e8 27 00 00 00       	call   0x80487fd
 80487d6:	05 96 42 00 00       	add    $0x4296,%eax
 80487db:	8b 54 24 04          	mov    0x4(%esp),%edx
 80487df:	8d 88 bc 00 00 00    	lea    0xbc(%eax),%ecx
 80487e5:	87 d3                	xchg   %edx,%ebx
 80487e7:	b8 01 00 00 00       	mov    $0x1,%eax
 80487ec:	cd 80                	int    $0x80
 80487ee:	87 d3                	xchg   %edx,%ebx
 80487f0:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 80487f5:	76 ee                	jbe    0x80487e5
 80487f7:	f7 d8                	neg    %eax
 80487f9:	89 01                	mov    %eax,(%ecx)
 80487fb:	eb e8                	jmp    0x80487e5
 80487fd:	8b 04 24             	mov    (%esp),%eax
 8048800:	c3                   	ret    
 8048801:	53                   	push   %ebx
 8048802:	e8 c5 fd ff ff       	call   0x80485cc
 8048807:	81 c3 65 42 00 00    	add    $0x4265,%ebx
 804880d:	8b 54 24 10          	mov    0x10(%esp),%edx
 8048811:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 8048815:	8b 44 24 08          	mov    0x8(%esp),%eax
 8048819:	53                   	push   %ebx
 804881a:	89 c3                	mov    %eax,%ebx
 804881c:	b8 7d 00 00 00       	mov    $0x7d,%eax
 8048821:	cd 80                	int    $0x80
 8048823:	5b                   	pop    %ebx
 8048824:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 8048829:	76 0d                	jbe    0x8048838
 804882b:	f7 d8                	neg    %eax
 804882d:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 8048833:	89 02                	mov    %eax,(%edx)
 8048835:	83 c8 ff             	or     $0xffffffff,%eax
 8048838:	5b                   	pop    %ebx
 8048839:	c3                   	ret    
 804883a:	53                   	push   %ebx
 804883b:	e8 8c fd ff ff       	call   0x80485cc
 8048840:	81 c3 2c 42 00 00    	add    $0x422c,%ebx
 8048846:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 804884a:	8b 54 24 08          	mov    0x8(%esp),%edx
 804884e:	87 d3                	xchg   %edx,%ebx
 8048850:	b8 5b 00 00 00       	mov    $0x5b,%eax
 8048855:	cd 80                	int    $0x80
 8048857:	87 d3                	xchg   %edx,%ebx
 8048859:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 804885e:	76 0d                	jbe    0x804886d
 8048860:	f7 d8                	neg    %eax
 8048862:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 8048868:	89 02                	mov    %eax,(%edx)
 804886a:	83 c8 ff             	or     $0xffffffff,%eax
 804886d:	5b                   	pop    %ebx
 804886e:	c3                   	ret    
 804886f:	53                   	push   %ebx
 8048870:	e8 57 fd ff ff       	call   0x80485cc
 8048875:	81 c3 f7 41 00 00    	add    $0x41f7,%ebx
 804887b:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 804887f:	31 d2                	xor    %edx,%edx
 8048881:	f6 c1 40             	test   $0x40,%cl
 8048884:	74 04                	je     0x804888a
 8048886:	8b 54 24 10          	mov    0x10(%esp),%edx
 804888a:	8b 44 24 08          	mov    0x8(%esp),%eax
 804888e:	53                   	push   %ebx
 804888f:	89 c3                	mov    %eax,%ebx
 8048891:	b8 05 00 00 00       	mov    $0x5,%eax
 8048896:	cd 80                	int    $0x80
 8048898:	5b                   	pop    %ebx
 8048899:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 804889e:	76 0d                	jbe    0x80488ad
 80488a0:	f7 d8                	neg    %eax
 80488a2:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 80488a8:	89 02                	mov    %eax,(%edx)
 80488aa:	83 c8 ff             	or     $0xffffffff,%eax
 80488ad:	5b                   	pop    %ebx
 80488ae:	c3                   	ret    
 80488af:	53                   	push   %ebx
 80488b0:	e8 17 fd ff ff       	call   0x80485cc
 80488b5:	81 c3 b7 41 00 00    	add    $0x41b7,%ebx
 80488bb:	8b 54 24 10          	mov    0x10(%esp),%edx
 80488bf:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 80488c3:	8b 44 24 08          	mov    0x8(%esp),%eax
 80488c7:	53                   	push   %ebx
 80488c8:	89 c3                	mov    %eax,%ebx
 80488ca:	b8 03 00 00 00       	mov    $0x3,%eax
 80488cf:	cd 80                	int    $0x80
 80488d1:	5b                   	pop    %ebx
 80488d2:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 80488d7:	76 0d                	jbe    0x80488e6
 80488d9:	f7 d8                	neg    %eax
 80488db:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 80488e1:	89 02                	mov    %eax,(%edx)
 80488e3:	83 c8 ff             	or     $0xffffffff,%eax
 80488e6:	5b                   	pop    %ebx
 80488e7:	c3                   	ret    
 80488e8:	53                   	push   %ebx
 80488e9:	e8 de fc ff ff       	call   0x80485cc
 80488ee:	81 c3 7e 41 00 00    	add    $0x417e,%ebx
 80488f4:	8b 54 24 10          	mov    0x10(%esp),%edx
 80488f8:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 80488fc:	8b 44 24 08          	mov    0x8(%esp),%eax
 8048900:	53                   	push   %ebx
 8048901:	89 c3                	mov    %eax,%ebx
 8048903:	b8 04 00 00 00       	mov    $0x4,%eax
 8048908:	cd 80                	int    $0x80
 804890a:	5b                   	pop    %ebx
 804890b:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 8048910:	76 0d                	jbe    0x804891f
 8048912:	f7 d8                	neg    %eax
 8048914:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 804891a:	89 02                	mov    %eax,(%edx)
 804891c:	83 c8 ff             	or     $0xffffffff,%eax
 804891f:	5b                   	pop    %ebx
 8048920:	c3                   	ret    
 8048921:	e8 d7 fe ff ff       	call   0x80487fd
 8048926:	05 46 41 00 00       	add    $0x4146,%eax
 804892b:	8d 54 24 08          	lea    0x8(%esp),%edx
 804892f:	52                   	push   %edx
 8048930:	ff 74 24 08          	pushl  0x8(%esp)
 8048934:	8d 80 24 00 00 00    	lea    0x24(%eax),%eax
 804893a:	ff 30                	pushl  (%eax)
 804893c:	e8 99 00 00 00       	call   0x80489da
 8048941:	83 c4 0c             	add    $0xc,%esp
 8048944:	c3                   	ret    
 8048945:	53                   	push   %ebx
 8048946:	e8 b2 fe ff ff       	call   0x80487fd
 804894b:	05 21 41 00 00       	add    $0x4121,%eax
 8048950:	8d 80 14 00 00 00    	lea    0x14(%eax),%eax
 8048956:	8b 18                	mov    (%eax),%ebx
 8048958:	85 db                	test   %ebx,%ebx
 804895a:	74 11                	je     0x804896d
 804895c:	f6 03 40             	testb  $0x40,(%ebx)
 804895f:	74 07                	je     0x8048968
 8048961:	53                   	push   %ebx
 8048962:	e8 4e 00 00 00       	call   0x80489b5
 8048967:	58                   	pop    %eax
 8048968:	8b 5b 20             	mov    0x20(%ebx),%ebx
 804896b:	eb eb                	jmp    0x8048958
 804896d:	5b                   	pop    %ebx
 804896e:	c3                   	ret    
 804896f:	57                   	push   %edi
 8048970:	56                   	push   %esi
 8048971:	53                   	push   %ebx
 8048972:	e8 55 fc ff ff       	call   0x80485cc
 8048977:	81 c3 f5 40 00 00    	add    $0x40f5,%ebx
 804897d:	8d b3 bc 00 00 00    	lea    0xbc(%ebx),%esi
 8048983:	8b 3e                	mov    (%esi),%edi
 8048985:	6a 00                	push   $0x0
 8048987:	e8 c3 0c 00 00       	call   0x804964f
 804898c:	59                   	pop    %ecx
 804898d:	85 c0                	test   %eax,%eax
 804898f:	75 09                	jne    0x804899a
 8048991:	66 81 b3 34 00 00 00 	xorw   $0x100,0x34(%ebx)
 8048998:	00 01 
 804899a:	6a 01                	push   $0x1
 804899c:	e8 ae 0c 00 00       	call   0x804964f
 80489a1:	5a                   	pop    %edx
 80489a2:	85 c0                	test   %eax,%eax
 80489a4:	75 09                	jne    0x80489af
 80489a6:	66 81 b3 58 00 00 00 	xorw   $0x100,0x58(%ebx)
 80489ad:	00 01 
 80489af:	89 3e                	mov    %edi,(%esi)
 80489b1:	5b                   	pop    %ebx
 80489b2:	5e                   	pop    %esi
 80489b3:	5f                   	pop    %edi
 80489b4:	c3                   	ret    
 80489b5:	53                   	push   %ebx
 80489b6:	8b 5c 24 08          	mov    0x8(%esp),%ebx
 80489ba:	8b 43 08             	mov    0x8(%ebx),%eax
 80489bd:	8b 53 10             	mov    0x10(%ebx),%edx
 80489c0:	29 c2                	sub    %eax,%edx
 80489c2:	74 0e                	je     0x80489d2
 80489c4:	89 43 10             	mov    %eax,0x10(%ebx)
 80489c7:	52                   	push   %edx
 80489c8:	50                   	push   %eax
 80489c9:	53                   	push   %ebx
 80489ca:	e8 71 10 00 00       	call   0x8049a40
 80489cf:	83 c4 0c             	add    $0xc,%esp
 80489d2:	8b 43 10             	mov    0x10(%ebx),%eax
 80489d5:	2b 43 08             	sub    0x8(%ebx),%eax
 80489d8:	5b                   	pop    %ebx
 80489d9:	c3                   	ret    
 80489da:	57                   	push   %edi
 80489db:	56                   	push   %esi
 80489dc:	53                   	push   %ebx
 80489dd:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 80489e1:	8b 74 24 14          	mov    0x14(%esp),%esi
 80489e5:	8b 7c 24 18          	mov    0x18(%esp),%edi
 80489e9:	f6 03 40             	testb  $0x40,(%ebx)
 80489ec:	74 14                	je     0x8048a02
 80489ee:	89 7c 24 18          	mov    %edi,0x18(%esp)
 80489f2:	89 74 24 14          	mov    %esi,0x14(%esp)
 80489f6:	89 5c 24 10          	mov    %ebx,0x10(%esp)
 80489fa:	5b                   	pop    %ebx
 80489fb:	5e                   	pop    %esi
 80489fc:	5f                   	pop    %edi
 80489fd:	e9 a0 00 00 00       	jmp    0x8048aa2
 8048a02:	53                   	push   %ebx
 8048a03:	e8 91 11 00 00       	call   0x8049b99
 8048a08:	5a                   	pop    %edx
 8048a09:	85 c0                	test   %eax,%eax
 8048a0b:	74 e1                	je     0x80489ee
 8048a0d:	83 c8 ff             	or     $0xffffffff,%eax
 8048a10:	5b                   	pop    %ebx
 8048a11:	5e                   	pop    %esi
 8048a12:	5f                   	pop    %edi
 8048a13:	c3                   	ret    
 8048a14:	55                   	push   %ebp
 8048a15:	57                   	push   %edi
 8048a16:	56                   	push   %esi
 8048a17:	53                   	push   %ebx
 8048a18:	53                   	push   %ebx
 8048a19:	89 c7                	mov    %eax,%edi
 8048a1b:	89 cb                	mov    %ecx,%ebx
 8048a1d:	88 54 24 03          	mov    %dl,0x3(%esp)
 8048a21:	89 ce                	mov    %ecx,%esi
 8048a23:	8d 6c 24 03          	lea    0x3(%esp),%ebp
 8048a27:	85 f6                	test   %esi,%esi
 8048a29:	74 12                	je     0x8048a3d
 8048a2b:	57                   	push   %edi
 8048a2c:	6a 01                	push   $0x1
 8048a2e:	55                   	push   %ebp
 8048a2f:	e8 8c 10 00 00       	call   0x8049ac0
 8048a34:	83 c4 0c             	add    $0xc,%esp
 8048a37:	48                   	dec    %eax
 8048a38:	75 03                	jne    0x8048a3d
 8048a3a:	4e                   	dec    %esi
 8048a3b:	eb ea                	jmp    0x8048a27
 8048a3d:	89 d8                	mov    %ebx,%eax
 8048a3f:	29 f0                	sub    %esi,%eax
 8048a41:	5a                   	pop    %edx
 8048a42:	5b                   	pop    %ebx
 8048a43:	5e                   	pop    %esi
 8048a44:	5f                   	pop    %edi
 8048a45:	5d                   	pop    %ebp
 8048a46:	c3                   	ret    
 8048a47:	55                   	push   %ebp
 8048a48:	57                   	push   %edi
 8048a49:	56                   	push   %esi
 8048a4a:	53                   	push   %ebx
 8048a4b:	8b 74 24 1c          	mov    0x1c(%esp),%esi
 8048a4f:	8b 7c 24 20          	mov    0x20(%esp),%edi
 8048a53:	f6 44 24 18 80       	testb  $0x80,0x18(%esp)
 8048a58:	74 29                	je     0x8048a83
 8048a5a:	57                   	push   %edi
 8048a5b:	e8 c2 0b 00 00       	call   0x8049622
 8048a60:	5a                   	pop    %edx
 8048a61:	89 c3                	mov    %eax,%ebx
 8048a63:	29 c6                	sub    %eax,%esi
 8048a65:	85 f6                	test   %esi,%esi
 8048a67:	7e 1c                	jle    0x8048a85
 8048a69:	8b 54 24 18          	mov    0x18(%esp),%edx
 8048a6d:	83 e2 7f             	and    $0x7f,%edx
 8048a70:	89 f1                	mov    %esi,%ecx
 8048a72:	8b 44 24 14          	mov    0x14(%esp),%eax
 8048a76:	e8 99 ff ff ff       	call   0x8048a14
 8048a7b:	89 c5                	mov    %eax,%ebp
 8048a7d:	39 c6                	cmp    %eax,%esi
 8048a7f:	75 1c                	jne    0x8048a9d
 8048a81:	eb 04                	jmp    0x8048a87
 8048a83:	89 f3                	mov    %esi,%ebx
 8048a85:	31 ed                	xor    %ebp,%ebp
 8048a87:	31 c0                	xor    %eax,%eax
 8048a89:	85 db                	test   %ebx,%ebx
 8048a8b:	7e 0e                	jle    0x8048a9b
 8048a8d:	ff 74 24 14          	pushl  0x14(%esp)
 8048a91:	53                   	push   %ebx
 8048a92:	57                   	push   %edi
 8048a93:	e8 28 10 00 00       	call   0x8049ac0
 8048a98:	83 c4 0c             	add    $0xc,%esp
 8048a9b:	01 e8                	add    %ebp,%eax
 8048a9d:	5b                   	pop    %ebx
 8048a9e:	5e                   	pop    %esi
 8048a9f:	5f                   	pop    %edi
 8048aa0:	5d                   	pop    %ebp
 8048aa1:	c3                   	ret    
 8048aa2:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 8048aa6:	83 e4 f8             	and    $0xfffffff8,%esp
 8048aa9:	ff 71 fc             	pushl  -0x4(%ecx)
 8048aac:	55                   	push   %ebp
 8048aad:	89 e5                	mov    %esp,%ebp
 8048aaf:	57                   	push   %edi
 8048ab0:	56                   	push   %esi
 8048ab1:	53                   	push   %ebx
 8048ab2:	51                   	push   %ecx
 8048ab3:	81 ec 60 01 00 00    	sub    $0x160,%esp
 8048ab9:	e8 3f fd ff ff       	call   0x80487fd
 8048abe:	05 ae 3f 00 00       	add    $0x3fae,%eax
 8048ac3:	89 85 9c fe ff ff    	mov    %eax,-0x164(%ebp)
 8048ac9:	8b 01                	mov    (%ecx),%eax
 8048acb:	89 85 a4 fe ff ff    	mov    %eax,-0x15c(%ebp)
 8048ad1:	8b 59 04             	mov    0x4(%ecx),%ebx
 8048ad4:	8b 79 08             	mov    0x8(%ecx),%edi
 8048ad7:	53                   	push   %ebx
 8048ad8:	8d b5 34 ff ff ff    	lea    -0xcc(%ebp),%esi
 8048ade:	56                   	push   %esi
 8048adf:	e8 10 05 00 00       	call   0x8048ff4
 8048ae4:	5a                   	pop    %edx
 8048ae5:	59                   	pop    %ecx
 8048ae6:	85 c0                	test   %eax,%eax
 8048ae8:	79 34                	jns    0x8048b1e
 8048aea:	8b 9d 34 ff ff ff    	mov    -0xcc(%ebp),%ebx
 8048af0:	53                   	push   %ebx
 8048af1:	e8 2c 0b 00 00       	call   0x8049622
 8048af6:	5f                   	pop    %edi
 8048af7:	c7 85 a8 fe ff ff ff 	movl   $0xffffffff,-0x158(%ebp)
 8048afe:	ff ff ff 
 8048b01:	85 c0                	test   %eax,%eax
 8048b03:	0f 84 d9 04 00 00    	je     0x8048fe2
 8048b09:	ff b5 a4 fe ff ff    	pushl  -0x15c(%ebp)
 8048b0f:	50                   	push   %eax
 8048b10:	53                   	push   %ebx
 8048b11:	e8 aa 0f 00 00       	call   0x8049ac0
 8048b16:	83 c4 0c             	add    $0xc,%esp
 8048b19:	e9 c4 04 00 00       	jmp    0x8048fe2
 8048b1e:	57                   	push   %edi
 8048b1f:	56                   	push   %esi
 8048b20:	e8 35 05 00 00       	call   0x804905a
 8048b25:	59                   	pop    %ecx
 8048b26:	5e                   	pop    %esi
 8048b27:	89 da                	mov    %ebx,%edx
 8048b29:	c7 85 a8 fe ff ff 00 	movl   $0x0,-0x158(%ebp)
 8048b30:	00 00 00 
 8048b33:	8b 85 9c fe ff ff    	mov    -0x164(%ebp),%eax
 8048b39:	8d 80 24 df ff ff    	lea    -0x20dc(%eax),%eax
 8048b3f:	89 85 94 fe ff ff    	mov    %eax,-0x16c(%ebp)
 8048b45:	8b 85 9c fe ff ff    	mov    -0x164(%ebp),%eax
 8048b4b:	8d 80 1a df ff ff    	lea    -0x20e6(%eax),%eax
 8048b51:	89 85 98 fe ff ff    	mov    %eax,-0x168(%ebp)
 8048b57:	8a 03                	mov    (%ebx),%al
 8048b59:	84 c0                	test   %al,%al
 8048b5b:	74 07                	je     0x8048b64
 8048b5d:	3c 25                	cmp    $0x25,%al
 8048b5f:	74 03                	je     0x8048b64
 8048b61:	43                   	inc    %ebx
 8048b62:	eb f3                	jmp    0x8048b57
 8048b64:	39 d3                	cmp    %edx,%ebx
 8048b66:	74 28                	je     0x8048b90
 8048b68:	89 de                	mov    %ebx,%esi
 8048b6a:	29 d6                	sub    %edx,%esi
 8048b6c:	31 c0                	xor    %eax,%eax
 8048b6e:	85 f6                	test   %esi,%esi
 8048b70:	7e 10                	jle    0x8048b82
 8048b72:	ff b5 a4 fe ff ff    	pushl  -0x15c(%ebp)
 8048b78:	56                   	push   %esi
 8048b79:	52                   	push   %edx
 8048b7a:	e8 41 0f 00 00       	call   0x8049ac0
 8048b7f:	83 c4 0c             	add    $0xc,%esp
 8048b82:	39 f0                	cmp    %esi,%eax
 8048b84:	0f 85 4e 04 00 00    	jne    0x8048fd8
 8048b8a:	01 85 a8 fe ff ff    	add    %eax,-0x158(%ebp)
 8048b90:	80 3b 00             	cmpb   $0x0,(%ebx)
 8048b93:	0f 84 49 04 00 00    	je     0x8048fe2
 8048b99:	80 7b 01 25          	cmpb   $0x25,0x1(%ebx)
 8048b9d:	8d 53 01             	lea    0x1(%ebx),%edx
 8048ba0:	0f 84 2a 04 00 00    	je     0x8048fd0
 8048ba6:	89 95 34 ff ff ff    	mov    %edx,-0xcc(%ebp)
 8048bac:	8d 9d 34 ff ff ff    	lea    -0xcc(%ebp),%ebx
 8048bb2:	53                   	push   %ebx
 8048bb3:	e8 fc 05 00 00       	call   0x80491b4
 8048bb8:	53                   	push   %ebx
 8048bb9:	e8 d5 04 00 00       	call   0x8049093
 8048bbe:	0f b6 bd 5a ff ff ff 	movzbl -0xa6(%ebp),%edi
 8048bc5:	58                   	pop    %eax
 8048bc6:	5a                   	pop    %edx
 8048bc7:	83 bd 4c ff ff ff 00 	cmpl   $0x0,-0xb4(%ebp)
 8048bce:	8d 45 84             	lea    -0x7c(%ebp),%eax
 8048bd1:	7e 07                	jle    0x8048bda
 8048bd3:	6b d7 0c             	imul   $0xc,%edi,%edx
 8048bd6:	8d 44 10 f4          	lea    -0xc(%eax,%edx,1),%eax
 8048bda:	8b 8d 50 ff ff ff    	mov    -0xb0(%ebp),%ecx
 8048be0:	31 d2                	xor    %edx,%edx
 8048be2:	89 c3                	mov    %eax,%ebx
 8048be4:	83 c0 0c             	add    $0xc,%eax
 8048be7:	39 ca                	cmp    %ecx,%edx
 8048be9:	7d 09                	jge    0x8048bf4
 8048beb:	42                   	inc    %edx
 8048bec:	89 9d a0 fe ff ff    	mov    %ebx,-0x160(%ebp)
 8048bf2:	eb ee                	jmp    0x8048be2
 8048bf4:	8b 85 54 ff ff ff    	mov    -0xac(%ebp),%eax
 8048bfa:	85 c0                	test   %eax,%eax
 8048bfc:	75 2a                	jne    0x8048c28
 8048bfe:	8b 85 a8 fe ff ff    	mov    -0x158(%ebp),%eax
 8048c04:	99                   	cltd   
 8048c05:	52                   	push   %edx
 8048c06:	50                   	push   %eax
 8048c07:	8b 85 44 ff ff ff    	mov    -0xbc(%ebp),%eax
 8048c0d:	25 00 0f 00 00       	and    $0xf00,%eax
 8048c12:	50                   	push   %eax
 8048c13:	8b 85 a0 fe ff ff    	mov    -0x160(%ebp),%eax
 8048c19:	ff 30                	pushl  (%eax)
 8048c1b:	e8 5f 10 00 00       	call   0x8049c7f
 8048c20:	83 c4 10             	add    $0x10,%esp
 8048c23:	e9 9b 03 00 00       	jmp    0x8048fc3
 8048c28:	83 f8 07             	cmp    $0x7,%eax
 8048c2b:	0f 87 a5 01 00 00    	ja     0x8048dd6
 8048c31:	8b 8d 9c fe ff ff    	mov    -0x164(%ebp),%ecx
 8048c37:	0f b6 b4 01 2f df ff 	movzbl -0x20d1(%ecx,%eax,1),%esi
 8048c3e:	ff 
 8048c3f:	bb 57 00 00 00       	mov    $0x57,%ebx
 8048c44:	83 fe 0a             	cmp    $0xa,%esi
 8048c47:	75 1e                	jne    0x8048c67
 8048c49:	8b 8d 44 ff ff ff    	mov    -0xbc(%ebp),%ecx
 8048c4f:	89 ca                	mov    %ecx,%edx
 8048c51:	83 e2 20             	and    $0x20,%edx
 8048c54:	83 fa 01             	cmp    $0x1,%edx
 8048c57:	19 db                	sbb    %ebx,%ebx
 8048c59:	83 e3 2b             	and    $0x2b,%ebx
 8048c5c:	83 c3 2c             	add    $0x2c,%ebx
 8048c5f:	80 e1 40             	and    $0x40,%cl
 8048c62:	74 03                	je     0x8048c67
 8048c64:	80 cb 80             	or     $0x80,%bl
 8048c67:	83 f8 05             	cmp    $0x5,%eax
 8048c6a:	77 1d                	ja     0x8048c89
 8048c6c:	83 f8 03             	cmp    $0x3,%eax
 8048c6f:	74 11                	je     0x8048c82
 8048c71:	c7 85 b0 fe ff ff 06 	movl   $0x6,-0x150(%ebp)
 8048c78:	00 00 00 
 8048c7b:	83 f8 01             	cmp    $0x1,%eax
 8048c7e:	75 0b                	jne    0x8048c8b
 8048c80:	eb 13                	jmp    0x8048c95
 8048c82:	bb 37 00 00 00       	mov    $0x37,%ebx
 8048c87:	eb 02                	jmp    0x8048c8b
 8048c89:	f7 de                	neg    %esi
 8048c8b:	c7 85 b0 fe ff ff 0b 	movl   $0xb,-0x150(%ebp)
 8048c92:	00 00 00 
 8048c95:	b1 20                	mov    $0x20,%cl
 8048c97:	83 bd 38 ff ff ff 00 	cmpl   $0x0,-0xc8(%ebp)
 8048c9e:	79 06                	jns    0x8048ca6
 8048ca0:	8a 8d 48 ff ff ff    	mov    -0xb8(%ebp),%cl
 8048ca6:	ba 00 04 00 00       	mov    $0x400,%edx
 8048cab:	48                   	dec    %eax
 8048cac:	74 0d                	je     0x8048cbb
 8048cae:	8b 94 bd 58 ff ff ff 	mov    -0xa8(%ebp,%edi,4),%edx
 8048cb5:	81 e2 00 0f 00 00    	and    $0xf00,%edx
 8048cbb:	88 8d ac fe ff ff    	mov    %cl,-0x154(%ebp)
 8048cc1:	56                   	push   %esi
 8048cc2:	ff b5 a0 fe ff ff    	pushl  -0x160(%ebp)
 8048cc8:	52                   	push   %edx
 8048cc9:	e8 54 0f 00 00       	call   0x8049c22
 8048cce:	53                   	push   %ebx
 8048ccf:	56                   	push   %esi
 8048cd0:	52                   	push   %edx
 8048cd1:	50                   	push   %eax
 8048cd2:	8d 85 33 ff ff ff    	lea    -0xcd(%ebp),%eax
 8048cd8:	50                   	push   %eax
 8048cd9:	e8 de 0f 00 00       	call   0x8049cbc
 8048cde:	89 c7                	mov    %eax,%edi
 8048ce0:	8b 85 54 ff ff ff    	mov    -0xac(%ebp),%eax
 8048ce6:	83 c4 20             	add    $0x20,%esp
 8048ce9:	83 f8 05             	cmp    $0x5,%eax
 8048cec:	8a 8d ac fe ff ff    	mov    -0x154(%ebp),%cl
 8048cf2:	76 3f                	jbe    0x8048d33
 8048cf4:	80 3f 2d             	cmpb   $0x2d,(%edi)
 8048cf7:	75 14                	jne    0x8048d0d
 8048cf9:	83 8d 44 ff ff ff 02 	orl    $0x2,-0xbc(%ebp)
 8048d00:	47                   	inc    %edi
 8048d01:	c7 85 b0 fe ff ff 02 	movl   $0x2,-0x150(%ebp)
 8048d08:	00 00 00 
 8048d0b:	eb 26                	jmp    0x8048d33
 8048d0d:	8b 95 44 ff ff ff    	mov    -0xbc(%ebp),%edx
 8048d13:	f6 c2 02             	test   $0x2,%dl
 8048d16:	75 11                	jne    0x8048d29
 8048d18:	80 e2 01             	and    $0x1,%dl
 8048d1b:	74 16                	je     0x8048d33
 8048d1d:	c7 85 b0 fe ff ff 04 	movl   $0x4,-0x150(%ebp)
 8048d24:	00 00 00 
 8048d27:	eb 0a                	jmp    0x8048d33
 8048d29:	c7 85 b0 fe ff ff 00 	movl   $0x0,-0x150(%ebp)
 8048d30:	00 00 00 
 8048d33:	8d b5 33 ff ff ff    	lea    -0xcd(%ebp),%esi
 8048d39:	29 fe                	sub    %edi,%esi
 8048d3b:	8b 9d 38 ff ff ff    	mov    -0xc8(%ebp),%ebx
 8048d41:	85 db                	test   %ebx,%ebx
 8048d43:	79 05                	jns    0x8048d4a
 8048d45:	bb 01 00 00 00       	mov    $0x1,%ebx
 8048d4a:	f6 85 44 ff ff ff 10 	testb  $0x10,-0xbc(%ebp)
 8048d51:	74 38                	je     0x8048d8b
 8048d53:	83 f8 02             	cmp    $0x2,%eax
 8048d56:	76 1d                	jbe    0x8048d75
 8048d58:	83 f8 03             	cmp    $0x3,%eax
 8048d5b:	74 24                	je     0x8048d81
 8048d5d:	83 f8 04             	cmp    $0x4,%eax
 8048d60:	75 29                	jne    0x8048d8b
 8048d62:	39 de                	cmp    %ebx,%esi
 8048d64:	72 25                	jb     0x8048d8b
 8048d66:	bb 01 00 00 00       	mov    $0x1,%ebx
 8048d6b:	80 3f 30             	cmpb   $0x30,(%edi)
 8048d6e:	74 1b                	je     0x8048d8b
 8048d70:	8d 5e 01             	lea    0x1(%esi),%ebx
 8048d73:	eb 16                	jmp    0x8048d8b
 8048d75:	c7 85 b0 fe ff ff 06 	movl   $0x6,-0x150(%ebp)
 8048d7c:	00 00 00 
 8048d7f:	eb 0a                	jmp    0x8048d8b
 8048d81:	c7 85 b0 fe ff ff 09 	movl   $0x9,-0x150(%ebp)
 8048d88:	00 00 00 
 8048d8b:	80 3f 30             	cmpb   $0x30,(%edi)
 8048d8e:	75 37                	jne    0x8048dc7
 8048d90:	83 bd b0 fe ff ff 05 	cmpl   $0x5,-0x150(%ebp)
 8048d97:	7e 0a                	jle    0x8048da3
 8048d99:	c7 85 b0 fe ff ff 0b 	movl   $0xb,-0x150(%ebp)
 8048da0:	00 00 00 
 8048da3:	48                   	dec    %eax
 8048da4:	74 0b                	je     0x8048db1
 8048da6:	85 db                	test   %ebx,%ebx
 8048da8:	75 1d                	jne    0x8048dc7
 8048daa:	31 f6                	xor    %esi,%esi
 8048dac:	e9 12 01 00 00       	jmp    0x8048ec3
 8048db1:	8b 85 9c fe ff ff    	mov    -0x164(%ebp),%eax
 8048db7:	8d b8 14 df ff ff    	lea    -0x20ec(%eax),%edi
 8048dbd:	be 05 00 00 00       	mov    $0x5,%esi
 8048dc2:	e9 fc 00 00 00       	jmp    0x8048ec3
 8048dc7:	39 f3                	cmp    %esi,%ebx
 8048dc9:	0f 86 f4 00 00 00    	jbe    0x8048ec3
 8048dcf:	29 f3                	sub    %esi,%ebx
 8048dd1:	e9 ef 00 00 00       	jmp    0x8048ec5
 8048dd6:	83 f8 0f             	cmp    $0xf,%eax
 8048dd9:	77 50                	ja     0x8048e2b
 8048ddb:	8b 85 a0 fe ff ff    	mov    -0x160(%ebp),%eax
 8048de1:	f6 85 45 ff ff ff 08 	testb  $0x8,-0xbb(%ebp)
 8048de8:	74 04                	je     0x8048dee
 8048dea:	db 28                	fldt   (%eax)
 8048dec:	eb 02                	jmp    0x8048df0
 8048dee:	dd 00                	fldl   (%eax)
 8048df0:	8b 85 9c fe ff ff    	mov    -0x164(%ebp),%eax
 8048df6:	8d 80 db bf ff ff    	lea    -0x4025(%eax),%eax
 8048dfc:	50                   	push   %eax
 8048dfd:	8d 85 38 ff ff ff    	lea    -0xc8(%ebp),%eax
 8048e03:	50                   	push   %eax
 8048e04:	83 ec 0c             	sub    $0xc,%esp
 8048e07:	db 3c 24             	fstpt  (%esp)
 8048e0a:	ff b5 a4 fe ff ff    	pushl  -0x15c(%ebp)
 8048e10:	e8 66 0f 00 00       	call   0x8049d7b
 8048e15:	83 c4 18             	add    $0x18,%esp
 8048e18:	85 c0                	test   %eax,%eax
 8048e1a:	0f 88 b8 01 00 00    	js     0x8048fd8
 8048e20:	01 85 a8 fe ff ff    	add    %eax,-0x158(%ebp)
 8048e26:	e9 98 01 00 00       	jmp    0x8048fc3
 8048e2b:	8d 50 ee             	lea    -0x12(%eax),%edx
 8048e2e:	83 fa 01             	cmp    $0x1,%edx
 8048e31:	0f 87 a1 01 00 00    	ja     0x8048fd8
 8048e37:	83 f8 13             	cmp    $0x13,%eax
 8048e3a:	8b 85 a0 fe ff ff    	mov    -0x160(%ebp),%eax
 8048e40:	75 57                	jne    0x8048e99
 8048e42:	8b 38                	mov    (%eax),%edi
 8048e44:	85 ff                	test   %edi,%edi
 8048e46:	74 28                	je     0x8048e70
 8048e48:	8b 95 38 ff ff ff    	mov    -0xc8(%ebp),%edx
 8048e4e:	83 c8 ff             	or     $0xffffffff,%eax
 8048e51:	85 d2                	test   %edx,%edx
 8048e53:	78 02                	js     0x8048e57
 8048e55:	89 d0                	mov    %edx,%eax
 8048e57:	50                   	push   %eax
 8048e58:	57                   	push   %edi
 8048e59:	e8 d7 07 00 00       	call   0x8049635
 8048e5e:	5b                   	pop    %ebx
 8048e5f:	5e                   	pop    %esi
 8048e60:	89 c6                	mov    %eax,%esi
 8048e62:	b1 20                	mov    $0x20,%cl
 8048e64:	c7 85 b0 fe ff ff 0b 	movl   $0xb,-0x150(%ebp)
 8048e6b:	00 00 00 
 8048e6e:	eb 53                	jmp    0x8048ec3
 8048e70:	8b bd 98 fe ff ff    	mov    -0x168(%ebp),%edi
 8048e76:	b1 20                	mov    $0x20,%cl
 8048e78:	31 f6                	xor    %esi,%esi
 8048e7a:	83 bd 38 ff ff ff 05 	cmpl   $0x5,-0xc8(%ebp)
 8048e81:	c7 85 b0 fe ff ff 0b 	movl   $0xb,-0x150(%ebp)
 8048e88:	00 00 00 
 8048e8b:	bb 00 00 00 00       	mov    $0x0,%ebx
 8048e90:	76 33                	jbe    0x8048ec5
 8048e92:	be 06 00 00 00       	mov    $0x6,%esi
 8048e97:	eb 2c                	jmp    0x8048ec5
 8048e99:	8b 00                	mov    (%eax),%eax
 8048e9b:	88 85 b4 fe ff ff    	mov    %al,-0x14c(%ebp)
 8048ea1:	c6 85 b5 fe ff ff 00 	movb   $0x0,-0x14b(%ebp)
 8048ea8:	8d bd b4 fe ff ff    	lea    -0x14c(%ebp),%edi
 8048eae:	b1 20                	mov    $0x20,%cl
 8048eb0:	c7 85 b0 fe ff ff 0b 	movl   $0xb,-0x150(%ebp)
 8048eb7:	00 00 00 
 8048eba:	31 db                	xor    %ebx,%ebx
 8048ebc:	be 01 00 00 00       	mov    $0x1,%esi
 8048ec1:	eb 02                	jmp    0x8048ec5
 8048ec3:	31 db                	xor    %ebx,%ebx
 8048ec5:	8d 04 33             	lea    (%ebx,%esi,1),%eax
 8048ec8:	83 bd b0 fe ff ff 0b 	cmpl   $0xb,-0x150(%ebp)
 8048ecf:	74 10                	je     0x8048ee1
 8048ed1:	31 d2                	xor    %edx,%edx
 8048ed3:	83 bd b0 fe ff ff 06 	cmpl   $0x6,-0x150(%ebp)
 8048eda:	0f 9d c2             	setge  %dl
 8048edd:	8d 44 10 01          	lea    0x1(%eax,%edx,1),%eax
 8048ee1:	8b 95 3c ff ff ff    	mov    -0xc4(%ebp),%edx
 8048ee7:	c7 85 ac fe ff ff 00 	movl   $0x0,-0x154(%ebp)
 8048eee:	00 00 00 
 8048ef1:	39 c2                	cmp    %eax,%edx
 8048ef3:	76 08                	jbe    0x8048efd
 8048ef5:	29 c2                	sub    %eax,%edx
 8048ef7:	89 95 ac fe ff ff    	mov    %edx,-0x154(%ebp)
 8048efd:	03 85 a8 fe ff ff    	add    -0x158(%ebp),%eax
 8048f03:	03 85 ac fe ff ff    	add    -0x154(%ebp),%eax
 8048f09:	89 85 a8 fe ff ff    	mov    %eax,-0x158(%ebp)
 8048f0f:	80 f9 30             	cmp    $0x30,%cl
 8048f12:	75 10                	jne    0x8048f24
 8048f14:	03 9d ac fe ff ff    	add    -0x154(%ebp),%ebx
 8048f1a:	c7 85 ac fe ff ff 00 	movl   $0x0,-0x154(%ebp)
 8048f21:	00 00 00 
 8048f24:	f6 85 44 ff ff ff 08 	testb  $0x8,-0xbc(%ebp)
 8048f2b:	75 2c                	jne    0x8048f59
 8048f2d:	8b 8d ac fe ff ff    	mov    -0x154(%ebp),%ecx
 8048f33:	ba 20 00 00 00       	mov    $0x20,%edx
 8048f38:	8b 85 a4 fe ff ff    	mov    -0x15c(%ebp),%eax
 8048f3e:	e8 d1 fa ff ff       	call   0x8048a14
 8048f43:	39 85 ac fe ff ff    	cmp    %eax,-0x154(%ebp)
 8048f49:	0f 85 89 00 00 00    	jne    0x8048fd8
 8048f4f:	c7 85 ac fe ff ff 00 	movl   $0x0,-0x154(%ebp)
 8048f56:	00 00 00 
 8048f59:	ff b5 a4 fe ff ff    	pushl  -0x15c(%ebp)
 8048f5f:	8b 85 b0 fe ff ff    	mov    -0x150(%ebp),%eax
 8048f65:	03 85 94 fe ff ff    	add    -0x16c(%ebp),%eax
 8048f6b:	50                   	push   %eax
 8048f6c:	e8 d4 05 00 00       	call   0x8049545
 8048f71:	89 d9                	mov    %ebx,%ecx
 8048f73:	ba 30 00 00 00       	mov    $0x30,%edx
 8048f78:	8b 85 a4 fe ff ff    	mov    -0x15c(%ebp),%eax
 8048f7e:	e8 91 fa ff ff       	call   0x8048a14
 8048f83:	5a                   	pop    %edx
 8048f84:	59                   	pop    %ecx
 8048f85:	39 c3                	cmp    %eax,%ebx
 8048f87:	75 4f                	jne    0x8048fd8
 8048f89:	85 f6                	test   %esi,%esi
 8048f8b:	75 20                	jne    0x8048fad
 8048f8d:	8b 8d ac fe ff ff    	mov    -0x154(%ebp),%ecx
 8048f93:	ba 20 00 00 00       	mov    $0x20,%edx
 8048f98:	8b 85 a4 fe ff ff    	mov    -0x15c(%ebp),%eax
 8048f9e:	e8 71 fa ff ff       	call   0x8048a14
 8048fa3:	39 85 ac fe ff ff    	cmp    %eax,-0x154(%ebp)
 8048fa9:	74 18                	je     0x8048fc3
 8048fab:	eb 2b                	jmp    0x8048fd8
 8048fad:	ff b5 a4 fe ff ff    	pushl  -0x15c(%ebp)
 8048fb3:	56                   	push   %esi
 8048fb4:	57                   	push   %edi
 8048fb5:	e8 06 0b 00 00       	call   0x8049ac0
 8048fba:	83 c4 0c             	add    $0xc,%esp
 8048fbd:	39 c6                	cmp    %eax,%esi
 8048fbf:	75 17                	jne    0x8048fd8
 8048fc1:	eb ca                	jmp    0x8048f8d
 8048fc3:	8b 9d 34 ff ff ff    	mov    -0xcc(%ebp),%ebx
 8048fc9:	89 da                	mov    %ebx,%edx
 8048fcb:	e9 87 fb ff ff       	jmp    0x8048b57
 8048fd0:	83 c3 02             	add    $0x2,%ebx
 8048fd3:	e9 7f fb ff ff       	jmp    0x8048b57
 8048fd8:	c7 85 a8 fe ff ff ff 	movl   $0xffffffff,-0x158(%ebp)
 8048fdf:	ff ff ff 
 8048fe2:	8b 85 a8 fe ff ff    	mov    -0x158(%ebp),%eax
 8048fe8:	8d 65 f0             	lea    -0x10(%ebp),%esp
 8048feb:	59                   	pop    %ecx
 8048fec:	5b                   	pop    %ebx
 8048fed:	5e                   	pop    %esi
 8048fee:	5f                   	pop    %edi
 8048fef:	5d                   	pop    %ebp
 8048ff0:	8d 61 fc             	lea    -0x4(%ecx),%esp
 8048ff3:	c3                   	ret    
 8048ff4:	57                   	push   %edi
 8048ff5:	56                   	push   %esi
 8048ff6:	53                   	push   %ebx
 8048ff7:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 8048ffb:	8b 74 24 14          	mov    0x14(%esp),%esi
 8048fff:	b9 2f 00 00 00       	mov    $0x2f,%ecx
 8049004:	89 df                	mov    %ebx,%edi
 8049006:	31 c0                	xor    %eax,%eax
 8049008:	f3 ab                	rep stos %eax,%es:(%edi)
 804900a:	ff 4b 18             	decl   0x18(%ebx)
 804900d:	89 33                	mov    %esi,(%ebx)
 804900f:	8d 53 28             	lea    0x28(%ebx),%edx
 8049012:	c7 04 02 08 00 00 00 	movl   $0x8,(%edx,%eax,1)
 8049019:	83 c0 04             	add    $0x4,%eax
 804901c:	83 f8 24             	cmp    $0x24,%eax
 804901f:	75 f1                	jne    0x8049012
 8049021:	89 f0                	mov    %esi,%eax
 8049023:	8a 10                	mov    (%eax),%dl
 8049025:	84 d2                	test   %dl,%dl
 8049027:	74 24                	je     0x804904d
 8049029:	80 fa 25             	cmp    $0x25,%dl
 804902c:	75 1c                	jne    0x804904a
 804902e:	8d 50 01             	lea    0x1(%eax),%edx
 8049031:	80 78 01 25          	cmpb   $0x25,0x1(%eax)
 8049035:	74 11                	je     0x8049048
 8049037:	89 13                	mov    %edx,(%ebx)
 8049039:	53                   	push   %ebx
 804903a:	e8 75 01 00 00       	call   0x80491b4
 804903f:	5a                   	pop    %edx
 8049040:	85 c0                	test   %eax,%eax
 8049042:	78 0f                	js     0x8049053
 8049044:	8b 03                	mov    (%ebx),%eax
 8049046:	eb db                	jmp    0x8049023
 8049048:	89 d0                	mov    %edx,%eax
 804904a:	40                   	inc    %eax
 804904b:	eb d6                	jmp    0x8049023
 804904d:	89 33                	mov    %esi,(%ebx)
 804904f:	31 c0                	xor    %eax,%eax
 8049051:	eb 03                	jmp    0x8049056
 8049053:	83 c8 ff             	or     $0xffffffff,%eax
 8049056:	5b                   	pop    %ebx
 8049057:	5e                   	pop    %esi
 8049058:	5f                   	pop    %edi
 8049059:	c3                   	ret    
 804905a:	56                   	push   %esi
 804905b:	53                   	push   %ebx
 804905c:	8b 5c 24 0c          	mov    0xc(%esp),%ebx
 8049060:	8b 44 24 10          	mov    0x10(%esp),%eax
 8049064:	89 43 4c             	mov    %eax,0x4c(%ebx)
 8049067:	8b 73 18             	mov    0x18(%ebx),%esi
 804906a:	85 f6                	test   %esi,%esi
 804906c:	7e 22                	jle    0x8049090
 804906e:	89 73 1c             	mov    %esi,0x1c(%ebx)
 8049071:	c7 43 18 00 00 00 00 	movl   $0x0,0x18(%ebx)
 8049078:	c7 43 04 00 00 00 00 	movl   $0x0,0x4(%ebx)
 804907f:	c7 43 08 00 00 00 00 	movl   $0x0,0x8(%ebx)
 8049086:	53                   	push   %ebx
 8049087:	e8 07 00 00 00       	call   0x8049093
 804908c:	89 73 18             	mov    %esi,0x18(%ebx)
 804908f:	58                   	pop    %eax
 8049090:	5b                   	pop    %ebx
 8049091:	5e                   	pop    %esi
 8049092:	c3                   	ret    
 8049093:	8d 4c 24 04          	lea    0x4(%esp),%ecx
 8049097:	83 e4 f8             	and    $0xfffffff8,%esp
 804909a:	ff 71 fc             	pushl  -0x4(%ecx)
 804909d:	55                   	push   %ebp
 804909e:	89 e5                	mov    %esp,%ebp
 80490a0:	56                   	push   %esi
 80490a1:	53                   	push   %ebx
 80490a2:	51                   	push   %ecx
 80490a3:	8b 09                	mov    (%ecx),%ecx
 80490a5:	8d 59 50             	lea    0x50(%ecx),%ebx
 80490a8:	83 79 18 00          	cmpl   $0x0,0x18(%ecx)
 80490ac:	0f 85 ad 00 00 00    	jne    0x804915f
 80490b2:	81 79 08 00 00 00 80 	cmpl   $0x80000000,0x8(%ecx)
 80490b9:	75 11                	jne    0x80490cc
 80490bb:	8b 41 4c             	mov    0x4c(%ecx),%eax
 80490be:	8d 50 04             	lea    0x4(%eax),%edx
 80490c1:	89 51 4c             	mov    %edx,0x4c(%ecx)
 80490c4:	8b 00                	mov    (%eax),%eax
 80490c6:	89 41 50             	mov    %eax,0x50(%ecx)
 80490c9:	89 41 08             	mov    %eax,0x8(%ecx)
 80490cc:	81 79 04 00 00 00 80 	cmpl   $0x80000000,0x4(%ecx)
 80490d3:	75 11                	jne    0x80490e6
 80490d5:	8b 41 4c             	mov    0x4c(%ecx),%eax
 80490d8:	8d 50 04             	lea    0x4(%eax),%edx
 80490db:	89 51 4c             	mov    %edx,0x4c(%ecx)
 80490de:	8b 00                	mov    (%eax),%eax
 80490e0:	89 41 50             	mov    %eax,0x50(%ecx)
 80490e3:	89 41 04             	mov    %eax,0x4(%ecx)
 80490e6:	31 f6                	xor    %esi,%esi
 80490e8:	3b 71 1c             	cmp    0x1c(%ecx),%esi
 80490eb:	0f 8d 9c 00 00 00    	jge    0x804918d
 80490f1:	46                   	inc    %esi
 80490f2:	8b 54 b1 24          	mov    0x24(%ecx,%esi,4),%edx
 80490f6:	83 fa 08             	cmp    $0x8,%edx
 80490f9:	74 ed                	je     0x80490e8
 80490fb:	8b 41 4c             	mov    0x4c(%ecx),%eax
 80490fe:	7f 18                	jg     0x8049118
 8049100:	83 fa 02             	cmp    $0x2,%edx
 8049103:	74 4b                	je     0x8049150
 8049105:	7e 49                	jle    0x8049150
 8049107:	83 fa 07             	cmp    $0x7,%edx
 804910a:	75 44                	jne    0x8049150
 804910c:	8d 50 08             	lea    0x8(%eax),%edx
 804910f:	89 51 4c             	mov    %edx,0x4c(%ecx)
 8049112:	dd 00                	fldl   (%eax)
 8049114:	dd 1b                	fstpl  (%ebx)
 8049116:	eb 42                	jmp    0x804915a
 8049118:	81 fa 00 04 00 00    	cmp    $0x400,%edx
 804911e:	74 30                	je     0x8049150
 8049120:	7e 2e                	jle    0x8049150
 8049122:	81 fa 00 08 00 00    	cmp    $0x800,%edx
 8049128:	74 14                	je     0x804913e
 804912a:	81 fa 07 08 00 00    	cmp    $0x807,%edx
 8049130:	75 1e                	jne    0x8049150
 8049132:	8d 50 0c             	lea    0xc(%eax),%edx
 8049135:	89 51 4c             	mov    %edx,0x4c(%ecx)
 8049138:	db 28                	fldt   (%eax)
 804913a:	db 3b                	fstpt  (%ebx)
 804913c:	eb 1c                	jmp    0x804915a
 804913e:	8d 50 08             	lea    0x8(%eax),%edx
 8049141:	89 51 4c             	mov    %edx,0x4c(%ecx)
 8049144:	8b 50 04             	mov    0x4(%eax),%edx
 8049147:	8b 00                	mov    (%eax),%eax
 8049149:	89 03                	mov    %eax,(%ebx)
 804914b:	89 53 04             	mov    %edx,0x4(%ebx)
 804914e:	eb 0a                	jmp    0x804915a
 8049150:	8d 50 04             	lea    0x4(%eax),%edx
 8049153:	89 51 4c             	mov    %edx,0x4c(%ecx)
 8049156:	8b 00                	mov    (%eax),%eax
 8049158:	89 03                	mov    %eax,(%ebx)
 804915a:	83 c3 0c             	add    $0xc,%ebx
 804915d:	eb 89                	jmp    0x80490e8
 804915f:	81 79 08 00 00 00 80 	cmpl   $0x80000000,0x8(%ecx)
 8049166:	75 0e                	jne    0x8049176
 8049168:	0f b6 41 24          	movzbl 0x24(%ecx),%eax
 804916c:	6b c0 0c             	imul   $0xc,%eax,%eax
 804916f:	8b 44 03 f4          	mov    -0xc(%ebx,%eax,1),%eax
 8049173:	89 41 08             	mov    %eax,0x8(%ecx)
 8049176:	81 79 04 00 00 00 80 	cmpl   $0x80000000,0x4(%ecx)
 804917d:	75 0e                	jne    0x804918d
 804917f:	0f b6 41 25          	movzbl 0x25(%ecx),%eax
 8049183:	6b c0 0c             	imul   $0xc,%eax,%eax
 8049186:	8b 44 03 f4          	mov    -0xc(%ebx,%eax,1),%eax
 804918a:	89 41 04             	mov    %eax,0x4(%ecx)
 804918d:	8b 41 08             	mov    0x8(%ecx),%eax
 8049190:	85 c0                	test   %eax,%eax
 8049192:	79 18                	jns    0x80491ac
 8049194:	f7 d8                	neg    %eax
 8049196:	89 41 08             	mov    %eax,0x8(%ecx)
 8049199:	8b 41 10             	mov    0x10(%ecx),%eax
 804919c:	83 e0 fe             	and    $0xfffffffe,%eax
 804919f:	83 c8 08             	or     $0x8,%eax
 80491a2:	89 41 10             	mov    %eax,0x10(%ecx)
 80491a5:	c7 41 14 20 00 00 00 	movl   $0x20,0x14(%ecx)
 80491ac:	59                   	pop    %ecx
 80491ad:	5b                   	pop    %ebx
 80491ae:	5e                   	pop    %esi
 80491af:	5d                   	pop    %ebp
 80491b0:	8d 61 fc             	lea    -0x4(%ecx),%esp
 80491b3:	c3                   	ret    
 80491b4:	55                   	push   %ebp
 80491b5:	57                   	push   %edi
 80491b6:	56                   	push   %esi
 80491b7:	53                   	push   %ebx
 80491b8:	83 ec 30             	sub    $0x30,%esp
 80491bb:	e8 90 f5 ff ff       	call   0x8048750
 80491c0:	81 c7 ac 38 00 00    	add    $0x38ac,%edi
 80491c6:	8b 44 24 44          	mov    0x44(%esp),%eax
 80491ca:	89 04 24             	mov    %eax,(%esp)
 80491cd:	c7 44 24 24 00 00 00 	movl   $0x0,0x24(%esp)
 80491d4:	00 
 80491d5:	c7 44 24 28 00 00 00 	movl   $0x0,0x28(%esp)
 80491dc:	00 
 80491dd:	c7 44 24 18 08 00 00 	movl   $0x8,0x18(%esp)
 80491e4:	00 
 80491e5:	c7 44 24 1c 08 00 00 	movl   $0x8,0x1c(%esp)
 80491ec:	00 
 80491ed:	8b 40 18             	mov    0x18(%eax),%eax
 80491f0:	89 44 24 04          	mov    %eax,0x4(%esp)
 80491f4:	8b 04 24             	mov    (%esp),%eax
 80491f7:	8b 18                	mov    (%eax),%ebx
 80491f9:	8b 87 a0 00 00 00    	mov    0xa0(%edi),%eax
 80491ff:	89 c5                	mov    %eax,%ebp
 8049201:	31 f6                	xor    %esi,%esi
 8049203:	c7 44 24 08 00 00 00 	movl   $0x0,0x8(%esp)
 804920a:	00 
 804920b:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
 8049212:	00 
 8049213:	8a 03                	mov    (%ebx),%al
 8049215:	88 44 24 10          	mov    %al,0x10(%esp)
 8049219:	89 d8                	mov    %ebx,%eax
 804921b:	80 7c 24 10 2a       	cmpb   $0x2a,0x10(%esp)
 8049220:	75 0f                	jne    0x8049231
 8049222:	89 f0                	mov    %esi,%eax
 8049224:	f7 d8                	neg    %eax
 8049226:	c7 44 84 18 00 00 00 	movl   $0x0,0x18(%esp,%eax,4)
 804922d:	00 
 804922e:	8d 43 01             	lea    0x1(%ebx),%eax
 8049231:	31 d2                	xor    %edx,%edx
 8049233:	0f b6 08             	movzbl (%eax),%ecx
 8049236:	88 4c 24 14          	mov    %cl,0x14(%esp)
 804923a:	f6 44 4d 00 08       	testb  $0x8,0x0(%ebp,%ecx,2)
 804923f:	74 26                	je     0x8049267
 8049241:	81 fa cb cc cc 0c    	cmp    $0xccccccb,%edx
 8049247:	7e 0d                	jle    0x8049256
 8049249:	81 fa cc cc cc 0c    	cmp    $0xccccccc,%edx
 804924f:	75 0e                	jne    0x804925f
 8049251:	83 f9 37             	cmp    $0x37,%ecx
 8049254:	7f 09                	jg     0x804925f
 8049256:	6b d2 0a             	imul   $0xa,%edx,%edx
 8049259:	8d 54 0a d0          	lea    -0x30(%edx,%ecx,1),%edx
 804925d:	eb 05                	jmp    0x8049264
 804925f:	ba ff ff ff 7f       	mov    $0x7fffffff,%edx
 8049264:	40                   	inc    %eax
 8049265:	eb cc                	jmp    0x8049233
 8049267:	80 7b ff 25          	cmpb   $0x25,-0x1(%ebx)
 804926b:	0f 85 92 00 00 00    	jne    0x8049303
 8049271:	80 7c 24 14 24       	cmpb   $0x24,0x14(%esp)
 8049276:	75 28                	jne    0x80492a0
 8049278:	85 d2                	test   %edx,%edx
 804927a:	7e 24                	jle    0x80492a0
 804927c:	8d 58 01             	lea    0x1(%eax),%ebx
 804927f:	83 7c 24 04 00       	cmpl   $0x0,0x4(%esp)
 8049284:	75 08                	jne    0x804928e
 8049286:	83 c8 ff             	or     $0xffffffff,%eax
 8049289:	e9 af 02 00 00       	jmp    0x804953d
 804928e:	89 54 24 2c          	mov    %edx,0x2c(%esp)
 8049292:	39 54 24 04          	cmp    %edx,0x4(%esp)
 8049296:	7d 04                	jge    0x804929c
 8049298:	89 54 24 04          	mov    %edx,0x4(%esp)
 804929c:	89 d8                	mov    %ebx,%eax
 804929e:	eb 36                	jmp    0x80492d6
 80492a0:	83 7c 24 04 00       	cmpl   $0x0,0x4(%esp)
 80492a5:	7f df                	jg     0x8049286
 80492a7:	80 7c 24 10 30       	cmpb   $0x30,0x10(%esp)
 80492ac:	74 0c                	je     0x80492ba
 80492ae:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
 80492b5:	00 
 80492b6:	39 c3                	cmp    %eax,%ebx
 80492b8:	72 49                	jb     0x8049303
 80492ba:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
 80492c1:	00 
 80492c2:	eb d8                	jmp    0x804929c
 80492c4:	01 d2                	add    %edx,%edx
 80492c6:	80 3b 00             	cmpb   $0x0,(%ebx)
 80492c9:	74 1a                	je     0x80492e5
 80492cb:	43                   	inc    %ebx
 80492cc:	3a 4b ff             	cmp    -0x1(%ebx),%cl
 80492cf:	75 f3                	jne    0x80492c4
 80492d1:	40                   	inc    %eax
 80492d2:	09 54 24 08          	or     %edx,0x8(%esp)
 80492d6:	8a 08                	mov    (%eax),%cl
 80492d8:	ba 01 00 00 00       	mov    $0x1,%edx
 80492dd:	8d 9f b4 df ff ff    	lea    -0x204c(%edi),%ebx
 80492e3:	eb e6                	jmp    0x80492cb
 80492e5:	8b 54 24 08          	mov    0x8(%esp),%edx
 80492e9:	83 e2 0a             	and    $0xa,%edx
 80492ec:	d1 fa                	sar    %edx
 80492ee:	f7 d2                	not    %edx
 80492f0:	21 54 24 08          	and    %edx,0x8(%esp)
 80492f4:	80 78 ff 25          	cmpb   $0x25,-0x1(%eax)
 80492f8:	74 07                	je     0x8049301
 80492fa:	89 c3                	mov    %eax,%ebx
 80492fc:	e9 12 ff ff ff       	jmp    0x8049213
 8049301:	31 d2                	xor    %edx,%edx
 8049303:	80 3b 2a             	cmpb   $0x2a,(%ebx)
 8049306:	75 35                	jne    0x804933d
 8049308:	83 7c 24 04 00       	cmpl   $0x0,0x4(%esp)
 804930d:	74 20                	je     0x804932f
 804930f:	8d 48 01             	lea    0x1(%eax),%ecx
 8049312:	80 38 24             	cmpb   $0x24,(%eax)
 8049315:	0f 85 6b ff ff ff    	jne    0x8049286
 804931b:	85 d2                	test   %edx,%edx
 804931d:	0f 8e 63 ff ff ff    	jle    0x8049286
 8049323:	89 f0                	mov    %esi,%eax
 8049325:	f7 d8                	neg    %eax
 8049327:	89 54 84 24          	mov    %edx,0x24(%esp,%eax,4)
 804932b:	89 c8                	mov    %ecx,%eax
 804932d:	eb 09                	jmp    0x8049338
 804932f:	43                   	inc    %ebx
 8049330:	39 d8                	cmp    %ebx,%eax
 8049332:	0f 85 4e ff ff ff    	jne    0x8049286
 8049338:	ba 00 00 00 80       	mov    $0x80000000,%edx
 804933d:	85 f6                	test   %esi,%esi
 804933f:	75 16                	jne    0x8049357
 8049341:	80 38 2e             	cmpb   $0x2e,(%eax)
 8049344:	75 0a                	jne    0x8049350
 8049346:	40                   	inc    %eax
 8049347:	89 54 24 0c          	mov    %edx,0xc(%esp)
 804934b:	83 ce ff             	or     $0xffffffff,%esi
 804934e:	eb aa                	jmp    0x80492fa
 8049350:	89 54 24 0c          	mov    %edx,0xc(%esp)
 8049354:	83 ca ff             	or     $0xffffffff,%edx
 8049357:	8a 18                	mov    (%eax),%bl
 8049359:	8d 8f 64 df ff ff    	lea    -0x209c(%edi),%ecx
 804935f:	89 ce                	mov    %ecx,%esi
 8049361:	3a 19                	cmp    (%ecx),%bl
 8049363:	75 03                	jne    0x8049368
 8049365:	40                   	inc    %eax
 8049366:	eb 06                	jmp    0x804936e
 8049368:	41                   	inc    %ecx
 8049369:	80 39 00             	cmpb   $0x0,(%ecx)
 804936c:	75 f3                	jne    0x8049361
 804936e:	89 cb                	mov    %ecx,%ebx
 8049370:	29 f3                	sub    %esi,%ebx
 8049372:	4b                   	dec    %ebx
 8049373:	7f 0a                	jg     0x804937f
 8049375:	8a 19                	mov    (%ecx),%bl
 8049377:	38 18                	cmp    %bl,(%eax)
 8049379:	75 04                	jne    0x804937f
 804937b:	83 c1 09             	add    $0x9,%ecx
 804937e:	40                   	inc    %eax
 804937f:	0f b6 49 09          	movzbl 0x9(%ecx),%ecx
 8049383:	c1 e1 08             	shl    $0x8,%ecx
 8049386:	89 4c 24 10          	mov    %ecx,0x10(%esp)
 804938a:	8a 18                	mov    (%eax),%bl
 804938c:	84 db                	test   %bl,%bl
 804938e:	0f 84 f2 fe ff ff    	je     0x8049286
 8049394:	8d 8f 9c df ff ff    	lea    -0x2064(%edi),%ecx
 804939a:	89 ce                	mov    %ecx,%esi
 804939c:	3a 19                	cmp    (%ecx),%bl
 804939e:	75 5a                	jne    0x80493fa
 80493a0:	29 f1                	sub    %esi,%ecx
 80493a2:	83 f9 11             	cmp    $0x11,%ecx
 80493a5:	7e 0d                	jle    0x80493b4
 80493a7:	f7 44 24 10 00 04 00 	testl  $0x400,0x10(%esp)
 80493ae:	00 
 80493af:	74 03                	je     0x80493b4
 80493b1:	83 e9 02             	sub    $0x2,%ecx
 80493b4:	8b 34 24             	mov    (%esp),%esi
 80493b7:	89 4e 20             	mov    %ecx,0x20(%esi)
 80493ba:	8d 9f 58 df ff ff    	lea    -0x20a8(%edi),%ebx
 80493c0:	89 de                	mov    %ebx,%esi
 80493c2:	8d 6b 01             	lea    0x1(%ebx),%ebp
 80493c5:	89 6c 24 14          	mov    %ebp,0x14(%esp)
 80493c9:	0f b6 2b             	movzbl (%ebx),%ebp
 80493cc:	39 e9                	cmp    %ebp,%ecx
 80493ce:	7e 06                	jle    0x80493d6
 80493d0:	8b 5c 24 14          	mov    0x14(%esp),%ebx
 80493d4:	eb ec                	jmp    0x80493c2
 80493d6:	29 f3                	sub    %esi,%ebx
 80493d8:	0f bf b4 5f 48 df ff 	movswl -0x20b8(%edi,%ebx,2),%esi
 80493df:	ff 
 80493e0:	0b 74 24 10          	or     0x10(%esp),%esi
 80493e4:	0f bf 8c 5f 38 df ff 	movswl -0x20c8(%edi,%ebx,2),%ecx
 80493eb:	ff 
 80493ec:	21 f1                	and    %esi,%ecx
 80493ee:	89 4c 24 20          	mov    %ecx,0x20(%esp)
 80493f2:	8d 8f 9c df ff ff    	lea    -0x2064(%edi),%ecx
 80493f8:	eb 06                	jmp    0x8049400
 80493fa:	41                   	inc    %ecx
 80493fb:	80 39 00             	cmpb   $0x0,(%ecx)
 80493fe:	75 9c                	jne    0x804939c
 8049400:	0f b6 18             	movzbl (%eax),%ebx
 8049403:	8b 34 24             	mov    (%esp),%esi
 8049406:	89 5e 0c             	mov    %ebx,0xc(%esi)
 8049409:	89 56 04             	mov    %edx,0x4(%esi)
 804940c:	8b 74 24 0c          	mov    0xc(%esp),%esi
 8049410:	8b 1c 24             	mov    (%esp),%ebx
 8049413:	89 73 08             	mov    %esi,0x8(%ebx)
 8049416:	8b 54 24 08          	mov    0x8(%esp),%edx
 804941a:	83 e2 04             	and    $0x4,%edx
 804941d:	83 fa 01             	cmp    $0x1,%edx
 8049420:	19 d2                	sbb    %edx,%edx
 8049422:	83 e2 f0             	and    $0xfffffff0,%edx
 8049425:	83 c2 30             	add    $0x30,%edx
 8049428:	89 de                	mov    %ebx,%esi
 804942a:	89 53 14             	mov    %edx,0x14(%ebx)
 804942d:	8b 54 24 08          	mov    0x8(%esp),%edx
 8049431:	83 e2 fb             	and    $0xfffffffb,%edx
 8049434:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 8049438:	81 e3 00 0f 00 00    	and    $0xf00,%ebx
 804943e:	09 da                	or     %ebx,%edx
 8049440:	89 56 10             	mov    %edx,0x10(%esi)
 8049443:	c7 46 1c 01 00 00 00 	movl   $0x1,0x1c(%esi)
 804944a:	80 39 00             	cmpb   $0x0,(%ecx)
 804944d:	0f 84 33 fe ff ff    	je     0x8049286
 8049453:	83 7c 24 04 00       	cmpl   $0x0,0x4(%esp)
 8049458:	0f 8e bf 00 00 00    	jle    0x804951d
 804945e:	31 c9                	xor    %ecx,%ecx
 8049460:	8d b7 78 df ff ff    	lea    -0x2088(%edi),%esi
 8049466:	89 74 24 0c          	mov    %esi,0xc(%esp)
 804946a:	8b 54 8c 24          	mov    0x24(%esp,%ecx,4),%edx
 804946e:	8b 34 24             	mov    (%esp),%esi
 8049471:	88 54 0e 24          	mov    %dl,0x24(%esi,%ecx,1)
 8049475:	0f b6 d2             	movzbl %dl,%edx
 8049478:	39 54 24 04          	cmp    %edx,0x4(%esp)
 804947c:	7d 0d                	jge    0x804948b
 804947e:	83 fa 09             	cmp    $0x9,%edx
 8049481:	0f 8f ff fd ff ff    	jg     0x8049286
 8049487:	89 54 24 04          	mov    %edx,0x4(%esp)
 804948b:	8b 74 8c 18          	mov    0x18(%esp,%ecx,4),%esi
 804948f:	83 fe 08             	cmp    $0x8,%esi
 8049492:	74 7d                	je     0x8049511
 8049494:	8b 1c 24             	mov    (%esp),%ebx
 8049497:	8d 1c 93             	lea    (%ebx,%edx,4),%ebx
 804949a:	89 5c 24 08          	mov    %ebx,0x8(%esp)
 804949e:	8b 5b 24             	mov    0x24(%ebx),%ebx
 80494a1:	83 fb 08             	cmp    $0x8,%ebx
 80494a4:	74 64                	je     0x804950a
 80494a6:	39 de                	cmp    %ebx,%esi
 80494a8:	74 60                	je     0x804950a
 80494aa:	8d 97 9c df ff ff    	lea    -0x2064(%edi),%edx
 80494b0:	8d af 84 df ff ff    	lea    -0x207c(%edi),%ebp
 80494b6:	89 6c 24 10          	mov    %ebp,0x10(%esp)
 80494ba:	83 ea 02             	sub    $0x2,%edx
 80494bd:	0f bf 2a             	movswl (%edx),%ebp
 80494c0:	39 dd                	cmp    %ebx,%ebp
 80494c2:	74 06                	je     0x80494ca
 80494c4:	3b 54 24 10          	cmp    0x10(%esp),%edx
 80494c8:	77 f0                	ja     0x80494ba
 80494ca:	8d 9f 84 df ff ff    	lea    -0x207c(%edi),%ebx
 80494d0:	29 da                	sub    %ebx,%edx
 80494d2:	d1 fa                	sar    %edx
 80494d4:	8b 6c 24 0c          	mov    0xc(%esp),%ebp
 80494d8:	0f b6 54 15 00       	movzbl 0x0(%ebp,%edx,1),%edx
 80494dd:	89 54 24 10          	mov    %edx,0x10(%esp)
 80494e1:	8d 53 18             	lea    0x18(%ebx),%edx
 80494e4:	89 5c 24 14          	mov    %ebx,0x14(%esp)
 80494e8:	83 ea 02             	sub    $0x2,%edx
 80494eb:	0f bf 2a             	movswl (%edx),%ebp
 80494ee:	39 f5                	cmp    %esi,%ebp
 80494f0:	74 06                	je     0x80494f8
 80494f2:	3b 54 24 14          	cmp    0x14(%esp),%edx
 80494f6:	77 f0                	ja     0x80494e8
 80494f8:	29 da                	sub    %ebx,%edx
 80494fa:	d1 fa                	sar    %edx
 80494fc:	8b 5c 24 0c          	mov    0xc(%esp),%ebx
 8049500:	0f b6 14 13          	movzbl (%ebx,%edx,1),%edx
 8049504:	3b 54 24 10          	cmp    0x10(%esp),%edx
 8049508:	7c 07                	jl     0x8049511
 804950a:	8b 5c 24 08          	mov    0x8(%esp),%ebx
 804950e:	89 73 24             	mov    %esi,0x24(%ebx)
 8049511:	41                   	inc    %ecx
 8049512:	83 f9 03             	cmp    $0x3,%ecx
 8049515:	0f 85 4f ff ff ff    	jne    0x804946a
 804951b:	eb 0e                	jmp    0x804952b
 804951d:	8b 3c 24             	mov    (%esp),%edi
 8049520:	c6 47 26 01          	movb   $0x1,0x26(%edi)
 8049524:	8b 54 24 20          	mov    0x20(%esp),%edx
 8049528:	89 57 28             	mov    %edx,0x28(%edi)
 804952b:	8b 7c 24 04          	mov    0x4(%esp),%edi
 804952f:	8b 34 24             	mov    (%esp),%esi
 8049532:	89 7e 18             	mov    %edi,0x18(%esi)
 8049535:	40                   	inc    %eax
 8049536:	89 06                	mov    %eax,(%esi)
 8049538:	b8 03 00 00 00       	mov    $0x3,%eax
 804953d:	83 c4 30             	add    $0x30,%esp
 8049540:	5b                   	pop    %ebx
 8049541:	5e                   	pop    %esi
 8049542:	5f                   	pop    %edi
 8049543:	5d                   	pop    %ebp
 8049544:	c3                   	ret    
 8049545:	56                   	push   %esi
 8049546:	53                   	push   %ebx
 8049547:	8b 74 24 0c          	mov    0xc(%esp),%esi
 804954b:	56                   	push   %esi
 804954c:	e8 d1 00 00 00       	call   0x8049622
 8049551:	5a                   	pop    %edx
 8049552:	89 c3                	mov    %eax,%ebx
 8049554:	ff 74 24 10          	pushl  0x10(%esp)
 8049558:	50                   	push   %eax
 8049559:	6a 01                	push   $0x1
 804955b:	56                   	push   %esi
 804955c:	e8 11 00 00 00       	call   0x8049572
 8049561:	83 c4 10             	add    $0x10,%esp
 8049564:	89 da                	mov    %ebx,%edx
 8049566:	39 c3                	cmp    %eax,%ebx
 8049568:	74 03                	je     0x804956d
 804956a:	83 ca ff             	or     $0xffffffff,%edx
 804956d:	89 d0                	mov    %edx,%eax
 804956f:	5b                   	pop    %ebx
 8049570:	5e                   	pop    %esi
 8049571:	c3                   	ret    
 8049572:	55                   	push   %ebp
 8049573:	57                   	push   %edi
 8049574:	56                   	push   %esi
 8049575:	53                   	push   %ebx
 8049576:	e8 67 00 00 00       	call   0x80495e2
 804957b:	81 c5 f1 34 00 00    	add    $0x34f1,%ebp
 8049581:	8b 5c 24 18          	mov    0x18(%esp),%ebx
 8049585:	8b 7c 24 1c          	mov    0x1c(%esp),%edi
 8049589:	8b 74 24 20          	mov    0x20(%esp),%esi
 804958d:	f6 06 40             	testb  $0x40,(%esi)
 8049590:	74 0a                	je     0x804959c
 8049592:	85 ff                	test   %edi,%edi
 8049594:	74 45                	je     0x80495db
 8049596:	85 db                	test   %ebx,%ebx
 8049598:	75 0f                	jne    0x80495a9
 804959a:	eb 3f                	jmp    0x80495db
 804959c:	56                   	push   %esi
 804959d:	e8 f7 05 00 00       	call   0x8049b99
 80495a2:	5a                   	pop    %edx
 80495a3:	85 c0                	test   %eax,%eax
 80495a5:	74 eb                	je     0x8049592
 80495a7:	eb 32                	jmp    0x80495db
 80495a9:	83 c8 ff             	or     $0xffffffff,%eax
 80495ac:	31 d2                	xor    %edx,%edx
 80495ae:	f7 f3                	div    %ebx
 80495b0:	39 c7                	cmp    %eax,%edi
 80495b2:	77 17                	ja     0x80495cb
 80495b4:	56                   	push   %esi
 80495b5:	0f af fb             	imul   %ebx,%edi
 80495b8:	57                   	push   %edi
 80495b9:	ff 74 24 1c          	pushl  0x1c(%esp)
 80495bd:	e8 fe 04 00 00       	call   0x8049ac0
 80495c2:	31 d2                	xor    %edx,%edx
 80495c4:	f7 f3                	div    %ebx
 80495c6:	83 c4 0c             	add    $0xc,%esp
 80495c9:	eb 12                	jmp    0x80495dd
 80495cb:	66 83 0e 08          	orw    $0x8,(%esi)
 80495cf:	8d 85 bc 00 00 00    	lea    0xbc(%ebp),%eax
 80495d5:	c7 00 16 00 00 00    	movl   $0x16,(%eax)
 80495db:	31 c0                	xor    %eax,%eax
 80495dd:	5b                   	pop    %ebx
 80495de:	5e                   	pop    %esi
 80495df:	5f                   	pop    %edi
 80495e0:	5d                   	pop    %ebp
 80495e1:	c3                   	ret    
 80495e2:	8b 2c 24             	mov    (%esp),%ebp
 80495e5:	c3                   	ret    
 80495e6:	53                   	push   %ebx
 80495e7:	e8 32 00 00 00       	call   0x804961e
 80495ec:	81 c2 80 34 00 00    	add    $0x3480,%edx
 80495f2:	8b 44 24 08          	mov    0x8(%esp),%eax
 80495f6:	8d 92 24 00 00 00    	lea    0x24(%edx),%edx
 80495fc:	8b 12                	mov    (%edx),%edx
 80495fe:	8b 4a 10             	mov    0x10(%edx),%ecx
 8049601:	3b 4a 1c             	cmp    0x1c(%edx),%ecx
 8049604:	73 0d                	jae    0x8049613
 8049606:	8d 59 01             	lea    0x1(%ecx),%ebx
 8049609:	89 5a 10             	mov    %ebx,0x10(%edx)
 804960c:	88 01                	mov    %al,(%ecx)
 804960e:	0f b6 c0             	movzbl %al,%eax
 8049611:	eb 09                	jmp    0x804961c
 8049613:	52                   	push   %edx
 8049614:	50                   	push   %eax
 8049615:	e8 03 0d 00 00       	call   0x804a31d
 804961a:	5a                   	pop    %edx
 804961b:	59                   	pop    %ecx
 804961c:	5b                   	pop    %ebx
 804961d:	c3                   	ret    
 804961e:	8b 14 24             	mov    (%esp),%edx
 8049621:	c3                   	ret    
 8049622:	57                   	push   %edi
 8049623:	83 c9 ff             	or     $0xffffffff,%ecx
 8049626:	8b 7c 24 08          	mov    0x8(%esp),%edi
 804962a:	31 c0                	xor    %eax,%eax
 804962c:	f2 ae                	repnz scas %es:(%edi),%al
 804962e:	f7 d1                	not    %ecx
 8049630:	8d 41 ff             	lea    -0x1(%ecx),%eax
 8049633:	5f                   	pop    %edi
 8049634:	c3                   	ret    
 8049635:	8b 44 24 08          	mov    0x8(%esp),%eax
 8049639:	8d 50 01             	lea    0x1(%eax),%edx
 804963c:	8b 4c 24 04          	mov    0x4(%esp),%ecx
 8049640:	8d 41 ff             	lea    -0x1(%ecx),%eax
 8049643:	40                   	inc    %eax
 8049644:	4a                   	dec    %edx
 8049645:	74 05                	je     0x804964c
 8049647:	80 38 00             	cmpb   $0x0,(%eax)
 804964a:	75 f7                	jne    0x8049643
 804964c:	29 c8                	sub    %ecx,%eax
 804964e:	c3                   	ret    
 804964f:	83 ec 3c             	sub    $0x3c,%esp
 8049652:	89 e0                	mov    %esp,%eax
 8049654:	50                   	push   %eax
 8049655:	ff 74 24 44          	pushl  0x44(%esp)
 8049659:	e8 0c 00 00 00       	call   0x804966a
 804965e:	85 c0                	test   %eax,%eax
 8049660:	0f 94 c0             	sete   %al
 8049663:	0f b6 c0             	movzbl %al,%eax
 8049666:	83 c4 44             	add    $0x44,%esp
 8049669:	c3                   	ret    
 804966a:	57                   	push   %edi
 804966b:	56                   	push   %esi
 804966c:	83 ec 24             	sub    $0x24,%esp
 804966f:	8b 7c 24 34          	mov    0x34(%esp),%edi
 8049673:	89 e0                	mov    %esp,%eax
 8049675:	50                   	push   %eax
 8049676:	68 01 54 00 00       	push   $0x5401
 804967b:	ff 74 24 38          	pushl  0x38(%esp)
 804967f:	e8 44 03 00 00       	call   0x80499c8
 8049684:	83 c4 0c             	add    $0xc,%esp
 8049687:	85 c0                	test   %eax,%eax
 8049689:	75 33                	jne    0x80496be
 804968b:	8b 14 24             	mov    (%esp),%edx
 804968e:	89 17                	mov    %edx,(%edi)
 8049690:	8b 54 24 04          	mov    0x4(%esp),%edx
 8049694:	89 57 04             	mov    %edx,0x4(%edi)
 8049697:	8b 54 24 08          	mov    0x8(%esp),%edx
 804969b:	89 57 08             	mov    %edx,0x8(%edi)
 804969e:	8b 54 24 0c          	mov    0xc(%esp),%edx
 80496a2:	89 57 0c             	mov    %edx,0xc(%edi)
 80496a5:	8a 54 24 10          	mov    0x10(%esp),%dl
 80496a9:	88 57 10             	mov    %dl,0x10(%edi)
 80496ac:	8d 74 24 11          	lea    0x11(%esp),%esi
 80496b0:	83 c7 11             	add    $0x11,%edi
 80496b3:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 80496b4:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 80496b5:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 80496b6:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 80496b7:	66 a5                	movsw  %ds:(%esi),%es:(%edi)
 80496b9:	a4                   	movsb  %ds:(%esi),%es:(%edi)
 80496ba:	ab                   	stos   %eax,%es:(%edi)
 80496bb:	ab                   	stos   %eax,%es:(%edi)
 80496bc:	ab                   	stos   %eax,%es:(%edi)
 80496bd:	aa                   	stos   %al,%es:(%edi)
 80496be:	83 c4 24             	add    $0x24,%esp
 80496c1:	5e                   	pop    %esi
 80496c2:	5f                   	pop    %edi
 80496c3:	c3                   	ret    
 80496c4:	56                   	push   %esi
 80496c5:	53                   	push   %ebx
 80496c6:	83 ec 28             	sub    $0x28,%esp
 80496c9:	e8 8e 00 00 00       	call   0x804975c
 80496ce:	81 c6 9e 33 00 00    	add    $0x339e,%esi
 80496d4:	8b 5c 24 34          	mov    0x34(%esp),%ebx
 80496d8:	8b 44 24 38          	mov    0x38(%esp),%eax
 80496dc:	8d 53 ff             	lea    -0x1(%ebx),%edx
 80496df:	83 fa 3f             	cmp    $0x3f,%edx
 80496e2:	77 05                	ja     0x80496e9
 80496e4:	83 f8 ff             	cmp    $0xffffffff,%eax
 80496e7:	75 11                	jne    0x80496fa
 80496e9:	8d 86 bc 00 00 00    	lea    0xbc(%esi),%eax
 80496ef:	c7 00 16 00 00 00    	movl   $0x16,(%eax)
 80496f5:	83 ca ff             	or     $0xffffffff,%edx
 80496f8:	eb 5a                	jmp    0x8049754
 80496fa:	89 04 24             	mov    %eax,(%esp)
 80496fd:	c7 44 24 0c 00 00 00 	movl   $0x0,0xc(%esp)
 8049704:	00 
 8049705:	c7 44 24 10 00 00 00 	movl   $0x0,0x10(%esp)
 804970c:	00 
 804970d:	53                   	push   %ebx
 804970e:	8d 44 24 10          	lea    0x10(%esp),%eax
 8049712:	50                   	push   %eax
 8049713:	e8 67 00 00 00       	call   0x804977f
 8049718:	53                   	push   %ebx
 8049719:	8d 86 e0 20 00 00    	lea    0x20e0(%esi),%eax
 804971f:	50                   	push   %eax
 8049720:	e8 3b 00 00 00       	call   0x8049760
 8049725:	83 c4 10             	add    $0x10,%esp
 8049728:	83 f8 01             	cmp    $0x1,%eax
 804972b:	19 c0                	sbb    %eax,%eax
 804972d:	25 00 00 00 10       	and    $0x10000000,%eax
 8049732:	89 44 24 04          	mov    %eax,0x4(%esp)
 8049736:	8d 44 24 14          	lea    0x14(%esp),%eax
 804973a:	50                   	push   %eax
 804973b:	8d 44 24 04          	lea    0x4(%esp),%eax
 804973f:	50                   	push   %eax
 8049740:	53                   	push   %ebx
 8049741:	e8 27 02 00 00       	call   0x804996d
 8049746:	83 c4 0c             	add    $0xc,%esp
 8049749:	83 ca ff             	or     $0xffffffff,%edx
 804974c:	85 c0                	test   %eax,%eax
 804974e:	78 04                	js     0x8049754
 8049750:	8b 54 24 14          	mov    0x14(%esp),%edx
 8049754:	89 d0                	mov    %edx,%eax
 8049756:	83 c4 28             	add    $0x28,%esp
 8049759:	5b                   	pop    %ebx
 804975a:	5e                   	pop    %esi
 804975b:	c3                   	ret    
 804975c:	8b 34 24             	mov    (%esp),%esi
 804975f:	c3                   	ret    
 8049760:	8b 44 24 08          	mov    0x8(%esp),%eax
 8049764:	8d 48 ff             	lea    -0x1(%eax),%ecx
 8049767:	b8 01 00 00 00       	mov    $0x1,%eax
 804976c:	d3 e0                	shl    %cl,%eax
 804976e:	c1 e9 05             	shr    $0x5,%ecx
 8049771:	8b 54 24 04          	mov    0x4(%esp),%edx
 8049775:	85 04 8a             	test   %eax,(%edx,%ecx,4)
 8049778:	0f 95 c0             	setne  %al
 804977b:	0f b6 c0             	movzbl %al,%eax
 804977e:	c3                   	ret    
 804977f:	8b 44 24 08          	mov    0x8(%esp),%eax
 8049783:	8d 48 ff             	lea    -0x1(%eax),%ecx
 8049786:	89 c8                	mov    %ecx,%eax
 8049788:	c1 e8 05             	shr    $0x5,%eax
 804978b:	8b 54 24 04          	mov    0x4(%esp),%edx
 804978f:	8d 04 82             	lea    (%edx,%eax,4),%eax
 8049792:	ba 01 00 00 00       	mov    $0x1,%edx
 8049797:	d3 e2                	shl    %cl,%edx
 8049799:	09 10                	or     %edx,(%eax)
 804979b:	31 c0                	xor    %eax,%eax
 804979d:	c3                   	ret    
 804979e:	8b 44 24 08          	mov    0x8(%esp),%eax
 80497a2:	8d 48 ff             	lea    -0x1(%eax),%ecx
 80497a5:	89 c8                	mov    %ecx,%eax
 80497a7:	c1 e8 05             	shr    $0x5,%eax
 80497aa:	8b 54 24 04          	mov    0x4(%esp),%edx
 80497ae:	8d 04 82             	lea    (%edx,%eax,4),%eax
 80497b1:	ba 01 00 00 00       	mov    $0x1,%edx
 80497b6:	d3 e2                	shl    %cl,%edx
 80497b8:	f7 d2                	not    %edx
 80497ba:	21 10                	and    %edx,(%eax)
 80497bc:	31 c0                	xor    %eax,%eax
 80497be:	c3                   	ret    
 80497bf:	6a 0a                	push   $0xa
 80497c1:	6a 00                	push   $0x0
 80497c3:	ff 74 24 0c          	pushl  0xc(%esp)
 80497c7:	e8 04 00 00 00       	call   0x80497d0
 80497cc:	83 c4 0c             	add    $0xc,%esp
 80497cf:	c3                   	ret    
 80497d0:	6a 01                	push   $0x1
 80497d2:	ff 74 24 10          	pushl  0x10(%esp)
 80497d6:	ff 74 24 10          	pushl  0x10(%esp)
 80497da:	ff 74 24 10          	pushl  0x10(%esp)
 80497de:	e8 04 00 00 00       	call   0x80497e7
 80497e3:	83 c4 10             	add    $0x10,%esp
 80497e6:	c3                   	ret    
 80497e7:	55                   	push   %ebp
 80497e8:	57                   	push   %edi
 80497e9:	56                   	push   %esi
 80497ea:	53                   	push   %ebx
 80497eb:	83 ec 10             	sub    $0x10,%esp
 80497ee:	e8 ef fd ff ff       	call   0x80495e2
 80497f3:	81 c5 79 32 00 00    	add    $0x3279,%ebp
 80497f9:	8b 4c 24 2c          	mov    0x2c(%esp),%ecx
 80497fd:	8b 95 a0 00 00 00    	mov    0xa0(%ebp),%edx
 8049803:	8b 5c 24 24          	mov    0x24(%esp),%ebx
 8049807:	0f b6 33             	movzbl (%ebx),%esi
 804980a:	89 f0                	mov    %esi,%eax
 804980c:	f6 04 72 20          	testb  $0x20,(%edx,%esi,2)
 8049810:	74 03                	je     0x8049815
 8049812:	43                   	inc    %ebx
 8049813:	eb f2                	jmp    0x8049807
 8049815:	3c 2b                	cmp    $0x2b,%al
 8049817:	74 0b                	je     0x8049824
 8049819:	bf 01 00 00 00       	mov    $0x1,%edi
 804981e:	3c 2d                	cmp    $0x2d,%al
 8049820:	74 04                	je     0x8049826
 8049822:	eb 05                	jmp    0x8049829
 8049824:	31 ff                	xor    %edi,%edi
 8049826:	43                   	inc    %ebx
 8049827:	eb 02                	jmp    0x804982b
 8049829:	31 ff                	xor    %edi,%edi
 804982b:	f7 c1 ef ff ff ff    	test   $0xffffffef,%ecx
 8049831:	75 33                	jne    0x8049866
 8049833:	80 3b 30             	cmpb   $0x30,(%ebx)
 8049836:	74 05                	je     0x804983d
 8049838:	83 c1 0a             	add    $0xa,%ecx
 804983b:	eb 1f                	jmp    0x804985c
 804983d:	8d 43 01             	lea    0x1(%ebx),%eax
 8049840:	89 44 24 24          	mov    %eax,0x24(%esp)
 8049844:	83 c1 08             	add    $0x8,%ecx
 8049847:	8a 43 01             	mov    0x1(%ebx),%al
 804984a:	83 c8 20             	or     $0x20,%eax
 804984d:	3c 78                	cmp    $0x78,%al
 804984f:	75 07                	jne    0x8049858
 8049851:	83 c3 02             	add    $0x2,%ebx
 8049854:	01 c9                	add    %ecx,%ecx
 8049856:	eb 04                	jmp    0x804985c
 8049858:	8b 5c 24 24          	mov    0x24(%esp),%ebx
 804985c:	83 f9 10             	cmp    $0x10,%ecx
 804985f:	7e 05                	jle    0x8049866
 8049861:	b9 10 00 00 00       	mov    $0x10,%ecx
 8049866:	8d 41 fe             	lea    -0x2(%ecx),%eax
 8049869:	31 f6                	xor    %esi,%esi
 804986b:	83 f8 22             	cmp    $0x22,%eax
 804986e:	0f 87 8a 00 00 00    	ja     0x80498fe
 8049874:	83 c8 ff             	or     $0xffffffff,%eax
 8049877:	31 d2                	xor    %edx,%edx
 8049879:	f7 f1                	div    %ecx
 804987b:	89 44 24 04          	mov    %eax,0x4(%esp)
 804987f:	88 54 24 0f          	mov    %dl,0xf(%esp)
 8049883:	8d 85 bc 00 00 00    	lea    0xbc(%ebp),%eax
 8049889:	89 44 24 08          	mov    %eax,0x8(%esp)
 804988d:	8b 00                	mov    (%eax),%eax
 804988f:	89 04 24             	mov    %eax,(%esp)
 8049892:	c6 44 24 0e 00       	movb   $0x0,0xe(%esp)
 8049897:	8a 03                	mov    (%ebx),%al
 8049899:	8d 50 d0             	lea    -0x30(%eax),%edx
 804989c:	80 fa 09             	cmp    $0x9,%dl
 804989f:	76 0c                	jbe    0x80498ad
 80498a1:	83 c8 20             	or     $0x20,%eax
 80498a4:	b2 28                	mov    $0x28,%dl
 80498a6:	3c 60                	cmp    $0x60,%al
 80498a8:	76 03                	jbe    0x80498ad
 80498aa:	8d 50 a9             	lea    -0x57(%eax),%edx
 80498ad:	0f b6 c2             	movzbl %dl,%eax
 80498b0:	39 c1                	cmp    %eax,%ecx
 80498b2:	7f 12                	jg     0x80498c6
 80498b4:	80 7c 24 0e 00       	cmpb   $0x0,0xe(%esp)
 80498b9:	74 43                	je     0x80498fe
 80498bb:	8b 44 24 08          	mov    0x8(%esp),%eax
 80498bf:	8b 1c 24             	mov    (%esp),%ebx
 80498c2:	89 18                	mov    %ebx,(%eax)
 80498c4:	eb 38                	jmp    0x80498fe
 80498c6:	43                   	inc    %ebx
 80498c7:	3b 74 24 04          	cmp    0x4(%esp),%esi
 80498cb:	77 0c                	ja     0x80498d9
 80498cd:	3a 54 24 0f          	cmp    0xf(%esp),%dl
 80498d1:	76 21                	jbe    0x80498f4
 80498d3:	3b 74 24 04          	cmp    0x4(%esp),%esi
 80498d7:	75 1b                	jne    0x80498f4
 80498d9:	8a 44 24 30          	mov    0x30(%esp),%al
 80498dd:	21 c7                	and    %eax,%edi
 80498df:	c6 44 24 0e 01       	movb   $0x1,0xe(%esp)
 80498e4:	c7 04 24 22 00 00 00 	movl   $0x22,(%esp)
 80498eb:	83 ce ff             	or     $0xffffffff,%esi
 80498ee:	89 5c 24 24          	mov    %ebx,0x24(%esp)
 80498f2:	eb a3                	jmp    0x8049897
 80498f4:	0f af f1             	imul   %ecx,%esi
 80498f7:	0f b6 d2             	movzbl %dl,%edx
 80498fa:	01 d6                	add    %edx,%esi
 80498fc:	eb f0                	jmp    0x80498ee
 80498fe:	83 7c 24 28 00       	cmpl   $0x0,0x28(%esp)
 8049903:	74 0a                	je     0x804990f
 8049905:	8b 44 24 28          	mov    0x28(%esp),%eax
 8049909:	8b 54 24 24          	mov    0x24(%esp),%edx
 804990d:	89 10                	mov    %edx,(%eax)
 804990f:	89 f8                	mov    %edi,%eax
 8049911:	3c 01                	cmp    $0x1,%al
 8049913:	19 c0                	sbb    %eax,%eax
 8049915:	05 00 00 00 80       	add    $0x80000000,%eax
 804991a:	39 c6                	cmp    %eax,%esi
 804991c:	76 15                	jbe    0x8049933
 804991e:	83 7c 24 30 00       	cmpl   $0x0,0x30(%esp)
 8049923:	74 0e                	je     0x8049933
 8049925:	8d 95 bc 00 00 00    	lea    0xbc(%ebp),%edx
 804992b:	c7 02 22 00 00 00    	movl   $0x22,(%edx)
 8049931:	89 c6                	mov    %eax,%esi
 8049933:	89 f0                	mov    %esi,%eax
 8049935:	89 fb                	mov    %edi,%ebx
 8049937:	84 db                	test   %bl,%bl
 8049939:	74 02                	je     0x804993d
 804993b:	f7 d8                	neg    %eax
 804993d:	83 c4 10             	add    $0x10,%esp
 8049940:	5b                   	pop    %ebx
 8049941:	5e                   	pop    %esi
 8049942:	5f                   	pop    %edi
 8049943:	5d                   	pop    %ebp
 8049944:	c3                   	ret    
 8049945:	e8 d4 fc ff ff       	call   0x804961e
 804994a:	81 c2 22 31 00 00    	add    $0x3122,%edx
 8049950:	8d 92 bc 00 00 00    	lea    0xbc(%edx),%edx
 8049956:	f7 d8                	neg    %eax
 8049958:	89 02                	mov    %eax,(%edx)
 804995a:	83 c8 ff             	or     $0xffffffff,%eax
 804995d:	c3                   	ret    
 804995e:	b8 ad 00 00 00       	mov    $0xad,%eax
 8049963:	cd 80                	int    $0x80
 8049965:	58                   	pop    %eax
 8049966:	b8 77 00 00 00       	mov    $0x77,%eax
 804996b:	cd 80                	int    $0x80
 804996d:	57                   	push   %edi
 804996e:	56                   	push   %esi
 804996f:	53                   	push   %ebx
 8049970:	83 ec 14             	sub    $0x14,%esp
 8049973:	e8 54 ec ff ff       	call   0x80485cc
 8049978:	81 c3 f4 30 00 00    	add    $0x30f4,%ebx
 804997e:	8b 44 24 28          	mov    0x28(%esp),%eax
 8049982:	85 c0                	test   %eax,%eax
 8049984:	74 2b                	je     0x80499b1
 8049986:	89 e2                	mov    %esp,%edx
 8049988:	89 c6                	mov    %eax,%esi
 804998a:	89 e7                	mov    %esp,%edi
 804998c:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 804998d:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 804998e:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 804998f:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 8049990:	a5                   	movsl  %ds:(%esi),%es:(%edi)
 8049991:	81 4c 24 04 00 00 00 	orl    $0x4000000,0x4(%esp)
 8049998:	04 
 8049999:	8d 8b f2 ce ff ff    	lea    -0x310e(%ebx),%ecx
 804999f:	f6 40 04 04          	testb  $0x4,0x4(%eax)
 80499a3:	75 06                	jne    0x80499ab
 80499a5:	8d 8b f9 ce ff ff    	lea    -0x3107(%ebx),%ecx
 80499ab:	89 4c 24 08          	mov    %ecx,0x8(%esp)
 80499af:	89 d0                	mov    %edx,%eax
 80499b1:	6a 08                	push   $0x8
 80499b3:	ff 74 24 30          	pushl  0x30(%esp)
 80499b7:	50                   	push   %eax
 80499b8:	ff 74 24 30          	pushl  0x30(%esp)
 80499bc:	e8 40 00 00 00       	call   0x8049a01
 80499c1:	83 c4 24             	add    $0x24,%esp
 80499c4:	5b                   	pop    %ebx
 80499c5:	5e                   	pop    %esi
 80499c6:	5f                   	pop    %edi
 80499c7:	c3                   	ret    
 80499c8:	53                   	push   %ebx
 80499c9:	e8 fe eb ff ff       	call   0x80485cc
 80499ce:	81 c3 9e 30 00 00    	add    $0x309e,%ebx
 80499d4:	8b 54 24 10          	mov    0x10(%esp),%edx
 80499d8:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 80499dc:	8b 44 24 08          	mov    0x8(%esp),%eax
 80499e0:	53                   	push   %ebx
 80499e1:	89 c3                	mov    %eax,%ebx
 80499e3:	b8 36 00 00 00       	mov    $0x36,%eax
 80499e8:	cd 80                	int    $0x80
 80499ea:	5b                   	pop    %ebx
 80499eb:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 80499f0:	76 0d                	jbe    0x80499ff
 80499f2:	f7 d8                	neg    %eax
 80499f4:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 80499fa:	89 02                	mov    %eax,(%edx)
 80499fc:	83 c8 ff             	or     $0xffffffff,%eax
 80499ff:	5b                   	pop    %ebx
 8049a00:	c3                   	ret    
 8049a01:	56                   	push   %esi
 8049a02:	53                   	push   %ebx
 8049a03:	e8 c4 eb ff ff       	call   0x80485cc
 8049a08:	81 c3 64 30 00 00    	add    $0x3064,%ebx
 8049a0e:	8b 54 24 14          	mov    0x14(%esp),%edx
 8049a12:	8b 4c 24 10          	mov    0x10(%esp),%ecx
 8049a16:	8b 44 24 0c          	mov    0xc(%esp),%eax
 8049a1a:	8b 74 24 18          	mov    0x18(%esp),%esi
 8049a1e:	53                   	push   %ebx
 8049a1f:	89 c3                	mov    %eax,%ebx
 8049a21:	b8 ae 00 00 00       	mov    $0xae,%eax
 8049a26:	cd 80                	int    $0x80
 8049a28:	5b                   	pop    %ebx
 8049a29:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 8049a2e:	76 0d                	jbe    0x8049a3d
 8049a30:	f7 d8                	neg    %eax
 8049a32:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 8049a38:	89 02                	mov    %eax,(%edx)
 8049a3a:	83 c8 ff             	or     $0xffffffff,%eax
 8049a3d:	5b                   	pop    %ebx
 8049a3e:	5e                   	pop    %esi
 8049a3f:	c3                   	ret    
 8049a40:	55                   	push   %ebp
 8049a41:	57                   	push   %edi
 8049a42:	56                   	push   %esi
 8049a43:	53                   	push   %ebx
 8049a44:	8b 74 24 14          	mov    0x14(%esp),%esi
 8049a48:	8b 7c 24 18          	mov    0x18(%esp),%edi
 8049a4c:	8b 5c 24 1c          	mov    0x1c(%esp),%ebx
 8049a50:	85 db                	test   %ebx,%ebx
 8049a52:	74 63                	je     0x8049ab7
 8049a54:	b8 ff ff ff 7f       	mov    $0x7fffffff,%eax
 8049a59:	78 02                	js     0x8049a5d
 8049a5b:	89 d8                	mov    %ebx,%eax
 8049a5d:	50                   	push   %eax
 8049a5e:	57                   	push   %edi
 8049a5f:	ff 76 04             	pushl  0x4(%esi)
 8049a62:	e8 81 ee ff ff       	call   0x80488e8
 8049a67:	83 c4 0c             	add    $0xc,%esp
 8049a6a:	85 c0                	test   %eax,%eax
 8049a6c:	78 06                	js     0x8049a74
 8049a6e:	29 c3                	sub    %eax,%ebx
 8049a70:	01 c7                	add    %eax,%edi
 8049a72:	eb dc                	jmp    0x8049a50
 8049a74:	66 83 0e 08          	orw    $0x8,(%esi)
 8049a78:	8b 46 08             	mov    0x8(%esi),%eax
 8049a7b:	8b 4e 0c             	mov    0xc(%esi),%ecx
 8049a7e:	29 c1                	sub    %eax,%ecx
 8049a80:	74 2d                	je     0x8049aaf
 8049a82:	39 cb                	cmp    %ecx,%ebx
 8049a84:	73 02                	jae    0x8049a88
 8049a86:	89 d9                	mov    %ebx,%ecx
 8049a88:	89 fd                	mov    %edi,%ebp
 8049a8a:	8a 55 00             	mov    0x0(%ebp),%dl
 8049a8d:	88 10                	mov    %dl,(%eax)
 8049a8f:	80 fa 0a             	cmp    $0xa,%dl
 8049a92:	75 07                	jne    0x8049a9b
 8049a94:	66 f7 06 00 01       	testw  $0x100,(%esi)
 8049a99:	75 0a                	jne    0x8049aa5
 8049a9b:	40                   	inc    %eax
 8049a9c:	45                   	inc    %ebp
 8049a9d:	89 ca                	mov    %ecx,%edx
 8049a9f:	29 ea                	sub    %ebp,%edx
 8049aa1:	01 fa                	add    %edi,%edx
 8049aa3:	75 e5                	jne    0x8049a8a
 8049aa5:	89 46 10             	mov    %eax,0x10(%esi)
 8049aa8:	8b 56 08             	mov    0x8(%esi),%edx
 8049aab:	29 c2                	sub    %eax,%edx
 8049aad:	01 d3                	add    %edx,%ebx
 8049aaf:	8b 44 24 1c          	mov    0x1c(%esp),%eax
 8049ab3:	29 d8                	sub    %ebx,%eax
 8049ab5:	eb 04                	jmp    0x8049abb
 8049ab7:	8b 44 24 1c          	mov    0x1c(%esp),%eax
 8049abb:	5b                   	pop    %ebx
 8049abc:	5e                   	pop    %esi
 8049abd:	5f                   	pop    %edi
 8049abe:	5d                   	pop    %ebp
 8049abf:	c3                   	ret    
 8049ac0:	55                   	push   %ebp
 8049ac1:	57                   	push   %edi
 8049ac2:	56                   	push   %esi
 8049ac3:	53                   	push   %ebx
 8049ac4:	8b 7c 24 14          	mov    0x14(%esp),%edi
 8049ac8:	8b 5c 24 18          	mov    0x18(%esp),%ebx
 8049acc:	8b 74 24 1c          	mov    0x1c(%esp),%esi
 8049ad0:	66 f7 06 00 02       	testw  $0x200,(%esi)
 8049ad5:	74 15                	je     0x8049aec
 8049ad7:	89 5c 24 1c          	mov    %ebx,0x1c(%esp)
 8049adb:	89 7c 24 18          	mov    %edi,0x18(%esp)
 8049adf:	89 74 24 14          	mov    %esi,0x14(%esp)
 8049ae3:	5b                   	pop    %ebx
 8049ae4:	5e                   	pop    %esi
 8049ae5:	5f                   	pop    %edi
 8049ae6:	5d                   	pop    %ebp
 8049ae7:	e9 54 ff ff ff       	jmp    0x8049a40
 8049aec:	83 7e 04 fe          	cmpl   $0xfffffffe,0x4(%esi)
 8049af0:	8b 46 10             	mov    0x10(%esi),%eax
 8049af3:	8b 6e 0c             	mov    0xc(%esi),%ebp
 8049af6:	75 18                	jne    0x8049b10
 8049af8:	29 c5                	sub    %eax,%ebp
 8049afa:	39 dd                	cmp    %ebx,%ebp
 8049afc:	76 02                	jbe    0x8049b00
 8049afe:	89 dd                	mov    %ebx,%ebp
 8049b00:	55                   	push   %ebp
 8049b01:	57                   	push   %edi
 8049b02:	50                   	push   %eax
 8049b03:	e8 b6 08 00 00       	call   0x804a3be
 8049b08:	01 6e 10             	add    %ebp,0x10(%esi)
 8049b0b:	83 c4 0c             	add    $0xc,%esp
 8049b0e:	eb 1b                	jmp    0x8049b2b
 8049b10:	29 c5                	sub    %eax,%ebp
 8049b12:	39 eb                	cmp    %ebp,%ebx
 8049b14:	77 64                	ja     0x8049b7a
 8049b16:	53                   	push   %ebx
 8049b17:	57                   	push   %edi
 8049b18:	50                   	push   %eax
 8049b19:	e8 a0 08 00 00       	call   0x804a3be
 8049b1e:	01 5e 10             	add    %ebx,0x10(%esi)
 8049b21:	83 c4 0c             	add    $0xc,%esp
 8049b24:	66 f7 06 00 01       	testw  $0x100,(%esi)
 8049b29:	75 04                	jne    0x8049b2f
 8049b2b:	89 d8                	mov    %ebx,%eax
 8049b2d:	eb 65                	jmp    0x8049b94
 8049b2f:	53                   	push   %ebx
 8049b30:	6a 0a                	push   $0xa
 8049b32:	57                   	push   %edi
 8049b33:	e8 a9 08 00 00       	call   0x804a3e1
 8049b38:	83 c4 0c             	add    $0xc,%esp
 8049b3b:	85 c0                	test   %eax,%eax
 8049b3d:	74 ec                	je     0x8049b2b
 8049b3f:	56                   	push   %esi
 8049b40:	e8 70 ee ff ff       	call   0x80489b5
 8049b45:	59                   	pop    %ecx
 8049b46:	85 c0                	test   %eax,%eax
 8049b48:	74 e1                	je     0x8049b2b
 8049b4a:	89 da                	mov    %ebx,%edx
 8049b4c:	39 c3                	cmp    %eax,%ebx
 8049b4e:	76 02                	jbe    0x8049b52
 8049b50:	89 c2                	mov    %eax,%edx
 8049b52:	89 dd                	mov    %ebx,%ebp
 8049b54:	29 d5                	sub    %edx,%ebp
 8049b56:	01 fd                	add    %edi,%ebp
 8049b58:	89 ef                	mov    %ebp,%edi
 8049b5a:	89 d1                	mov    %edx,%ecx
 8049b5c:	e3 09                	jecxz  0x8049b67
 8049b5e:	b0 0a                	mov    $0xa,%al
 8049b60:	f2 ae                	repnz scas %es:(%edi),%al
 8049b62:	8d 7f ff             	lea    -0x1(%edi),%edi
 8049b65:	74 02                	je     0x8049b69
 8049b67:	31 ff                	xor    %edi,%edi
 8049b69:	85 ff                	test   %edi,%edi
 8049b6b:	74 be                	je     0x8049b2b
 8049b6d:	01 ea                	add    %ebp,%edx
 8049b6f:	29 fa                	sub    %edi,%edx
 8049b71:	29 56 10             	sub    %edx,0x10(%esi)
 8049b74:	89 d8                	mov    %ebx,%eax
 8049b76:	29 d0                	sub    %edx,%eax
 8049b78:	eb 1a                	jmp    0x8049b94
 8049b7a:	39 46 08             	cmp    %eax,0x8(%esi)
 8049b7d:	0f 84 54 ff ff ff    	je     0x8049ad7
 8049b83:	56                   	push   %esi
 8049b84:	e8 2c ee ff ff       	call   0x80489b5
 8049b89:	5a                   	pop    %edx
 8049b8a:	85 c0                	test   %eax,%eax
 8049b8c:	0f 84 45 ff ff ff    	je     0x8049ad7
 8049b92:	31 c0                	xor    %eax,%eax
 8049b94:	5b                   	pop    %ebx
 8049b95:	5e                   	pop    %esi
 8049b96:	5f                   	pop    %edi
 8049b97:	5d                   	pop    %ebp
 8049b98:	c3                   	ret    
 8049b99:	53                   	push   %ebx
 8049b9a:	e8 7f fa ff ff       	call   0x804961e
 8049b9f:	81 c2 cd 2e 00 00    	add    $0x2ecd,%edx
 8049ba5:	8b 5c 24 08          	mov    0x8(%esp),%ebx
 8049ba9:	8b 03                	mov    (%ebx),%eax
 8049bab:	a8 20                	test   $0x20,%al
 8049bad:	74 15                	je     0x8049bc4
 8049baf:	8d 82 bc 00 00 00    	lea    0xbc(%edx),%eax
 8049bb5:	c7 00 09 00 00 00    	movl   $0x9,(%eax)
 8049bbb:	66 83 0b 08          	orw    $0x8,(%ebx)
 8049bbf:	83 c8 ff             	or     $0xffffffff,%eax
 8049bc2:	eb 5c                	jmp    0x8049c20
 8049bc4:	a8 03                	test   $0x3,%al
 8049bc6:	74 41                	je     0x8049c09
 8049bc8:	a8 04                	test   $0x4,%al
 8049bca:	74 12                	je     0x8049bde
 8049bcc:	66 83 23 fc          	andw   $0xfffc,(%ebx)
 8049bd0:	8b 43 08             	mov    0x8(%ebx),%eax
 8049bd3:	89 43 18             	mov    %eax,0x18(%ebx)
 8049bd6:	89 43 10             	mov    %eax,0x10(%ebx)
 8049bd9:	89 43 14             	mov    %eax,0x14(%ebx)
 8049bdc:	eb 2b                	jmp    0x8049c09
 8049bde:	8b 4b 10             	mov    0x10(%ebx),%ecx
 8049be1:	39 4b 14             	cmp    %ecx,0x14(%ebx)
 8049be4:	75 04                	jne    0x8049bea
 8049be6:	a8 02                	test   $0x2,%al
 8049be8:	74 e2                	je     0x8049bcc
 8049bea:	66 25 00 04          	and    $0x400,%ax
 8049bee:	66 83 f8 01          	cmp    $0x1,%ax
 8049bf2:	19 c0                	sbb    %eax,%eax
 8049bf4:	83 c0 02             	add    $0x2,%eax
 8049bf7:	50                   	push   %eax
 8049bf8:	6a 00                	push   $0x0
 8049bfa:	53                   	push   %ebx
 8049bfb:	e8 78 08 00 00       	call   0x804a478
 8049c00:	83 c4 0c             	add    $0xc,%esp
 8049c03:	85 c0                	test   %eax,%eax
 8049c05:	74 c5                	je     0x8049bcc
 8049c07:	eb b2                	jmp    0x8049bbb
 8049c09:	8b 13                	mov    (%ebx),%edx
 8049c0b:	89 d0                	mov    %edx,%eax
 8049c0d:	83 c8 40             	or     $0x40,%eax
 8049c10:	66 89 03             	mov    %ax,(%ebx)
 8049c13:	31 c0                	xor    %eax,%eax
 8049c15:	80 e6 03             	and    $0x3,%dh
 8049c18:	75 06                	jne    0x8049c20
 8049c1a:	8b 53 0c             	mov    0xc(%ebx),%edx
 8049c1d:	89 53 1c             	mov    %edx,0x1c(%ebx)
 8049c20:	5b                   	pop    %ebx
 8049c21:	c3                   	ret    
 8049c22:	55                   	push   %ebp
 8049c23:	89 e5                	mov    %esp,%ebp
 8049c25:	51                   	push   %ecx
 8049c26:	8d 4d 08             	lea    0x8(%ebp),%ecx
 8049c29:	8b 11                	mov    (%ecx),%edx
 8049c2b:	8b 41 04             	mov    0x4(%ecx),%eax
 8049c2e:	83 79 08 00          	cmpl   $0x0,0x8(%ecx)
 8049c32:	78 23                	js     0x8049c57
 8049c34:	f6 c6 08             	test   $0x8,%dh
 8049c37:	75 23                	jne    0x8049c5c
 8049c39:	8b 00                	mov    (%eax),%eax
 8049c3b:	81 fa 00 01 00 00    	cmp    $0x100,%edx
 8049c41:	75 05                	jne    0x8049c48
 8049c43:	0f b6 c0             	movzbl %al,%eax
 8049c46:	eb 0b                	jmp    0x8049c53
 8049c48:	81 fa 00 02 00 00    	cmp    $0x200,%edx
 8049c4e:	75 03                	jne    0x8049c53
 8049c50:	0f b7 c0             	movzwl %ax,%eax
 8049c53:	31 d2                	xor    %edx,%edx
 8049c55:	eb 25                	jmp    0x8049c7c
 8049c57:	f6 c6 08             	test   $0x8,%dh
 8049c5a:	74 07                	je     0x8049c63
 8049c5c:	8b 50 04             	mov    0x4(%eax),%edx
 8049c5f:	8b 00                	mov    (%eax),%eax
 8049c61:	eb 19                	jmp    0x8049c7c
 8049c63:	8b 00                	mov    (%eax),%eax
 8049c65:	81 fa 00 01 00 00    	cmp    $0x100,%edx
 8049c6b:	75 05                	jne    0x8049c72
 8049c6d:	0f b6 c0             	movzbl %al,%eax
 8049c70:	eb 09                	jmp    0x8049c7b
 8049c72:	81 fa 00 02 00 00    	cmp    $0x200,%edx
 8049c78:	75 01                	jne    0x8049c7b
 8049c7a:	98                   	cwtl   
 8049c7b:	99                   	cltd   
 8049c7c:	59                   	pop    %ecx
 8049c7d:	5d                   	pop    %ebp
 8049c7e:	c3                   	ret    
 8049c7f:	53                   	push   %ebx
 8049c80:	8b 44 24 08          	mov    0x8(%esp),%eax
 8049c84:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 8049c88:	8b 54 24 10          	mov    0x10(%esp),%edx
 8049c8c:	8b 5c 24 14          	mov    0x14(%esp),%ebx
 8049c90:	81 f9 00 01 00 00    	cmp    $0x100,%ecx
 8049c96:	75 04                	jne    0x8049c9c
 8049c98:	88 10                	mov    %dl,(%eax)
 8049c9a:	eb 1e                	jmp    0x8049cba
 8049c9c:	81 f9 00 08 00 00    	cmp    $0x800,%ecx
 8049ca2:	75 07                	jne    0x8049cab
 8049ca4:	89 10                	mov    %edx,(%eax)
 8049ca6:	89 58 04             	mov    %ebx,0x4(%eax)
 8049ca9:	eb 0f                	jmp    0x8049cba
 8049cab:	81 f9 00 02 00 00    	cmp    $0x200,%ecx
 8049cb1:	75 05                	jne    0x8049cb8
 8049cb3:	66 89 10             	mov    %dx,(%eax)
 8049cb6:	eb 02                	jmp    0x8049cba
 8049cb8:	89 10                	mov    %edx,(%eax)
 8049cba:	5b                   	pop    %ebx
 8049cbb:	c3                   	ret    
 8049cbc:	55                   	push   %ebp
 8049cbd:	57                   	push   %edi
 8049cbe:	56                   	push   %esi
 8049cbf:	53                   	push   %ebx
 8049cc0:	83 ec 0c             	sub    $0xc,%esp
 8049cc3:	8b 6c 24 20          	mov    0x20(%esp),%ebp
 8049cc7:	8b 74 24 24          	mov    0x24(%esp),%esi
 8049ccb:	8b 7c 24 28          	mov    0x28(%esp),%edi
 8049ccf:	8b 4c 24 2c          	mov    0x2c(%esp),%ecx
 8049cd3:	31 db                	xor    %ebx,%ebx
 8049cd5:	85 c9                	test   %ecx,%ecx
 8049cd7:	79 12                	jns    0x8049ceb
 8049cd9:	f7 d9                	neg    %ecx
 8049cdb:	85 ff                	test   %edi,%edi
 8049cdd:	79 0c                	jns    0x8049ceb
 8049cdf:	f7 de                	neg    %esi
 8049ce1:	83 d7 00             	adc    $0x0,%edi
 8049ce4:	f7 df                	neg    %edi
 8049ce6:	bb 01 00 00 00       	mov    $0x1,%ebx
 8049ceb:	c6 45 00 00          	movb   $0x0,0x0(%ebp)
 8049cef:	83 c8 ff             	or     $0xffffffff,%eax
 8049cf2:	31 d2                	xor    %edx,%edx
 8049cf4:	f7 f1                	div    %ecx
 8049cf6:	89 44 24 08          	mov    %eax,0x8(%esp)
 8049cfa:	8d 42 01             	lea    0x1(%edx),%eax
 8049cfd:	89 44 24 04          	mov    %eax,0x4(%esp)
 8049d01:	39 c1                	cmp    %eax,%ecx
 8049d03:	75 0c                	jne    0x8049d11
 8049d05:	ff 44 24 08          	incl   0x8(%esp)
 8049d09:	c7 44 24 04 00 00 00 	movl   $0x0,0x4(%esp)
 8049d10:	00 
 8049d11:	89 34 24             	mov    %esi,(%esp)
 8049d14:	85 ff                	test   %edi,%edi
 8049d16:	74 2d                	je     0x8049d45
 8049d18:	89 f8                	mov    %edi,%eax
 8049d1a:	31 d2                	xor    %edx,%edx
 8049d1c:	f7 f1                	div    %ecx
 8049d1e:	89 d6                	mov    %edx,%esi
 8049d20:	89 c7                	mov    %eax,%edi
 8049d22:	8b 04 24             	mov    (%esp),%eax
 8049d25:	31 d2                	xor    %edx,%edx
 8049d27:	f7 f1                	div    %ecx
 8049d29:	89 04 24             	mov    %eax,(%esp)
 8049d2c:	8b 44 24 04          	mov    0x4(%esp),%eax
 8049d30:	0f af c6             	imul   %esi,%eax
 8049d33:	01 d0                	add    %edx,%eax
 8049d35:	0f af 74 24 08       	imul   0x8(%esp),%esi
 8049d3a:	03 34 24             	add    (%esp),%esi
 8049d3d:	31 d2                	xor    %edx,%edx
 8049d3f:	f7 f1                	div    %ecx
 8049d41:	01 f0                	add    %esi,%eax
 8049d43:	eb 07                	jmp    0x8049d4c
 8049d45:	8b 04 24             	mov    (%esp),%eax
 8049d48:	31 d2                	xor    %edx,%edx
 8049d4a:	f7 f1                	div    %ecx
 8049d4c:	89 04 24             	mov    %eax,(%esp)
 8049d4f:	4d                   	dec    %ebp
 8049d50:	88 d0                	mov    %dl,%al
 8049d52:	03 44 24 30          	add    0x30(%esp),%eax
 8049d56:	83 fa 09             	cmp    $0x9,%edx
 8049d59:	77 03                	ja     0x8049d5e
 8049d5b:	8d 42 30             	lea    0x30(%edx),%eax
 8049d5e:	88 45 00             	mov    %al,0x0(%ebp)
 8049d61:	8b 04 24             	mov    (%esp),%eax
 8049d64:	09 f8                	or     %edi,%eax
 8049d66:	75 ac                	jne    0x8049d14
 8049d68:	85 db                	test   %ebx,%ebx
 8049d6a:	74 05                	je     0x8049d71
 8049d6c:	c6 45 ff 2d          	movb   $0x2d,-0x1(%ebp)
 8049d70:	4d                   	dec    %ebp
 8049d71:	89 e8                	mov    %ebp,%eax
 8049d73:	83 c4 0c             	add    $0xc,%esp
 8049d76:	5b                   	pop    %ebx
 8049d77:	5e                   	pop    %esi
 8049d78:	5f                   	pop    %edi
 8049d79:	5d                   	pop    %ebp
 8049d7a:	c3                   	ret    
 8049d7b:	55                   	push   %ebp
 8049d7c:	57                   	push   %edi
 8049d7d:	56                   	push   %esi
 8049d7e:	53                   	push   %ebx
 8049d7f:	81 ec b8 00 00 00    	sub    $0xb8,%esp
 8049d85:	e8 58 f8 ff ff       	call   0x80495e2
 8049d8a:	81 c5 e2 2c 00 00    	add    $0x2ce2,%ebp
 8049d90:	db ac 24 d0 00 00 00 	fldt   0xd0(%esp)
 8049d97:	8b 84 24 dc 00 00 00 	mov    0xdc(%esp),%eax
 8049d9e:	8b 40 04             	mov    0x4(%eax),%eax
 8049da1:	89 44 24 10          	mov    %eax,0x10(%esp)
 8049da5:	8b 84 24 dc 00 00 00 	mov    0xdc(%esp),%eax
 8049dac:	8b 30                	mov    (%eax),%esi
 8049dae:	8b 40 08             	mov    0x8(%eax),%eax
 8049db1:	88 44 24 03          	mov    %al,0x3(%esp)
 8049db5:	c6 44 24 2a 65       	movb   $0x65,0x2a(%esp)
 8049dba:	88 c2                	mov    %al,%dl
 8049dbc:	83 ca 20             	or     $0x20,%edx
 8049dbf:	80 fa 61             	cmp    $0x61,%dl
 8049dc2:	75 07                	jne    0x8049dcb
 8049dc4:	83 c0 06             	add    $0x6,%eax
 8049dc7:	88 44 24 03          	mov    %al,0x3(%esp)
 8049dcb:	85 f6                	test   %esi,%esi
 8049dcd:	79 05                	jns    0x8049dd4
 8049dcf:	be 06 00 00 00       	mov    $0x6,%esi
 8049dd4:	c6 44 24 24 00       	movb   $0x0,0x24(%esp)
 8049dd9:	8b 84 24 dc 00 00 00 	mov    0xdc(%esp),%eax
 8049de0:	8b 40 0c             	mov    0xc(%eax),%eax
 8049de3:	a8 02                	test   $0x2,%al
 8049de5:	74 07                	je     0x8049dee
 8049de7:	c6 44 24 24 2b       	movb   $0x2b,0x24(%esp)
 8049dec:	eb 09                	jmp    0x8049df7
 8049dee:	a8 01                	test   $0x1,%al
 8049df0:	74 05                	je     0x8049df7
 8049df2:	c6 44 24 24 20       	movb   $0x20,0x24(%esp)
 8049df7:	c6 44 24 25 00       	movb   $0x0,0x25(%esp)
 8049dfc:	c7 44 24 6c 00 00 00 	movl   $0x0,0x6c(%esp)
 8049e03:	00 
 8049e04:	dd e0                	fucom  %st(0)
 8049e06:	df e0                	fnstsw %ax
 8049e08:	9e                   	sahf   
 8049e09:	7a 13                	jp     0x8049e1e
 8049e0b:	d9 ee                	fldz   
 8049e0d:	d9 c9                	fxch   %st(1)
 8049e0f:	dd e1                	fucom  %st(1)
 8049e11:	df e0                	fnstsw %ax
 8049e13:	9e                   	sahf   
 8049e14:	d9 c1                	fld    %st(1)
 8049e16:	7b 12                	jnp    0x8049e2a
 8049e18:	dd da                	fstp   %st(2)
 8049e1a:	d9 c9                	fxch   %st(1)
 8049e1c:	eb 31                	jmp    0x8049e4f
 8049e1e:	dd d8                	fstp   %st(0)
 8049e20:	c7 44 24 6c 08 00 00 	movl   $0x8,0x6c(%esp)
 8049e27:	00 
 8049e28:	eb 4a                	jmp    0x8049e74
 8049e2a:	75 1f                	jne    0x8049e4b
 8049e2c:	dd d8                	fstp   %st(0)
 8049e2e:	d9 e8                	fld1   
 8049e30:	d8 f1                	fdiv   %st(1),%st
 8049e32:	d9 ca                	fxch   %st(2)
 8049e34:	dd ea                	fucomp %st(2)
 8049e36:	df e0                	fnstsw %ax
 8049e38:	dd d9                	fstp   %st(1)
 8049e3a:	9e                   	sahf   
 8049e3b:	0f 86 f8 00 00 00    	jbe    0x8049f39
 8049e41:	c6 44 24 24 2d       	movb   $0x2d,0x24(%esp)
 8049e46:	e9 ee 00 00 00       	jmp    0x8049f39
 8049e4b:	dd da                	fstp   %st(2)
 8049e4d:	d9 c9                	fxch   %st(1)
 8049e4f:	dd e9                	fucomp %st(1)
 8049e51:	df e0                	fnstsw %ax
 8049e53:	9e                   	sahf   
 8049e54:	76 07                	jbe    0x8049e5d
 8049e56:	c6 44 24 24 2d       	movb   $0x2d,0x24(%esp)
 8049e5b:	d9 e0                	fchs   
 8049e5d:	d9 c0                	fld    %st(0)
 8049e5f:	d8 8d 84 e3 ff ff    	fmuls  -0x1c7c(%ebp)
 8049e65:	d9 c9                	fxch   %st(1)
 8049e67:	dd e1                	fucom  %st(1)
 8049e69:	df e0                	fnstsw %ax
 8049e6b:	dd d9                	fstp   %st(1)
 8049e6d:	9e                   	sahf   
 8049e6e:	7a 41                	jp     0x8049eb1
 8049e70:	75 3f                	jne    0x8049eb1
 8049e72:	dd d8                	fstp   %st(0)
 8049e74:	8b 84 24 dc 00 00 00 	mov    0xdc(%esp),%eax
 8049e7b:	c7 40 10 20 00 00 00 	movl   $0x20,0x10(%eax)
 8049e82:	c7 44 24 64 70 00 00 	movl   $0x70,0x64(%esp)
 8049e89:	00 
 8049e8a:	c7 44 24 68 03 00 00 	movl   $0x3,0x68(%esp)
 8049e91:	00 
 8049e92:	80 7c 24 03 60       	cmpb   $0x60,0x3(%esp)
 8049e97:	77 05                	ja     0x8049e9e
 8049e99:	83 44 24 6c 04       	addl   $0x4,0x6c(%esp)
 8049e9e:	8d 85 70 e3 ff ff    	lea    -0x1c90(%ebp),%eax
 8049ea4:	01 44 24 6c          	add    %eax,0x6c(%esp)
 8049ea8:	8d 5c 24 70          	lea    0x70(%esp),%ebx
 8049eac:	e9 94 03 00 00       	jmp    0x804a245
 8049eb1:	8d 95 d4 e2 ff ff    	lea    -0x1d2c(%ebp),%edx
 8049eb7:	8d 9a 64 ff ff ff    	lea    -0x9c(%edx),%ebx
 8049ebd:	d9 c0                	fld    %st(0)
 8049ebf:	b9 00 10 00 00       	mov    $0x1000,%ecx
 8049ec4:	bf 08 00 00 00       	mov    $0x8,%edi
 8049ec9:	d9 85 88 e3 ff ff    	flds   -0x1c78(%ebp)
 8049ecf:	eb 02                	jmp    0x8049ed3
 8049ed1:	d9 c9                	fxch   %st(1)
 8049ed3:	dd e2                	fucom  %st(2)
 8049ed5:	df e0                	fnstsw %ax
 8049ed7:	9e                   	sahf   
 8049ed8:	db aa 90 00 00 00    	fldt   0x90(%edx)
 8049ede:	76 17                	jbe    0x8049ef7
 8049ee0:	d8 ca                	fmul   %st(2),%st
 8049ee2:	d9 85 8c e3 ff ff    	flds   -0x1c74(%ebp)
 8049ee8:	dd e9                	fucomp %st(1)
 8049eea:	df e0                	fnstsw %ax
 8049eec:	9e                   	sahf   
 8049eed:	76 19                	jbe    0x8049f08
 8049eef:	dd da                	fstp   %st(2)
 8049ef1:	d9 c9                	fxch   %st(1)
 8049ef3:	29 cf                	sub    %ecx,%edi
 8049ef5:	eb 0f                	jmp    0x8049f06
 8049ef7:	d8 fa                	fdivr  %st(2),%st
 8049ef9:	dd e1                	fucom  %st(1)
 8049efb:	df e0                	fnstsw %ax
 8049efd:	9e                   	sahf   
 8049efe:	72 0e                	jb     0x8049f0e
 8049f00:	dd da                	fstp   %st(2)
 8049f02:	d9 c9                	fxch   %st(1)
 8049f04:	01 cf                	add    %ecx,%edi
 8049f06:	eb 0a                	jmp    0x8049f12
 8049f08:	dd d8                	fstp   %st(0)
 8049f0a:	d9 c9                	fxch   %st(1)
 8049f0c:	eb 04                	jmp    0x8049f12
 8049f0e:	dd d8                	fstp   %st(0)
 8049f10:	d9 c9                	fxch   %st(1)
 8049f12:	d1 f9                	sar    %ecx
 8049f14:	83 ea 0c             	sub    $0xc,%edx
 8049f17:	39 d3                	cmp    %edx,%ebx
 8049f19:	75 b6                	jne    0x8049ed1
 8049f1b:	dd d9                	fstp   %st(1)
 8049f1d:	dd d9                	fstp   %st(1)
 8049f1f:	d9 85 8c e3 ff ff    	flds   -0x1c74(%ebp)
 8049f25:	d9 c9                	fxch   %st(1)
 8049f27:	dd e1                	fucom  %st(1)
 8049f29:	df e0                	fnstsw %ax
 8049f2b:	dd d9                	fstp   %st(1)
 8049f2d:	9e                   	sahf   
 8049f2e:	72 0c                	jb     0x8049f3c
 8049f30:	d8 b5 90 e3 ff ff    	fdivs  -0x1c70(%ebp)
 8049f36:	47                   	inc    %edi
 8049f37:	eb 03                	jmp    0x8049f3c
 8049f39:	83 cf ff             	or     $0xffffffff,%edi
 8049f3c:	8d 4c 24 3c          	lea    0x3c(%esp),%ecx
 8049f40:	d9 85 8c e3 ff ff    	flds   -0x1c74(%ebp)
 8049f46:	d9 c9                	fxch   %st(1)
 8049f48:	8d 44 24 57          	lea    0x57(%esp),%eax
 8049f4c:	89 44 24 14          	mov    %eax,0x14(%esp)
 8049f50:	d9 7c 24 22          	fnstcw 0x22(%esp)
 8049f54:	66 8b 44 24 22       	mov    0x22(%esp),%ax
 8049f59:	80 cc 0c             	or     $0xc,%ah
 8049f5c:	66 89 44 24 20       	mov    %ax,0x20(%esp)
 8049f61:	d9 c0                	fld    %st(0)
 8049f63:	d9 6c 24 20          	fldcw  0x20(%esp)
 8049f67:	df 7c 24 18          	fistpll 0x18(%esp)
 8049f6b:	d9 6c 24 22          	fldcw  0x22(%esp)
 8049f6f:	8b 44 24 18          	mov    0x18(%esp),%eax
 8049f73:	89 44 24 04          	mov    %eax,0x4(%esp)
 8049f77:	c7 44 24 08 00 00 00 	movl   $0x0,0x8(%esp)
 8049f7e:	00 
 8049f7f:	df 6c 24 04          	fildll 0x4(%esp)
 8049f83:	de e9                	fsubrp %st,%st(1)
 8049f85:	d8 c9                	fmul   %st(1),%st
 8049f87:	8d 51 09             	lea    0x9(%ecx),%edx
 8049f8a:	89 54 24 0c          	mov    %edx,0xc(%esp)
 8049f8e:	c7 44 24 04 09 00 00 	movl   $0x9,0x4(%esp)
 8049f95:	00 
 8049f96:	bb 0a 00 00 00       	mov    $0xa,%ebx
 8049f9b:	31 d2                	xor    %edx,%edx
 8049f9d:	f7 f3                	div    %ebx
 8049f9f:	83 c2 30             	add    $0x30,%edx
 8049fa2:	8b 5c 24 04          	mov    0x4(%esp),%ebx
 8049fa6:	88 54 19 ff          	mov    %dl,-0x1(%ecx,%ebx,1)
 8049faa:	ff 4c 24 04          	decl   0x4(%esp)
 8049fae:	75 e6                	jne    0x8049f96
 8049fb0:	8b 4c 24 0c          	mov    0xc(%esp),%ecx
 8049fb4:	3b 4c 24 14          	cmp    0x14(%esp),%ecx
 8049fb8:	75 a7                	jne    0x8049f61
 8049fba:	dd d8                	fstp   %st(0)
 8049fbc:	dd d8                	fstp   %st(0)
 8049fbe:	80 7c 24 03 60       	cmpb   $0x60,0x3(%esp)
 8049fc3:	77 0a                	ja     0x8049fcf
 8049fc5:	c6 44 24 2a 45       	movb   $0x45,0x2a(%esp)
 8049fca:	80 44 24 03 20       	addb   $0x20,0x3(%esp)
 8049fcf:	80 7c 24 03 67       	cmpb   $0x67,0x3(%esp)
 8049fd4:	75 0f                	jne    0x8049fe5
 8049fd6:	85 f6                	test   %esi,%esi
 8049fd8:	0f 84 23 03 00 00    	je     0x804a301
 8049fde:	8d 5e ff             	lea    -0x1(%esi),%ebx
 8049fe1:	89 de                	mov    %ebx,%esi
 8049fe3:	eb 26                	jmp    0x804a00b
 8049fe5:	89 f3                	mov    %esi,%ebx
 8049fe7:	80 7c 24 03 66       	cmpb   $0x66,0x3(%esp)
 8049fec:	75 1d                	jne    0x804a00b
 8049fee:	8d 1c 37             	lea    (%edi,%esi,1),%ebx
 8049ff1:	83 fb ff             	cmp    $0xffffffff,%ebx
 8049ff4:	7d 15                	jge    0x804a00b
 8049ff6:	8d 7c 24 3a          	lea    0x3a(%esp),%edi
 8049ffa:	b8 30 30 30 30       	mov    $0x30303030,%eax
 8049fff:	ab                   	stos   %eax,%es:(%edi)
 804a000:	ab                   	stos   %eax,%es:(%edi)
 804a001:	ab                   	stos   %eax,%es:(%edi)
 804a002:	ab                   	stos   %eax,%es:(%edi)
 804a003:	ab                   	stos   %eax,%es:(%edi)
 804a004:	aa                   	stos   %al,%es:(%edi)
 804a005:	83 cf ff             	or     $0xffffffff,%edi
 804a008:	83 cb ff             	or     $0xffffffff,%ebx
 804a00b:	c6 44 24 3a 00       	movb   $0x0,0x3a(%esp)
 804a010:	c6 44 24 3b 30       	movb   $0x30,0x3b(%esp)
 804a015:	83 fb 14             	cmp    $0x14,%ebx
 804a018:	7f 0e                	jg     0x804a028
 804a01a:	8d 44 1c 3d          	lea    0x3d(%esp,%ebx,1),%eax
 804a01e:	31 c9                	xor    %ecx,%ecx
 804a020:	80 38 34             	cmpb   $0x34,(%eax)
 804a023:	0f 97 c1             	seta   %cl
 804a026:	eb 06                	jmp    0x804a02e
 804a028:	31 c9                	xor    %ecx,%ecx
 804a02a:	8d 44 24 51          	lea    0x51(%esp),%eax
 804a02e:	48                   	dec    %eax
 804a02f:	88 ca                	mov    %cl,%dl
 804a031:	02 10                	add    (%eax),%dl
 804a033:	88 10                	mov    %dl,(%eax)
 804a035:	80 fa 39             	cmp    $0x39,%dl
 804a038:	77 f4                	ja     0x804a02e
 804a03a:	80 fa 30             	cmp    $0x30,%dl
 804a03d:	74 ef                	je     0x804a02e
 804a03f:	8d 54 24 3b          	lea    0x3b(%esp),%edx
 804a043:	8d 4c 24 3c          	lea    0x3c(%esp),%ecx
 804a047:	39 d0                	cmp    %edx,%eax
 804a049:	77 05                	ja     0x804a050
 804a04b:	47                   	inc    %edi
 804a04c:	89 d0                	mov    %edx,%eax
 804a04e:	89 d1                	mov    %edx,%ecx
 804a050:	8d 50 01             	lea    0x1(%eax),%edx
 804a053:	c6 40 01 00          	movb   $0x0,0x1(%eax)
 804a057:	80 7c 24 03 67       	cmpb   $0x67,0x3(%esp)
 804a05c:	75 17                	jne    0x804a075
 804a05e:	83 ff fc             	cmp    $0xfffffffc,%edi
 804a061:	0f 8c 8e 02 00 00    	jl     0x804a2f5
 804a067:	39 df                	cmp    %ebx,%edi
 804a069:	0f 8f 86 02 00 00    	jg     0x804a2f5
 804a06f:	89 de                	mov    %ebx,%esi
 804a071:	29 fe                	sub    %edi,%esi
 804a073:	eb 10                	jmp    0x804a085
 804a075:	8a 44 24 03          	mov    0x3(%esp),%al
 804a079:	88 44 24 0c          	mov    %al,0xc(%esp)
 804a07d:	3c 66                	cmp    $0x66,%al
 804a07f:	0f 85 75 02 00 00    	jne    0x804a2fa
 804a085:	89 f8                	mov    %edi,%eax
 804a087:	85 ff                	test   %edi,%edi
 804a089:	79 07                	jns    0x804a092
 804a08b:	c6 41 ff 30          	movb   $0x30,-0x1(%ecx)
 804a08f:	89 f8                	mov    %edi,%eax
 804a091:	49                   	dec    %ecx
 804a092:	c6 44 24 0c 66       	movb   $0x66,0xc(%esp)
 804a097:	c7 44 24 64 b0 00 00 	movl   $0xb0,0x64(%esp)
 804a09e:	00 
 804a09f:	c7 44 24 68 01 00 00 	movl   $0x1,0x68(%esp)
 804a0a6:	00 
 804a0a7:	8d 5c 24 28          	lea    0x28(%esp),%ebx
 804a0ab:	89 5c 24 6c          	mov    %ebx,0x6c(%esp)
 804a0af:	8d 59 01             	lea    0x1(%ecx),%ebx
 804a0b2:	89 5c 24 04          	mov    %ebx,0x4(%esp)
 804a0b6:	8a 09                	mov    (%ecx),%cl
 804a0b8:	88 4c 24 28          	mov    %cl,0x28(%esp)
 804a0bc:	c6 44 24 29 00       	movb   $0x0,0x29(%esp)
 804a0c1:	29 da                	sub    %ebx,%edx
 804a0c3:	8d 5c 24 70          	lea    0x70(%esp),%ebx
 804a0c7:	85 c0                	test   %eax,%eax
 804a0c9:	78 60                	js     0x804a12b
 804a0cb:	c7 44 24 70 70 00 00 	movl   $0x70,0x70(%esp)
 804a0d2:	00 
 804a0d3:	8b 4c 24 04          	mov    0x4(%esp),%ecx
 804a0d7:	89 4c 24 78          	mov    %ecx,0x78(%esp)
 804a0db:	39 c2                	cmp    %eax,%edx
 804a0dd:	7f 2f                	jg     0x804a10e
 804a0df:	89 54 24 74          	mov    %edx,0x74(%esp)
 804a0e3:	29 d0                	sub    %edx,%eax
 804a0e5:	74 3b                	je     0x804a122
 804a0e7:	c7 44 24 7c b0 00 00 	movl   $0xb0,0x7c(%esp)
 804a0ee:	00 
 804a0ef:	89 84 24 80 00 00 00 	mov    %eax,0x80(%esp)
 804a0f6:	8d 85 73 e3 ff ff    	lea    -0x1c8d(%ebp),%eax
 804a0fc:	89 84 24 84 00 00 00 	mov    %eax,0x84(%esp)
 804a103:	31 d2                	xor    %edx,%edx
 804a105:	8d 9c 24 88 00 00 00 	lea    0x88(%esp),%ebx
 804a10c:	eb 1a                	jmp    0x804a128
 804a10e:	8d 5c 24 70          	lea    0x70(%esp),%ebx
 804a112:	85 c0                	test   %eax,%eax
 804a114:	74 12                	je     0x804a128
 804a116:	89 44 24 74          	mov    %eax,0x74(%esp)
 804a11a:	01 44 24 04          	add    %eax,0x4(%esp)
 804a11e:	29 c2                	sub    %eax,%edx
 804a120:	eb 02                	jmp    0x804a124
 804a122:	31 d2                	xor    %edx,%edx
 804a124:	8d 5c 24 7c          	lea    0x7c(%esp),%ebx
 804a128:	83 c8 ff             	or     $0xffffffff,%eax
 804a12b:	8b 8c 24 dc 00 00 00 	mov    0xdc(%esp),%ecx
 804a132:	8b 49 0c             	mov    0xc(%ecx),%ecx
 804a135:	89 4c 24 14          	mov    %ecx,0x14(%esp)
 804a139:	c1 e9 04             	shr    $0x4,%ecx
 804a13c:	83 e1 01             	and    $0x1,%ecx
 804a13f:	88 4c 24 14          	mov    %cl,0x14(%esp)
 804a143:	85 d2                	test   %edx,%edx
 804a145:	75 0f                	jne    0x804a156
 804a147:	84 c9                	test   %cl,%cl
 804a149:	75 0b                	jne    0x804a156
 804a14b:	80 7c 24 03 67       	cmpb   $0x67,0x3(%esp)
 804a150:	74 1d                	je     0x804a16f
 804a152:	85 f6                	test   %esi,%esi
 804a154:	7e 19                	jle    0x804a16f
 804a156:	c7 03 70 00 00 00    	movl   $0x70,(%ebx)
 804a15c:	c7 43 04 01 00 00 00 	movl   $0x1,0x4(%ebx)
 804a163:	8d 8d 80 e3 ff ff    	lea    -0x1c80(%ebp),%ecx
 804a169:	89 4b 08             	mov    %ecx,0x8(%ebx)
 804a16c:	83 c3 0c             	add    $0xc,%ebx
 804a16f:	40                   	inc    %eax
 804a170:	89 c1                	mov    %eax,%ecx
 804a172:	74 17                	je     0x804a18b
 804a174:	c7 03 b0 00 00 00    	movl   $0xb0,(%ebx)
 804a17a:	f7 d8                	neg    %eax
 804a17c:	89 43 04             	mov    %eax,0x4(%ebx)
 804a17f:	8d 85 73 e3 ff ff    	lea    -0x1c8d(%ebp),%eax
 804a185:	89 43 08             	mov    %eax,0x8(%ebx)
 804a188:	83 c3 0c             	add    $0xc,%ebx
 804a18b:	85 d2                	test   %edx,%edx
 804a18d:	74 13                	je     0x804a1a2
 804a18f:	c7 03 70 00 00 00    	movl   $0x70,(%ebx)
 804a195:	89 53 04             	mov    %edx,0x4(%ebx)
 804a198:	8b 44 24 04          	mov    0x4(%esp),%eax
 804a19c:	89 43 08             	mov    %eax,0x8(%ebx)
 804a19f:	83 c3 0c             	add    $0xc,%ebx
 804a1a2:	80 7c 24 03 67       	cmpb   $0x67,0x3(%esp)
 804a1a7:	75 07                	jne    0x804a1b0
 804a1a9:	80 7c 24 14 00       	cmpb   $0x0,0x14(%esp)
 804a1ae:	74 1f                	je     0x804a1cf
 804a1b0:	29 ca                	sub    %ecx,%edx
 804a1b2:	39 f2                	cmp    %esi,%edx
 804a1b4:	7d 19                	jge    0x804a1cf
 804a1b6:	c7 03 b0 00 00 00    	movl   $0xb0,(%ebx)
 804a1bc:	89 f0                	mov    %esi,%eax
 804a1be:	29 d0                	sub    %edx,%eax
 804a1c0:	89 43 04             	mov    %eax,0x4(%ebx)
 804a1c3:	8d 85 73 e3 ff ff    	lea    -0x1c8d(%ebp),%eax
 804a1c9:	89 43 08             	mov    %eax,0x8(%ebx)
 804a1cc:	83 c3 0c             	add    $0xc,%ebx
 804a1cf:	80 7c 24 0c 66       	cmpb   $0x66,0xc(%esp)
 804a1d4:	74 6f                	je     0x804a245
 804a1d6:	8a 44 24 2a          	mov    0x2a(%esp),%al
 804a1da:	88 44 24 0c          	mov    %al,0xc(%esp)
 804a1de:	c6 44 24 03 2b       	movb   $0x2b,0x3(%esp)
 804a1e3:	85 ff                	test   %edi,%edi
 804a1e5:	79 07                	jns    0x804a1ee
 804a1e7:	f7 df                	neg    %edi
 804a1e9:	c6 44 24 03 2d       	movb   $0x2d,0x3(%esp)
 804a1ee:	c6 44 24 39 00       	movb   $0x0,0x39(%esp)
 804a1f3:	be 02 00 00 00       	mov    $0x2,%esi
 804a1f8:	8d 4c 24 39          	lea    0x39(%esp),%ecx
 804a1fc:	8d 41 ff             	lea    -0x1(%ecx),%eax
 804a1ff:	89 44 24 04          	mov    %eax,0x4(%esp)
 804a203:	89 f8                	mov    %edi,%eax
 804a205:	bf 0a 00 00 00       	mov    $0xa,%edi
 804a20a:	99                   	cltd   
 804a20b:	f7 ff                	idiv   %edi
 804a20d:	83 c2 30             	add    $0x30,%edx
 804a210:	88 51 ff             	mov    %dl,-0x1(%ecx)
 804a213:	89 c7                	mov    %eax,%edi
 804a215:	46                   	inc    %esi
 804a216:	83 fe 03             	cmp    $0x3,%esi
 804a219:	75 06                	jne    0x804a221
 804a21b:	8b 4c 24 04          	mov    0x4(%esp),%ecx
 804a21f:	eb db                	jmp    0x804a1fc
 804a221:	85 c0                	test   %eax,%eax
 804a223:	75 f6                	jne    0x804a21b
 804a225:	8a 44 24 03          	mov    0x3(%esp),%al
 804a229:	88 41 fe             	mov    %al,-0x2(%ecx)
 804a22c:	8a 44 24 0c          	mov    0xc(%esp),%al
 804a230:	88 41 fd             	mov    %al,-0x3(%ecx)
 804a233:	c7 03 70 00 00 00    	movl   $0x70,(%ebx)
 804a239:	89 73 04             	mov    %esi,0x4(%ebx)
 804a23c:	83 e9 03             	sub    $0x3,%ecx
 804a23f:	89 4b 08             	mov    %ecx,0x8(%ebx)
 804a242:	83 c3 0c             	add    $0xc,%ebx
 804a245:	8d 44 24 68          	lea    0x68(%esp),%eax
 804a249:	8b 38                	mov    (%eax),%edi
 804a24b:	29 7c 24 10          	sub    %edi,0x10(%esp)
 804a24f:	83 c0 0c             	add    $0xc,%eax
 804a252:	39 c3                	cmp    %eax,%ebx
 804a254:	77 f3                	ja     0x804a249
 804a256:	c7 44 24 58 a0 00 00 	movl   $0xa0,0x58(%esp)
 804a25d:	00 
 804a25e:	31 c0                	xor    %eax,%eax
 804a260:	80 7c 24 24 00       	cmpb   $0x0,0x24(%esp)
 804a265:	0f 95 c0             	setne  %al
 804a268:	89 44 24 5c          	mov    %eax,0x5c(%esp)
 804a26c:	8d 54 24 24          	lea    0x24(%esp),%edx
 804a270:	89 54 24 60          	mov    %edx,0x60(%esp)
 804a274:	8b 74 24 10          	mov    0x10(%esp),%esi
 804a278:	29 c6                	sub    %eax,%esi
 804a27a:	89 f0                	mov    %esi,%eax
 804a27c:	85 f6                	test   %esi,%esi
 804a27e:	7e 3f                	jle    0x804a2bf
 804a280:	8b b4 24 dc 00 00 00 	mov    0xdc(%esp),%esi
 804a287:	f6 46 0c 08          	testb  $0x8,0xc(%esi)
 804a28b:	74 17                	je     0x804a2a4
 804a28d:	c7 03 a0 00 00 00    	movl   $0xa0,(%ebx)
 804a293:	89 43 04             	mov    %eax,0x4(%ebx)
 804a296:	8d 85 73 e3 ff ff    	lea    -0x1c8d(%ebp),%eax
 804a29c:	89 43 08             	mov    %eax,0x8(%ebx)
 804a29f:	83 c3 0c             	add    $0xc,%ebx
 804a2a2:	eb 1b                	jmp    0x804a2bf
 804a2a4:	8b b4 24 dc 00 00 00 	mov    0xdc(%esp),%esi
 804a2ab:	83 7e 10 30          	cmpl   $0x30,0x10(%esi)
 804a2af:	75 06                	jne    0x804a2b7
 804a2b1:	01 44 24 68          	add    %eax,0x68(%esp)
 804a2b5:	eb 08                	jmp    0x804a2bf
 804a2b7:	8b 44 24 10          	mov    0x10(%esp),%eax
 804a2bb:	89 44 24 5c          	mov    %eax,0x5c(%esp)
 804a2bf:	8d 7c 24 58          	lea    0x58(%esp),%edi
 804a2c3:	31 f6                	xor    %esi,%esi
 804a2c5:	8b 6f 04             	mov    0x4(%edi),%ebp
 804a2c8:	ff 77 08             	pushl  0x8(%edi)
 804a2cb:	55                   	push   %ebp
 804a2cc:	ff 37                	pushl  (%edi)
 804a2ce:	ff b4 24 d8 00 00 00 	pushl  0xd8(%esp)
 804a2d5:	ff 94 24 f0 00 00 00 	call   *0xf0(%esp)
 804a2dc:	83 c4 10             	add    $0x10,%esp
 804a2df:	39 e8                	cmp    %ebp,%eax
 804a2e1:	75 0d                	jne    0x804a2f0
 804a2e3:	01 c6                	add    %eax,%esi
 804a2e5:	83 c7 0c             	add    $0xc,%edi
 804a2e8:	39 fb                	cmp    %edi,%ebx
 804a2ea:	77 d9                	ja     0x804a2c5
 804a2ec:	89 f0                	mov    %esi,%eax
 804a2ee:	eb 22                	jmp    0x804a312
 804a2f0:	83 c8 ff             	or     $0xffffffff,%eax
 804a2f3:	eb 1d                	jmp    0x804a312
 804a2f5:	c6 44 24 0c 67       	movb   $0x67,0xc(%esp)
 804a2fa:	31 c0                	xor    %eax,%eax
 804a2fc:	e9 96 fd ff ff       	jmp    0x804a097
 804a301:	c6 44 24 3a 00       	movb   $0x0,0x3a(%esp)
 804a306:	c6 44 24 3b 30       	movb   $0x30,0x3b(%esp)
 804a30b:	31 db                	xor    %ebx,%ebx
 804a30d:	e9 08 fd ff ff       	jmp    0x804a01a
 804a312:	81 c4 b8 00 00 00    	add    $0xb8,%esp
 804a318:	5b                   	pop    %ebx
 804a319:	5e                   	pop    %esi
 804a31a:	5f                   	pop    %edi
 804a31b:	5d                   	pop    %ebp
 804a31c:	c3                   	ret    
 804a31d:	56                   	push   %esi
 804a31e:	53                   	push   %ebx
 804a31f:	53                   	push   %ebx
 804a320:	8b 5c 24 10          	mov    0x10(%esp),%ebx
 804a324:	8b 74 24 14          	mov    0x14(%esp),%esi
 804a328:	8b 46 10             	mov    0x10(%esi),%eax
 804a32b:	3b 46 1c             	cmp    0x1c(%esi),%eax
 804a32e:	73 0a                	jae    0x804a33a
 804a330:	8d 50 01             	lea    0x1(%eax),%edx
 804a333:	89 56 10             	mov    %edx,0x10(%esi)
 804a336:	88 18                	mov    %bl,(%eax)
 804a338:	eb 39                	jmp    0x804a373
 804a33a:	f6 06 40             	testb  $0x40,(%esi)
 804a33d:	74 08                	je     0x804a347
 804a33f:	83 7e 04 fe          	cmpl   $0xfffffffe,0x4(%esi)
 804a343:	75 0f                	jne    0x804a354
 804a345:	eb 2c                	jmp    0x804a373
 804a347:	56                   	push   %esi
 804a348:	e8 4c f8 ff ff       	call   0x8049b99
 804a34d:	59                   	pop    %ecx
 804a34e:	85 c0                	test   %eax,%eax
 804a350:	74 ed                	je     0x804a33f
 804a352:	eb 44                	jmp    0x804a398
 804a354:	8b 46 0c             	mov    0xc(%esi),%eax
 804a357:	39 46 08             	cmp    %eax,0x8(%esi)
 804a35a:	74 41                	je     0x804a39d
 804a35c:	39 46 10             	cmp    %eax,0x10(%esi)
 804a35f:	74 17                	je     0x804a378
 804a361:	8b 46 10             	mov    0x10(%esi),%eax
 804a364:	8d 50 01             	lea    0x1(%eax),%edx
 804a367:	89 56 10             	mov    %edx,0x10(%esi)
 804a36a:	88 18                	mov    %bl,(%eax)
 804a36c:	66 f7 06 00 01       	testw  $0x100,(%esi)
 804a371:	75 12                	jne    0x804a385
 804a373:	0f b6 d3             	movzbl %bl,%edx
 804a376:	eb 40                	jmp    0x804a3b8
 804a378:	56                   	push   %esi
 804a379:	e8 37 e6 ff ff       	call   0x80489b5
 804a37e:	5a                   	pop    %edx
 804a37f:	85 c0                	test   %eax,%eax
 804a381:	74 de                	je     0x804a361
 804a383:	eb 13                	jmp    0x804a398
 804a385:	80 fb 0a             	cmp    $0xa,%bl
 804a388:	75 e9                	jne    0x804a373
 804a38a:	56                   	push   %esi
 804a38b:	e8 25 e6 ff ff       	call   0x80489b5
 804a390:	59                   	pop    %ecx
 804a391:	85 c0                	test   %eax,%eax
 804a393:	74 de                	je     0x804a373
 804a395:	ff 4e 10             	decl   0x10(%esi)
 804a398:	83 ca ff             	or     $0xffffffff,%edx
 804a39b:	eb 1b                	jmp    0x804a3b8
 804a39d:	88 5c 24 03          	mov    %bl,0x3(%esp)
 804a3a1:	6a 01                	push   $0x1
 804a3a3:	8d 44 24 07          	lea    0x7(%esp),%eax
 804a3a7:	50                   	push   %eax
 804a3a8:	56                   	push   %esi
 804a3a9:	e8 92 f6 ff ff       	call   0x8049a40
 804a3ae:	83 c4 0c             	add    $0xc,%esp
 804a3b1:	83 ca ff             	or     $0xffffffff,%edx
 804a3b4:	85 c0                	test   %eax,%eax
 804a3b6:	75 bb                	jne    0x804a373
 804a3b8:	89 d0                	mov    %edx,%eax
 804a3ba:	5a                   	pop    %edx
 804a3bb:	5b                   	pop    %ebx
 804a3bc:	5e                   	pop    %esi
 804a3bd:	c3                   	ret    
 804a3be:	57                   	push   %edi
 804a3bf:	56                   	push   %esi
 804a3c0:	8b 44 24 0c          	mov    0xc(%esp),%eax
 804a3c4:	8b 54 24 14          	mov    0x14(%esp),%edx
 804a3c8:	89 d1                	mov    %edx,%ecx
 804a3ca:	c1 e9 02             	shr    $0x2,%ecx
 804a3cd:	89 c7                	mov    %eax,%edi
 804a3cf:	8b 74 24 10          	mov    0x10(%esp),%esi
 804a3d3:	f3 a5                	rep movsl %ds:(%esi),%es:(%edi)
 804a3d5:	89 d1                	mov    %edx,%ecx
 804a3d7:	83 e1 03             	and    $0x3,%ecx
 804a3da:	74 02                	je     0x804a3de
 804a3dc:	f3 a4                	rep movsb %ds:(%esi),%es:(%edi)
 804a3de:	5e                   	pop    %esi
 804a3df:	5f                   	pop    %edi
 804a3e0:	c3                   	ret    
 804a3e1:	55                   	push   %ebp
 804a3e2:	57                   	push   %edi
 804a3e3:	56                   	push   %esi
 804a3e4:	53                   	push   %ebx
 804a3e5:	8b 54 24 18          	mov    0x18(%esp),%edx
 804a3e9:	8b 4c 24 1c          	mov    0x1c(%esp),%ecx
 804a3ed:	88 d3                	mov    %dl,%bl
 804a3ef:	8b 44 24 14          	mov    0x14(%esp),%eax
 804a3f3:	01 c8                	add    %ecx,%eax
 804a3f5:	85 c9                	test   %ecx,%ecx
 804a3f7:	74 0c                	je     0x804a405
 804a3f9:	a8 03                	test   $0x3,%al
 804a3fb:	74 08                	je     0x804a405
 804a3fd:	48                   	dec    %eax
 804a3fe:	3a 18                	cmp    (%eax),%bl
 804a400:	74 71                	je     0x804a473
 804a402:	49                   	dec    %ecx
 804a403:	eb f0                	jmp    0x804a3f5
 804a405:	0f b6 d2             	movzbl %dl,%edx
 804a408:	89 d6                	mov    %edx,%esi
 804a40a:	c1 e6 08             	shl    $0x8,%esi
 804a40d:	09 f2                	or     %esi,%edx
 804a40f:	89 d7                	mov    %edx,%edi
 804a411:	c1 e7 10             	shl    $0x10,%edi
 804a414:	09 d7                	or     %edx,%edi
 804a416:	89 c2                	mov    %eax,%edx
 804a418:	29 c1                	sub    %eax,%ecx
 804a41a:	8d 04 0a             	lea    (%edx,%ecx,1),%eax
 804a41d:	83 f8 03             	cmp    $0x3,%eax
 804a420:	76 40                	jbe    0x804a462
 804a422:	8d 42 fc             	lea    -0x4(%edx),%eax
 804a425:	8b 72 fc             	mov    -0x4(%edx),%esi
 804a428:	31 fe                	xor    %edi,%esi
 804a42a:	8d ae ff fe fe 7e    	lea    0x7efefeff(%esi),%ebp
 804a430:	f7 d6                	not    %esi
 804a432:	31 ee                	xor    %ebp,%esi
 804a434:	81 e6 00 01 01 81    	and    $0x81010100,%esi
 804a43a:	74 22                	je     0x804a45e
 804a43c:	3a 58 03             	cmp    0x3(%eax),%bl
 804a43f:	75 05                	jne    0x804a446
 804a441:	8d 42 ff             	lea    -0x1(%edx),%eax
 804a444:	eb 2d                	jmp    0x804a473
 804a446:	3a 58 02             	cmp    0x2(%eax),%bl
 804a449:	75 05                	jne    0x804a450
 804a44b:	8d 42 fe             	lea    -0x2(%edx),%eax
 804a44e:	eb 23                	jmp    0x804a473
 804a450:	3a 58 01             	cmp    0x1(%eax),%bl
 804a453:	75 05                	jne    0x804a45a
 804a455:	8d 42 fd             	lea    -0x3(%edx),%eax
 804a458:	eb 19                	jmp    0x804a473
 804a45a:	3a 18                	cmp    (%eax),%bl
 804a45c:	74 15                	je     0x804a473
 804a45e:	89 c2                	mov    %eax,%edx
 804a460:	eb b8                	jmp    0x804a41a
 804a462:	89 d0                	mov    %edx,%eax
 804a464:	89 c7                	mov    %eax,%edi
 804a466:	01 cf                	add    %ecx,%edi
 804a468:	74 07                	je     0x804a471
 804a46a:	48                   	dec    %eax
 804a46b:	3a 18                	cmp    (%eax),%bl
 804a46d:	75 f5                	jne    0x804a464
 804a46f:	eb 02                	jmp    0x804a473
 804a471:	31 c0                	xor    %eax,%eax
 804a473:	5b                   	pop    %ebx
 804a474:	5e                   	pop    %esi
 804a475:	5f                   	pop    %edi
 804a476:	5d                   	pop    %ebp
 804a477:	c3                   	ret    
 804a478:	ff 74 24 0c          	pushl  0xc(%esp)
 804a47c:	8b 44 24 0c          	mov    0xc(%esp),%eax
 804a480:	99                   	cltd   
 804a481:	52                   	push   %edx
 804a482:	50                   	push   %eax
 804a483:	ff 74 24 10          	pushl  0x10(%esp)
 804a487:	e8 04 00 00 00       	call   0x804a490
 804a48c:	83 c4 10             	add    $0x10,%esp
 804a48f:	c3                   	ret    
 804a490:	57                   	push   %edi
 804a491:	56                   	push   %esi
 804a492:	53                   	push   %ebx
 804a493:	83 ec 08             	sub    $0x8,%esp
 804a496:	e8 03 e3 ff ff       	call   0x804879e
 804a49b:	81 c1 d1 25 00 00    	add    $0x25d1,%ecx
 804a4a1:	8b 5c 24 18          	mov    0x18(%esp),%ebx
 804a4a5:	8b 74 24 24          	mov    0x24(%esp),%esi
 804a4a9:	8b 44 24 1c          	mov    0x1c(%esp),%eax
 804a4ad:	8b 54 24 20          	mov    0x20(%esp),%edx
 804a4b1:	89 04 24             	mov    %eax,(%esp)
 804a4b4:	89 54 24 04          	mov    %edx,0x4(%esp)
 804a4b8:	83 fe 02             	cmp    $0x2,%esi
 804a4bb:	76 0e                	jbe    0x804a4cb
 804a4bd:	8d 81 bc 00 00 00    	lea    0xbc(%ecx),%eax
 804a4c3:	c7 00 16 00 00 00    	movl   $0x16,(%eax)
 804a4c9:	eb 19                	jmp    0x804a4e4
 804a4cb:	f6 03 40             	testb  $0x40,(%ebx)
 804a4ce:	75 09                	jne    0x804a4d9
 804a4d0:	83 fe 01             	cmp    $0x1,%esi
 804a4d3:	89 e7                	mov    %esp,%edi
 804a4d5:	75 1f                	jne    0x804a4f6
 804a4d7:	eb 10                	jmp    0x804a4e9
 804a4d9:	53                   	push   %ebx
 804a4da:	e8 d6 e4 ff ff       	call   0x80489b5
 804a4df:	5f                   	pop    %edi
 804a4e0:	85 c0                	test   %eax,%eax
 804a4e2:	74 ec                	je     0x804a4d0
 804a4e4:	83 c8 ff             	or     $0xffffffff,%eax
 804a4e7:	eb 31                	jmp    0x804a51a
 804a4e9:	57                   	push   %edi
 804a4ea:	53                   	push   %ebx
 804a4eb:	e8 31 00 00 00       	call   0x804a521
 804a4f0:	5a                   	pop    %edx
 804a4f1:	59                   	pop    %ecx
 804a4f2:	85 c0                	test   %eax,%eax
 804a4f4:	78 ee                	js     0x804a4e4
 804a4f6:	56                   	push   %esi
 804a4f7:	57                   	push   %edi
 804a4f8:	53                   	push   %ebx
 804a4f9:	e8 aa 00 00 00       	call   0x804a5a8
 804a4fe:	83 c4 0c             	add    $0xc,%esp
 804a501:	85 c0                	test   %eax,%eax
 804a503:	78 df                	js     0x804a4e4
 804a505:	66 83 23 b8          	andw   $0xffb8,(%ebx)
 804a509:	8b 43 08             	mov    0x8(%ebx),%eax
 804a50c:	89 43 10             	mov    %eax,0x10(%ebx)
 804a50f:	89 43 14             	mov    %eax,0x14(%ebx)
 804a512:	89 43 18             	mov    %eax,0x18(%ebx)
 804a515:	89 43 1c             	mov    %eax,0x1c(%ebx)
 804a518:	31 c0                	xor    %eax,%eax
 804a51a:	83 c4 08             	add    $0x8,%esp
 804a51d:	5b                   	pop    %ebx
 804a51e:	5e                   	pop    %esi
 804a51f:	5f                   	pop    %edi
 804a520:	c3                   	ret    
 804a521:	55                   	push   %ebp
 804a522:	57                   	push   %edi
 804a523:	56                   	push   %esi
 804a524:	53                   	push   %ebx
 804a525:	83 ec 08             	sub    $0x8,%esp
 804a528:	e8 f1 f0 ff ff       	call   0x804961e
 804a52d:	81 c2 3f 25 00 00    	add    $0x253f,%edx
 804a533:	8b 4c 24 1c          	mov    0x1c(%esp),%ecx
 804a537:	8b 6c 24 20          	mov    0x20(%esp),%ebp
 804a53b:	8b 19                	mov    (%ecx),%ebx
 804a53d:	89 d8                	mov    %ebx,%eax
 804a53f:	66 83 e0 03          	and    $0x3,%ax
 804a543:	74 08                	je     0x804a54d
 804a545:	0f b7 c0             	movzwl %ax,%eax
 804a548:	8d 70 ff             	lea    -0x1(%eax),%esi
 804a54b:	eb 02                	jmp    0x804a54f
 804a54d:	31 f6                	xor    %esi,%esi
 804a54f:	80 e3 40             	and    $0x40,%bl
 804a552:	74 05                	je     0x804a559
 804a554:	8b 41 08             	mov    0x8(%ecx),%eax
 804a557:	eb 03                	jmp    0x804a55c
 804a559:	8b 41 14             	mov    0x14(%ecx),%eax
 804a55c:	2b 41 10             	sub    0x10(%ecx),%eax
 804a55f:	01 f0                	add    %esi,%eax
 804a561:	8b 75 00             	mov    0x0(%ebp),%esi
 804a564:	8b 7d 04             	mov    0x4(%ebp),%edi
 804a567:	89 c3                	mov    %eax,%ebx
 804a569:	c1 fb 1f             	sar    $0x1f,%ebx
 804a56c:	89 04 24             	mov    %eax,(%esp)
 804a56f:	89 5c 24 04          	mov    %ebx,0x4(%esp)
 804a573:	89 f1                	mov    %esi,%ecx
 804a575:	89 fb                	mov    %edi,%ebx
 804a577:	2b 0c 24             	sub    (%esp),%ecx
 804a57a:	1b 5c 24 04          	sbb    0x4(%esp),%ebx
 804a57e:	89 4d 00             	mov    %ecx,0x0(%ebp)
 804a581:	89 5d 04             	mov    %ebx,0x4(%ebp)
 804a584:	39 df                	cmp    %ebx,%edi
 804a586:	7f 08                	jg     0x804a590
 804a588:	7c 04                	jl     0x804a58e
 804a58a:	39 ce                	cmp    %ecx,%esi
 804a58c:	73 02                	jae    0x804a590
 804a58e:	f7 d8                	neg    %eax
 804a590:	85 c0                	test   %eax,%eax
 804a592:	79 0c                	jns    0x804a5a0
 804a594:	8d 92 bc 00 00 00    	lea    0xbc(%edx),%edx
 804a59a:	c7 02 4b 00 00 00    	movl   $0x4b,(%edx)
 804a5a0:	83 c4 08             	add    $0x8,%esp
 804a5a3:	5b                   	pop    %ebx
 804a5a4:	5e                   	pop    %esi
 804a5a5:	5f                   	pop    %edi
 804a5a6:	5d                   	pop    %ebp
 804a5a7:	c3                   	ret    
 804a5a8:	53                   	push   %ebx
 804a5a9:	8b 5c 24 0c          	mov    0xc(%esp),%ebx
 804a5ad:	ff 74 24 10          	pushl  0x10(%esp)
 804a5b1:	ff 73 04             	pushl  0x4(%ebx)
 804a5b4:	ff 33                	pushl  (%ebx)
 804a5b6:	8b 44 24 14          	mov    0x14(%esp),%eax
 804a5ba:	ff 70 04             	pushl  0x4(%eax)
 804a5bd:	e8 14 00 00 00       	call   0x804a5d6
 804a5c2:	83 c4 10             	add    $0x10,%esp
 804a5c5:	89 c1                	mov    %eax,%ecx
 804a5c7:	85 d2                	test   %edx,%edx
 804a5c9:	78 07                	js     0x804a5d2
 804a5cb:	89 03                	mov    %eax,(%ebx)
 804a5cd:	89 53 04             	mov    %edx,0x4(%ebx)
 804a5d0:	31 c9                	xor    %ecx,%ecx
 804a5d2:	89 c8                	mov    %ecx,%eax
 804a5d4:	5b                   	pop    %ebx
 804a5d5:	c3                   	ret    
 804a5d6:	55                   	push   %ebp
 804a5d7:	89 e5                	mov    %esp,%ebp
 804a5d9:	57                   	push   %edi
 804a5da:	56                   	push   %esi
 804a5db:	53                   	push   %ebx
 804a5dc:	51                   	push   %ecx
 804a5dd:	83 ec 0c             	sub    $0xc,%esp
 804a5e0:	8d 4d 08             	lea    0x8(%ebp),%ecx
 804a5e3:	e8 e4 df ff ff       	call   0x80485cc
 804a5e8:	81 c3 84 24 00 00    	add    $0x2484,%ebx
 804a5ee:	8b 01                	mov    (%ecx),%eax
 804a5f0:	8b 51 04             	mov    0x4(%ecx),%edx
 804a5f3:	8b 79 08             	mov    0x8(%ecx),%edi
 804a5f6:	89 7d e4             	mov    %edi,-0x1c(%ebp)
 804a5f9:	8b 79 0c             	mov    0xc(%ecx),%edi
 804a5fc:	8d 75 e8             	lea    -0x18(%ebp),%esi
 804a5ff:	8b 4d e4             	mov    -0x1c(%ebp),%ecx
 804a602:	53                   	push   %ebx
 804a603:	89 c3                	mov    %eax,%ebx
 804a605:	b8 8c 00 00 00       	mov    $0x8c,%eax
 804a60a:	cd 80                	int    $0x80
 804a60c:	5b                   	pop    %ebx
 804a60d:	3d 00 f0 ff ff       	cmp    $0xfffff000,%eax
 804a612:	76 0f                	jbe    0x804a623
 804a614:	f7 d8                	neg    %eax
 804a616:	8d 93 bc 00 00 00    	lea    0xbc(%ebx),%edx
 804a61c:	89 02                	mov    %eax,(%edx)
 804a61e:	83 c8 ff             	or     $0xffffffff,%eax
 804a621:	eb 04                	jmp    0x804a627
 804a623:	85 c0                	test   %eax,%eax
 804a625:	74 03                	je     0x804a62a
 804a627:	99                   	cltd   
 804a628:	eb 06                	jmp    0x804a630
 804a62a:	8b 45 e8             	mov    -0x18(%ebp),%eax
 804a62d:	8b 55 ec             	mov    -0x14(%ebp),%edx
 804a630:	83 c4 0c             	add    $0xc,%esp
 804a633:	59                   	pop    %ecx
 804a634:	5b                   	pop    %ebx
 804a635:	5e                   	pop    %esi
 804a636:	5f                   	pop    %edi
 804a637:	5d                   	pop    %ebp
 804a638:	c3                   	ret    
