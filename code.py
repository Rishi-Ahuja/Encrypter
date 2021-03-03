while True:
    import time
    s=''
    a='abcdefghijklmnopqrstuvwxyz'
    b=input ('encrypt or decrypt')
    if b== 'encrypt':
        print ('Welcome to the Great Encrypters!')
        time.sleep(1)
        i=input('Enter the word to be encrypted: \n')
        print('processing')
        time.sleep(1)
        d=len(i)
        for w in range(0,d):
           for x in range (0,26):
              if (i[w])==(a[x]):
                 q= (a[(x+3)%26])
                 s=s+q
        print(s)
    if b== 'decrypt':
         print ('Welcome to the Great Decrypters!')
         time.sleep(1)
         i=input('Enter the word to be decrypted: \n')
         print('processing')
         time.sleep(1)
         d=len(i)
         for w in range(0,d):
            for x in range (0,26):
               if (i[w])==(a[x]):
                  q= (a[(x-3)%26])
                  s=s+q
         print(s)

