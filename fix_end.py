import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# find the last <script> tag and remove everything up to </script>
idx = html.rfind('<script>')
if idx != -1:
    end_idx = html.find('</script>', idx)
    if end_idx != -1:
        html = html[:idx] + html[end_idx + 9:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
