import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('style="padding: 0.7rem 1.8rem;"', 'class="px-[1.8rem] py-[0.7rem]"')
html = html.replace('class="btn-primary" class="px-[1.8rem] py-[0.7rem]"', 'class="btn-primary px-[1.8rem] py-[0.7rem]"')
# Wait, I can just use regex for this

# Let's handle them specifically
def rep_style(m):
    cls = m.group(1)
    style = m.group(2)
    # manual replacements
    if "padding: 0.7rem 1.8rem;" in style: return f'class="{cls} px-[1.8rem] py-[0.7rem]"'
    if "padding: 0 2rem; border-radius: 1rem;" in style: return f'class="{cls} px-[2rem] py-0 rounded-[1rem]"'
    if "padding: 0.8rem 1.8rem;" in style: return f'class="{cls} px-[1.8rem] py-[0.8rem]"'
    if "padding: 0.7rem 1.4rem;" in style: return f'class="{cls} px-[1.4rem] py-[0.7rem]"'
    if "padding: 0.8rem 1.8rem; background-color: #071321;" in style: return f'class="{cls} px-[1.8rem] py-[0.8rem] !bg-[#071321]"'
    if "width: 32%;" in style: return f'class="{cls} w-[32%]"'
    if "transition-delay: 100ms" in style: return f'class="{cls} delay-100"'
    if "transition-delay: 200ms" in style: return f'class="{cls} delay-200"'
    if "animation-delay: 2s;" in style: return f'class="{cls} [animation-delay:2s]"'
    if "animation-delay: 4s;" in style: return f'class="{cls} [animation-delay:4s]"'
    if "width: 0%;" in style: return f'class="{cls}" style="width: 0%;"' # Leave width:0% for JS
    return m.group(0)

html = re.sub(r'class="([^"]+)"\s*style="([^"]+)"', rep_style, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
