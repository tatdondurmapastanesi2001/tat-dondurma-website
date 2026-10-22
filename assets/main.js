(function(){var $=function(s,c){return(c||document).querySelector(s)},$$=function(s,c){return[].slice.call((c||document).querySelectorAll(s))},R=document.body.dataset.root||'';
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
})();