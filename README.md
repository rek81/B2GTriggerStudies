# B2G Trigger Studies

B2G trigger studies repository.
More information in the twiki: [Beyond Two Generations Trigger Studies Page](https://twiki.cern.ch/twiki/bin/viewauth/CMS/B2GTrigger)

 * CMSSW Release: 9_0_1

## Recipe

This is the official recipe for trigger studies taken from [Trigger development for Run-2](https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideGlobalHLT#Trigger_development_for_Run_2). The last part is cloning this repository.

```
cmsrel CMSSW_9_0_1
cd CMSSW_9_0_1/src
cmsenv
git cms-merge-topic cms-tsg-storm:for83Xsamples
scram b -j8

git clone git@github.com:alefisico/B2GTriggerStudies.git -b CMSSW_9_0_1
scram b -j 4
cmsenv
```


## Folders

 * TriggerDevelopment: to test and develop B2G triggers


