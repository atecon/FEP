author = Artur Tarassow and Sven Schreiber
email = atecon@cryptolab.net
version = 2.3
date = 2018-07-02
description = Forecast Evaluation Package
tags = C12 C52 C53
min-version = 2017a
data-requirement = no-data-ok
public = doKS doEKTtest_series doHPtest applyFCtests doDLtest \
  getLoss doDMtest doGWtest doMZtest doPTtest \
  doCGtest \
  doPS probscore \
  DrawLoss DrawLoss2 \
  GUI_FEP_print GUI_FEP \
  doCGWILCtest doCGRANKtest \
  doKStest doEKTtest doKGtest \
  CamDufStats
  
help = FEP.pdf
sample-script = FEP_sample.inp
data-files = FEPdata.gdt

# still some zip-related things missing?
# lives-in-subdir and stuff?

gui-main = GUI_FEP
# no-print = GUI_FEP
bundle-print = GUI_FEP_print
menu-attachment = MAINWIN/View
label = Forecast evaluations
