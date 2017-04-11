# Trigger Development


 * CMSSW Release: 9_0_1

This is just a quick list of recipes.

 * For the hlt_B2GTriggers_MC.py:
```
hltGetConfiguration /users/algomez/B2GTriggers/V24 --full --offline --mc --unprescale --process TEST --globaltag 90X_upgrade2017_TSG_Hcal_V2 --setup /dev/CMSSW_9_0_1/GRun --no-output --max-events 10 --input root://eoscms.cern.ch//eos/cms/store/mc/PhaseIFall16DR/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/130000/BE521173-FD10-E711-A3FE-02163E0176C2.root --l1-emulator FullSimHcalTP  > hlt_B2GTriggers_MC.py 
```

 * For the hlt_B2GTriggers_2016Data.py:
```
hltGetConfiguration /users/algomez/B2GTriggers/V24 --full --offline --data --unprescale --process TEST --globaltag auto:run2_hlt_GRun --setup /dev/CMSSW_9_0_1/GRun --no-output --max-events 10  --l1-emulator FullSimHcalTP  > hlt_B2GTriggers_2016Data.py
```


More information in the twiki: [https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger](Beyond Two Generations Trigger Studies Page)
