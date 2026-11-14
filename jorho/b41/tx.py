import sys,json,subprocess,numpy as np
from faster_whisper import WhisperModel
src,out=sys.argv[1],sys.argv[2]
pcm=subprocess.run(['ffmpeg','-v','error','-i',src,'-ac','1','-ar','16000','-f','s16le','-'],capture_output=True).stdout
a=np.frombuffer(pcm,np.int16).astype(np.float32)/32768
m=WhisperModel('small.en',compute_type='int8')
segs,_=m.transcribe(a,word_timestamps=True)
W=[];L=[]
for s in segs:
  L.append(f"{s.start:6.2f}-{s.end:6.2f} {s.text.strip()}")
  W+=[{'w':w.word.strip(),'s':round(w.start,2),'e':round(w.end,2)} for w in s.words]
json.dump(W,open(out+'.json','w')); open(out+'.txt','w').write('\n'.join(L)); print('\n'.join(L))
