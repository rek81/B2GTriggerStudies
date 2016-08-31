##################################################################
########   TO RUN THIS: python crab3_QCD.py
########   DO NOT DO: crab submit crab3_QCD.py
##################################################################

from CRABClient.UserUtilities import config
from httplib import HTTPException
import glob

config = config()

version = 'v02p2'

config.General.requestName = ''
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'TestNewTriggers.py'
config.JobType.allowUndistributedCMSSW = True
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
		#'/JetHT/Run2016C-v2/RAW'
		'/JetHT/Run2016E-v2/RAW'
			]

	
	from multiprocessing import Process
	for dataset in Samples:
		config.Data.inputDataset = dataset
		procName = dataset.split('/')[1]+dataset.split('/')[2].replace('algomez-','')+'_'+version
		#config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-276811_13TeV_PromptReco_Collisions16_JSON.txt'
		config.Data.lumiMask = 'json277069_1e34.json'
		config.Data.splitting = 'LumiBased'
		config.Data.unitsPerJob = 1
		#config.Data.runRange = '276242'  ### 6e33
		#config.Data.runRange = '277069'   ### 1e34

		config.General.requestName = procName
		p = Process(target=submit, args=(config,))
		p.start()
		p.join()
