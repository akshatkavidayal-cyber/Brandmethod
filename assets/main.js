document.querySelectorAll('[data-filter]').forEach(button=>{
  button.addEventListener('click',()=>{
    const filter=button.dataset.filter;
    document.querySelectorAll('[data-filter]').forEach(other=>{
      const selected=other===button;
      other.classList.toggle('active',selected);
      other.setAttribute('aria-pressed',String(selected));
    });
    let visible=0;
    document.querySelectorAll('.study-card').forEach(card=>{
      const match=filter==='all'||card.dataset.category===filter;
      card.hidden=!match;
      if(match)visible++;
    });
    const empty=document.querySelector('.filter-empty');
    if(empty)empty.hidden=visible>0;
  });
});
