cd "$(dirname "$0")"
while IFS=$'\t' read -r n id; do
  [ -s $n.mp4 ] || curl -sSL -A "MeEditingVideoTool/1.0" -o $n.mp4 "https://drive.usercontent.google.com/download?id=$id&export=download&confirm=t" </dev/null
  echo "$n $(ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 $n.mp4 </dev/null | tr '\n' ' ')"
  [ -s $n.json ] || python3 -I ../tx.py $n.mp4 $n </dev/null >/dev/null 2>&1
done < list.tsv
echo ALLDONE
