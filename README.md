# AETHER — Visual Art Director v3.1

**ChatGPT Image ile çalışan, konseptten nihai reklam görseline kadar süreci yöneten bir sanat yönetmeni skill’i.**

AETHER ürün fotoğraflarını, marka bilgilerini ve kampanya hedefini bir yaratıcı brief’e dönüştürür. Konsept geliştirir, kompozisyonu planlar, ChatGPT Image ile görseli üretir ve sonucu seçilen fikre göre değerlendirir.

**v3.1’in temel farkı:** İyi puan alan bir fikir tek başına yeterli değildir. Üretilen görsel, seçilen konseptin temel özelliklerini taşımalıdır. Eksikse teslimden önce düzeltme gerekir.

[İlk kullanım](#ilk-kullanım-önce-ne-yapmalısın) · [Örnekler](#kopyalanabilir-kullanım-örnekleri) · [İş akışı](#director-iş-akışı) · [Modüller](#dosyalar-ve-modüller) · [Sürüm notları](CHANGELOG.md)

## Ne yapar?

| Kullanım alanı | Örnek iş |
|---|---|
| Kreatif konsept geliştirme | Bir ısıtıcı için kış/sıcaklık karşıtlığına dayanan kampanya fikri |
| Premium ürün reklamı | Teknoloji, ev aleti, mobilya veya kozmetik ürününe özel reklam |
| Kampanya ve lansman | Kasım indirimi, yeni ürün, sezon veya özel gün görseli |
| Ürün sahneleme | Kaynak ürün fotoğrafının görünümüne uygun stüdyo, iç mekân veya mimari ortam |
| Konsept odaklı sürreal reklam | Ürün gerçeğine dayanan, kontrollü yaratıcı metafor |
| Sosyal medya | Feed postu, Story veya Reels kapağı için ayrı kompozisyon |
| Marka kampanya serisi | Aynı görsel dili koruyan, her üründe aynı şablonu tekrarlamayan seri |
| Tasarım revizyonu | Metin, kompozisyon, ışık veya konseptten sapma düzeltmesi |
| Prompt hazırlama | Görsel üretmeden, İngilizce ve üretime hazır prompt |

Video, animasyon, web sitesi veya kodla grafik üretimi bu sürümün kapsamına dahil değildir. AETHER bir görüntü modeli değildir; erişilebilir ChatGPT Image aracını yönlendiren talimat ve uzmanlık paketidir.

## Başlamak için gerekenler

- Skill talimatlarını okuyup uygulayabilen bir ortam.
- Gerçek görsel üretimi için **ChatGPT Image erişimi**. Skill kurulumu bu erişimi kendiliğinden sağlamaz.
- Gerçek bir ürün kullanılacaksa mümkünse net ürün fotoğrafı.
- Kullanılacak zorunlu metinler ve doğrulanmış kampanya bilgileri.

Depoyu indirmek tek başına skill’i etkinleştirmez. Ortamının desteklediği skill yükleme yöntemini kullan; giriş dosyası [SKILL.md](SKILL.md), destekleyici kaynaklar `references/`, arayüz metaverisi `agents/` içindedir. Yalnızca SKILL.md’yi kopyalamak bağlı uzmanlık modüllerini eksik bırakır.

Skill zaten yüklüyse ortamının skill seçicisinden **AETHER Visual Art Director**’ı seç. İstek içinde `@aether-visual-art-director` ifadesiyle açıkça çağırabilirsin; bazı ortamlarda çağırma biçimi `$aether-visual-art-director` olarak gösterilir. Kullandığın ortamın sunduğu seçiciyi esas al.

Skill yönetimi olmayan bir ortamda dosyaları sohbet bağlamında okutmak, o görev için talimatların uygulanmasına yardımcı olabilir; kalıcı kurulum anlamına gelmez.

**Python kurulumu, pip komutu veya üretim script’i gerekmez.** Bu depoda Pillow tabanlı üretim hattı bulunmaz.

## İlk kullanım: önce ne yapmalısın?

**Önce ürün ve marka referanslarını ekle, ardından tek mesajda kısa bir brief ver.** Baştan ayrıntılı sanat yönetimi yapman gerekmez; eksik yaratıcı kararları AETHER tamamlar.

1. **Çıktıyı belirt:** Tam reklam görseli mi, konsept önerileri mi, revizyon mu, yalnızca prompt mu?
2. **Ürün fotoğrafını ekle:** Ürün kimliğini koruyacak referansın hangisi olduğunu söyle. Ürün linki bilgi doğrulamaya yarar; fotoğrafın görsel araca aktarıldığını tek başına garanti etmez.
3. **Stil referansını ayır:** “Fotoğraf 1 ürünüm, Fotoğraf 2 yalnızca ışık ve atmosfer referansı.”
4. **Markayı tanımla:** Logo, renkler ve varsa onaylı kampanya örnekleri.
5. **Boyut ve kanalı yaz:** Örneğin Instagram Feed, hedef 1080×1350, 4:5.
6. **Kesin metinleri ver:** Başlık, tarih, fiyat veya teklif varsa aynen yaz. Olmayan bilgiler uydurulmaz.
7. **Korunacak detayları belirt:** Ürün rengi, ekran içeriği, ayaklar, logo, mevcut kamera açısı gibi.
8. **Çalışma şeklini seç:** Doğrudan final üretim, önce konseptleri görme veya ayrı alternatif görseller.

### Kısa brief şablonu

```text
@aether-visual-art-director

İstenen çıktı: Tam reklam görseli
Marka:
Ürün:
Hedef kitle / kampanya amacı:
Kanal ve hedef boyut:
Ürün kimliği referansı:
Yalnızca stil referansı:
Aynen kullanılacak metinler:
Marka renkleri / logo:
Korunması gereken detaylar:
Kaçınılacak unsurlar:
Çalışma şekli: Konseptleri değerlendir, en uygun yönü seç ve final görseli üret.
```

Kritik eksik bilgi yoksa AETHER yaratıcı kararları alıp ilerler. Fiyat veya teknik özellik gibi doğrulanmamış bilgileri tasarıma eklemez.

## Director iş akışı

1. **Brief ve referansları okur.** Ürün kimliğini, stil referansını, gerçek bilgileri ve zorunlu metinleri ayırır.
2. **Konsept geliştirir.** Kapsamlı yeni işlerde üç farklı yaratıcı yön düşünür; küçük revizyonlarda bu süreci tekrarlamaz.
3. **Uygun yönü seçer.** Karmaşık brief’lerde marka uyumu, özgünlük, hiyerarşi, ürün sadakati, doğruluk ve format açısından gerekçeli değerlendirme yapar. Puanlar yaratıcı tahmindir; objektif başarı ölçümü değildir.
4. **Seçilen konsepti tanımlar.** Konsept adı, ana fikir ve 3–5 görünür temel özellik kaydedilir. Hangilerinin konsept için vazgeçilmez olduğu belirlenir.
5. **Tam görseli üretir.** Ürün, sahne, ışık ve istenen tipografi ChatGPT Image içinde birlikte oluşturulur.
6. **Görseli konseptle karşılaştırır.** Temel özellikler “uyumlu / kısmen / eksik / doğrulanamadı” olarak değerlendirilir. Fikir puanı doğrudan sonuca kopyalanmaz.
7. **Gerekirse düzeltir.** Konseptten sapma veya genel kalite sorunu varsa aynı araçla hedefli düzenleme yapılır; tüm kare yeniden kontrol edilir.
8. **Sonucu teslim eder.** Konsept sadakati ve kalite koşulları birlikte karşılanmalıdır. Kontrol edilemeyen veya çözülemeyen bir durum varsa açıkça belirtilir.

### Konsept sadakati örneği

Seçilen fikir: **Sıcak bir ev ile pencereden görünen soğuk kışın karşıtlığı.**

Final görsel güzel bir bej stüdyo sahnesine dönüşmüş, pencere ve kış görünümü kaybolmuşsa sonuç konsepti karşılamaz. Fikir önceden 94/100 almış olsa bile bu puan görselin başarılı olduğunu kanıtlamaz. AETHER pencere/kış ilişkisini geri getirecek düzeltme ister.

Varsayılan olarak konseptler içeride değerlendirilir; üç ayrı önizleme otomatik üretilmez. Konseptleri veya puan tablosunu görmek istiyorsan bunu belirt. Üç görsel istiyorsan ayrıca “her birini ayrı bir görsel olarak üret” de.

## Tasarımda korunan kurallar

### Boş footer alanı

- Varsayılan olarak alt yüksekliğin **%12’si**, sonradan footer eklenebilmesi için boş bırakılır.
- Arka plan doğal biçimde devam eder; otomatik olarak beyaz şerit veya footer bileşeni çizilmez.
- Bu bölgeye ürün, yazı, logo, fiyat, sahne nesnesi veya güçlü gölge/yansıma yerleştirilmez.
- Hedef 1080×1350 için bu, altta 162 px’lik bir kompozisyon rezervidir; üretilen dosyada piksel ölçümünün yapıldığı anlamına gelmez.
- Footer yüksekliğini veya kullanımını açıkça değiştirmen mümkündür. Mevcut v3.1 varsayılanı bağımsız grafiklerde de uygulanır; istemiyorsan “Bu bağımsız asset için footer rezervi kullanma” diye belirt.

### Dekoratif çizgi yok

Metinlerin yanına, üstüne veya altına kısa/uzun çizgiler, alt çizgiler, ayraçlar, köşe işaretleri veya süs çerçeveleri eklenmez. Hiyerarşi ölçü, ağırlık, renk ve boşlukla kurulur. “13–27 Kasım” içindeki noktalama ve ürünün gerçek çizgisel detayları bu yasağa dahil değildir. Özel olarak istediğin çerçeve gibi istisnaları açıkça belirt.

### Tek üretim yolu

Bütün görsel üretimi ve düzeltmeler **ChatGPT Image** ile yapılır. Pillow, OpenCV, SVG/HTML çizimi, harici ürün birleştirme ve dışarıdan metin ekleme kullanılmaz. `assets/icon.svg` sadece skill arayüz simgesidir; reklam üretim yöntemi değildir.

## Kopyalanabilir kullanım örnekleri

### 1. İlk ürün reklamın

```text
@aether-visual-art-director
Ekteki Hausberg ısıtıcı fotoğrafıyla TechnoPlus için hedef 1080×1350,
4:5 Instagram reklamı oluştur. Başlık tam olarak “Kışın Sıcak Hali” olsun.
Modern ve sıcak bir yaşam alanı kullan. Fiyat veya indirim ekleme.
Ürünün görünen tasarımını ve mevcut kamera açısını korumaya çalış.
Konsepti seçip final görseli üret; sonucu seçilen fikre göre kontrol et.
```

### 2. Önce konseptleri görmek

```text
@aether-visual-art-director
Bu ürün için üç farklı kampanya konsepti geliştir.
Her biri için ana fikir, kompozisyon, ışık, malzeme ve kısa başlık öner.
Gerekçeli puan tablosunu ve önerdiğin yönü göster.
Şimdilik görsel üretme; önce konseptleri değerlendireceğim.
```

### 3. Seçilen konsepti final görsele dönüştürmek

```text
@aether-visual-art-director
İkinci konseptle devam et. Ana fikri ve onu tanımlayan temel özellikleri
koruyarak tam reklam görselini üret. Diğer konseptlerin öğelerini ekleme.
Teslimden önce görselin bu fikre sadık kaldığını kontrol et.
```

### 4. Çok ürünlü Kasım kampanyası

```text
@aether-visual-art-director
Ekteki üç Segway scooter fotoğrafını ürün kimliği referansı olarak kullan.
TechnoPlus için hedef 1080×1350 kampanya görseli oluştur.
Başlık “Kasım Fırsatları”, tarih “13–27 Kasım” olsun; başka teklif ekleme.
Öndeki ürün baskın, arkadakiler destekleyici olsun. Ürünlerin gerçekçi ölçeğini
ve ayırt edici detaylarını korumaya çalış. Her referansı ilgili ürünle eşleştir.
Alt footer rezervini ve çizgisiz metin kuralını koru.
```

### 5. Mevcut tasarımda hedefli düzeltme

```text
@aether-visual-art-director
Bu tasarımın konseptini, ürün görünümünü ve renklerini koru.
Kampanya başlığını biraz küçült; destek metnini yukarı taşı.
Metin çevresindeki dekoratif çizgileri kaldır. Footer alanı boş kalsın.
Düzeltmeden sonra seçilen konsepti ve ürün detaylarını tekrar kontrol et.
```

### 6. Yalnızca İngilizce prompt

```text
@aether-visual-art-director
Bu ürün için sinematik bir iç mekân reklamının İngilizce promptunu yaz.
Görsel üretme. Görseldeki Türkçe başlık tam olarak “Kışın Sıcak Hali” olsun.
Referans ürünün kimliğini koruma, boş footer ve çizgisiz tipografi kurallarını ekle.
```

### 7. Ayrı konsept görselleri

```text
@aether-visual-art-director
Üç farklı konseptin her birini ayrı bir reklam görseli olarak üret.
Kolaj veya tek karede üç panel yapma. Her biri aynı zorunlu metinleri ve
marka dilini korusun. Her görseli kendi konseptine göre değerlendir.
```

### 8. Transparan kampanya yazısı

```text
@aether-visual-art-director
Yazı tam olarak “KASIM İNDİRİMLERİ” olsun. Premium kırmızı-siyah estetikle,
minimal 3D metin efekti kullanarak transparan arka planlı bağımsız grafik üret.
Bu bağımsız asset için footer rezervi kullanma. Dekoratif çizgi veya çerçeve ekleme.
PNG hedefle; desteklenmeyen bir dosya özelliğini doğrulanmış gibi sunma.
```

## Dosyalar ve modüller

| Dosya / dizin | Görev |
|---|---|
| [SKILL.md](SKILL.md) | Ana amaç, üretim sınırları, tasarım kuralları ve iş akışı |
| [agents/openai.yaml](agents/openai.yaml) | Skill adı, kısa açıklama ve varsayılan çağırma metni |
| [Creative Concept Engine](references/creative-concept-engine.md) | Ürün gerçeğinden yaratıcı fikir geliştirme |
| [Concept Evaluation](references/concept-evaluation.md) | Gerekçeli konsept değerlendirmesi |
| [Concept Fidelity](references/concept-fidelity.md) | Seçilen fikrin final görselde korunmasının kontrolü |
| [Cinematic Photography](references/cinematic-photography-director.md) | Kamera, ışık ve malzeme yönetimi |
| [Product Fidelity](references/advanced-product-fidelity.md) | Referans ürünün görünümünü koruma |
| [Product Scene Direction](references/product-scene-direction.md) | Ürüne uygun çevre ve gerçekçi sahneleme |
| [Layout & Typography](references/advanced-layout-typography.md) | Hiyerarşi, tipografi ve boşluk |
| [Brand Visual DNA](references/brand-visual-dna.md) | Kampanya serilerinde marka tutarlılığı |
| [Visual Research](references/visual-research-playbook.md) | Orantılı görsel araştırma ve özgün yorum |
| [Platform Safe Zones](references/platform-safe-zones.md) | Çalışma geometrisi ve kırpma senaryoları |
| [Production](references/visual-production.md) | ChatGPT Image üzerinden tam üretim |
| [Prompt Examples](references/prompt-examples.md) | Araca gönderilecek brief örnekleri |
| [Iteration](references/visual-iteration-retouching.md) | Hedefli revizyon ve yeniden kontrol |
| [Quality Checklist](references/quality-checklist.md) | Son kabul koşulları |

## Sınırlar ve doğru beklenti

- Gerçek ürün görünümü korunmaya çalışılır; üretken düzenleme **piksel düzeyinde birebir koruma garantisi vermez**.
- İstenen boyut, PNG kodlaması, font eşleşmesi veya ölçülmüş kontrast yalnızca gerçekten doğrulandığında kesin olarak söylenir. Promptta yazılması tek başına doğrulama değildir.
- Görsel üretim aracı yoksa AETHER bunu söyler ve kullanıma hazır prompt önerebilir. Kodla reklam çizimine geçmez.
- Görsel inceleme mümkün değilse konsept sadakati ve kalite kontrolü “doğrulanamadı” olarak kalır.
- Puanlar estetik karar desteğidir; satış, reklam performansı veya dönüşüm garantisi değildir.
- Tek bir görselde aşırı ürün, çok uzun metin ve katı yerleşim talepleri sonucu zorlaştırabilir. Net brief ve güçlü hiyerarşi daha iyi yönlendirme sağlar.

**Sürüm:** 3.1. Bu depodaki talimatlar mevcut v3.1 skill paketinden alınmıştır. Lisans dosyası eklenmemiştir; üçüncü taraf marka görselleri, ürün fotoğrafları ve fontlar otomatik olarak serbest kullanım hakkı kazanmaz.
