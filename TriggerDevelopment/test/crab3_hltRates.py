##################################################################
########   TO RUN THIS: python crab3_QCD.py
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
from httplib import HTTPException
import glob

config = config()

version = 'v01'

config.General.requestName = ''
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'hlt_B2GTriggers_83XMC_v2.py'  
#config.JobType.psetName = 'hlt_B2GTriggers_2017Data_v3.py'
config.JobType.allowUndistributedCMSSW = True
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
		crabCommand('submit', config = config)
	except HTTPException, hte:
		print 'Cannot execute commend'
		print hte.headers

if __name__ == '__main__':

	from CRABAPI.RawCommand import crabCommand

	Samples = [ 
		'/HLTPhysics/Run2017A-v1/RAW',
		#'/QCD_Pt_30to50_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_50to80_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_80to120_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_120to170_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_170to300_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_300to470_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
		#'/QCD_Pt_470to600_TuneCUETP8M1_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v1/GEN-SIM-RAW',
			]

	
	from multiprocessing import Process
	for dataset in Samples:
		config.Data.inputDataset = dataset
		#procName = dataset.split('/')[1]+dataset.split('/')[2]+'_'+version
		procName = dataset.split('/')[1]+'_'+version
		#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
		config.Data.lumiMask = '/afs/cern.ch/work/t/tosi/public/STEAM/json/2e34_v1p0p2.json'
		config.Data.splitting = ('LumiBased' if 'HLTPhysics' in dataset.split('/')[1] else 'FileBased')
		#config.JobType.outputFiles = ['hltbits.root']
		#config.JobType.maxMemoryMB = 2500
		config.JobType.numCores = 4
		config.Data.unitsPerJob = 2 
		#config.Data.runRange = '295612:295614'

		config.General.requestName = procName
		print config
		p = Process(target=submit, args=(config,))
		p.start()
		p.join()
