import json,os,hashlib,csv
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__));R=D+'/repo/'
plan=json.load(open(D+'/plan.json'))
frames=[];idx={};used_files=set()
def frame(path):
    if path in idx:return idx[path]
    try:im=Image.open(R+path).convert('RGBA')
    except Exception:return None
    f=im.crop((0,128,64,192)) if im.size[1]==256 else im.crop((32,288,96,352))
    if f.getbbox() is None: idx[path]=None;return None
    h=hashlib.md5(f.tobytes()).hexdigest()
    for i,(hh,_) in enumerate(frames):
        if hh==h: idx[path]=i;used_files.add(path);return i
    frames.append((h,f));idx[path]=len(frames)-1;used_files.add(path);return idx[path]
items={}
for n,it in plan.items():
    layers=[]
    for L in it['layers']:
        fr={k:frame(v) for k,v in L['files'].items()}
        fr={k:v for k,v in fr.items() if v is not None}
        if fr: layers.append({'z':L['z'],'b':L['body'],'f':fr})
    if layers: items[n]={'slot':it['slot'],'name':it['name'],'rc':it['recolors'],'v':it['variants'],'L':layers}
cols=32;rows=(len(frames)+cols-1)//cols
atlas=Image.new('RGBA',(cols*64,rows*64))
for i,(_,f) in enumerate(frames): atlas.paste(f,((i%cols)*64,(i//cols)*64))
atlas.save(D+'/out/lpc.png',optimize=True)
pal={}
for m in ['body','hair','cloth','metal','eye','wood']:
    p=R+f'palette_definitions/{m}/{m}_ulpc.json'
    if os.path.exists(p):
        meta=json.load(open(R+f'palette_definitions/{m}/meta_{m}.json'))
        pal[m]={'base':meta.get('base'),'ramps':json.load(open(p))}
json.dump({'cols':cols,'items':items,'pal':pal},open(D+'/out/lpc.json','w'),separators=(',',':'))
# credits for files used
used={u[len('spritesheets/'):] for u in used_files}
rows=[]
with open(R+'CREDITS.csv',newline='') as fh:
    rd=csv.reader(fh);hdr=next(rd)
    for r in rd:
        f0=r[0].strip();base=f0[:-4] if f0.endswith('.png') else f0.rstrip('/')
        if f0 in used or any(u.startswith(base+'/') for u in used): rows.append([c.strip() for c in r])
agg={}
for r in rows:
    k=(r[2],r[3]);agg.setdefault(k,{'files':[],'urls':set()});agg[k]['files'].append(r[0]);agg[k]['urls'].update(u.strip() for u in r[4].split(',') if u.strip())
out=[{'authors':a,'licenses':l,'parts':sorted({f.rsplit('/',1)[0] for f in v['files']}),'urls':sorted(v['urls'])} for (a,l),v in agg.items()]
json.dump(out,open(D+'/out/lpc-credits.json','w'),separators=(',',':'))
lic=set()
for (a,l) in agg: lic.update(x.strip() for x in l.split(','))
cov=sum(1 for u in used if any(u==r[0] or u.startswith((r[0][:-4] if r[0].endswith('.png') else r[0].rstrip('/'))+'/') for r in rows));print('covered',cov);print(len(items),'items',len(frames),'frames',atlas.size,os.path.getsize(D+'/out/lpc.png'),'png',os.path.getsize(D+'/out/lpc.json'),'json',len(rows),'rows',len(out),'groups',sorted(lic),os.path.getsize(D+'/out/lpc-credits.json'),'credits bytes', len(used),'used')
