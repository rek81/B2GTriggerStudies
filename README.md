# B2G Trigger Studies

B2G trigger studies repository.
More information in the twiki: [Beyond Two Generations Trigger Studies Page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger)

 * CMSSW Release: 9_0_1

## Recipe

This is the official recipe for trigger studies taken from [Trigger development for Run-2](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Trigger_development_for_Run_2). The last part is cloning this repository.

```
cmsrel CMSSW_9_2_3_patch1
cd CMSSW_9_2_3_patch1/src
cmsenv
git cms-init

# L1T

git remote add cms-l1t-offline git@github.com:cms-l1t-offline/cmssw.git
git fetch cms-l1t-offline
# v95.11.7 old MC / data with factor 0.7 included in HF
git cms-merge-topic -u cms-l1t-offline:l1t-integration-v95.11.7
# v95.11.8 new data since Wednesday - facto 0.7 no longer applied
# git cms-merge-topic -u cms-l1t-offline:l1t-integration-v95.11.8
git cms-addpkg L1Trigger/L1TCommon
git cms-addpkg L1Trigger/L1TMuon
git clone https://github.com/cms-l1t-offline/L1Trigger-L1TMuon.git L1Trigger/L1TMuon/data

git cms-addpkg L1Trigger/L1TGlobal

# L1T 2017 menu
# to get the updated L1T menu circulated May 17th (L1Menu_Collisions2017_dev_r3)
git clone https://github.com/cms-l1-dpg/2017-pp-menu-dev -b 2017-05-17 ../2017-pp-menu-dev
# alternatively, to checkout the work-in-progress branch (updated without notice!)
# git clone https://github.com/cms-l1-dpg/2017-pp-menu-dev -b work-in-progress ../2017-pp-menu-dev
mkdir -p L1Trigger/L1TGlobal/data/Luminosity/startup
cp ../2017-pp-menu-dev/Apr12/*.xml L1Trigger/L1TGlobal/data/Luminosity/startup/

# HLT
git cms-addpkg HLTrigger/Configuration
##### Only for 83X samples #####
git cms-merge-topic -u cms-tsg-storm:for83Xsamples92X
################################
git cms-merge-topic -u cms-tsg-storm:HLT_2017_V1p1

git clone git@github.com:alefisico/B2GTriggerStudies.git -b CMSSW_9_2_X
git clone git@github.com:cms-jet/JetToolbox.git JMEAnalysis/JetToolbox -b jetToolbox_80X_V2   ## for jet studies
scram b -j 4
cmsenv
```


## Folders

 * TriggerDevelopment: to test and develop B2G triggers


