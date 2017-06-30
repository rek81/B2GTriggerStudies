from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'test_Matching'
config.General.workArea = 'crab_projects'
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TriggerValidationAndEfficiencies_cfg.py'

config.Data.inputDataset = '/JetHT/Run2017A-PromptReco-v2/MINIAOD'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
NJOBS = 1000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.publication = True
config.Data.outputDatasetTag  = 'SimpleMatching'
config.Data.ignoreLocality = True
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions17/13TeV/PromptReco/Cert_294297-999999_13TeV_PromptReco_Collisions17_JSON.txt'

#config.Site.storageSite = 'T3_US_FNALLPC'

#### Only for hexfarm.. it still does not work
config.Data.outLFNDirBase  = '/store/user/rkowalsk/EOS/'### only for hexfarm
config.Site.storageSite = 'T3_US_Rutgers'
