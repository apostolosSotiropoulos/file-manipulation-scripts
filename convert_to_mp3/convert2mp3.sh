## flac2mp3 - copyright 2009 Chris F.A. Johnson
for f in *.flac
do
  outf=${f%.flac}.mp3

  eval "$(
     metaflac "$f" --show-tag=ARTIST \
                   --show-tag=TITLE \
                   --show-tag=ALBUM \
                   --show-tag=GENRE \
                   --show-tag=TRACKNUMBER \
                   --show-tag=DATE | sed 's/=\(.*\)/="\1"/'
    )"

  flac -c -d "$f" | lame -m j -q 0 --vbr-new -V 0 -s 44.1 - "$outf"
  id3 -t "$TITLE" -T "${TRACKNUMBER:-0}" -a "$ARTIST" -A "$ALBUM" -y "$DATE" -g "${GENRE:-12}" "$outf"
done

