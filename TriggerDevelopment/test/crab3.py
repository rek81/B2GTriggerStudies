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
#config.JobType.psetName = 'hlt_B2GTriggers_MC.py'  
config.JobType.psetName = 'hlt_B2GTriggers_2017Data.py'
config.JobType.allowUndistributedCMSSW = True
#config.JobType.inputFiles = [ '/afs/cern.ch/user/s/sdonato/AFSwork/public/genJetPtHatPU/0.txt' ]
config.General.transferLogs = True

config.Data.inputDataset = ''
#config.Data.inputDBS = 'https://cmsweb.cern.ch/dbs/prod/phys03/DBSReader'
config.Data.publication = False
config.Data.ignoreLocality = True

#config.Site.storageSite = 'T3_US_FNALLPC'
config.Site.storageSite = 'T3_US_Rutgers'
config.Data.outLFNDirBase = '/store/user/algomez/myArea/EOS/'

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
		#'/QCD_Pt-15to3000_TuneCUETP8M1_Flat_13TeV_pythia8/PhaseIFall16DR-FlatPU28to62HcalNZSRAW_90X_upgrade2017_realistic_v6_C1-v2/GEN-SIM-RAW'
			]

	
	from multiprocessing import Process
	for dataset in Samples:
		config.Data.inputDataset = dataset
		#procName = dataset.split('/')[1]+dataset.split('/')[2]+'_'+version
		procName = dataset.split('/')[1]+'_'+version
		#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
		config.Data.lumiMask = '/afs/cern.ch/work/t/tosi/public/STEAM/json/firstCollisions17_v3p1_v3_PS_2e34.json'
		config.Data.splitting = 'LumiBased'
		config.Data.unitsPerJob = 1
		#config.Data.runRange = '295612:295614'

		config.General.requestName = procName
		print config
		p = Process(target=submit, args=(config,))
		p.start()
		p.join()
