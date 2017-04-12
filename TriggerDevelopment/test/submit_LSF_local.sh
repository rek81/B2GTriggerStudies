export X509_USER_PROXY=/afs/cern.ch/user/a/algomez/x509up_u15148
cd /afs/cern.ch/work/a/algomez/triggerStudies/CMSSW_8_0_14/src/
eval `scramv1 runtime -sh`
cd /afs/cern.ch/work/a/algomez/triggerStudies/CMSSW_8_0_14/src/B2GTriggerStudies
cmsRun TestNewTriggers.py 
