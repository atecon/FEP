author = Artur Tarassow and Sven Schreiber
email = atecon@posteo.de
version = 2.7
date = 2022-12-14
description = Forecast Evaluation Package
tags = C12 C52 C53
min-version = 2020c # 2019b because of feval(), 2020b for errorif(), 2020c because of quiet loops
data-requirement = no-data-ok
public = doKS doEKTtest doHPtest applyFCtests doDLtest \
  getLoss doMZtest doPTtest \
  doCGtest doDMtest doGWtest doCWtest \
  doPS probscore ForecastMetrics \
  getForecastMetricsNames DrawLoss DrawLoss2 \
  GUI_FEP_print GUI_FEP \
  doEKTtest_matrix CamDufStats
help = FEP.pdf
sample-script = FEP_sample.inp
data-files = FEPdata.gdt
gui-main = GUI_FEP
bundle-print = GUI_FEP_print
menu-attachment = MAINWIN/View
label = Forecast evaluations
