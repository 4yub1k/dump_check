# dump_check
Hex dump xCheck for altered hex, Buffer Overflow
This is ESP dump from Imunnity Debugger
```
02ABF9C8  01 02 03 04 05 06 07 08  
02ABF9D0  09 0A 0B 0C 0D 0E 0F 10  ....
02ABF9D8  11 12 13 14 15 16 17 18  
02ABF9E0  19 1A 1B 1C 1D 1E 1F 20  
02ABF9E8  21 22 23 24 25 26 27 28  !"#$%&'(
02ABF9F0  29 2A 2B 2C 2D 2E 2F 30  )*+,-./0
02ABF9F8  31 32 33 34 35 36 37 38  12345678
02ABFA00  39 3A 3B 3C 3D 3E 3F 40  9:;<=>?@
02ABFA08  41 42 43 44 45 46 47 48  ABCDEFGH
02ABFA10  49 4A 4B 4C 4D 4E 4F 50  IJKLMNOP
02ABFA18  51 52 53 54 55 56 57 58  QRSTUVWX
02ABFA20  59 5A 5B 5C 5D 5E 5F 60  YZ[\]^_`
02ABFA28  61 62 63 64 65 66 67 68  abcdefgh
02ABFA30  69 6A 6B 6C 6D 6E 6F 70  ijklmnop
02ABFA38  71 72 73 74 75 76 77 78  qrstuvwx
02ABFA40  79 7A 7B 7C 7D 7E 7F 80  yz{|}~€
02ABFA48  81 82 83 84 85 86 87 88  ‚ƒ„…†‡ˆ
02ABFA50  89 8A 8B 8C 8D 8E 8F 90  ‰Š‹ŒŽ
02ABFA58  91 92 93 94 95 96 97 98  ‘’“”•–—˜
02ABFA60  99 9A 9B 9C 9D 9E 9F A0  ™š›œžŸ 
02ABFA68  A1 A2 A3 A4 A5 A6 A7 A8  ¡¢£¤¥¦§¨
02ABFA70  A9 AA AB AC AD AE AF B0  ©ª«¬­®¯°
02ABFA78  B1 B2 B3 D4 B5 B6 B7 B8  ±²³´µ¶·¸
02ABFA80  B9 BA BB BC BD BE BF C0  ¹º»¼½¾¿À
02ABFA88  C1 C2 C3 C4 C5 C6 C7 C8  ÁÂÃÄÅÆÇÈ
02ABFA90  C9 CA CB CC CC CE CF D0  ÉÊËÌÍÎÏÐ
02ABFA98  D1 D2 D3 D4 D5 D6 D7 D8  ÑÒÓÔÕÖ×Ø
02ABFAA0  D9 DA DB DC DD DE DF E0  ÙÚÛÜÝÞßà
02ABFAA8  E1 E2 E3 E4 E5 E6 E7 E8  áâãäåæçè
02ABFAB0  E9 EA EB EC ED EE EF F0  éêëìíîïð
02ABFAB8  F1 F2 F3 F4 F5 F6 F7 F8  ñòóôõö÷ø
02ABFAC0  F9 FA FB FC FD FE FF 00  ùúûüýþÿ.
```
Copy the dump into dum.txt, Make sure there are exact 32 lines, remove empty lines.

 
```
ADDRESS            REAL CHARS                    ALTERED CHARS 

02ABF9C8  01  02  03  04  05  06  07  08   01  02  03  04  05  06  07  08 
02ABF9D0  09  0A  0B  0C  0D  0E  0F  10   09  0A  0B  0C  0D  0E  0F  10 
02ABF9D8  11  12  13  14  15  16  17  18   11  12  13  14  15  16  17  18 
02ABF9E0  19  1A  1B  1C  1D  1E  1F  20   19  1A  1B  1C  1D  1E  1F  20 
02ABF9E8  21  22  23  24  25  26  27  28   21  22  23  24  25  26  27  28 
02ABF9F0  29  2A  2B  2C  2D  2E  2F  30   29  2A  2B  2C  2D  2E  2F  30 
02ABF9F8  31  32  33  34  35  36  37  38   31  32  33  34  35  36  37  38 
02ABFA00  39  3A  3B  3C  3D  3E  3F  40   39  3A  3B  3C  3D  3E  3F  40 
02ABFA08  41  42  43  44  45  46  47  48   41  42  43  44  45  46  47  48 
02ABFA10  49  4A  4B  4C  4D  4E  4F  50   49  4A  4B  4C  4D  4E  4F  50 
02ABFA18  51  52  53  54  55  56  57  58   51  52  53  54  55  56  57  58 
02ABFA20  59  5A  5B  5C  5D  5E  5F  60   59  5A  5B  5C  5D  5E  5F  60 
02ABFA28  61  62  63  64  65  66  67  68   61  62  63  64  65  66  67  68 
02ABFA30  69  6A  6B  6C  6D  6E  6F  70   69  6A  6B  6C  6D  6E  6F  70 
02ABFA38  71  72  73  74  75  76  77  78   71  72  73  74  75  76  77  78 
02ABFA40  79  7A  7B  7C  7D  7E  7F  80   79  7A  7B  7C  7D  7E  7F  80 
02ABFA48  81  82  83  84  85  86  87  88   81  82  83  84  85  86  87  88 
02ABFA50  89  8A  8B  8C  8D  8E  8F  90   89  8A  8B  8C  8D  8E  8F  90 
02ABFA58  91  92  93  94  95  96  97  98   91  92  93  94  95  96  97  98 
02ABFA60  99  9A  9B  9C  9D  9E  9F  A0   99  9A  9B  9C  9D  9E  9F  A0 
02ABFA68  A1  A2  A3  A4  A5  A6  A7  A8   A1  A2  A3  A4  A5  A6  A7  A8 
02ABFA70  A9  AA  AB  AC  AD  AE  AF  B0   A9  AA  AB  AC  AD  AE  AF  B0 
02ABFA78  B1  B2  B3 [B4] B5  B6  B7  B8   B1  B2  B3 [D4] B5  B6  B7  B8 
02ABFA80  B9  BA  BB  BC  BD  BE  BF  C0   B9  BA  BB  BC  BD  BE  BF  C0 
02ABFA88  C1  C2  C3  C4  C5  C6  C7  C8   C1  C2  C3  C4  C5  C6  C7  C8 
02ABFA90  C9  CA  CB  CC [CD] CE  CF  D0   C9  CA  CB  CC [CC] CE  CF  D0 
02ABFA98  D1  D2  D3  D4  D5  D6  D7  D8   D1  D2  D3  D4  D5  D6  D7  D8 
02ABFAA0  D9  DA  DB  DC  DD  DE  DF  E0   D9  DA  DB  DC  DD  DE  DF  E0 
02ABFAA8  E1  E2  E3  E4  E5  E6  E7  E8   E1  E2  E3  E4  E5  E6  E7  E8 
02ABFAB0  E9  EA  EB  EC  ED  EE  EF  F0   E9  EA  EB  EC  ED  EE  EF  F0 
02ABFAB8  F1  F2  F3  F4  F5  F6  F7  F8   F1  F2  F3  F4  F5  F6  F7  F8 
02ABFAC0  F9  FA  FB  FC  FD  FE  FF  00   F9  FA  FB  FC  FD  FE  FF  00 
```
```
OUTPUT IMAGE
```
![DUMP](https://github.com/4yub1k/dump_check/raw/master/output.png)

Installation :
```
git clone https://github.com/4yub1k/dump_check.git
chmod +x dumo.py
./dump.y
```
