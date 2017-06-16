# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step2 --filein /store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/DE222E42-3A1B-E711-BE59-002590200908.root --fileout file:test.root --mc --conditions 92X_upgrade2017_TSG_For83XSamples_V4 --step HLT:User --era Run2_2017 --python_filename reRunHLTOnly_cfg.py --processName=HLT2 -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT2',eras.Run2_2017)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('HLTrigger.Configuration.HLT_User_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16MiniAOD/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/MINIAODSIM/FlatPU28to62HcalNZSRAW_PhaseIFall16_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/148E2F5B-A51C-E711-81B2-001E67398E6C.root'),
    secondaryFileNames = cms.untracked.vstring(
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/6E7C1EA3-491C-E711-95A1-001E677925E8.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/10397DA2-5B1B-E711-90E8-001E6779239C.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/325A6F9B-4B1B-E711-8427-001E67792576.root',
	    )

)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:test.root'),
    outputCommands = cms.untracked.vstring("keep *"),  #process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '92X_upgrade2017_TSG_For83XSamples_V4', '')

# Path and EndPath definitions
process.HLTriggerFinalPath = cms.Path(process.SimL1Emulator+process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelector+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)
process.HLTriggerFirstPath = cms.Path(process.SimL1Emulator+process.hltDummyConditions+process.hltGetRaw+process.hltBoolFalse)
process.endjob_step = cms.EndPath(process.endOfProcess)
#process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)


process.TFileService=cms.Service("TFileService",fileName=cms.string( 'reRunHLTwithAnalyzerv2.root' ) )

process.PFHTTriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		baseTrigger = cms.string("empty"),
		triggerPass = cms.vstring([ "HLT_PFHT1050_v" ] ), 
		recoJets = cms.InputTag("slimmedJetsAK8"),
		recojetPt = cms.double( 200 ),
		AK8jets = cms.bool( True ),
		objects = cms.InputTag("selectedPatTrigger")
)
process.PFHTTriggerEfficiency_step = cms.EndPath( process.PFHTTriggerEfficiency )

process.AK8PFJet400Trim30TriggerEfficiency = process.PFHTTriggerEfficiency.clone( triggerPass = cms.vstring([ "HLT_AK8PFJet400_TrimMass30_v" ] ) )
process.AK8PFJet400Trim30TriggerEfficiency_step = cms.EndPath( process.AK8PFJet400Trim30TriggerEfficiency )

process.AK8PFJet400SD30TriggerEfficiency = process.PFHTTriggerEfficiency.clone( triggerPass = cms.vstring([ "HLT_AK8PFJet400_SDMass30_v" ] ) )
process.AK8PFJet400SD30TriggerEfficiency_step = cms.EndPath( process.AK8PFJet400SD30TriggerEfficiency )

process.AK8PFJet400Trim30CaloBtagp080TriggerEfficiency = process.PFHTTriggerEfficiency.clone( triggerPass = cms.vstring([ "HLT_AK8PFJet380_TrimMass30_AK4CaloBtagCSV_p080_v" ] ) )
process.AK8PFJet400Trim30CaloBtagp080TriggerEfficiency_step = cms.EndPath( process.AK8PFJet400Trim30CaloBtagp080TriggerEfficiency )

process.AK8PFJet400Trim30PFBtagp080TriggerEfficiency = process.PFHTTriggerEfficiency.clone( triggerPass = cms.vstring([ "HLT_AK8PFJet380_TrimMass30_AK4PFBtagCSV_p080_v" ] ) )
process.AK8PFJet400Trim30PFBtagp080TriggerEfficiency_step = cms.EndPath( process.AK8PFJet400Trim30PFBtagp080TriggerEfficiency )

process.AK8PFHT850Trim50TriggerEfficiency = process.PFHTTriggerEfficiency.clone( triggerPass = cms.vstring([ "HLT_AK8PFHT850_TrimMass50_v" ] ) )
process.AK8PFHT850Trim50TriggerEfficiency_step = cms.EndPath( process.AK8PFHT850Trim50TriggerEfficiency )


# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
#process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step])
process.schedule.extend([process.endjob_step,
			process.PFHTTriggerEfficiency_step,
			process.AK8PFJet400Trim30TriggerEfficiency_step,
			process.AK8PFJet400SD30TriggerEfficiency_step,
			process.AK8PFJet400Trim30CaloBtagp080TriggerEfficiency_step,
			process.AK8PFJet400Trim30PFBtagp080TriggerEfficiency_step, 
			process.AK8PFHT850Trim50TriggerEfficiency_step,
			])
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
#from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
#process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
#from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
#process = customiseEarlyDelete(process)
# End adding early deletion
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
