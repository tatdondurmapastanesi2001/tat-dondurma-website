import os, shutil, urllib.parse as up
OUT = '/mnt/user-data/outputs/tatpastanesi'
shutil.rmtree(OUT, ignore_errors=True)
for d in ['', 'urunlerimiz', 'menu', 'ozel-siparis', 'subelerimiz', 'hakkimizda', 'iletisim', 'assets', 'images/menu', 'images/products', 'images/covers']:
    os.makedirs(f'{OUT}/{d}', exist_ok=True)

NAME = 'Tat Dondurma & Pastanesi'
IG = 'https://www.instagram.com/tatdondurma.pastanesi/'
GMAPS = 'https://www.google.com/maps/place/Tat+Dondurma+%26+Pastanesi/@39.9548,32.7588,15z'
HOURS = '09:00 – 01:00'
B = [  # slug, ad, ilçe, adres, tel, wa, harita sorgusu, görsel
 ('batikent', 'Batıkent', 'Yenimahalle / Ankara', 'Kentkoop Mahallesi, 1865. Cadde No:13/B, 06220 Batıkent / Ankara', '0554 172 78 08', '905541727808', 'Tat Dondurma Pastanesi Kentkoop Mahallesi 1865. Cadde 13/B Batıkent Ankara', 'batikent.jpg'),
 ('cakirlar', 'Çakırlar', 'Yenimahalle / Ankara', 'Turgut Özal Mah. 2179. Sk. No:6 D:F, 06370 Batıkent - Yenimahalle / Ankara', '0536 631 50 11', '905366315011', 'Tat Dondurma Pastanesi 2179. Sk. No:6 Batıkent Yenimahalle Ankara', 'cakirlar.jpg'),
 ('baglica', 'Bağlıca', 'Etimesgut / Ankara', 'Mermeroğlu Caddesi No:61/5, 06790 Bağlıca / Etimesgut / Ankara', '0501 123 55 06', '905011235506', 'Tat Dondurma Pastanesi Mermeroğlu Caddesi 61 Bağlıca Etimesgut Ankara', 'baglica.jpg'),
 ('eryaman-concept', 'Eryaman Concept', 'Etimesgut / Ankara', 'Yavuz Selim Mah. 11. Cadde 618. Sokak Concept Çarşı 7A/1, Eryaman / Etimesgut / Ankara', '0543 684 56 72', '905436845672', 'Concept Çarşı 7A/1 Yavuz Selim Mahallesi Eryaman Etimesgut Ankara', ''),
 ('eryaman-rada-park', 'Eryaman Rada Park', 'Etimesgut / Ankara', 'Eryaman Mah. 271. Cadde, Rada Park AVM No:3, Etimesgut / Ankara', '0501 370 19 06', '905013701906', 'Rada Park AVM Eryaman Etimesgut Ankara', ''),
]
FLAVORS = 'Tahin,Nero,Meyve Kokteyli,Antep Fıstıklı,Damla Çikolata,Bodrum Mandalina,İncir,Şeftali,Kavun,Portakal,Mango,Vişne,Atom,Limon,Çikolata,Sade,Çilek,Karamel,Bal Badem,Tiramisu,Meyveli Yoğurt,Karadut,Ceviz,Nane,Bitter,Yeşil Elma,Kestane,Şirinler,Damla Sakız,Çikolata Portakal,Yaban Mersini,Belçika,Lotus,Hindistan Cevizi,Beyaz Çikolata,Dağ Çileği,Muz,Keçi Sütü'.split(',')
# kategori: slug, başlık, üst yazı, açıklama, [(ad, açıklama, görsel, fiyat)], çeşit listesi başlığı, çeşitler
def I(n, d='', img='menu/1.jpg', p=''): return (n, d, img, p)
CATS = [
 ('dondurma', 'Dondurma', 'Onlarca çeşit, %100 doğal', 'Taze meyve ve gerçek malzemelerle her gün üretilen imza dondurmalarımız; külah, kâğıt helva, cup ve paket seçenekleriyle.',
  [I('Tat Dondurma', 'Külah, kâğıt helva, cup ve paket seçenekleriyle; dilediğiniz çeşitleri birlikte seçin.'), I('Paket Dondurma', 'Evinize, sofranıza, kutlamalarınıza; istediğiniz çeşitlerle doldurulan paketler.')], 'Dondurma Çeşitlerimiz', FLAVORS),
 ('yas-pasta', 'Yaş Pasta', 'Günlük ve tasarım', 'Vitrinimizde her gün taze hazırlanan pastalar ve hayalinizdeki modele göre yapılan kişiye özel tasarım pastalar.',
  [I('Günlük Pasta', 'Her gün taze hazırlanan, vitrinimizde sizi bekleyen pastalar.', 'covers/beyaz-pasta.jpg'), I('Tasarım Pasta', 'Beğendiğiniz modeli, dilediğiniz fotoğraf ve yazıyla size özel bir tasarıma dönüştürüyoruz.', 'products/sippas.jpg'),
   I('Şeker Hamurlu Tasarım Pasta', 'Şeker hamuru figürler ve özel detaylarla doğum günü, nişan ve kutlamalara özel pastalar.', 'products/sekerpas.jpg'), I('Doğum Günü Pastası', 'Çocuğunuzun sevdiği karakterle, adına özel hazırlanan pastalar.', 'robloxp.jpg'),
   I('Çilekli Mois Adet Pasta', 'Çilekli, nemli keki ve hafif kremasıyla tek kişilik pasta.', 'menu/41.jpg'), I('Tek Kişilik Pastalar', 'Vitrinimizden seçeceğiniz tek kişilik pasta dilimleri.', 'menu/42.jpg')],
  'Pasta Çeşitlerimiz', 'Çilekli,Frambuazlı,Vişneli,Damla Çikolatalı,Parça Çikolatalı,Muzlu,Kestaneli,Draje Fıstıklı,Lotuslu,Meyveli,Krokanlı'.split(',')),
 ('sutlu-tatlilar', 'Sütlü Tatlılar', "Klasikler ve cheesecake'ler", "Profiterolden Rumeli çileklisine, magnolyalardan cheesecake'lere; günlük taze sütle hazırlanan tatlılar.",
  [I('Rumeli Çileklisi', 'Misafirlerimizin favorisi.', 'menu/16.jpg'), I('Profiterol', '', 'menu/5.jpg'), I('Supangle', '', 'menu/6.jpg'), I('Sütlaç', '', 'menu/7.jpg'), I('Keşkül', '', 'menu/8.jpg'), I('İncirli Muhallebi', '', 'menu/9.jpg'),
   I('Spoonful', '', 'menu/10.jpg'), I('Çilekli Magnolya', '', 'menu/11.jpg'), I('Çikolatalı Magnolya', '', 'menu/12.jpg'), I('Orman Meyveli Magnolya', '', 'menu/14.jpg'), I('Renkli Petibör', '', 'menu/15.jpg'), I('Tiramisu', '', 'menu/18.jpg'),
   I('Alman Pastası', '', 'menu/19.jpg'), I('Beyaz Kremalı Muzlu Ankara Sarması', '', 'products/beyan.jpg'), I('Beyaz Kremalı Çilekli Ankara Sarması', '', 'products/ankarasarc.jpg'), I('Çikolatalı Muzlu Ankara Sarması', '', 'menu/22.jpg'),
   I('Kazandibi', '', 'menu/28.jpg'), I('Trileçe', '', 'menu/29.jpg'), I('Brownie', '', 'menu/30.jpg'), I('Kıbrıs Tatlısı', '', 'menu/31.jpg'), I('Ekler', '', 'menu/32.jpg'), I('Acıbadem', '', 'products/acib.jpg'),
   I('Limonlu Cheesecake', '', 'menu/43.jpg'), I('Frambuazlı Cheesecake', '', 'products/fram.jpg'), I('Lotus Cheesecake', '', 'products/lotuschh.jpg'), I('Adet Pasta', '', 'products/moz.jpg'), I('Mozaik Pasta', '', 'products/mozaikkk.jpg'),
   I('Çikolatalı Muzlu Malaga', '', 'menu/39.jpg'), I('Beyaz Muzlu Malaga', '', 'menu/40.jpg'), I('Fıstıklı Soğuk Baklava', '', 'menu/34.jpg')], '', []),
 ('serbetli-tatlilar', 'Şerbetli Tatlılar', 'El açması, bol fıstıklı', 'İncecik el açması yufka, bol Antep fıstığı ve kıvamında şerbetle geleneksel lezzetler.',
  [I(n, '', 'products/baklava.jpg') for n in ['Fıstıklı Baklava', 'Cevizli Baklava', 'Fıstık Sarma', 'Fıstıklı Şöbiyet', 'Fıstıklı Havuç Dilimi', 'Fıstıklı Midye']], '', []),
 ('kuru-pasta', 'Kuru Pasta', 'Çay saatinin yıldızı', 'Tuzlu ve tatlı, birbirinden farklı çeşitlerle günlük taze kuru pastalar; gramajla veya kutuda.',
  [I('Kuru Pasta Çeşitleri', 'Vitrinimizden dilediğiniz çeşitleri seçin; misafirlik ve hediye için kutuda hazırlıyoruz.', 'menu/23.jpg')], '', []),
 ('waffle', 'Waffle', 'Sıcak, taze, sizin seçiminiz', 'Anında pişen waffle; dilediğiniz meyve, sos ve süslemelerle.',
  [I('Waffle', 'Dilediğiniz meyve, sos ve süsleme seçenekleriyle taze hazırlanır.', 'covers/waffle-tabak.jpg')], '', []),
]
VIT = {'dondurma': 'Onlarca çeşit, %100 doğal', 'yas-pasta': 'Günlük ve tasarım', 'sutlu-tatlilar': "Klasikler ve cheesecake'ler", 'serbetli-tatlilar': 'El açması, bol fıstıklı', 'kuru-pasta': 'Çay saatinin yıldızı', 'waffle': 'Sıcak, taze, sizin seçiminiz'}
NAV = [('urunlerimiz/', 'Ürünlerimiz'), ('ozel-siparis/', 'Özel Sipariş'), ('subelerimiz/', 'Şubelerimiz'), ('hakkimizda/', 'Hakkımızda'), ('iletisim/', 'İletişim')]
e = lambda s: s.replace('&', '&amp;').replace('"', '&quot;')
def img(R, src, alt='', cls=''): return f'<span class="ph {cls}"><img src="{R}images/{src}" alt="{e(alt)}" loading="lazy" onerror="this.remove()"></span>'
def tel(p): return 'tel:+9' + p.replace(' ', '')

def page(depth, slug, title, desc, body):
    R = '../' * depth
    nav = ''.join(f'<a href="{R}{h}"{" aria-current=page" if h.startswith(slug) and slug else ""}>{t}</a>' for h, t in NAV)
    mnav = ''.join(f'<a href="{R}{h}">{t}</a>' for h, t in [NAV[0], ('menu/', 'Menü & Fiyatlar')] + NAV[1:])
    pages = ''.join(f'<li><a href="{R}{h}">{t}</a></li>' for h, t in [('', 'Ana Sayfa'), NAV[0], ('menu/', 'Menü & Fiyatlar')] + NAV[1:])
    fb = ''.join(f'<li>{b[1]}<a href="{tel(b[4])}">{b[4]}</a></li>' for b in B)
    return f'''<!doctype html><html lang="tr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{e(desc)}"><meta name="theme-color" content="#1c120e"><meta property="og:title" content="{e(title)}"><meta property="og:description" content="{e(desc)}"><meta property="og:locale" content="tr_TR">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,700&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/style.css"></head><body data-root="{R}">
<a class="skip" href="#icerik">İçeriğe geç</a>
<header class="hd"><a class="logo" href="{R}"><img src="{R}images/tat-logo.png" alt="{NAME}" onerror="this.replaceWith(document.createTextNode('Tat'))"></a>
<nav class="nav">{nav}</nav><div class="hd-r"><a class="btn ghost sm" href="{R}urunlerimiz/?ara">Ara</a><a class="btn sm" href="{R}menu/">Menü</a><button class="burger" aria-label="Menü" aria-expanded="false"><i></i><i></i></button></div></header>
<div class="mnav" hidden>{mnav}<a href="https://wa.me/905541727808">WhatsApp</a><p>{HOURS} · <a href="{IG}">Instagram</a></p></div>
<main id="icerik">{body}</main>
<footer class="ft"><div class="ft-g"><div><img class="ft-logo" src="{R}images/tat-logo.png" alt="{NAME}" onerror="this.remove()"><p>2001'den beri Ankara'nın tatlı anlarına eşlik ediyoruz.</p>
<p><a class="btn sm" href="{R}menu/">Dijital Menü</a> <a class="btn ghost sm" href="{R}ozel-siparis/">Pasta Siparişi</a></p><p><a href="{IG}">Instagram @tatdondurma.pastanesi</a></p></div>
<div><h3>Sayfalar</h3><ul>{pages}</ul></div><div><h3>Şubelerimiz</h3><ul>{fb}</ul></div></div>
<p class="ft-c">© 2026 {NAME}. Tüm hakları saklıdır.</p></footer>
<div class="dock"><a href="{R}subelerimiz/">Şubeler</a><a href="https://wa.me/905541727808" class="wa">WhatsApp</a><a href="{R}menu/">Menü</a></div>
<script src="{R}assets/main.js"></script></body></html>'''

def hero(R, kick, h, p, im, extra=''):
    return f'<section class="ph-hero">{img(R, im, "", "bg")}<div class="wrap"><p class="kick">{kick}</p><h1>{h}</h1><p class="lead">{p}</p>{extra}</div></section>'

def write(path, html):
    with open(f'{OUT}/{path}', 'w', encoding='utf-8') as f: f.write(html)

# ---------- ANA SAYFA ----------
R = ''
vit = ''.join(f'<a class="vc" href="urunlerimiz/#{c[0]}">{img(R, c[4][0][2], c[1])}<strong>{c[1]}</strong><span>{VIT[c[0]]}</span></a>' for c in CATS)
sig = ''.join(f'<a href="urunlerimiz/#sutlu-tatlilar">{n}</a>' for n in ['Rumeli Çileklisi', 'Profiterol', 'Supangle', 'Sütlaç', 'Keşkül', 'İncirli Muhallebi', 'Spoonful', 'Çilekli Magnolya'])
chips = ''.join(f'<button type="button" class="chip">{f}</button>' for f in FLAVORS)
rev = [('Gülçin Biber', 'Rumeli çileklisi diye bir tatlıları var. Uzun zamandır dışarıda yediğim en iyi tatlıydı, çok lezzetliydi. Diğer tatlıları da denemeye en kısa sürede yine gideceğim.'),
       ('Sevilay Arı', "Her zaman sipariş veriyorum, hiç pişman olmadım; her şey her zaman çok taze ve lezzetli. Ankara'da en sevdiğim pastane net. Her yaz dondurmalarının bağımlısı oluyorum."),
       ('Kaan', "Ankara'nın en iyi dondurmacılarından biri. Temiz ve kaliteli bir işletme, çalışanlar ilgili ve güler yüzlü, servis hızlı. Bal badem, karamel, sade, portakallı çikolata gayet güzel.")]
revh = ''.join(f'<blockquote><p>“{t}”</p><cite><b>{n[0]}</b>{n}<small>Google yorumu</small></cite></blockquote>' for n, t in rev)
brh = ''.join(f'<article class="bc"><h3>{b[1]}</h3><p>{b[3]}</p><div><a class="btn sm" href="{tel(b[4])}">Ara</a> <a class="btn ghost sm" href="https://www.google.com/maps/search/?api=1&amp;query={up.quote(b[6])}">Yol tarifi</a></div></article>' for b in B)
steps = [('Fikrinizi paylaşın', 'Model fotoğrafı, tema, yazı ve kişi sayısını bize iletin.'), ('Birlikte netleştirelim', 'Ustalarımız tasarımı, lezzeti ve teslim gününü sizinle belirlesin.'), ('Mutluluğu teslim alın', 'Pastanız, seçtiğiniz şubede taptaze hazır olsun.')]
sth = ''.join(f'<li><b>{i+1}</b><h3>{a}</h3><p>{c}</p></li>' for i, (a, c) in enumerate(steps))
vals = [('Gelenek', 'Kuşaktan kuşağa reçeteler', "2001'den bu yana aynı özenle uyguladığımız tariflerimizi her gün yeniden, ilk günkü heyecanla hazırlıyoruz.", 'covers/deger-gelenek.jpg'),
        ('Ustalık', 'Usta ellerin dokunuşu', 'Her hamur ustalarımızın elinde şekil bulur, her süsleme tek tek, sabırla yapılır. Seri üretim değil, zanaat.', 'covers/deger-ustalik.jpg'),
        ('Doğallık', 'Saf ve taze malzeme', 'Günlük taze süt, mevsiminde olgunlaşmış meyveler, gerçek Antep fıstığı. Katkı yok, kestirme yok.', 'covers/deger-dogallik.jpg')]
valh = ''.join(f'<article class="val">{img(R, v[3])}<small>{v[0]}</small><h3>{v[1]}</h3><p>{v[2]}</p></article>' for v in vals)
STATS = '<div class="stats"><div><b>2001</b>Kuruluş yılı</div><div><b>%100</b>Doğal malzeme</div><div><b>500+</b>Günlük taze ürün</div><div><b>50B+</b>Mutlu misafir</div></div>'
mq = ''.join(f'<span>{t}</span>' for t in ['%100 Doğal Malzeme', 'Günlük Üretim', 'El Yapımı', 'Tasarım Pastalar', 'Katkısız Dondurma', "2001'den Beri"] * 2)
home = f'''<section class="hero">{img(R, 'neden3.jpg', '', 'bg')}<div class="wrap"><p class="kick">Kuruluş 2001</p><h1>Ustalıkla<br>Tatlı Sanatı</h1>
<p class="lead">Geleneksel lezzetleri modern ve zarif dokunuşlarla yeniden yorumluyoruz. Her dilimde 25 yılın tecrübesi var.</p>
<p><a class="btn" href="urunlerimiz/">Lezzetlerimizi Keşfet</a> <a class="btn ghost" href="ozel-siparis/">Pasta Siparişi Ver</a></p>
<p class="meta"><a href="{GMAPS}">Google yorumları</a> 5 şube · 38 çeşit dondurma · Her gün taze</p></div></section>
<div class="mq"><div>{mq}</div></div>
<section class="sec wrap" id="vitrin"><p class="kick">Vitrinimizden</p><h2>Her damak için bir lezzet</h2><a class="more" href="urunlerimiz/">Tüm ürünleri gör</a><div class="vg">{vit}</div></section>
<section class="sec dark"><div class="wrap two">{img(R, 'menu/16.jpg', 'Tat Pastanesi Rumeli Çileklisi', 'tall')}<div><blockquote class="q">“Uzun zamandır dışarıda yediğim en iyi tatlıydı.”<cite>— Gülçin Biber, Google</cite></blockquote>
<p class="kick">İmza lezzetimiz</p><h2>Rumeli Çileklisi</h2><p>Hafif kreması, taze çilekleri ve yumuşacık dokusuyla misafirlerimizin en çok sorduğu tatlı. Yanında; magnolyalar, profiterol, trileçe ve günlük taze sütlü tatlılarımız sizi bekliyor.</p><div class="tags">{sig}</div></div></div></section>
<section class="sec wrap two" id="kulah"><div><p class="kick">Tat Dondurma</p><h2>38 çeşit, %100 doğal.</h2><p>Gerçek meyve, gerçek fıstık, gerçek kakao. Her gün taze üretilen dondurmalarımızı külah, kâğıt helva, cup ya da paket olarak dilediğiniz gibi seçin.</p>
<div class="cone"><p class="kick">Külahını oluştur</p><h3 id="cone-t">Antep Fıstıklı · Vişne</h3><p class="hint">En fazla 3 top. Seçtiklerinize dokunarak çıkarabilirsiniz.</p><div class="chips">{chips}</div></div></div>
<div class="duo">{img(R, 'neden3.jpg', 'Böğürtlenli ve portakallı dondurmalar')}{img(R, 'covers/kulah.jpg', 'Fındıklı, çikolata kaplı külah dondurma')}</div></section>
<section class="sec cream2"><div class="wrap two"><div class="duo3">{img(R, 'robloxp.jpg', 'Roblox temalı doğum günü pastası')}{img(R, 'products/sekerpas.jpg', 'Şeker hamurlu tasarım pasta')}{img(R, 'products/sippas.jpg', 'Çiçekli katlı tasarım pasta')}</div>
<div><p class="kick">Özel günleriniz için</p><h2>Hayalinizdeki pastayı birlikte tasarlayalım.</h2><ol class="steps">{sth}</ol><a class="btn" href="ozel-siparis/">Sipariş Formunu Doldur</a></div></div></section>
<section class="sec wrap"><p class="kick">Bizi biz yapanlar</p><h2>Sanatın Zirvesi</h2><div class="vals">{valh}</div>{STATS}</section>
<section class="sec dark"><div class="wrap"><p class="kick">Misafirlerimiz ne diyor?</p><h2>Tatlı sözler için teşekkürler.</h2><a class="more" href="{GMAPS}">Tüm Google yorumları</a><div class="revs">{revh}</div></div></section>
<section class="sec wrap"><p class="kick">5 şube, aynı lezzet</p><h2>Size en yakın Tat</h2><a class="more" href="subelerimiz/">Tüm şube bilgileri</a><div class="bg5">{brh}</div></section>'''
write('index.html', page(0, '', "Tat Pastanesi | 2001'den Beri Ankara'nın Pasta, Tatlı ve Dondurma Durağı", "2001'den beri Ankara'da; Batıkent, Çakırlar, Bağlıca ve Eryaman şubelerimizde günlük taze yaş pasta, sütlü ve şerbetli tatlılar ile %100 doğal dondurma.", home))

# ---------- ÜRÜNLER ----------
R = '../'
tabs = ''.join(f'<a href="#{c[0]}">{c[1]}</a>' for c in CATS)
secs = ''
for c in CATS:
    items = ''.join(f'<li class="item">{img(R, i[2], i[0])}<h3>{i[0]}</h3>{"<p>"+i[1]+"</p>" if i[1] else ""}</li>' for i in c[4])
    extra = f'<h3 class="sub">{c[5]}</h3><ul class="pills">{"".join("<li>"+x+"</li>" for x in c[6])}</ul>' if c[6] else ''
    secs += f'<section class="sec wrap prodsec" id="{c[0]}"><p class="kick">{c[2]}</p><h2>{c[1]}</h2><p class="lead2">{c[3]}</p><ul class="pg">{items}</ul>{extra}</section>'
prod = hero(R, 'Şefin imzası', 'Koleksiyon menüsü', 'Doğal malzemelerle, ustalarımızın ellerinden çıkan lezzetler. Her gün taze, her gün aynı özenle.', 'covers/pasta-vitrini.jpg') + \
  f'<div class="tabs"><div class="wrap">{tabs}<input id="q" type="search" placeholder="Ürün ara" aria-label="Ürün ara"></div></div>{secs}' + \
  '<section class="sec dark"><div class="wrap cta"><p class="kick">Güncel fiyatlar</p><h2>Tüm menü ve fiyatlar dijital menümüzde.</h2><p><a class="btn" href="../menu/">Menüyü Aç</a> <a class="btn ghost" href="../ozel-siparis/">Pasta Siparişi</a></p></div></section>'
write('urunlerimiz/index.html', page(1, 'urunlerimiz', 'Ürünlerimiz – Pasta, Tatlı ve Dondurma | Tat Pastanesi', 'Tat Pastanesi ürünleri: doğal dondurma, günlük ve tasarım yaş pastalar, Rumeli çileklisi, magnolya, profiterol, baklava, kuru pasta ve waffle.', prod))

# ---------- MENÜ (TR/EN) ----------
EN = {'dondurma': 'Ice Cream', 'yas-pasta': 'Cakes', 'sutlu-tatlilar': 'Milk Desserts', 'serbetli-tatlilar': 'Syrup Desserts', 'kuru-pasta': 'Cookies & Biscuits', 'waffle': 'Waffle'}
mc = ''
for c in CATS:
    rows = ''.join(f'<li><span>{i[0]}</span><b>{i[3] or "—"}</b></li>' for i in c[4])
    mc += f'<section class="msec"><h2 data-tr="{c[1]}" data-en="{EN[c[0]]}">{c[1]}</h2><ul>{rows}</ul></section>'
menu = f'''<section class="mhero">{img(R, 'menu/16.jpg', '', 'bg')}<div class="wrap"><div class="lang"><button class="on" data-l="tr">TR</button><button data-l="en">EN</button></div><img class="mlogo" src="{R}images/tat-logo.png" alt="{NAME}" onerror="this.remove()">
<h1 data-tr="Lezzetlerimizi keşfedin" data-en="Discover our flavours">Lezzetlerimizi keşfedin</h1><p data-tr="2001'den beri, her gün taze." data-en="Since 2001, fresh every day.">2001'den beri, her gün taze.</p><a class="btn" href="#liste" data-tr="Menüyü Görüntüle" data-en="View Menu">Menüyü Görüntüle</a></div></section>
<div class="wrap" id="liste">{mc}<p class="note" data-tr="Fiyatlar ve alerjen bilgisi için şubemize danışabilirsiniz." data-en="Ask your branch for prices and allergen information.">Fiyatlar ve alerjen bilgisi için şubemize danışabilirsiniz.</p></div>'''
write('menu/index.html', page(1, 'menu', 'Menü & Fiyatlar | Tat Pastanesi', 'Tat Pastanesi güncel menü ve fiyat listesi: dondurma, yaş pasta, sütlü tatlılar, kuru pasta, waffle. Türkçe / English.', menu))

# ---------- ÖZEL SİPARİŞ ----------
opt = lambda L: ''.join(f'<option>{x}</option>' for x in L)
bo = ''.join(f'<option value="{b[5]}">{b[1]}</option>' for b in B)
faq = [('Siparişimi ne kadar önceden vermeliyim?', 'Tasarım ve şeker hamurlu pastalar için en az 2–3 gün önceden, yoğun dönemlerde (bayram, yılbaşı, mezuniyet) daha erken sipariş vermenizi öneririz.'),
       ('Fotoğraflı pasta yapıyor musunuz?', 'Evet. Dilediğiniz fotoğrafı ve yazıyı pastanızın üzerine uyguluyoruz; görseli WhatsApp üzerinden iletmeniz yeterli.'),
       ('Fiyat nasıl belirleniyor?', 'Fiyat; kişi sayısına, seçtiğiniz lezzete ve tasarımın detayına göre değişir. Formu gönderdikten sonra şubemiz size net fiyat bilgisi verir.'),
       ('Alerji veya özel isteklerimi belirtebilir miyim?', 'Elbette. Notlar alanına yazdığınız tüm bilgileri ustalarımız dikkate alır; içerikler hakkında şubemizden detaylı bilgi alabilirsiniz.')]
fq = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
order = hero(R, 'Özel sipariş', 'Hayalinizdeki pasta, ustalarımızın ellerinde.', 'Doğum günü, nişan, kutlama… Formu doldurun, seçtiğiniz şubemiz tasarımı ve fiyatı sizinle netleştirsin.', 'products/sippas.jpg') + f'''
<section class="sec wrap two"><form id="of" class="form"><h2>Sipariş formu</h2><p class="hint">Yıldızlı alanlar zorunludur.</p>
<label>Ad Soyad *<input name="ad" required></label><label>Telefon *<input name="tel" type="tel" required></label>
<label>Teslim alacağınız şube *<select name="sube" required>{bo}</select></label><div class="r2"><label>Teslim tarihi *<input name="tarih" type="date" required></label><label>Teslim saati<input name="saat" type="time"></label></div>
<label>Ürün *<select name="urun" required>{opt(['Tasarım Pasta (fotoğraflı / yazılı)', 'Şeker Hamurlu Tasarım Pasta', 'Günlük Pasta', 'Tatlı / Baklava Tepsisi', 'Paket Dondurma', 'Diğer'])}</select></label>
<div class="r2"><label>Özel gün<select name="gun">{opt(['Doğum günü', 'Nişan / Söz', 'Düğün', 'Yıl dönümü', 'Kutlama / Organizasyon', 'Diğer'])}</select></label><label>Kişi sayısı *<input name="kisi" type="number" min="1" required></label></div>
<label>Lezzet tercihi<input name="lezzet"></label><label>Pasta üzerine yazı<input name="yazi"></label><label>Tasarım ve notlarınız<textarea name="not" rows="4"></textarea></label>
<p class="hint">Gönder'e bastığınızda bilgileriniz seçtiğiniz şubenin WhatsApp hattına hazır mesaj olarak aktarılır. Örnek fotoğrafı oradan iletebilirsiniz.</p><button class="btn" type="submit">WhatsApp ile Gönder</button></form>
<div class="duo4">{img(R, 'robloxp.jpg', 'Roblox temalı doğum günü pastası')}{img(R, 'products/sippas.jpg', 'Çiçekli katlı tasarım pasta')}{img(R, 'products/sekerpas.jpg', 'Şeker hamurlu pasta')}{img(R, 'covers/pembe-pasta.jpg', 'Pembe çikolatalı, frambuazlı pasta')}</div></section>
<section class="sec wrap narrow"><h2>Sık sorulanlar</h2>{fq}</section>'''
write('ozel-siparis/index.html', page(1, 'ozel-siparis', 'Özel Sipariş – Tasarım ve Doğum Günü Pastası | Tat Pastanesi', "Ankara'da doğum günü, nişan ve kutlamalarınız için tasarım pasta, şeker hamurlu pasta ve tatlı siparişi. Formu doldurun, ustalarımız size dönsün.", order))

# ---------- ŞUBELER ----------
bl = ''
for i, b in enumerate(B, 1):
    mp = up.quote(b[6])
    bl += f'''<article class="branch" id="{b[0]}">{img(R, b[7] or 'neden1.jpg', 'Tat Pastanesi ' + b[1] + ' şubesi')}<div><small>0{i}</small><h2>{b[1]}</h2><p class="kick">{b[2]}</p>
<dl><dt>Adres</dt><dd>{b[3]}</dd><dt>Telefon</dt><dd>{b[4]}</dd><dt>Çalışma saatleri</dt><dd>Her gün {HOURS}</dd></dl>
<p><a class="btn sm" href="https://www.google.com/maps/search/?api=1&amp;query={mp}">Yol Tarifi Al</a> <a class="btn ghost sm" href="{tel(b[4])}">Ara</a> <a class="btn ghost sm" href="https://wa.me/{b[5]}">WhatsApp</a></p>
<button class="maptog btn ghost sm" data-q="{mp}">Haritayı göster</button></div></article>'''
sub = hero(R, 'Mekanlarımız', 'Size en yakın lezzet noktası', f"Ankara'da 5 şubemizle her gün {HOURS} arası hizmetinizdeyiz.", 'baglica.jpg', '<p class="tabs-i">' + ''.join(f'<a class="btn ghost sm" href="#{b[0]}">{b[1]}</a> ' for b in B) + '</p>') + f'<div class="wrap">{bl}</div>'
write('subelerimiz/index.html', page(1, 'subelerimiz', 'Şubelerimiz – Batıkent, Çakırlar, Bağlıca, Eryaman | Tat Pastanesi', 'Tat Pastanesi şubeleri: Batıkent, Çakırlar, Bağlıca, Eryaman Concept ve Eryaman Rada Park. Adres, telefon, çalışma saatleri ve yol tarifi.', sub))

# ---------- HAKKIMIZDA ----------
about = hero(R, 'Hikayemiz', 'Lezzet ve kalitenin zirvesi', "2001'den bu yana aynı özen, aynı tutku ve kuşaktan kuşağa aktarılan reçetelerle.", 'batikent.jpg') + f'''
<section class="sec wrap two">{img(R, 'neden1.jpg', 'Ustalarımız dondurma hazırlarken', 'tall')}<div><p class="kick">Kuruluş 2001</p><blockquote class="q">“Amacımız yalnızca tatlı sunmak değil; keyifle vakit geçirebileceğiniz sıcak ve samimi bir buluşma noktası olmak.”</blockquote>
<p>Tat Dondurma & Pastaneleri, 2001 yılından bu yana lezzet ve kaliteyi bir araya getirerek misafirlerine hizmet veren bir markadır. Kurulduğumuz ilk günden itibaren amacımız; misafirlerimize yalnızca tatlı ürünler sunmak değil, aynı zamanda keyifle vakit geçirebilecekleri sıcak ve samimi bir ortam oluşturmaktır.</p>
<p>Yıllar içinde edindiğimiz tecrübe ve ustalıkla, geleneksel pastane kültürünü modern dokunuşlarla birleştiriyoruz. Pastalarımız, dondurmalarımız ve tatlılarımız; tazelik, kalite ve özen anlayışıyla, hem göze hem damağa hitap edecek şekilde hazırlanıyor.</p>
<p>Misafirlerimizin güveni ve memnuniyetiyle büyüyen Tat, bugün Ankara'da beş şubesiyle aynı özen ve kalite anlayışıyla hizmet vermeye devam ediyor.</p></div></section>
<section class="sec wrap two2"><article class="card"><h2>Misyonumuz</h2><p>Kaliteli malzemeler, hijyenik üretim ve ustalıkla hazırlanan ürünlerle misafirlerimize her zaman taze ve lezzetli seçenekler sunmak. Geleneksel pastane kültürünü modern sunumlarla birleştirerek güvenilir ve kaliteli bir buluşma noktası olmak.</p></article>
<article class="card"><h2>Vizyonumuz</h2><p>Lezzet, kalite ve müşteri memnuniyetini temel alarak pastane sektöründe güvenilir ve tercih edilen markalar arasında yer almak; hizmet anlayışımızı sürekli geliştirerek daha geniş kitlelere ulaşan güçlü bir marka olmak.</p></article></section>
<section class="wrap">{STATS}</section>
<section class="sec dark"><div class="wrap two"><div><p class="kick">Özel günlerinizde</p><h2>Tatlı anılar biriktirin.</h2><p>Doğum günlerinden nişanlara, küçük kutlamalardan büyük organizasyonlara; sevdiklerinizle paylaşacağınız her anı, size özel hazırlanan lezzetlerle taçlandırıyoruz.</p><a class="btn" href="../ozel-siparis/">Özel Sipariş Ver</a></div>
<div class="duo">{img(R, 'robloxp.jpg', 'Doğum günü pastası')}{img(R, 'products/sippas.jpg', 'Katlı tasarım pasta')}</div></div></section>'''
write('hakkimizda/index.html', page(1, 'hakkimizda', "Hakkımızda – 2001'den Beri Lezzet ve Kalite | Tat Pastanesi", "Tat Dondurma & Pastaneleri 2001'den bu yana geleneksel pastane kültürünü modern dokunuşlarla birleştirerek Ankara'da hizmet veriyor.", about))

# ---------- İLETİŞİM ----------
cl = ''.join(f'<article class="bc"><h3>{b[1]}</h3><p>{b[3]}</p><p><b>{b[4]}</b></p><div><a class="btn sm" href="{tel(b[4])}">Ara</a> <a class="btn ghost sm" href="https://wa.me/{b[5]}">WhatsApp</a> <a class="btn ghost sm" href="https://www.google.com/maps/search/?api=1&amp;query={up.quote(b[6])}">Yol tarifi</a></div></article>' for b in B)
cont = f'''<section class="sec wrap"><p class="kick">Bizimle iletişime geçin</p><h1>Bir telefon kadar yakınız.</h1><p class="lead2">Özel siparişleriniz, sorularınız ve önerileriniz için size en yakın şubemize ulaşabilirsiniz.</p>
<p><a class="btn" href="../ozel-siparis/">Pasta Siparişi Ver</a> <a class="btn ghost" href="../menu/">Dijital Menü</a></p><div class="bg5">{cl}</div>
<div class="hrs"><h3>Çalışma saatleri</h3><b>{HOURS}</b><p>Tüm şubelerimizde, haftanın her günü.</p><p><a class="btn ghost sm" href="{IG}">Instagram @tatdondurma.pastanesi</a> <a class="btn ghost sm" href="{GMAPS}">Bizi Google'da değerlendirin</a></p></div></section>'''
write('iletisim/index.html', page(1, 'iletisim', 'İletişim | Tat Pastanesi', 'Tat Pastanesi şubelerinin telefon, WhatsApp, Instagram ve adres bilgileri. Özel siparişleriniz ve sorularınız için bize ulaşın.', cont))

# ---------- CSS ----------
CSS = r''':root{--ink:#1c120e;--ch:#2b1b14;--cream:#f7f0e6;--cream2:#efe3d2;--gold:#c8924a;--rasp:#a8404f;--mut:#7a6659;--r:14px}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:84px}body{margin:0;font:400 17px/1.6 "Instrument Sans",system-ui,sans-serif;background:var(--cream);color:var(--ink)}
h1,h2,h3{font-family:Fraunces,Georgia,serif;line-height:1.1;margin:0 0 .5em}h1{font-size:clamp(2.6rem,7vw,5.4rem);font-weight:700}h2{font-size:clamp(1.9rem,4vw,3rem)}h3{font-size:1.25rem}
a{color:inherit}img{max-width:100%}.wrap{width:min(1180px,92%);margin:auto}.skip{position:absolute;left:-999px}.skip:focus{left:8px;top:8px;background:#fff;padding:8px;z-index:99}
:focus-visible{outline:3px solid var(--gold);outline-offset:3px}
.hd{position:sticky;top:0;z-index:30;display:flex;align-items:center;gap:20px;padding:10px 4%;background:rgba(28,18,14,.94);backdrop-filter:blur(8px);color:#f7f0e6}
.logo img{height:46px;display:block}.logo{font:700 1.6rem Fraunces,serif;text-decoration:none}.nav{display:flex;gap:26px;margin-left:auto}.nav a{text-decoration:none;opacity:.85}.nav a:hover,.nav [aria-current]{opacity:1;color:var(--gold)}
.hd-r{display:flex;gap:8px;align-items:center}.burger{display:none;background:none;border:0;width:40px;height:40px}.burger i{display:block;height:2px;background:#f7f0e6;margin:7px 8px}
.mnav{position:fixed;inset:64px 0 0;background:var(--ink);color:#f7f0e6;z-index:29;padding:24px 6%;overflow:auto}.mnav:not([hidden]){display:flex;flex-direction:column;gap:6px}.mnav a{font:600 1.6rem Fraunces,serif;padding:10px 0;text-decoration:none;border-bottom:1px solid #fff2}
.btn{display:inline-block;padding:.8em 1.5em;border-radius:99px;background:var(--gold);color:var(--ink);font-weight:600;text-decoration:none;border:2px solid var(--gold);cursor:pointer;font-size:1rem;font-family:inherit}.btn:hover{filter:brightness(1.08)}
.btn.ghost{background:transparent;color:inherit;border-color:currentColor}.btn.sm{padding:.45em 1.1em;font-size:.92rem}
.kick{color:var(--rasp);font-weight:600;margin:0 0 .6em}.dark .kick,.hero .kick,.ph-hero .kick,.mhero .kick{color:var(--gold)}
.ph{display:block;background:linear-gradient(135deg,#d8b98e,#a8404f55 70%,#7a5a3a);overflow:hidden;border-radius:var(--r);aspect-ratio:4/3}.ph img{width:100%;height:100%;object-fit:cover;display:block}.ph.tall{aspect-ratio:4/5}
.hero,.ph-hero,.mhero{position:relative;background:var(--ink);color:#f7f0e6;overflow:hidden}.hero{min-height:88vh;display:flex;align-items:center}.ph-hero{padding:90px 0 70px}.mhero{min-height:100vh;display:flex;align-items:center;text-align:center}
.ph.bg{position:absolute;inset:0;border-radius:0;aspect-ratio:auto;opacity:.38}.hero .wrap,.ph-hero .wrap,.mhero .wrap{position:relative}.lead{font-size:1.2rem;max-width:34em;opacity:.9}.meta{opacity:.8;margin-top:2em}.meta a{margin-right:1em;color:var(--gold)}
.mq{background:var(--gold);color:var(--ink);overflow:hidden;white-space:nowrap;font:600 1.05rem Fraunces,serif;padding:14px 0}.mq div{display:inline-block;animation:mq 30s linear infinite}.mq span{margin:0 28px}@keyframes mq{to{transform:translateX(-50%)}}
.sec{padding:84px 0}.dark{background:var(--ink);color:#f7f0e6}.cream2{background:var(--cream2)}.two{display:grid;grid-template-columns:1fr 1fr;gap:56px;align-items:center}.two2{display:grid;grid-template-columns:1fr 1fr;gap:24px}.narrow{max-width:820px}
.more{display:inline-block;margin:0 0 28px;color:var(--rasp);font-weight:600}.vg{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}.vc{position:relative;text-decoration:none;border-radius:var(--r);overflow:hidden;background:var(--ch);color:#f7f0e6;display:block}
.vc .ph{border-radius:0;aspect-ratio:5/4;transition:transform .5s}.vc:hover .ph{transform:scale(1.04)}.vc strong{display:block;font:700 1.4rem Fraunces,serif;padding:14px 18px 0}.vc span:last-child{display:block;padding:0 18px 16px;opacity:.75}
.q{font:500 clamp(1.4rem,3vw,2rem)/1.3 Fraunces,serif;margin:0 0 1.2em}.q cite{display:block;font:400 1rem "Instrument Sans";opacity:.7;margin-top:.8em}.tags{display:flex;flex-wrap:wrap;gap:8px}.tags a{border:1px solid #fff4;border-radius:99px;padding:.3em .9em;text-decoration:none;font-size:.92rem}.tags a:hover{border-color:var(--gold);color:var(--gold)}
.cone{background:#fff;border-radius:var(--r);padding:24px;margin-top:24px}.cone h3{font-size:1.6rem;color:var(--rasp);min-height:1.2em}.hint{color:var(--mut);font-size:.92rem}.chips{display:flex;flex-wrap:wrap;gap:8px;max-height:230px;overflow:auto;margin-top:12px}
.chip{border:1.5px solid #d9c7b0;background:var(--cream);border-radius:99px;padding:.3em .9em;font:inherit;font-size:.92rem;cursor:pointer}.chip[aria-pressed=true]{background:var(--rasp);border-color:var(--rasp);color:#fff}
.duo,.duo4{display:grid;gap:14px}.duo{grid-template-columns:1fr 1fr}.duo .ph:nth-child(2){margin-top:40px}.duo3{display:grid;grid-template-columns:1fr 1fr;gap:14px}.duo3 .ph:first-child{grid-row:span 2;aspect-ratio:auto;min-height:100%}.duo4{grid-template-columns:1fr 1fr}
.steps{list-style:none;padding:0;margin:0 0 28px;counter-reset:s}.steps li{padding:0 0 18px 64px;position:relative}.steps b{position:absolute;left:0;top:0;width:44px;height:44px;border-radius:50%;background:var(--rasp);color:#fff;display:grid;place-items:center;font:700 1.2rem Fraunces}.steps h3{margin-bottom:.15em}.steps p{margin:0}
.vals{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin:32px 0 56px}.val small{color:var(--rasp);font-weight:600}.val .ph{aspect-ratio:3/2;margin-bottom:14px}
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center;margin-top:20px}.stats div{background:var(--ink);color:var(--cream);border-radius:var(--r);padding:26px 10px;font-size:.95rem}.stats b{display:block;font:700 2.6rem Fraunces;color:var(--gold)}
.revs{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:20px}blockquote{margin:0}.revs blockquote{background:var(--ch);padding:26px;border-radius:var(--r)}.revs cite{display:block;font-style:normal;margin-top:14px}.revs cite b{display:inline-grid;place-items:center;width:36px;height:36px;border-radius:50%;background:var(--gold);color:var(--ink);margin-right:10px}.revs small{display:block;opacity:.6;margin-left:46px}
.bg5{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:20px;margin-top:20px}.bc{background:#fff;border-radius:var(--r);padding:24px;border:1px solid #e6d7c3}.bc p{color:var(--mut)}.bc div{display:flex;gap:8px;flex-wrap:wrap}
.tabs{position:sticky;top:66px;z-index:20;background:var(--cream);border-bottom:1px solid #e0d0ba}.tabs .wrap{display:flex;gap:6px;align-items:center;overflow-x:auto;padding:10px 0}.tabs a{white-space:nowrap;padding:.4em 1em;border-radius:99px;text-decoration:none}.tabs a:hover{background:var(--cream2)}.tabs input{margin-left:auto;min-width:160px;padding:.5em 1em;border:1.5px solid #d9c7b0;border-radius:99px;font:inherit;background:#fff}
.lead2{max-width:40em;color:var(--mut)}.pg{list-style:none;padding:0;margin:28px 0;display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:20px}.item h3{margin:.6em 0 .2em;font-size:1.1rem}.item p{margin:0;color:var(--mut);font-size:.93rem}.sub{margin-top:36px}.pills{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:8px}.pills li{background:#fff;border:1px solid #e0d0ba;border-radius:99px;padding:.25em .9em;font-size:.93rem}
.cta{text-align:center}.form{background:#fff;border-radius:var(--r);padding:32px;display:grid;gap:14px}.form label{display:grid;gap:4px;font-weight:600;font-size:.95rem}.form input,.form select,.form textarea{font:inherit;padding:.65em .8em;border:1.5px solid #d9c7b0;border-radius:10px;background:var(--cream)}.r2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
details{border-bottom:1px solid #d9c7b0;padding:16px 0}summary{font:600 1.15rem Fraunces,serif;cursor:pointer}details p{color:var(--mut);margin:.6em 0 0}
.branch{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center;padding:56px 0;border-bottom:1px solid #e0d0ba}.branch:nth-child(even) .ph{order:2}.branch small{color:var(--rasp);font-weight:600}dt{font-weight:600;margin-top:.8em}dd{margin:0;color:var(--mut)}.branch iframe{width:100%;height:300px;border:0;border-radius:var(--r);margin-top:14px}
.card{background:#fff;border-radius:var(--r);padding:32px}.hrs{background:var(--ink);color:var(--cream);border-radius:var(--r);padding:32px;margin-top:32px}.hrs b{font:700 2.4rem Fraunces;color:var(--gold)}
.mhero h1{margin:.3em 0}.mlogo{height:90px}.lang{position:absolute;right:0;top:-70px}.lang button{background:none;border:1.5px solid #fff6;color:#fff;padding:.3em .9em;border-radius:99px;cursor:pointer}.lang .on{background:var(--gold);color:var(--ink);border-color:var(--gold)}
.msec{padding:36px 0 0}.msec ul{list-style:none;padding:0;margin:0}.msec li{display:flex;justify-content:space-between;gap:16px;padding:10px 0;border-bottom:1px dotted #bba98f}.msec b{color:var(--rasp)}.note{color:var(--mut);padding:36px 0 90px}
.ft{background:var(--ink);color:#d9c9b6;padding:64px 4% 90px}.ft-g{display:grid;grid-template-columns:2fr 1fr 1fr;gap:40px;max-width:1180px;margin:auto}.ft h3{color:var(--cream)}.ft ul{list-style:none;padding:0}.ft li{margin:.4em 0}.ft li a{margin-left:10px;color:var(--gold)}.ft-logo{height:56px}.ft-c{text-align:center;margin-top:40px;opacity:.6;font-size:.9rem}
.dock{display:none}@media(max-width:860px){.nav,.hd-r .btn.ghost{display:none}.burger{display:block}.hd-r{margin-left:auto}.two,.two2,.branch,.ft-g,.vals,.revs{grid-template-columns:1fr}.vg{grid-template-columns:1fr 1fr}.stats{grid-template-columns:1fr 1fr}.branch:nth-child(even) .ph{order:0}.sec{padding:56px 0}
.dock{display:flex;position:fixed;bottom:0;left:0;right:0;z-index:25;background:var(--ink);padding:8px 10px;gap:8px}.dock a{flex:1;text-align:center;padding:.6em;color:#fff;text-decoration:none;border:1px solid #fff3;border-radius:99px}.dock .wa{background:#25d366;color:#04210f;border-color:#25d366;font-weight:600}.tabs{top:56px}}
@media(max-width:520px){.vg{grid-template-columns:1fr}}@media(prefers-reduced-motion:reduce){.mq div{animation:none}*{scroll-behavior:auto!important}}
'''
JS = r'''(function(){var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))},R=document.body.dataset.root||'';
var bg=$('.burger'),mn=$('.mnav');bg.onclick=function(){var o=mn.hidden;mn.hidden=!o;bg.setAttribute('aria-expanded',o)};
// külah oluşturucu
var cone=$('.cone');if(cone){var sel=['Antep Fıstıklı','Vişne'],t=$('#cone-t');var draw=function(){$$('.chip',cone).forEach(function(c){c.setAttribute('aria-pressed',sel.indexOf(c.textContent)>-1)});t.textContent=sel.join(' · ')||'Bir çeşit seç'};
$$('.chip',cone).forEach(function(c){c.onclick=function(){var i=sel.indexOf(c.textContent);if(i>-1)sel.splice(i,1);else{if(sel.length>=3)sel.shift();sel.push(c.textContent)}draw()}});draw()}
// ürün arama
var q=$('#q');if(q){q.oninput=function(){var v=q.value.toLocaleLowerCase('tr');$$('.prodsec').forEach(function(s){var any=0;$$('.item,.pills li',s).forEach(function(i){var m=i.textContent.toLocaleLowerCase('tr').indexOf(v)>-1;i.hidden=!m;if(m)any=1});s.hidden=!any})};if(/ara/.test(location.search))q.focus()}
// harita
$$('.maptog').forEach(function(b){b.onclick=function(){var f=b.parentNode.querySelector('iframe');if(f){f.remove();b.textContent='Haritayı göster'}else{f=document.createElement('iframe');f.loading='lazy';f.title='Harita';f.src='https://www.google.com/maps?q='+b.dataset.q+'&output=embed';b.before(f);b.textContent='Haritayı gizle'}}});
// menü dil
$$('.lang button').forEach(function(b){b.onclick=function(){$$('.lang button').forEach(function(x){x.classList.toggle('on',x===b)});document.documentElement.lang=b.dataset.l;$$('[data-tr]').forEach(function(e){e.textContent=e.dataset[b.dataset.l]})}});
// sipariş formu -> WhatsApp
var f=$('#of');if(f)f.onsubmit=function(ev){ev.preventDefault();var d=new FormData(f),g=function(k){return(d.get(k)||'').trim()};
var m='Merhaba, özel sipariş vermek istiyorum.\n\nAd Soyad: '+g('ad')+'\nTelefon: '+g('tel')+'\nÜrün: '+g('urun')+'\nÖzel gün: '+g('gun')+'\nKişi sayısı: '+g('kisi')+'\nTeslim: '+g('tarih')+' '+g('saat')+'\nLezzet: '+g('lezzet')+'\nYazı: '+g('yazi')+'\nNot: '+g('not');
window.open('https://wa.me/'+g('sube')+'?text='+encodeURIComponent(m),'_blank')};
})();'''
write('assets/style.css', CSS)
write('assets/main.js', JS)
write('README.md', '# Tat Pastanesi\nStatik site (GitHub Pages uyumlu). Görselleri `images/` klasörüne koyun (dosya adları sayfalarda kullanılanlarla aynı). İçerik/şube/ürün verileri `build.py` içindedir; `python build.py` ile yeniden üretilir.\n')
shutil.copy(__file__, f'{OUT}/build.py')
shutil.make_archive('/mnt/user-data/outputs/tatpastanesi', 'zip', OUT)
print('ok')
