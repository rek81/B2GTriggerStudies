# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: HLT2 --step HLT:User --era Run2_2017 --conditions 90X_upgrade2017_realistic_v6_C1 --mc --filein /store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/0EE009EF-F61A-E711-8572-0CC47A7E6AAA.root --processName HLT2 -n 100
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
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/AODSIM/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/0EE009EF-F61A-E711-8572-0CC47A7E6AAA.root'),
    secondaryFileNames = cms.untracked.vstring(
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/9E765F41-DD1A-E711-A627-FACADE00010E.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/D83EC62D-E71A-E711-85F8-70106F4A92D4.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/AC604FD1-E71A-E711-B93A-70106F4A9254.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/64AAD8D6-E81A-E711-95D2-70106F4A9254.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/E4DF50D2-EC1A-E711-8A37-70106F48B9A2.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/7077A4A4-EE1A-E711-BF93-0CC47A7E69CE.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/8A017985-EF1A-E711-91C3-0CC47A7DFFC8.root',
	    '/store/mc/PhaseIFall16DR/RPVStopStopToJets_UDD312_M-80_TuneCUETP8M1_13TeV-madgraph-pythia8/GEN-SIM-RAW/FlatPU28to62HcalNZSRAW_exo071_90X_upgrade2017_realistic_v6_C1-v1/60000/10CD84EF-F01A-E711-B1AC-0CC47A7E6A2C.root',
	    )
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('HLT2 nevts:100'),
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
    fileName = cms.untracked.string('HLT2_HLT_test.root'),
    #outputCommands = process.RECOSIMEventContent.outputCommands,
    outputCommands =  cms.untracked.vstring('keep *',
	    'keep *_hltPFHT*_*_*', 

#		"keep *_TriggerResults_*_*",
#		"keep *_hltTriggerSummaryAOD_*_*",
	    ), #process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)
#process.RECOSIMoutput.outputCommands = cms.untracked.vstring(
#		"drop *_*_*_RECO",
#		"keep *_ak8PFJets*_*_*",
#		"keep *_ak4PFJets*_*_*",
#		"keep *_hltGtStage2ObjectMap_*_*",
#		"keep *_genParticles_*_*",
#		"keep *_ak8GenJets_*_*",
#		)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '90X_upgrade2017_realistic_v6_C1', '')

# Path and EndPath definitions
#process.HLTriggerFinalPath = cms.Path(process.hltGtStage2Digis+process.hltScalersRawToDigi+process.hltFEDSelector+process.hltTriggerSummaryAOD+process.hltTriggerSummaryRAW+process.hltBoolFalse)
#process.HLTriggerFirstPath = cms.Path(process.hltDummyConditions+process.hltGetRaw+process.hltBoolFalse)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)


#### My Analyzer
process.demo = cms.EDAnalyzer('TriggerEfficiencyPlots',
                              recoJets = cms.InputTag("ak4PFJetsCHS"),
                              primaryVertex = cms.InputTag("offlinePrimaryVertices"),
			      triggerPath  = cms.string("HLT_PFHT900_v6"),
			      minHT	   = cms.double( 900.0 ),
			      minPt	   = cms.double( 0.0 ),
			      minMass	  = cms.double( 0.0 ),
                              triggerResults = cms.InputTag("TriggerResults::HLT2"),
			      triggerObjects = cms.InputTag('hltTriggerSummaryAOD'),
                              #et_Filter = cms.InputTag('hltEG27L1SingleEGOrEtFilter','','HLT2'),
			      )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( "out.root" )
                                   )
process.demo_step = cms.EndPath(process.demo)


# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step, process.demo_step])
#process.schedule.extend([process.endjob_step,process.demo_step])

# customisation of the process.

# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforMC 

#call to customisation function customizeHLTforMC imported from HLTrigger.Configuration.customizeHLTforMC
process = customizeHLTforMC(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
