(function(){
var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))};
var R=document.body.dataset.root||'',page=document.body.dataset.page,root=document.documentElement;
var BR=[['Batıkent','0554 172 78 08','905541727808'],['Çakırlar','0536 631 50 11','905366315011'],['Bağlıca','0501 123 55 06','905011235506'],['Eryaman Concept','0543 684 56 72','905436845672'],['Eryaman Rada Park','0501 370 19 06','905013701906']];
var WA={batikent:BR[0][2],cakirlar:BR[1][2],baglica:BR[2][2],'eryaman-concept':BR[3][2],'eryaman-rada-park':BR[4][2]};
// giriş animasyonu bir kez
try{if(sessionStorage.getItem('ti'))root.classList.add('intro-seen');else sessionStorage.setItem('ti','1')}catch(e){}
// reveal
var io='IntersectionObserver' in window?new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('is-visible');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'}):null;
$$('.reveal,.reveal-mask').forEach(function(el){io?io.observe(el):el.classList.add('is-visible')});
// header
var hd=$('header'),last=0;function sc(){var y=window.scrollY;if(hd)hd.classList.toggle('is-scrolled',y>40);
 if(page==='urunlerimiz'){if(y>last&&y>420)root.setAttribute('data-header-hidden','');else if(y<last)root.removeAttribute('data-header-hidden')}last=y}
addEventListener('scroll',sc,{passive:true});sc();
// mobil menü
var mm=$('#mobile-menu'),bt=hd&&$('button[aria-controls=mobile-menu]');
if(mm&&bt){$$('.menu-item',mm).forEach(function(l,i){l.style.setProperty('--d',(.15+i*.06)+'s')});
 var tog=function(o){mm.dataset.open=o;o?mm.removeAttribute('inert'):mm.setAttribute('inert','');bt.setAttribute('aria-expanded',o);bt.setAttribute('aria-label',o?'Menüyü kapat':'Menüyü aç');document.body.style.overflow=o?'hidden':''};
 bt.onclick=function(){tog(mm.dataset.open!=='true')};$$('a',mm).forEach(function(a){a.addEventListener('click',function(){tog(false)})});
 addEventListener('keydown',function(e){if(e.key==='Escape')tog(false)});var sp=bt.querySelectorAll('span span');
 new MutationObserver(function(){var o=mm.dataset.open==='true';if(sp.length===3){sp[0].style.transform=o?'translateY(6px) rotate(45deg)':'';sp[1].style.opacity=o?0:'';sp[2].style.transform=o?'translateY(-6px) rotate(-45deg)':''}}).observe(mm,{attributes:true})}
// Ara (arama) menüsü
var ab=hd&&$('button[aria-haspopup=menu]');
if(ab){var cm=document.createElement('div');cm.className='call-menu';cm.hidden=true;cm.innerHTML=BR.map(function(b){return '<a href="tel:+9'+b[1].replace(/ /g,'')+'">'+b[0]+'<span>'+b[1]+'</span></a>'}).join('');ab.parentNode.appendChild(cm);
 ab.onclick=function(e){e.stopPropagation();cm.hidden=!cm.hidden;ab.setAttribute('aria-expanded',!cm.hidden)};document.addEventListener('click',function(){cm.hidden=true;ab.setAttribute('aria-expanded','false')})}
// külah oluşturucu
var kc=$('#kulah');
if(kc){var svg=$('svg',kc),chips=$$('button[aria-pressed]',kc),h3=$('h3',kc),sel=chips.filter(function(c){return c.getAttribute('aria-pressed')==='true'});
 var col=function(c){return c.querySelector('span').style.background||'#ccc'};
 var draw=function(fresh){var g=$$('g',svg);g.forEach(function(x){x.remove()});
  sel.forEach(function(c,i){var cy=130-40*i,k=col(c),s=document.createElementNS('http://www.w3.org/2000/svg','g');s.style.transformOrigin='100px '+cy+'px';if(fresh&&i===sel.length-1)s.style.animation='scoop .5s cubic-bezier(.2,.8,.2,1)';
   s.innerHTML='<circle cx="100" cy="'+cy+'" r="46" fill="'+k+'"></circle><path d="M54 '+(cy+10)+' q11.5 16 23 0 q11.5 16 23 0 q11.5 16 23 0 q11.5 16 23 0" fill="'+k+'"></path><ellipse cx="82" cy="'+(cy-18)+'" rx="12" ry="7" fill="#fff" opacity="0.28"></ellipse>';svg.appendChild(s)});
  chips.forEach(function(c){c.setAttribute('aria-pressed',sel.indexOf(c)>-1)});var n=sel.map(function(c){return c.textContent.trim()});h3.textContent=n.join(' · ')||'Bir lezzet seç';svg.setAttribute('aria-label','Külahınız: '+n.join(', '))};
 chips.forEach(function(c){c.onclick=function(){var i=sel.indexOf(c);if(i>-1)sel.splice(i,1);else{if(sel.length>=3)sel.shift();sel.push(c)}draw(i<0)}});draw(false)}
// ürünler: arama + ürün sayfası (sheet)
var q=$('input[type=search]');
if(q&&page==='urunlerimiz'){var secs=$$('section[id]',document.querySelector('main'));q.oninput=function(){var v=q.value.trim().toLocaleLowerCase('tr');secs.forEach(function(s){var n=0;$$('li',s).forEach(function(l){var m=!v||l.textContent.toLocaleLowerCase('tr').indexOf(v)>-1;l.hidden=!m;if(m)n++});s.hidden=!!v&&!n})}
 var dlg=document.createElement('dialog');dlg.className='menu-sheet';document.body.appendChild(dlg);dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()});
 $$('li>button',document.querySelector('main')).forEach(function(b){b.onclick=function(){var im=$('img',b),t=$('h3',b),p=$('p',b);dlg.innerHTML='<button class="x" aria-label="Kapat">×</button>'+(im?'<img src="'+im.currentSrc+'" alt="">':'')+'<div class="sh"><h3>'+t.innerHTML+'</h3><p>'+(p?p.innerHTML:'')+'</p><a class="btn btn-primary" href="'+R+'ozel-siparis/">Pasta Siparişi</a> <a class="btn btn-ghost" style="color:inherit" href="'+R+'menu/">Menü & Fiyatlar</a></div>';$('.x',dlg).onclick=function(){dlg.close()};dlg.showModal()}});
 var tabs=$$('[data-slug]'),spy=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)tabs.forEach(function(t){var on=t.dataset.slug===e.target.id;t.style.background=on?'var(--color-ink)':'';t.style.color=on?'var(--color-cream)':''})})},{rootMargin:'-30% 0px -60% 0px'});secs.forEach(function(s){spy.observe(s)})}
// şube haritası
if(page==='subelerimiz')$$('article').forEach(function(a){var b=$$('button',a).filter(function(x){return/Haritayı göster/.test(x.textContent)})[0],l=$('a[href*="maps/search"]',a);if(!b||!l)return;
 b.onclick=function(){var f=document.createElement('iframe');f.className='map-frame';f.loading='lazy';f.title='Harita';f.src='https://www.google.com/maps?q='+encodeURIComponent(decodeURIComponent(l.href.split('query=')[1]))+'&output=embed';b.replaceWith(f)}});
// özel sipariş -> WhatsApp
var fm=$('main form');
if(fm&&page==='ozel-siparis'){fm.onsubmit=function(e){e.preventDefault();var d=new FormData(fm),v=function(k){return String(d.get(k)||'').trim()},sl=function(k){var el=fm.elements[k];return el&&el.tagName==='SELECT'?el.options[el.selectedIndex].text:v(k)};
 var br=$('input[name=branch]:checked',fm),bn=br?br.parentNode.textContent.trim():'';
 var m='Merhaba, özel sipariş vermek istiyorum.\n\nAd Soyad: '+v('name')+'\nTelefon: '+v('phone')+'\nŞube: '+bn+'\nTeslim: '+v('date')+(v('time')?' '+v('time'):'')+'\nÜrün: '+sl('type')+'\nÖzel gün: '+sl('occasion')+'\nKişi sayısı: '+v('people')+(v('flavor')?'\nLezzet: '+v('flavor'):'')+(v('text')?'\nPasta üzerine yazı: '+v('text'):'')+(v('notes')?'\nNotlar: '+v('notes'):'');
 window.open('https://wa.me/'+WA[br?br.value:'batikent']+'?text='+encodeURIComponent(m),'_blank','noopener')}}
// menü uygulaması
if(page==='menu'){var W=$('#menu-welcome'),C=$('#menu-cats'),L=$('#menu-list'),lang='tr';
 var EN={'Dondurma':'Ice Cream','Yaş Pasta':'Cakes','Sütlü Tatlılar':'Milk Desserts','Kuru Pasta':'Cookies','Waffle':'Waffle','İçecekler':'Drinks','Kategoriler':'Categories','Ne yemek istersiniz?':'What would you like?','Lezzetlerimizi keşfedin':'Discover our flavours',"2001'den beri, her gün taze.":'Since 2001, fresh every day.','Menüyü Görüntüle':'View Menu'};
 var orig=new Map();function tr(){var w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);var n;while(n=w.nextNode()){var t=n.nodeValue.trim();if(!t)continue;if(!orig.has(n)&&(EN[t]||/^\d+ ürün$/.test(t)))orig.set(n,n.nodeValue);if(orig.has(n)){var o=orig.get(n),k=o.trim();n.nodeValue=lang==='en'?(EN[k]||k.replace(' ürün',' items')):o}}}
 var setLang=function(l){lang=l;$$('[role=group][aria-label^=Dil] button').forEach(function(b){b.setAttribute('aria-pressed',b.textContent.trim().toLowerCase()===l)});tr()};
 document.addEventListener('click',function(e){var b=e.target.closest('[role=group][aria-label^=Dil] button');if(b)setLang(b.textContent.trim().toLowerCase())});
 var show=function(x){[W,C,L].forEach(function(s){s.hidden=s!==x});scrollTo(0,0);tr()};
 $$('button,a',W).forEach(function(b){if(/Menüyü Görüntüle/.test(b.textContent)){b.addEventListener('click',function(e){e.preventDefault();show(C)})}});
 var render=function(ci,term){var h='';MENU.forEach(function(c,i){if(ci!=null&&ci!==i)return;var it=c.items.filter(function(x){return!term||(x.n+' '+x.d).toLocaleLowerCase('tr').indexOf(term)>-1});if(!it.length&&term)return;
  h+='<h2>'+(lang==='en'&&EN[c.name]||c.name)+'</h2><ul>'+(it.map(function(x){return'<li>'+(x.i?'<img src="'+x.i+'" alt="">':'')+'<div><b>'+x.n+'</b><span>'+x.d+'</span></div></li>'}).join('')||'<li><span>'+(lang==='en'?'Ask your branch for details.':'Detaylar için şubemize danışın.')+'</span></li>')+'</ul>'});
  $('#ml',L).innerHTML=h+'<p class="note">'+(lang==='en'?'Ask your branch for current prices.':'Güncel fiyatlar için şubemize danışın.')+'</p>'};
 L.innerHTML='<div class="bar"><div class="container-x"><button class="b" id="mb">‹ Menü</button><input id="ms" type="search" placeholder="Ürün ara…" aria-label="Ürün ara"></div></div><div class="container-x" id="ml"></div>';
 var cur=null;$('#mb',L).onclick=function(){show(C)};$('#ms',L).oninput=function(){render(cur,this.value.trim().toLocaleLowerCase('tr'))};
 $$('li>button',C).forEach(function(b,i){b.onclick=function(){cur=i;$('#ms',L).value='';render(i);show(L)}});
 var bk=$('button[aria-label=Menü]',C);if(bk)bk.onclick=function(){show(W)};var sb=$('button[aria-label^="Ürün ara"]',C);if(sb)sb.onclick=function(){cur=null;render(null);show(L);$('#ms',L).focus()}}
})();
