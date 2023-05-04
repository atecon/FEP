#!/bin/bash
set -e

DIR=$(dirname $(realpath "$0")) 	# locate folder where this sh-script is located in

PROJECT="FEP"

FILELIST="./tests/test_forecast_metrics.inp \
          ./tests/test_private.inp"


cd $DIR
echo "Switched to ${DIR}"


for f in ${FILELIST};
  do gretlcli -b -e -q ${f}
done;

if [ $? -eq 0 ]
then
  echo "Success: All tests passed for '${PROJECT}'."
  exit 0
else
  echo "Failure: Tests not passed for '${PROJECT}'." >&2
  exit 1
fi

