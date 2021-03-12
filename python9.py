#Dictionary(sozluk)

#dictionary suslu parantezlerle ifade edilir ve iki kisimdan olusur.
#keys(anahtar)-----value(deger)
#keys kismi string ve int degerler alabilir.
#value kismi ise tum degerleri alabilir.
#sozluklerde de ekleme cikarma gibi islemler yapabiliyoruz.(degistirilebilir veri turu)

deneme={}
print(type(deneme))    #ciktisi: dict=dictionary olacaktir.

kursSec={1:"Python",
         2:"C++",
         3:"C",        #kursSec={1:"Python",2:"C++",3:"C",4:"c#",5:"Java"} seklinde de tanimlayabilirdik.
         4:"c#",       #Ama yaptigimiz sekilde kodumuz daha okunakli olacaktir.
         5:"Java"}          
print(kursSec)
print(kursSec[1])     #1 in degerini istiyoruz..
print(kursSec[3])

kursSec[6]="Html"
print(kursSec)        #kurs ekledik..
kursSec["Dil"]="Ingilizce"
print(kursSec)

kursSec[1]="Css"      #Guncellemeler de yapabiliyoruz.
print(kursSec)

#print(kursSec["C++"])  #Bu sekilde bir arama islemi yapamayiz cunku aradıgımız eleman keys degildir.
kursSec.pop(3)          #burada pop() icinde belirtilen keys degerini siler.
print(kursSec)

print(kursSec.keys())   #sozlukteki tum keysleri gosterecek.
print(kursSec.values())
print(kursSec.items())  #Burada ise sozluk icerisindeki keys ve values degerlerinin hepsini gosterecek.

kursSec["Gun"]=[1,2,3,4,5]   # "Gun" keysi olusacak ve degerleri :[1,2,3,4,5]
print(kursSec)

print(len(kursSec))  #Burada bize kac tane keys degeri oldugunu verecek.

print(2 in kursSec)  # 2 degerinin sozlukte olup olmadigini kontrol eder.
print("Dil" in kursSec)

print("Ingilizce" in kursSec)
print("Java"in kursSec)
#Bunlar false donecektir cunku values degerlerini degil keys degerlerini kontrol edebiliriz..

#Ornek yapalim:

kisilerim={
    "Tugba Kirac":"05001223212",
    "Sila Nur":"05018774595",
    "Can Hüseyin":"05216987845",
    "Mahir Kayseri":"05477884654"  
    }
kisi=input("Aramak istediginiz kisinin ismini yaziniz:")

VarMi=kisi in kisilerim      #burada girilen ismin kisilerimde olup olmadigina bakiyorum.varsa true yokse false doner.
if(VarMi==True):
    cevap=kisilerim[kisi]    #kisilerim[kisi] girilen ismin value degerini ister ve cevaba atar.
    print(f"{kisi} adli kisinin telefon numarasi:{cevap}")
else:
    print("Kisi yok!")