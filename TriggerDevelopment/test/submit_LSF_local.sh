export X509_USER_PROXY=/afs/cern.ch/user/a/algomez/x509up_u15148
cd /afs/cern.ch/work/a/algomez/triggerStudies/CMSSW_9_2_3_patch1/src
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/a/algomez/triggerStudies/CMSSW_9_2_3_patch1/src/B2GTriggerStudies/TriggerDevelopment/test/
cmsRun hlt_B2GTriggers_2017Data_v4.py
#cmsRun reRunHLTwithAnalyzer_cfg.py PROC=RPVStop80
