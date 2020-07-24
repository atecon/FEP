#!/bin/bash
set -e

DIR=$(dirname $(realpath "$0")) 	# locate folder where this sh-script is located in

PROJECT="FEP"
SCRIPT_1="./tests/run_tests_forecast_metrics.inp"


cd $DIR
echo "Switched to ${DIR}"


# Execute scripts
gretlcli -b -e -q ${SCRIPT_1}


if [ $? -eq 0 ]
then
  echo "Success: All tests passed for '${PROJECT}'."
  exit 0
else
  echo "Failure: Tests not passed for '${PROJECT}'." >&2
  exit 1
fi

