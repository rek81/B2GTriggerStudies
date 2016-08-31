# B2GTriggerStudies

B2G trigger studies repository.
More information in the twiki: [https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger](Beyond Two Generations Trigger Studies Page)

 * CMSSW Release: 8_0_19

## Recipe

This is the official recipe for trigger studies taken from [https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Trigger_development_for_Run_2](Trigger development for Run-2). The last part is cloning this repository.

```
cmsrel CMSSW_8_0_19
cd CMSSW_8_0_19/src
cmsenv
rehash

git cms-addpkg HLTrigger/Configuration
git cms-merge-topic -u cms-tsg-storm:80XHLTAfterMD2Train

git cms-checkdeps -A -a
scram b -j 4
cmsenv


git clone git@github.com:alefisico/B2GTriggerStudies.git -b CMSSW_8_0_19
scram b -j 4
cmsenv
```


## Folders

 * TriggerDevelopment: to test and develop B2G triggers


