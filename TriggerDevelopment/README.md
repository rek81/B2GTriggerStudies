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

 * For the reRunHLTOnly_cfg.py:
```
hltGetConfiguration --cff --offline /dev/CMSSW_9_2_0/GRun --paths HLTriggerFirstPath,HLTriggerFinalPath --unprescale --l1-emulator FullMC --l1 L1Menu_Collisions2017_dev_r5_m4_patch_xml  > HLT_User_cff.py
hltGetConfiguration --cff --offline /users/algomez/B2GTriggers/V42 >> HLT_User_cff.py
cp HLT_User_cff.py ../../../HLTrigger/Configuration/python/
cd ../../../
scram b -j 8
cd - 
cmsDriver.py step2 --filein /store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/DE222E42-3A1B-E711-BE59-002590200908.root --fileout file:test.root --mc --conditions 92X_upgrade2017_TSG_For83XSamples_V4 --step HLT:User --era Run2_2017 --python_filename reRunHLTOnly_cfg.py --processName=HLT2 -n 100
```

 * To estimate the rates, modify rateMC.C and run:
```
root -l .x rateMC.C
```
rateMC.C is provided by STEAM. More info here: https://twiki.cern.ch/twiki/bin/viewauth/CMS/RateEstimateSTEAM#Simplified_macro_for_users_to_ge

More information in the twiki: [Beyond Two Generations Trigger Studies Page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger)
