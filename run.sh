OUTFILE=$(echo "$1" | sed 's/ /_/g')
make PARTY="$1" OUTFILE="$OUTFILE"

