"""
编码
"""

print('-------- english ------- ')
# 普通英文
english = 'english'
result = english.encode(encoding='utf-8')
print('result :' ,result)
print('type(result) :', type(result))
for bt in result:
    print('type(bt) :', type(bt),' bt value :', bt)

print('---------- decode english ----------')
en_bts_raw_v1 = [101, 110, 103, 108, 105, 115, 104]
en_bts_v1 = bytes(en_bts_raw_v1)
en_decode_v1 = en_bts_v1.decode(encoding='utf-8')
print("english decode v1 is ", en_decode_v1)

en_bts_v2 = bytes(b'\x65\x6e\x67\x6c\x69\x73\x68')
en_decode_v2 = en_bts_v2.decode(encoding='utf-8')
print("english decode v2 is ", en_decode_v2)

bv = b'\x65\x6e\x67\x6c\x69\x73\x68'
print("type(bv) :",type(bv))
print("type(en_bts_v1) :",type(en_bts_v1))
print("type(en_bts_v2) :",type(en_bts_v2))

print("---------- chinese ---------- ")
# 中文
chinese = '中文'
cr = chinese.encode(encoding='utf-8')
print("cr :", cr)
print('type(cr) :', type(cr))
for crt in cr:
    print('type(crt) :', type(crt),' bt value :', crt)


print("---------- decode chinese ---------- ")
cn_bts_raw_v1 = [228, 184, 173, 230, 150, 135]
cn_bts_v1 = bytes(cn_bts_raw_v1)
cn_decode_v1 = cn_bts_v1.decode(encoding='utf-8')
print("chinese decode v1 is ", cn_decode_v1)
cn_bts_v2 = bytes(b'\xe4\xb8\xad\xe6\x96\x87')
cn_decode_v2 = cn_bts_v2.decode(encoding='utf-8')
print("chinese decode v2 is ", cn_decode_v2)

cn_bts_raw_v3 = [0xe4, 0xb8, 0xad, 0xe6, 0x96, 0x87]
cn_bts_v3 = bytes(cn_bts_raw_v3)
cn_decode_v3 = cn_bts_v3.decode(encoding='utf-8')
print("chinese decode v3 is ", cn_decode_v3)


print('------------ convert ------------ ')
en_1 = 'a'
dec_1 = 112
hex_1 = 0x79
print('ord(en_1) :', ord(en_1))
print('chr(dec_1) :', chr(dec_1))
print('hex(dec_1) :', hex(dec_1))
print('hex_1 :', hex_1)
print("type(hex_1) :", type(hex_1))
print('int(hex_1) :', int(hex_1))
print('chr(int(hex_1)) :', chr(int(hex_1)))


