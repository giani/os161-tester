#!/bin/bash

ASST_NR=$1
ECE_SVN=svn+ssh://ug131.eecg.utoronto.ca/svn
PATH=/cad2/ece344f/cs161/bin:$PATH
TOP_DIR=/cad2/ece344f
RESULTS_DIR=${TOP_DIR}/results
ASST_DIR=${RESULTS_DIR}/asst${ASST_NR}
TESTER_DIR=${TOP_DIR}/os161-tester
BINDIR=${TESTER_DIR}/bin
DESIGN_DIR=${ASST_DIR}/designs

pushd .
#Become the right group
#newgrp e344F12
mkdir -p ${DESIGN_DIR}
cd ${DESIGN_DIR}
for i in `seq -f "%03g" 1 39`
do
	svn co ${ECE_SVN}/os-${i}/svn/tags/asst${ASST_NR}-end/submit/${ASST_NR}/&& cp ${ASST_NR}/solution.txt solution-${i}.txt
	rm -rf ${ASST_NR}
done
popd
