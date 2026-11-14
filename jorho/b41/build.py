import json,sys,os
B=os.path.dirname(os.path.abspath(__file__))+'/..'
M=[('blue-yung-kai.mp3',37240),('du-bist-full.mp3',42050),('joyful-chess-slowed.mp3',84700)]
Y,C,G='#F9FC35','#21F5E6','#58EE28'
P=json.load(open(B+'/plan/plans.src.json'))
out=[]
for i,p in enumerate(P):
  w=json.load(open(f"{B}/{p['n']}.json"))
  words=[{'text':x['w'],'startMs':int(x['s']*1000)} for x in w]
  f,beat=M[i%3]
  q={'id':p['id'],'src':f"b41/{p['n']}.mp4",'segs':p['segs'],'top':p['top'],'words':words,'green':p.get('green',[]),'red':p.get('red',[]),
     'strobeSegs':p.get('strobe',[]),'fix':p.get('fix',{}),'colors':{k:{'Y':Y,'C':C,'G':G}[v] for k,v in p.get('colors',{}).items()},'music':{'file':f,'beat':beat}}
  if 'cut' in p: q['cut']=p['cut']
  segs=p['segs']; tot=sum(b-a for a,b in segs)
  for t in q['green']+q['red']: assert any(a<=t<b for a,b in segs),(p['id'],t)
  print(p['id'],round(tot/1000,1),'s')
  out.append(q)
json.dump(out,open(sys.argv[1],'w'))
