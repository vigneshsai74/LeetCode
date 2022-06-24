# hashmap={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
# s="IV"
# s=s[::-1]
# sum=0
# for i in range(len(s)):
#     print(i)
#     if(hashmap[s[i+1]]>=hashmap[s[i]]):
#         print("hello")
#     #     sum=sum+hashmap[s[i]]
#     #     print(i)
#     # else:
#     #     sum=sum+hashmap[s[i]]-1
#         i=i+2
#         # print(i)
#     # print(i)
s="IX"
converter = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
sum=0
for i in range(len(s)):
    key=s[i]
    if(i!=len(s)-1):
        key2=s[i+1]
        if(converter[key]<converter[key2]):
            sum=sum-converter[key]
        else:
            sum=sum+converter[key]
    else:
        sum=sum+converter[key]

print(sum)