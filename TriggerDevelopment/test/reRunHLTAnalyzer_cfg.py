import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run2_mc', '')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.options = cms.untracked.PSet( allowUnscheduled = cms.untracked.bool(True) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:reRunHLTwithAOD.root'
    )
)

##### Create puppi jets with softdrop
#from JMEAnalysis.JetToolbox.jetToolbox_cff import jetToolbox
#jetToolbox( process, 'ak8', 'jetSequence', 'out', PUMethod='Puppi', miniAOD=False, addSoftDrop=True )   ### For example

process.demo = cms.EDAnalyzer('TriggerEfficiencyPlots',
                              recoJets = cms.InputTag("ak4PFJetsCHS"),
                              #patJets = cms.InputTag("selectedPatJetsAK8PFPuppi"),
                              primaryVertex = cms.InputTag("offlinePrimaryVertices"),
			      triggerPath  = cms.string("HLT_PFHT900_v6"),
			      minHT	   = cms.double( 900.0 ),
			      minPt	   = cms.double( 0.0 ),
			      minMass	  = cms.double( 0.0 ),
                              triggerResults = cms.InputTag("TriggerResults::HLT2"),
			      #triggerObjects = cms.InputTag('hltTriggerSummaryAOD'),
			      triggerObjects = cms.InputTag('hltTriggerSummaryAOD'),
			      htHLT = cms.InputTag('hltAK8PFJets::HLT2'),
			      METFilter = cms.InputTag('hltPFHT900Jet30'),
			      )

process.TFileService = cms.Service("TFileService",
                                   fileName = cms.string( "out.root" )
                                   )

process.p = cms.Path(process.demo)
