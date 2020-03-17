#!/bin/bash
source /home/chris/.bashrc
DIR="/home/chris/Documents/coronaDeathCounter"
cd /home/chris/Documents/coronaDeathCounter

coronaArray=()
while read line ; do
  coronaArray+=($line)
done < <(python $DIR/coronaCount.py)

printf "Web scrape finished.\nCases: "$coronaArray[0]"\nDeaths: "$coronaArray[1]"\n"

if [ ${coronaArray[1]} -gt 0 ]; then
  sed -i "s/casesCount = [0-9]\+;/casesCount = ${coronaArray[0]};/" $DIR/coronaDeathCounter.ino
  sed -i "s/deathCount = [0-9]\+;/deathCount = ${coronaArray[1]};/" $DIR/coronaDeathCounter.ino
  /usr/local/bin/amake -u uno $DIR/coronaDeathCounter.ino /dev/ttyACM0
else
  echo "Scrape returned bad values. Exiting..."
  exit 1
fi
