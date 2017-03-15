# B2GTriggerStudies

B2G trigger studies repository.
More information in the twiki: [https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger](Beyond Two Generations Trigger Studies Page)

 * CMSSW Release: 9_0_0

## Recipe

This is the official recipe for trigger studies taken from [https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Trigger_development_for_Run_2](Trigger development for Run-2). The last part is cloning this repository.

```
cmsrel CMSSW_9_0_0_pre6
cd CMSSW_9_0_0_pre6/src
cmsenv

git cms-init
git cms-addpkg HLTrigger/Configuration
git cms-merge-topic 17853


git cms-checkdeps -A -a
scram b -j 4

git clone git@github.com:alefisico/B2GTriggerStudies.git -b CMSSW_8_0_19
scram b -j 4
cmsenv
```


## Folders

 * TriggerDevelopment: to test and develop B2G triggers


