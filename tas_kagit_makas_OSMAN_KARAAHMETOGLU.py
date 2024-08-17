import random

def tas_kagit_makas_OSMAN_KARAAHMETOGLU() :
  #1. Oyun Tanıtımı:
  #Program çalıştığında oyunu tanıtan mesaj
  tanitim_mesaji = a = """
    Taş kağıt makas oyunu döngülerden oluşur.
    İki döngü kazanan oyunu kazanır. Kullanıcı ve bilgisayarın isteğine göre yeni oyun oynanır.
    Kullanıcı ve bilgisayardan biri devam etmek istemezse oyun sonlanır.
    Kullanıcı ve bilgisayar Taş kağıt makas seçeneklerinden birini seçer. 
    Kullanıcı ve bilgisayar aynı seçeneği seçerse beraberlik olur.
    Oyun kurallarına göre Taş seçeneği, Makas seçeneğini,  Kağıt seçeneği, Taş seçeneğini, 
    Makas seçeneği, Kağıt seçeneğini yener.
    Oyun döngüsünü oyuncu kazanabilir, bilgisayar kazanabilir veya beraberlik olabilir.
    İlk iki turu kazanan oyunu kazanır.
    Kullanıcı bu üçü dışında çık seçeneğini de seçer. Doğru bir seçenek seçilmemişse seçim tekrarlanır.
    """


  print (tanitim_mesaji)

  #2. Oyun Kurulumu:


  #Taş kağıt makas oyunu seçim değerleri listesinin oluşturulması
 
  actions = ["Taş","Kağıt","Makas"]

  secim_mesaji = ', '.join(actions) + ", çık ? "

  evet_hayir_secim = ["Evet", "Hayır"]

  #Oynanan oyun sayısı, oynanan tur sayısı, oyuncu galibiyetleri ve bilgisayar galibiyetleri için sayaçlar başlatın.
  
  #Oyun döngü değişkenleri başlangıc değeri
  oyun = 1
  dongu = 1

  kullanici_skor = 0
  bilgisayar_skor = 0

  kullanici_oyun_skoru = 0
  bilgisayar_oyun_skoru = 0

  
  #3. Oyunun Ana Döngüsü:
  
  # Oyunu oynanabilir kılmak için bir while döngüsü kullanın

  while True :
    # Bu döngü içinde, her yeni oyun için tur ve galibiyet sayaçlarını sıfırlayın.
    kullanici_skor = 0
    bilgisayar_skor = 0
    dongu = 1
    
    # 4. Turların Döngüsü:
    
    # Oyuncu veya bilgisayar iki tur kazanana kadar başka bir while döngüsü kullanın

    while  kullanici_skor < 2 and bilgisayar_skor < 2  : 
      # Oyun döngü mesajı
      print(f'Oyun : {oyun}, Döngü : {dongu}')
      # Seçenekler ekrana yazdılır ve kullanıcı seçimi
      
      # Oyuncudan üç seçenekten birini yapmasını isteyin, geçersiz bir opsiyon seçerse, yeniden bir seçenek girmesini isteyin.
      kullanici_secimi = input(secim_mesaji)
      if kullanici_secimi == "çık" :
        print ("Mademki oynamayacaktın, neden programı açtın.")
        continue # döngüyü en başa alır
      # Geçersiz bir opsiyon seçerse, yeniden bir seçenek girmesini isteyin.
      if kullanici_secimi not in actions :
        print (f"Lütfen doğru bir seöim yapınız. {kullanici_secimi}")
        continue # döngüyü en başa alır
      
      # Bilgisayarın seçimini rastgele oluşturun (ipucu: random modülünü kullanabilirsiniz).
      bilgisayar_secimi = actions[random.randint(0, 2)]
      
      # Seçimleri aldıktan sonra turun kazananını belirlemek için mantıksal operasyonlar veya temel if-else ifadelerini kullanın.
      # İlk iki turu kazanan oyunu kazanacağından galibiyet sayaçlarını güncellemeyi unutmayın.
      #Her turun sonucunu ekrana yazdırın (ipucu: print() fonksiyonu tam da bu iş için).
      
      if kullanici_secimi == bilgisayar_secimi:
        print ("Beraberlik")
      elif kullanici_secimi ==  "Kağıt" and  bilgisayar_secimi == "Taş":
        kullanici_skor = kullanici_skor + 1
        print ("Kullanıcı kazandı.")
      elif kullanici_secimi ==  "Kağıt" and  bilgisayar_secimi == "Makas":
        bilgisayar_skor = bilgisayar_skor + 1
        print ("Bilgisayar kazandı.")
      elif kullanici_secimi ==  "Taş" and  bilgisayar_secimi == "Kağıt":
        bilgisayar_skor = bilgisayar_skor + 1
        print ("Bilgisayar kazandı.")
      elif kullanici_secimi ==  "Taş" and  bilgisayar_secimi == "Makas":
        kullanici_skor = kullanici_skor + 1
        print ("Kullanıcı kazandı.")
      elif kullanici_secimi ==  "Makas" and  bilgisayar_secimi == "Taş":
        bilgisayar_skor = bilgisayar_skor + 1
        print ("Bilgisayar kazandı.")
      elif kullanici_secimi ==  "Makas" and  bilgisayar_secimi == "Kağıt":
        kullanici_skor = kullanici_skor + 1
        print ("Kullanıcı kazandı.")

      print (f"Kullanıcı Seçimi : {kullanici_secimi} , Bilgisayar Seçimi : {bilgisayar_secimi}")
      print (f"Kullanıcı : {kullanici_skor}, Bilgisayar : {bilgisayar_skor}" )

      dongu = dongu + 1
    
    # 5. Oyun Galibini Belirleyin:
    
    # Turların döngüsü bittikten sonra (bir oyuncu iki tur kazandığında), oyunun genel galibini belirleyin ve uygun mesajı gösterin.
    
    kim_kazandi_mesaji = ""
    if kullanici_skor == 2 : 
      kim_kazandi_mesaji = "Tebrikler kazandınız."
      kullanici_oyun_skoru = kullanici_oyun_skoru + 1
    elif bilgisayar_skor == 2 :
      kim_kazandi_mesaji = "Ben kazandım."
      bilgisayar_oyun_skoru = bilgisayar_oyun_skoru + 1
   
    print (f"Oyun : {oyun}, Kullanıcı Oyun Skoru : {kullanici_oyun_skoru} , Bilgisayar Oyun Skoru : {bilgisayar_oyun_skoru}")
    
    # 6. Devam Etme İsteği:
    if kim_kazandi_mesaji != "" :
      
      # Kullanıcıya başka bir oyun oynamak isteyip istemediğini sorun
      kullanici_devam_secim = ''
      while kullanici_devam_secim not in evet_hayir_secim:
        kullanici_devam_secim = input (f"{kim_kazandi_mesaji} Yeni bir oyunla devam etmek ister misiniz?, (Evet, Hayır) : ")
      if kullanici_devam_secim == "Hayır":
        print(F"Kullanıcı oyuna devam etmek istemediği için oyun tmamamlandı.")
        # Her iki taraf da oyuna devam etmek istiyorsa oyun devam etsin; fakat iki taraftan biri devam etmek istemiyorsa oyun bitsin 
        # (ipucu:bunun için break kullanabilirsiniz).,
        # Her durum için uygun bir mesaj gösterin
        break
      
      # Bilgisayarın da oyuna devam etmek isteyip istemediğini sorun (rastgele bir cevap oluşturabilirsiniz).

      bilgisayar_devam_secim = evet_hayir_secim[random.randint(0, 1)]
      if bilgisayar_devam_secim == "Hayır":
        print(F"Bilgisayar oyuna devam etmek istemediği için oyun tmamamlandı.")
        # Her iki taraf da oyuna devam etmek istiyorsa oyun devam etsin; fakat iki taraftan biri devam etmek istemiyorsa oyun bitsin 
        # (ipucu:bunun için break kullanabilirsiniz).

        break

    oyun =  oyun + 1
      
  print ("Hoşçakalın. Yine bekleriz...")

tas_kagit_makas_OSMAN_KARAAHMETOGLU()