/* des.h
 *	Copyright (C) 1998 Free Software Foundation, Inc.
 *
 * This file is part of GnuPG.
 *
 * GnuPG is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * GnuPG is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA
 */
#ifndef G10_DES_H
#define G10_DES_H

#include "types.h"

/*
const char *
des_get_info( int algo, size_t *keylen,
		   size_t *blocksize, size_t *contextsize,
		   int	(**setkeyf)( void *c, byte *key, unsigned keylen ),
		   void (**encryptf)( void *c, byte *outbuf, byte *inbuf ),
		   void (**decryptf)( void *c, byte *outbuf, byte *inbuf )
		 );
*/

/*
 * Encryption/Decryption context of DES
 */
typedef struct _des_ctx
  {
    u32 encrypt_subkeys[32];
    u32 decrypt_subkeys[32];
  }
des_ctx[1];

/*
 * Encryption/Decryption context of Triple-DES
 */
typedef struct _tripledes_ctx
  {
    u32 encrypt_subkeys[96];
    u32 decrypt_subkeys[96];
  }
tripledes_ctx[1];

/*
 * Handy macros for encryption and decryption of data
 */
#define des_ecb_encrypt(ctx, from, to)		des_ecb_crypt(ctx, from, to, 0)
#define des_ecb_decrypt(ctx, from, to)		des_ecb_crypt(ctx, from, to, 1)
#define tripledes_ecb_encrypt(ctx, from, to)	tripledes_ecb_crypt(ctx, from, to, 0)
#define tripledes_ecb_decrypt(ctx, from, to)	tripledes_ecb_crypt(ctx, from, to, 1)

int des_setkey (struct _des_ctx *, const byte *);
int des_ecb_crypt (struct _des_ctx *, const byte *, byte *, int);

int tripledes_set2keys (struct _tripledes_ctx *, const byte *, const byte *);
int tripledes_set3keys (struct _tripledes_ctx *, const byte *, const byte *, const byte *);
int tripledes_ecb_crypt (struct _tripledes_ctx *, const byte *, byte *, int);

#endif /*G10_DES_H*/
