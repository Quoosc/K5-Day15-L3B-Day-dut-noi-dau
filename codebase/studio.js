'use strict';
const $ = id => document.getElementById(id);
const form = document.querySelector('form'), player = document.querySelector('video');
const catalog = new Map();
let active, busy = false;
const seconds = t => t.split(':').reduce((a,b)=>60*a+Number(b),0);
function element(tag,text,cls){
  const e=document.createElement(tag); if(text)e.textContent=text; if(cls)e.className=cls; return e;
}
function edit(){
  $('search').scrollIntoView(); $('question').focus();
}
function clearResult(){
  player.pause();player.removeAttribute('src');player.load();active=null;
  $('result').hidden=true;$('stage').hidden=true;$('choices').replaceChildren();
  $('refine').hidden=true;$('detail').value='';$('status').textContent='';
}
async function loadCatalog(){
  const res=await fetch('/catalog');if(!res.ok)throw Error();
  const videos=await res.json();
  $('counts').textContent=videos.reduce((n,v)=>n+v.count,0)+' đoạn';
  for(const v of videos){
    catalog.set(v.video_id,v);
    $('scope').add(new Option(v.title,v.video_id));
    const card=element('button','','card'),still=element('span','','still');
    const img=element('img');img.src='/frames/'+v.video_id+'.jpg';img.alt='';
    still.append(img,element('span',v.duration,'stamp'));const copy=element('span','','copy');
    copy.append(element('small',v.speaker+' · '+v.count+' đoạn'),element('strong',v.title));
    card.append(still,copy);card.onclick=()=>{if(busy)return;clearResult();$('scope').value=v.video_id;edit()};
    $('cards').append(card);
  }
}
for(const q of ['Vì sao Transformer cần biết thứ tự các từ?','Mounted khác Unmounted ở điểm nào?','Mình chưa hiểu context trong bài nào.']){
  const button=element('button',q);button.onclick=()=>{if(busy)return;clearResult();$('question').value=q;$('scope').value='';edit()};$('examples').append(button);
}
loadCatalog().catch(()=>{$('cards').textContent='Chưa tải được thư viện. Hãy tải lại trang.'});
async function search(clarification=''){
  const question=$('question').value.trim();
  if(!question){edit();return}if(busy)return;busy=true;
  form.setAttribute("aria-busy","true");
  clearResult();$('submit').disabled=true;$('question').readOnly=true;$('scope').disabled=true;
  $('status').textContent='Đang tra transcript và đối chiếu các đoạn phù hợp…';
  try{
    const res=await fetch('/ask',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({question,scope:$('scope').value,clarification})});
    if(!res.ok)throw Error();const r=await res.json();active=r.passage;
    $('result').hidden=false;$('stage').hidden=!active;
    $('heading').textContent=active?'Đoạn nên xem lại':r.choices?'Bạn muốn ôn phần nào?':'Chưa tìm được đoạn phù hợp';
    $('reply').textContent=active?active.refusal||active.title:r.choices?'Chọn ý gần nhất với câu vừa làm sai, hoặc bổ sung chi tiết bên dưới.':r.output;
    for(const topic of r.choices||[]){const b=element('button',topic);b.onclick=()=>search(topic);$('choices').append(b)}
    if(active){
      $('topic').textContent=active.refusal?'Tự đối chiếu trong bài giảng':active.topic;
      $('source').textContent=active.code+' · '+active.start+' – '+active.end;
      $('excerpt').textContent=active.text?'Theo bản ghi đoạn giảng: '+active.text:active.refusal;
      player.src='/media/'+encodeURIComponent(active.video_id)+'#t='+active.seconds;
      const duration=catalog.get(active.video_id)?.duration||active.end;
      $('interval').textContent='Đoạn chọn · '+active.start+' – '+active.end;$('total').textContent=duration;
      $('range').style.left=100*active.seconds/seconds(duration)+'%';
      $('range').style.width=100*(seconds(active.end)-active.seconds)/seconds(duration)+'%';
      $('play').textContent='▶  Xem từ '+active.start;
    }
    const s=r.stats;$('usage').textContent=s.model_calls?s.models.join(', ')+' · '+s.model_calls+' lần gọi · token vào '+s.tokens_in+' / ra '+s.tokens_out:'Tra cứu cục bộ · không gọi model';
    $('status').textContent='Đã tra cứu xong.';$('result').focus();
  }catch{ $('status').textContent='Chưa lấy được gợi ý. Kiểm tra kết nối rồi bấm Tìm đoạn cần ôn để thử lại.' }
  finally{form.removeAttribute("aria-busy");busy=false;$('submit').disabled=false;$('question').readOnly=false;$('scope').disabled=false}
}
form.onsubmit=e=>{e.preventDefault();search()};
$('scope').onchange=clearResult;$('question').oninput=clearResult;
$('play').onclick=async()=>{if(!active)return;try{player.currentTime=active.seconds;await player.play()}catch{$('status').textContent='Video chưa phát được. Hãy thử nút phát trên trình phát.'}};
$('revise').onclick=()=>{$('refine').hidden=false;$('detail').focus()};
$('again').onclick=()=>{const d=$('detail').value.trim();if(d)search(d);else $('detail').focus()};
$('detail').onkeydown=e=>{if(e.key==='Enter')$('again').click()};

$('question').addEventListener('keydown', event => {
  if ((event.ctrlKey || event.metaKey) && event.key === 'Enter' && !event.isComposing) {
    event.preventDefault();
    if (!busy) form.requestSubmit();
  }
});