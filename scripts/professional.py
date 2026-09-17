"""Crawlable professional pages, kept distinct from independent editorial studies."""
from html import escape

P = "/Brandmethod/"


def a(path, label):
    return f'<a href="{P}{path}">{escape(label)} <span aria-hidden="true">↗</span></a>'


def section(kicker, title, content):
    return f'<section class="pro-section"><p class="eyebrow">{kicker}</p><h2>{title}</h2>{content}</section>'


def page(kicker, title, lead, *sections):
    return f'<article class="pro-page"><header class="pro-hero"><p class="eyebrow light">{kicker}</p><h1>{title}</h1><p>{lead}</p></header><div class="pro-content">{"".join(sections)}</div></article>'


def links(*items):
    return '<div class="inline-links">' + ''.join(a(path, label) for path, label in items) + '</div>'


def professional_pages(studies, site):
    result = []
    def add(path, title, description, body): result.append((path, title, description, body))

    add('brand-marketing', 'Brand Marketing, FMCG & Consumer Insight',
        'Akshat Kavidayal on global brand marketing, FMCG, consumer insight, brand equity and integrated communications.',
        page('PRACTICE / BRAND MARKETING', 'The brand has to mean something before it asks to be chosen.',
             'I work at the intersection of consumer understanding, brand strategy and the decisions that make a brand recognizable in everyday life.',
             section('THE PRACTICE', 'From evidence to a brand people can feel', '<p>My background includes global brand marketing around Danone / Activia, consumer research, brand health, competitive benchmarking and communications and influencer strategy. The work is in translating a broad brand ambition into choices people actually notice, remember and understand.</p><p>I am interested in how global direction meets local context, how distinctive brand assets survive across channels, and where the consumer experience contradicts the presentation.</p>'),
             section('EXPLORE', 'Evidence, work and opinions', links(('work/activia-danone/', 'Danone / Activia experience'), ('work/influencer-strategy/', 'Influencer strategy'), ('research/influencer-selection-fmcg/', 'FMCG research'), ('insights/', 'Independent analysis')))))

    add('business-development', 'Business Development, Partnerships & Technology',
        'Akshat Kavidayal on B2B business development, channel partnerships, professional audio, AV and go-to-market strategy.',
        page('PRACTICE / BUSINESS DEVELOPMENT', 'A good partnership has to work after the pitch.',
             'My commercial experience spans professional audio and AV, B2B technology, client development, operations and partnerships.',
             section('THE PRACTICE', 'Where brand promise meets the buying process', '<p>Business development in technology depends on understanding who specifies a product, who buys it, who installs it and who lives with it. That makes channel relationships, clear positioning and practical enablement part of the same problem.</p><p>I bring a marketing lens to go-to-market decisions and a commercial lens to brand decisions. I am especially interested in professional AV and audio, where technical performance and human experience need to make sense together.</p>'),
             section('EXPLORE', 'Related work', links(('work/pro-av/', 'Professional AV experience'), ('work/', 'All professional work'), ('resume/', 'Résumé')))))

    add('work', 'Professional Work & Research',
        'Selected public summaries of Akshat Kavidayal’s brand marketing, influencer research and professional AV experience.',
        page('WORK / SELECTED EXPERIENCE', 'The work behind the questions.',
             'These are public summaries of my professional areas, kept separate from my independent opinions about other brands. They contain no internal data or claimed results.',
             section('01 / FMCG', 'Danone / Activia', '<p>Global brand marketing context: brand equity, consumer understanding and communication choices in FMCG.</p>' + links(('work/activia-danone/', 'Explore the public summary'))),
             section('02 / RESEARCH', 'Influencer strategy', '<p>How brand managers weigh fit, reach and credibility in low-involvement FMCG categories.</p>' + links(('work/influencer-strategy/', 'Explore the work'), ('research/influencer-selection-fmcg/', 'Read the thesis summary'))),
             section('03 / TECHNOLOGY', 'Professional audio & AV', '<p>Business development and channel thinking in technical B2B markets.</p>' + links(('work/pro-av/', 'Explore the public summary')))))

    add('work/activia-danone', 'Danone / Activia: Global Brand Marketing',
        'Public overview of Akshat Kavidayal’s Danone / Activia global brand marketing experience across FMCG brand equity and consumer insight.',
        page('WORK / FMCG / DANONE · ACTIVIA', 'The challenge of keeping a global brand coherent and locally alive.',
             'My experience with Danone / Activia sits within global brand marketing. This page describes the nature of that work at a public level; it does not disclose internal plans, numbers or assets.',
             section('WHAT THE WORK INVOLVES', 'Brand decisions need more than a campaign idea', '<p>The relevant disciplines include brand equity and health, consumer research, competitive and market analysis, integrated communications and influencer strategy. In a global FMCG context, the question is how a brand can stay recognizable while individual markets communicate in ways that feel native to their consumers.</p><p>That is the lens I bring to positioning, communications and consumer insight: look for the decision behind the asset and the behavior it is meant to change.</p>'),
             section('PUBLIC SCOPE', 'What I can show', '<p>I was Global Assistant Brand Manager for Activia at Danone from January to July 2026. My work included brand-health reporting, qualitative consumer research and competitive analysis. This summary stays at the level I can discuss publicly; it does not claim ownership of a particular campaign or disclose internal plans or results.</p>' + links(('brand-marketing/', 'Brand marketing practice'), ('resume/', 'Résumé')))))

    add('work/influencer-strategy', 'Influencer Strategy & FMCG Brand Research',
        'Akshat Kavidayal’s work and research on influencer selection, brand fit and decision-making for low-involvement FMCG brands.',
        page('WORK / INFLUENCER STRATEGY', 'The best creator is rarely just the biggest one.',
             'Influencer selection becomes a brand decision when reach, fit, credibility and the category’s buying behavior pull in different directions.',
             section('THE RESEARCH QUESTION', 'How do brand managers actually choose?', '<p>My MSc thesis examines strategic influencer selection and brand manager decision-making in low-involvement FMCG categories. The useful tension is between what is easy to measure and what is right for the brand. A large audience is one input, but a creator’s cultural fit, trust and ability to make a product feel relevant matter too.</p>'),
             section('HOW I APPLY THE LENS', 'A more useful brief', '<p>Start with the brand’s intended association and the consumer behavior in the category. Then assess creators for audience relevance, brand fit, content credibility and the role they can play in an integrated communications system. Treat performance signals as evidence, not as a substitute for judgment.</p>' + links(('research/influencer-selection-fmcg/', 'Research summary'), ('brand-marketing/', 'Brand marketing practice')))))

    add('work/pro-av', 'Professional Audio & AV Business Development',
        'Public overview of Akshat Kavidayal’s business development experience in professional audio, audiovisual and B2B technology.',
        page('WORK / B2B TECHNOLOGY', 'In professional AV, the route to market is part of the product story.',
             'My background in professional audio and audiovisual technology gives me a practical view of partnerships, channels and commercial strategy.',
             section('THE MARKET', 'More than a buyer and a seller', '<p>Professional AV decisions often involve integrators, distributors, technical specialists and end clients. Good business development means understanding each participant’s incentives and making the value of a solution clear at the point where it is evaluated, specified and used.</p>'),
             section('THE TRANSFERABLE LENS', 'Technical detail, human outcome', '<p>I am interested in go-to-market, client development and channel partnerships that connect technical capability with a real use case. This public summary deliberately excludes client names, commercial terms, performance data and confidential project specifics.</p>' + links(('business-development/', 'Business development practice'), ('resume/', 'Résumé')))))

    add('research/influencer-selection-fmcg', 'Strategic Influencer Selection in FMCG',
        'MSc thesis by Akshat Kavidayal at emlyon business school on brand manager decision-making in low-involvement FMCG influencer selection.',
        page('RESEARCH / MSC THESIS', 'Who gets to represent the brand?',
             '<cite>Strategic Influencer Selection: Brand Manager Decision-Making in Low-Involvement FMCG Brands</cite> is the title of my MSc research at emlyon business school. The qualitative research involved 14 brand, marketing and agency professionals.',
             section('THE CENTRAL QUESTION', 'Fit can be harder to count than reach', '<p>Low-involvement products are often chosen quickly. Influencer choices therefore raise a practical question: how should brand managers weigh audience size against category relevance, brand fit, perceived authenticity and the role of a creator within broader communications?</p><p>This is a public framing of the research topic, not a reproduction of the thesis or a claim about findings that have not been supplied here.</p>'),
             section('FOLLOW THE THREAD', 'From research to practice', links(('work/influencer-strategy/', 'Influencer strategy'), ('brand-marketing/', 'Brand marketing'), ('insights/', 'Related independent essays')))))

    add('resume', 'Résumé | Brand Marketing & Business Development',
        'Searchable professional overview of Akshat Kavidayal: Danone / Activia, FMCG, business development, professional AV and emlyon MSc.',
        page('RÉSUMÉ / AKSHAT KAVIDAYAL', 'Brand Marketing & Business Development',
             'FMCG · Consumer · Technology · Global Marketing · Partnerships · Strategy',
             section('PROFILE', 'Marketing × Consumer × Culture × Technology', '<p>I work across brand marketing, consumer insight and technology. At Danone, I supported global Activia brand work through research, reporting and market analysis. Earlier experience in professional AV, creative projects and recruitment gives me a practical view of how ideas move between people, teams and markets.</p><p>Based in Paris, France.</p>'),
             section('EXPERIENCE', 'Where I have worked', '<ul class="pro-list"><li><strong>Danone — Global Assistant Brand Manager, Activia</strong> · Jan–Jul 2026, Paris. Brand-health reporting, consumer research and cross-market benchmarking.</li><li><strong>Independent — Music, Creative & Event Projects, Deodar</strong> · Nov 2022–Aug 2024, India. Live events, brand activations and an independent electronic-music project.</li><li><strong>Alphatec Audio Video — Application Engineer</strong> · Aug 2019–Nov 2022, New Delhi. Professional AV recommendations, demonstrations and training from pre-sales through handover.</li><li><strong>Wipro Technologies — Talent Acquisition Manager</strong> · Jun 2015–Jun 2018, India. Technology recruitment across India, the UK and the US.</li></ul>'),
             section('EDUCATION & RESEARCH', 'What I studied', '<ul class="pro-list"><li><strong>emlyon business school</strong> — MSc International Marketing & Business Development, Sep 2024–Jul 2026; GPA 4.0. Thesis: <cite>Strategic Influencer Selection: Brand Manager Decision-Making in Low-Involvement FMCG Brands.</cite> Qualitative research with 14 brand, marketing and agency professionals.</li><li><strong>Audio Academy, Bangalore</strong> — Diploma in Live Sound Engineering, Distinction, Jul 2018–Jul 2019.</li><li><strong>Christ University, Bangalore</strong> — BA Economics, Politics & Sociology, May 2012–May 2015.</li></ul>' + links(('research/influencer-selection-fmcg/', 'Research summary'))),
             section('SKILLS & LANGUAGES', 'The working toolkit', '<p>Consumer research, market and competitor analysis, brand health, communications and project coordination. Nielsen, Kantar/Worldpanel, Mintel, Euromonitor, Power BI, Excel and PowerPoint.</p><p>English C2 · French B2 · Hindi native.</p>'),
             section('CONNECT', 'Keep a copy or get in touch', '<div class="inline-links"><a href="/Brandmethod/Akshat_Kavidayal_Public_CV.pdf" download>Download public CV (PDF) ↗</a><a href="mailto:akshatkavidayal@gmail.com">Email Akshat ↗</a></div>' + links(('work/', 'View selected work'), ('contact/', 'Contact Akshat')))))

    cards = ''.join(f'<li><a href="{P}studies/{escape(s["slug"])}.html"><span>{escape(s["brand"])} · {escape(s["industry"])}</span><strong>{escape(s["title"])}</strong><small>{escape(s["dek"])}</small></a></li>' for s in studies)
    add('insights', 'Insights: Independent Brand & Marketing Analysis',
        'Opinion-led independent analysis of campaigns, products, FMCG, consumer culture and brand decisions by Akshat Kavidayal.',
        page('INSIGHTS / THE EDITORIAL ARCHIVE', 'The question behind the campaign.',
             'I write about the brands I love, the products that irritate me and the decisions no one seems to be saying out loud. These essays are independent analysis, not client work.',
             section('THE ARCHIVE', f'{len(studies)} close reads', f'<ul class="insight-list">{cards}</ul>'),
             section('FOLLOW THE THINKING', 'Where the opinions come from', links(('brand-marketing/', 'Brand marketing'), ('business-development/', 'Business development'), ('research/influencer-selection-fmcg/', 'Research')))))

    add('contact', 'Contact Akshat Kavidayal',
        'Connect with Akshat Kavidayal about brand marketing, FMCG, consumer insight, business development and technology partnerships.',
        page('CONTACT / AKSHAT KAVIDAYAL', 'Have a brand question or a role worth talking about?',
             'I welcome conversations about FMCG brand marketing, consumer insight, partnerships and professional AV.',
             section('REACH OUT', 'Start a conversation', f'<div class="inline-links"><a href="mailto:{escape(site["contact_email"])}">{escape(site["contact_email"])} ↗</a><a href="{escape(site["linkedin_url"])}" target="_blank" rel="noopener noreferrer">Connect on LinkedIn ↗</a></div><p>Prefer a résumé first? You can read it here or download the public CV.</p>' + links(('resume/', 'View résumé'), ('work/', 'View work')))))
    return result
