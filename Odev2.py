"""
Kullanıcıdan maaş bilgisini istenir ve bu bilgiye göre maaşından ne kadar vergi kesileceğini hesaplanır. Kullanıcının geliri;


 10000 ve altındaysa maaşından %5 kesinti olur. 
 25000 ve altındaysa maaşından %10 kesinti olur. 
 45000 ve altındaysa maaşından %25 kesinti olur. 
 Diğer koşullarda %30 kesinti olur. """
maas=int(input("Lütfen maasınızı  TL cinsinden giriniz "))
if(maas<=10000):
    kesinti=maas*0.05
elif(maas<=25000):
    kesinti=maas*0.1
elif(maas<=45000):
    kesinti=maas*0.25
else:
    kesinti=maas*0.3
print("Maaşınızdan kesilen tutar",kesinti)    


"""
Kullanıcıdan kullanıcı adı ve şifre oluşturmasını istenir. Şifrenin uzunluğu altı haneye ulaşmışsa hesabınız oluşturuldu mesajı alınır,
altı haneden azsa altı haneli şifre oluşturması gerektiğinin mesajı alınır. (Sadece koşul kullanılması yeterli.)
"""
kullanici_Adi=input("Lütfen  Kullanıcı adınızı giriniz ")
sifreniz=input("Şifrenizi giriniz ")
if(len(sifreniz)<6):
    print("Geçersiz bir şifre,şifreniz en az 6 karakter uzunluğunda olmalıdır.Lütfen tekrara deneyizni")
else:
    print("Hesabınız başarılı bir şekilde oluşturuldu ! Hoş geldiniz ")

"""
Bir önceki örnek geliştirilir.
 Kullanıcı girdiği şifre 5 ve 10 hane arasında olmak zorunda. 
 Eğer bu koşula uyuyorsa "Hesabınız oluşturuldu." mesajı alır. 
 Koşulu sağlamıyorsa "Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!" uyarısı alır. 
 Bunu oluştururken kullanıcı istediğimiz şartlarda şifre oluşturana kadar sormaya devam eder 

"""    
kullanici_adiniz=input("Lütfen kullanıcı adınızı giriniz ")
while True:
    sifrenizi_Giriniz=input("Lütfen şifrenizi giriniz ")
    if(5<len(sifrenizi_Giriniz) and len(sifrenizi_Giriniz)<10):
        print("Şifreniz başarılı bir şekilde oluşturulmuştur ")
        break
    else:
        print("Lütfen girdiniz şifre 5 haneden az 10 haneden fazla olmasın!") 




"""
Ödev-4: Kullanıcıdan isim ve şifre isteyeceğiz ve şifre girişi için üç hak verilir.


 Eğer önceden tanımlı şifre ile kullanıcıdan gelen şifre aynıysa "Giriş yapıldı." yazar. 
 Şifre girişi yanlışsa "Yanlış şifre girildi!" uyarısı verilsin ve üç yanlış denemede program biter. 
 Tercihe göre kalan hak bilgisi verilir. 

"""
sifre="12345"
hak=3

while(hak!=0):
    adiniz=input("Lütfen kullanıcı adınızı giriniz ")
    sifreniz=input("Lütfen şifrenizi giriniz ")
    if(sifre==sifreniz):
        print("Başarılı bir şekilde giriş yapıldı ")
        break
    else:
        hak-=1
        print(" Girdiğiniz şifre yanlış Lütfen tekrar deneyiniz")
      


