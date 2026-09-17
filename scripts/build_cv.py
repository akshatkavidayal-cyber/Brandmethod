#!/usr/bin/env python3
"""Build the public, employer-neutral CV from verified facts in Akshat's 2026 CV."""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, KeepTogether

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'assets' / 'Akshat_Kavidayal_Public_CV.pdf'
INK = colors.HexColor('#291d37')
ACCENT = colors.HexColor('#a24669')
MUTED = colors.HexColor('#514458')

styles = {
    'section': ParagraphStyle('section', fontName='Helvetica-Bold', fontSize=8.5, leading=11,
        textColor=ACCENT, spaceBefore=13, spaceAfter=5),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=8.7, leading=12.6,
        textColor=INK, spaceAfter=4),
    'role': ParagraphStyle('role', fontName='Helvetica-Bold', fontSize=9, leading=12,
        textColor=INK, spaceBefore=7, spaceAfter=2),
    'small': ParagraphStyle('small', fontName='Helvetica', fontSize=8.2, leading=11.7,
        textColor=MUTED, spaceAfter=3),
    'bullet': ParagraphStyle('bullet', fontName='Helvetica', fontSize=8.4, leading=11.8,
        textColor=INK, leftIndent=11, firstLineIndent=-8, spaceAfter=2),
}


def p(text, style='body'):
    return Paragraph(text, styles[style])


def section(title):
    return p(title.upper(), 'section')


def role(name, date, location, bullets):
    return KeepTogether([
        p(f'{name} <font color="#a24669">| {date}</font>', 'role'),
        p(location, 'small'),
        *[p(f'&#8226; {line}', 'bullet') for line in bullets],
    ])


def header(canvas, doc):
    width, height = A4
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.rect(0, height-93, width, 93, fill=1, stroke=0)
    canvas.setFillColor(colors.HexColor('#f7eee8'))
    canvas.setFont('Helvetica-Bold', 22)
    canvas.drawString(41, height-42, 'AKSHAT KAVIDAYAL')
    canvas.setFillColor(colors.HexColor('#f3b097'))
    canvas.setFont('Helvetica-Bold', 9.5)
    canvas.drawString(41, height-61, 'BRAND MARKETING  |  FMCG  |  CONSUMER INSIGHTS  |  TECHNOLOGY')
    canvas.setFillColor(colors.HexColor('#e8dce8'))
    canvas.setFont('Helvetica', 8.5)
    canvas.drawString(41, height-78, 'Paris, France   |   akshatkavidayal@gmail.com')
    canvas.setStrokeColor(colors.HexColor('#d8c9d9'))
    canvas.line(41, 29, width-41, 29)
    canvas.setFillColor(MUTED)
    canvas.setFont('Helvetica', 7.3)
    canvas.drawString(41, 19, 'akshatkavidayal-cyber.github.io/Brandmethod/   |   linkedin.com/in/akshatkiran')
    canvas.restoreState()


def main():
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, leftMargin=41, rightMargin=41,
                            topMargin=107, bottomMargin=43, title='Akshat Kavidayal | Public CV',
                            author='Akshat Kavidayal')
    story = [
        section('Profile'),
        p('Brand marketing professional with global FMCG experience on Activia at Danone and an MSc in International Marketing &amp; Business Development from emlyon business school. Work spans consumer research, brand health, cross-market analysis, communications, professional AV and technology-facing collaboration.'),
        section('Experience'),
        role('DANONE - Global Assistant Brand Manager, Activia', 'Jan 2026 - Jul 2026',
             'Global HQ, Paris, France', [
                 'Synthesized brand-health and business reporting across markets for global brand discussions.',
                 'Supported qualitative consumer research and translated feedback into a clear story for senior stakeholders.',
                 'Contributed to brand and communications work through competitive and cross-market benchmarking.',
             ]),
        role('INDEPENDENT - Music, Creative &amp; Event Projects, Deodar', 'Nov 2022 - Aug 2024',
             'India', [
                 'Coordinated live events and brand activations across social content, artists, vendors and production.',
                 'Built an independent electronic-music project, including branding, content, outreach, 13+ tracks and several EPs.',
             ]),
        role('ALPHATEC AUDIO VIDEO - Application Engineer', 'Aug 2019 - Nov 2022',
             'New Delhi, India', [
                 'Translated professional AV products and customer needs into recommendations for customers, dealers and commercial teams.',
                 'Delivered product demonstrations and training; supported projects from pre-sales to handover.',
             ]),
        role('WIPRO TECHNOLOGIES - Talent Acquisition Manager', 'Jun 2015 - Jun 2018',
             'India', [
                 'Managed technology recruitment across India, the UK and US with hiring managers and senior stakeholders.',
             ]),
        section('Education & research'),
        p('<b>emlyon business school</b> - MSc International Marketing &amp; Business Development | Sep 2024 - Jul 2026 | GPA 4.0'),
        p('Thesis: Strategic Influencer Selection: Brand Manager Decision-Making in Low-Involvement FMCG Brands. Qualitative research with 14 brand, marketing and agency professionals.', 'small'),
        p('<b>Audio Academy, Bangalore</b> - Diploma in Live Sound Engineering, Distinction | Jul 2018 - Jul 2019'),
        p('<b>Christ University, Bangalore</b> - BA Economics, Politics &amp; Sociology | May 2012 - May 2015'),
        section('Capabilities & tools'),
        p('<b>Brand:</b> consumer research, market and competitor analysis, brand health, communications, cross-market benchmarking. <b>Execution:</b> brand activation, project coordination, stakeholder and agency collaboration. <b>Tools:</b> Nielsen, Kantar/Worldpanel, Mintel, Euromonitor, Power BI, Excel, PowerPoint.'),
        section('Languages'),
        p('English C2  |  French B2  |  Hindi native'),
    ]
    doc.build(story, onFirstPage=header, onLaterPages=header)
    print(OUTPUT)

if __name__ == '__main__':
    main()
