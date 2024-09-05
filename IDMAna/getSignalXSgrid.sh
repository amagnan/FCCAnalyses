#!/bin/bash

#rm inputNXSgrid.dat
#rm signalXSgrid.dat
#rm signalXSlatexgrid.dat

echo "!!!!!!!!!! Get input grid points"

inputfile="../../MG5prod/Teddy/cards/input_arguments.txt"


count=0
while IFS=', ' read -r i j; do
    mh[${count}]=$i
    ma[${count}]=$j
    let count=$count+1
done < $inputfile

echo "${mh[*]}"
echo "${ma[*]}"

echo "!!!!!!!!!! Get xs/numEvts "


echo "!!!!!!! Found $count lines in file"

let count=$count-1

#for ecm in 240 365; do
for ecm in 365; do

    
    for datadir in "h2h2ll" "h2h2llvv"; do
	for ic in `seq 0 ${count}`; do
	    #echo "ECM${ecm}_MH"${mh[${ic}]}"_MA"${ma[${ic}]}
	    ls ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out > /dev/null
	    if [ $? -ne 0 ]; then
		echo "!!!!!!!!!!!!! ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]} Not found, tail the log file instead"
		tail -n 2 ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.log
	    else
		myres=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $3}'`
		numevt=`grep "Nb of events" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
		if [ "${datadir}" == "h2h2ll" ]; then
		    #echo "case h2h2ll: "${datadir}
		    whhll[${ic}]=${myres}/${numevt}
		    themonth=$(ls -ltrh ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | awk '{print $6}')
		    theday=$(ls -ltrh ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | awk '{print $7}')
		    echo -e "${ecm}\t${datadir}\tMH${mh[${ic}]}\tMA${ma[${ic}]}\t$themonth\t$theday\t${numevt}"
		else
		    #echo "case h2h2llvv: "${datadir}
		    whhllvv[${ic}]=${myres}/${numevt}
		    themonth=$(ls -ltrh ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | awk '{print $6}')
		    theday=$(ls -ltrh ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | awk '{print $7}')
		    echo -e "${ecm}\t${datadir}\tMH${mh[${ic}]}\tMA${ma[${ic}]}\t$themonth\t$theday\t${numevt}"
		fi
	    fi
	done
    done

    echo "${whhll[*]}"
    echo "${whhllvv[*]}"
    
    echo "!!!!!!!!!! Get dictionary lines for final stage"
    
    
 #   for datadir in "h2h2ll" "h2h2llvv"; do
#	#    for ecm in 240 365;
#	#do
#	for ic in `seq 0 ${count}`; do
#	    myres=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $3}'`
#	    #numevt=`grep "Nb of events" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
#	    numevt=`root -b 'getNevtsDelphes.C("/eos/user/a/amagnan/FCC/iDMprod/winter2023/'"${datadir}"'/Delphes_EDM4HEPevents_e'"${ecm}"'_mH'"${mh[${ic}]}"'_mA'"${ma[${ic}]}"'.root")'|tail -n 1 |awk '{print $2}'`
#	    #echo $datadir" ECM " $ecm " BP "$bp" xs = "$myres  >> signalXSgrid.dat
#	    echo "\"e${ecm}_mh${mh[${ic}]}_ma${ma[${ic}]}_${datadir}\":{\"numberOfEvents\": $numevt, \"sumOfWeights\": $numevt, \"crossSection\":  $myres, \"kfactor\": 1.0, \"matchingEfficiency\": 1.0},"  >> signalXSgrid.dat
#	    echo "${ecm},${mh[${ic}]},${ma[${ic}]},${datadir},$numevt,$myres"  >> inputNXSgrid.dat
#	done
 #   done
  #  #done

    
    echo "!!!!!!!!!! Get latex table of xs"
    
    
#for ecm in 240 365;
#do
    echo "ECM: "$ecm >> signalXSlatexgrid.dat
    for ic in `seq 0 ${count}`; do
	output=${mh[${ic}]}" & "${ma[${ic}]}
	for datadir in "h2h2ll" "h2h2llvv"; do
	    myres=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $3}'`
	    numevtMG=`grep "Nb of events" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
	    numevt=`root -b 'getNevtsDelphes.C("/eos/user/a/amagnan/FCC/iDMprod/winter2023/'"${datadir}"'/Delphes_EDM4HEPevents_e'"${ecm}"'_mH'"${mh[${ic}]}"'_mA'"${ma[${ic}]}"'.root")'|tail -n 1 |awk '{print $2}'`
	    output=$output" & "$myres" & "$numevtMG" & "$numevt
	done
	echo $output" \\\\" >> signalXSlatexgrid.dat
    done
done

#cat signalXSgrid.dat
cat signalXSlatexgrid.dat
