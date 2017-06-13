# Trigger Development


 * CMSSW Release: 9_2_X

This is just a quick list of recipes.

 * For the hlt_B2GTriggers_83XMC.py:
```
hltGetConfiguration /users/algomez/B2GTriggers/V41 --full --offline --mc --input  root://eoscms.cern.ch//eos/cms/store/mc/PhaseIFall16DR/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/00000/00756078-A307-E711-B8AC-1866DAEA8178.root --unprescale --process TEST --globaltag  92X_upgrade2017_TSG_For83XSamples_V4 --l1-emulator FullMC --l1 L1Menu_Collisions2017_dev_r5_m4_patch_xml  --setup /dev/CMSSW_9_2_0/GRun --no-output > hlt_B2GTriggers_83XMC.py
```

 * For the hlt_B2GTriggers_2016Data_v2.py:
```
hltGetConfiguration /users/algomez/B2GTriggers/V41 --full --offline --data --unprescale --process TEST --globaltag 92X_dataRun2_HLT_v2 --setup /dev/CMSSW_9_2_0/GRun --no-output > hlt_B2GTriggers_2017Data_v2.py
```


More information in the twiki: [Beyond Two Generations Trigger Studies Page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger)
