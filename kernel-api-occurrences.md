
| Kernel Directory| Kernel API | Kernel API call |Kernel API Occurrences | Get the call |
|---|---|---|---|---|
| Crypto | [Linux Kernel Crypto API](https://www.kernel.org/doc/html/latest/crypto/index.html) | Initialization Call  |  grep  -c 'crypto_alloc*' crypto/*| grep  -n 'crypto_alloc*' crypto/* |
|  | | Symmetric Key Cipher API  | grep  -c 'crypto_skcipher*' crypto/* | grep  -n 'crypto_skcipher*' crypto/* |
|  | | Single Block Cipher API | grep  -c 'crypto_cipher*' crypto/ | grep  -c 'crypto_cipher*' crypto/ |
|  |  | Asynchronous Block Cipher API |  grep  -c 'crypto_ablkcipher*' crypto/ | grep  -n 'crypto_ablkcipher*' crypto/ |
|  |  | Synchronous Block Cipher API | grep  -c 'crypto_blkcipher*' crypto/* | grep  -n 'crypto_blkcipher*' crypto/* |
|  |  | Authenticated Encryption With Associated Data (AEAD) Cipher API | grep  -c 'crypto_aead*' crypto/* | grep  -c 'crypto_aead*' crypto/* |
|  |  | Asynchronous Message Digest API | grep  -c 'crypto_ahash*' crypto/* | grep  -n 'crypto_ahash*' crypto/*| 
|  |  | Synchronous Message Digest API | grep  -c 'crypto_shash*' crypto/* | grep  -n 'crypto_shash*' crypto/* |
|  |  | Crypto API Random Number API | grep  -c 'crypto_rng*' crypto/* | grep  -n 'crypto_rng*' crypto/* |
|  |  | Asymmetric Cipher API |  grep  -c 'crypto_akcipher*' crypto/* | grep  -n 'crypto_akcipher*' crypto/* |
|  |  | Key-agreement Protocol Primitives (KPP) Cipher API | grep  -c 'crypto_kpp*' crypto/* | grep  -n 'crypto_kpp*' crypto/* |
