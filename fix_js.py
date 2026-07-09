import re

with open('src/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace(
    'class="font-medium ${indent > 0 ? \'text-slate-600 bg-white shadow-[0_2px_8px_rgba(0,0,0,0.02)] border border-slate-100 py-2 px-3 rounded-lg mt-2\' : \'\'}" class="${indent > 0 ? `ml-[${indent}px]` : \'\'}"',
    'class="font-medium ${indent > 0 ? `text-slate-600 bg-white shadow-[0_2px_8px_rgba(0,0,0,0.02)] border border-slate-100 py-2 px-3 rounded-lg mt-2 ml-[${indent}px]` : \'\'}"'
)

with open('src/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
