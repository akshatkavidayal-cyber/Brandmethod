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

const analyticsBanner=document.querySelector('[data-analytics-consent]');
const analyticsChoice=localStorage.getItem('brand_method_analytics');
if(analyticsBanner&&!analyticsChoice)analyticsBanner.hidden=false;
document.querySelector('[data-analytics-allow]')?.addEventListener('click',()=>{
  localStorage.setItem('brand_method_analytics','granted');
  window.loadBrandMethodAnalytics?.();
  analyticsBanner.hidden=true;
});
document.querySelector('[data-analytics-decline]')?.addEventListener('click',()=>{
  localStorage.setItem('brand_method_analytics','denied');
  analyticsBanner.hidden=true;
});
document.querySelector('[data-analytics-reset]')?.addEventListener('click',()=>{
  localStorage.removeItem('brand_method_analytics');
  if(analyticsBanner)analyticsBanner.hidden=false;
});
