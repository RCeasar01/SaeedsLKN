import os

files = ['index.html','menu.html','daily-specials.html','events.html','contact.html','gallery.html']
base = r'E:\Documents\GitHub\SaeedsLKN' + '\\'

mobile_css = """
        .hamburger { display: none; flex-direction: column; gap: 5px; cursor: pointer; background: none; border: none; padding: 8px; }
        .hamburger span { display: block; width: 24px; height: 2px; background: #fff; border-radius: 2px; }
        @media (max-width: 860px) {
            .nav-links { display: none; flex-direction: column; position: absolute; top: 68px; left: 0; right: 0; background: rgba(0,0,0,0.97); padding: 0.5rem 0; z-index: 300; }
            .nav-links.open { display: flex; }
            .nav-links a { line-height: 1; padding: 1rem 2rem; border-bottom: 1px solid #222; }
            .nav-cta { display: none; }
            .hamburger { display: flex; }
        }"""

hamburger_btn = '        <button class="hamburger" aria-label="Menu" onclick="document.getElementById(\'navLinks\').classList.toggle(\'open\')"><span></span><span></span><span></span></button>\n'

for fname in files:
    path = base + fname
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('    </style>', mobile_css + '\n    </style>', 1)
    html = html.replace('<div class="nav-links">', '<div class="nav-links" id="navLinks">', 1)
    html = html.replace('</nav>', hamburger_btn + '    </nav>', 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Updated {fname}')

print('Done')
