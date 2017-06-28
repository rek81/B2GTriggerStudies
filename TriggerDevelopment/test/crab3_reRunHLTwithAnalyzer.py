##################################################################
########   TO RUN THIS: python crab3_QCD.py
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
from httplib import HTTPException
import glob

config = config()

version = 'v04'

config.General.requestName = ''
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'reRunHLTwithAnalyzer_cfg.py'
config.JobType.allowUndistributedCMSSW = True
config.JobType.maxMemoryMB = 2500
config.JobType.numCores = 4
#supportFiles = glob.glob('/afs/cern.ch/user/s/sdonato/AFSwork/public/genJetPtHadPU_RunIISummer15GS_ak4GenJetsNoNu/*txt')
#config.JobType.inputFiles = supportFiles
config.General.transferLogs = True

config.Data.inputDataset = ''
#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
config.Data.publication = False
config.Data.ignoreLocality = True

#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Rutgers'
config.Data.outLFNDirBase = '/store/user/algomez/myArea/EOS/B2GTriggerStudies/'

def submit(config):
	try:
		#crabCommand('submit', '--dryrun', config = config)
		crabCommand('submit', config = config)
	except HTTPException, hte:
		print 'Cannot execute commend'
		print hte.headers

if __name__ == '__main__':

	from CRABAPI.RawCommand import crabCommand

	Samples = [ 
			['/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/PhaseIFall16MiniAOD-FlatPU28to62HcalNZSRAW_PhaseIFall16_exo071_90X_upgrade2017_realistic_v6_C1-v1/MINIAODSIM', '/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW'],
			[ '/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/PhaseIFall16MiniAOD-PUFlat0to70_PhaseIFall16_90X_upgrade2017_realistic_v6_C1-v2/MINIAODSIM', '/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/PhaseIFall16DR-PUFlat0to70_90X_upgrade2017_realistic_v6_C1-v2/GEN-SIM-RAW' ],
			[ '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/PhaseIFall16MiniAOD-FlatPU28to62HcalNZSRAW_PhaseIFall16_90X_upgrade2017_realistic_v6_C1-v2/MINIAODSIM', '/TT_TuneCUETP8M2T4_13TeV-powheg-pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/GEN-SIM-RAW' ],
			]

	
	from multiprocessing import Process
	for dataset in Samples:
		config.Data.inputDataset = dataset[0]
		config.Data.secondaryInputDataset = dataset[1]
		#procName = dataset.split('/')[1]+dataset.split('/')[2]+'_'+version
		procName = dataset[0].split('/')[1]+'_TriggerEfficiencies_'+version
		#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
		config.Data.splitting = 'EventAwareLumiBased' # 'FileBased'
		#config.JobType.outputFiles = ['hltbits.root']
		#config.JobType.maxMemoryMB = 2500
		config.Data.unitsPerJob = 2000 #1 
		#config.Data.runRange = '295612:295614'

		config.General.requestName = procName
		print config
		p = Process(target=submit, args=(config,))
		p.start()
		p.join()
