#!/bin/bash

## Configuration START

# Program Config.
BERRYHOME="$HOME/Desktop/KindAnalyzer"
PROMPTFILE=$BERRYHOME/src/gAskExpInfo.py
SCOPEFILE=$BERRYHOME/src/timeLapse.py
ANALYFILE=$BERRYHOME/src/analyze.ijm
SCOPEBIN=python3
ANALYBIN=imagej

## Configuration END

## Check: File existence
if [ ! -f $SCOPEFILE ]; then echo "File Not Found! => $SCOPEFILE"; exit; fi
if [ ! -f $ANALYFILE ]; then echo "File Not Found! => $ANALYFILE"; exit; fi
echo "[ OK ] File Check Confirmed."

DATE=$(date +"%Y%m%d_%H%M%S")
OUTDIR=$BERRYHOME/data/$DATE
PHOTODIR=$OUTDIR/photo
LOGDIR=$OUTDIR/log
CONFIGDIR=$OUTDIR/config
CONFIGFILE=$CONFIGDIR/config.txt

mkdir $OUTDIR $PHOTODIR $LOGDIR $CONFIGDIR
echo "[ OK ] Directory generation completed."

## Experiment Config.
#IMGNUM=3
#TIMESTEP=5 # in seconds

# Ask basic experimental configuration
python3 $PROMPTFILE 1> $CONFIGFILE 2> $LOGDIR/promt.log

while IFS='= ' read var val
do
	declare "$var=$val"
	#echo "var: $var & val: $val"
done < $CONFIGFILE

# Variable List:
# IMGNUM, EXP_NAME, TIMELENGTH, TIMESTEP
#echo $OUTDIR $PHOTODIR $LOGDIR

## Send request to server for adding entry about this experiment
let TIMESTEP_SEC=TIMESTEP
exp_id=$DATE
PREFIX="http://dgist.dothome.co.kr/kindProject/addExperiment_public.php"
addURL="${PREFIX}?exp_id=${exp_id}&total_img_num=${IMGNUM}&done_img_num=0&timestep=${TIMESTEP_SEC}"
wget -O $LOGDIR/addExperiment_public.php.response  $addURL > $LOGDIR/addExperiment.log 2>&1

## Execution of microscope and analyzer
echo "[ .. ] Starting KindMicroscope . . ."
$SCOPEBIN $SCOPEFILE $PHOTODIR $IMGNUM $TIMESTEP $exp_id > $LOGDIR/timeLapse.log 2>&1 &
echo "[ .. ] Starting Analyzer . . ."
$ANALYBIN -m $ANALYFILE ${PHOTODIR}#${IMGNUM} > $LOGDIR/analysis.log 2>&1 &

## Testing
#echo $OUTDIR
#echo $SCOPEFILE
#echo $ANALYFILE
