"""Run with python3 tests/check_site.py from any working directory."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET
root=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
 def __init__(self):
  super().__init__();self.refs=[];self.ids=set();self.h1=0;self.active=0;self.canonical=[];self.description=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in a:
   assert a['id'] not in self.ids, f'Duplicate ID: {a["id"]}'
   self.ids.add(a['id'])
  if a.get('aria-current')=='page':self.active+=1
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='meta' and a.get('name')=='description':self.description.append(a['content'])
  for attr in ('src','href'):
   if attr in a:self.refs.append(a[attr])
pages={}
for file in root.glob('*.html'):
 page=Page();page.feed(file.read_text());pages[file.name]=page
 assert page.h1==1 and page.active==1, file.name
 assert len(page.canonical)==1 and len(page.description)==1,file.name
assert len({p.description[0] for p in pages.values()})==len(pages)
count=0
for name,page in pages.items():
 for ref in page.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=u.path or name
  assert (root/target).is_file(),(name,ref)
  if u.fragment:assert target in pages and u.fragment in pages[target].ids,(name,ref)
  count+=1
urls={e.text for e in ET.parse(root/'sitemap.xml').findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')}
assert urls=={p.canonical[0] for p in pages.values()}
print(f'PASS: {len(pages)} pages, {count} local references, unique descriptions, navigation, and sitemap.')
