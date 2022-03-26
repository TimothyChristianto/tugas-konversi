class KonversiTimothy:
    def OctaltoBinary(self,octnum):
        f = open("binary_poem", "a+")
        
        rev = 0
        chk = 0
        
        while octnum!=0:
            rem = octnum%10
            if rem>7:
                chk = 1
                break
            rev = rem + (rev*10)
            octnum = int(octnum/10)
        
        if chk == 0:
            octnum = rev
            binnum = ""
        
            while octnum!=0:
                rem = octnum%10
                if rem==0:
                    binnum = binnum + "000"
                elif rem==1:
                    binnum = binnum + "001"
                elif rem==2:
                    binnum = binnum + "010"
                elif rem==3:
                    binnum = binnum + "011"
                elif rem==4:
                    binnum = binnum + "100"
                elif rem==5:
                    binnum = binnum + "101"
                elif rem==6:
                    binnum = binnum + "110"
                elif rem==7:
                    binnum = binnum + "111"
                octnum = int(octnum/10)
        
            print("Setara dengan Binary = ", binnum)
        
        else:
            print("Salah Input!")
        
        f.write(binnum)
        f.write("\n")
        print("Berhasil Menu 1 di cetak di text file!")
        f.close()
    
    def DecimaltoBinary(self,decnum):
        f = open("binary_poem", "a+")
        i = 0
        bnum = []
        while decnum!=0:
            rem = decnum%2
            bnum.insert(i, rem)
            i = i+1
            decnum = int(decnum/2)
        
        i = i-1
        print("Setara dengan Binary:",end="")
        while i>=0:
            print(str(bnum[i]),end="")
            i = i-1
        print()
        
        f.write(str(bnum))
        f.write("\n")
        print("Berhasil Menu 2 di cetak di text file!")
        f.close()
    
    def HexatoBinary(self,hexdecnum):
        f = open("binary_poem", "a+")
        binnum = ""
        hexlen = len(hexdecnum)
        i = 0
        while i<hexlen:
            if hexdecnum[i] == '0':
                binnum = binnum + "0000"
            elif hexdecnum[i] == '1':
                binnum = binnum + "0001"
            elif hexdecnum[i] == '2':
                binnum = binnum + "0010"
            elif hexdecnum[i] == '3':
                binnum = binnum + "0011"
            elif hexdecnum[i] == '4':
                binnum = binnum + "0100"
            elif hexdecnum[i] == '5':
                binnum = binnum + "0101"
            elif hexdecnum[i] == '6':
                binnum = binnum + "0110"
            elif hexdecnum[i] == '7':
                binnum = binnum + "0111"
            elif hexdecnum[i] == '8':
                binnum = binnum + "1000"
            elif hexdecnum[i] == '9':
                binnum = binnum + "1001"
            elif hexdecnum[i] == 'a' or hexdecnum[i] == 'A':
                binnum = binnum + "1010"
            elif hexdecnum[i] == 'b' or hexdecnum[i] == 'B':
                binnum = binnum + "1011"
            elif hexdecnum[i] == 'c' or hexdecnum[i] == 'C':
                binnum = binnum + "1100"
            elif hexdecnum[i] == 'd' or hexdecnum[i] == 'D':
                binnum = binnum + "1101"
            elif hexdecnum[i] == 'e' or hexdecnum[i] == 'E':
                binnum = binnum + "1110"
            elif hexdecnum[i] == 'f' or hexdecnum[i] == 'F':
                binnum = binnum + "1111"
            i = i+1
        
        print("Setara dengan Binary: ", binnum)
        f.write(binnum)
        f.write("\n")
        print("Berhasil Menu 3 di cetak di text file!")
        f.close()
        
mulai = 0
konversi = KonversiTimothy()
while(mulai == 0):
    print("1. Octal to Binary")
    print("2. Desimal to Binary")
    print("3. Hexadesimal to Binary")
    print("4. Kosongkan isi txt file")
    print("5. Cetak isi txt file")
    print("Else exit!")
    print("Masukan nilai: ",end="")
    tanya = input()
    if(tanya == "1"):
        print("Masukan Bilangan Octal: ",end="")
        octnum = int(input())
        
        konversi.OctaltoBinary(octnum)
    elif(tanya == "2"):
        print("\nMasukan Bilangan Desimal: ",end="")
        decnum = int(input())
        konversi.DecimaltoBinary(decnum)
    elif(tanya == "3"):
        print("\nMasukan Bilangan Hexa: ",end="")
        hexdecnum = input()
        konversi.HexatoBinary(hexdecnum)
    elif(tanya == "4"):
        f = open("binary_poem", "w")
        f.write("")
        f.close()
    elif(tanya == "5"):
        f = open("binary_poem", "r")
        tampung = f.read()
        print("Isi text file :"+tampung)
        f.close()
    else:
        mulai = 1
        print("Telah Keluar!")




