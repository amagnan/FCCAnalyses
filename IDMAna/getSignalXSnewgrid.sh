#!/bin/bash

prod="241113"
#rm inputNXSgrid_${prod}.dat

echo "!!!!!!!!!! Get input grid points"
xsmax=0.0001

scen[1]="cards_scenario_1_base"
scen[2]="cards_scenario_2_max_lam345"
scen[3]="cards_scenario_3_max_lam345_max_mHch"

#for ecm in 240 365; do
#    for scenId in 1 2 3; do 
for ecm in 365; do
    for scenId in 3; do

	inputfile="../../MG5prod/Teddy/FCC_newRun_all/e${ecm}/${scen[${scenId}]}/input_arguments.txt"


	count=0
	while IFS=', ' read -r s i j k; do
	    dummy[${count}]=$s
	    mh[${count}]=$i
	    ma[${count}]=$j
	    mch[${count}]=$k
	    let count=$count+1
	done < $inputfile

	echo "$ecm ${scen[${scenId}]} ${mh[*]}"
#	echo "${ma[*]}"

	
	echo "!!!!!!!!!! Get xs/numEvts "


	echo "!!!!!!! Found $count lines in file"

	let count=$count-1

#	for datadir in "h2h2ll" "h2h2llvv"; do
	for datadir in "h2h2llvv"; do
	    for ic in `seq 0 ${count}`; do
		myres=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_S${scenId}_MH${mh[${ic}]}_MA${ma[${ic}]}_MHPM${mch[${ic}]}/condor.out | tail -n 1 | awk '{print $3}'`
		myreserr=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_S${scenId}_MH${mh[${ic}]}_MA${ma[${ic}]}_MHPM${mch[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
		myresunit=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_S${scenId}_MH${mh[${ic}]}_MA${ma[${ic}]}_MHPM${mch[${ic}]}/condor.out | tail -n 1 | awk '{print $6}'`
		numevtMG=`grep "Nb of events" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_S${scenId}_MH${mh[${ic}]}_MA${ma[${ic}]}_MHPM${mch[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
		numevtD=`root -b 'getNevtsDelphes.C("/eos/experiment/fcc/ee/analyses_storage/BSM/IDM/241113/'"${datadir}"'/Delphes_EDM4HEPevents_e'"${ecm}"'_s'"${scenId}"'_mH'"${mh[${ic}]}"'_mA'"${ma[${ic}]}"'_mCh'"${mch[${ic}]}"'.root")'|tail -n 1 |awk '{print $2}'`
		echo "${ecm},${scenId},${mh[${ic}]},${ma[${ic}]},${mch[${ic}]},${datadir},$numevtMG,$numevtD,$myres,$myreserr,$myresunit"  >> inputNXSgrid_h2h2llvv_${prod}_fin.dat

		echo "\"e${ecm}_s${scenId}_mh${mh[${ic}]}_ma${ma[${ic}]}_mch${mch[${ic}]}_${datadir}\":{\"numberOfEvents\": $numevtD, \"sumOfWeights\": $numevtD, \"crossSection\":  $myres, \"kfactor\": 1.0, \"matchingEfficiency\": 1.0},"  >> FCCee_signal_h2h2llvv_${prod}_fin.txt
		
	    done
	done
    done
done

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

    
#echo "!!!!!!!!!! Get latex table of xs"
    
    
#for ecm in 240 365;
#do
#    echo "ECM: "$ecm >> signalXSlatexgridNote.dat
#echo "m_{H} (GeV) & m_{A} (GeV) & \multicolumns{4}{c}{\sqrt{E} = 240 GeV} &  \multicolumns{4}{c}{\sqrt{E} = 365 GeV} \\\\">> signalXSlatexgridNote.dat     
#echo " & & \multicolumns{2}{c}{h2h2ll} &  \multicolumns{2}{c}{h2h2llvv} & \multicolumns{2}{c}{h2h2ll} &  \multicolumns{2}{c}{h2h2llvv} \\\\">> signalXSlatexgridNote.dat     
#for ic in `seq 0 ${count}`; do
#    doprint=1
#    output=${mh[${ic}]}" & "${ma[${ic}]}
#    for ecm in 240 365;
#    do
#	for datadir in "h2h2ll" "h2h2llvv"; do
#	    myres=`grep "Cross-section :" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $3}'`
#	    numevtMG=`grep "Nb of events" ../../MG5prod/Teddy/${datadir}/ECM${ecm}_MH${mh[${ic}]}_MA${ma[${ic}]}/condor.out | tail -n 1 | awk '{print $5}'`
##	    #numevt=`root -b 'getNevtsDelphes.C("/eos/user/a/amagnan/FCC/iDMprod/winter2023/'"${datadir}"'/Delphes_EDM4HEPevents_e'"${ecm}"'_mH'"${mh[${ic}]}"'_mA'"${ma[${ic}]}"'.root")'|tail -n 1 |awk '{print $2}'`
##	    if [ "${ecm}" = "365" ]; then
##		if [ "${datadir}" = "h2h2ll" ]; then
##		    if (( $(echo "$myres < $xsmax" |bc -l) )); then
##			doprint=0
##		    fi
##		fi
##	    fi
#	    output=$output" & "$myres" & "$numevtMG
#	    #" & "$numevt
#	done
#    done
#   if [ "${doprint}" == "1" ]; then
#    echo $output" \\\\" >> signalXSlatexgridNote.dat
#  fi
#done
#done

#cat signalXSgrid.dat
#cat signalXSlatexgridNote.dat
