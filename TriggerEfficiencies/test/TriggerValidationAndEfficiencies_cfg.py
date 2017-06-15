import FWCore.ParameterSet.Config as cms

from FWCore.ParameterSet.VarParsing import VarParsing

###############################
####### Parameters ############
###############################

options = VarParsing ('python')

options.register('RUN', 
		'JetHT_Run2016C',
		VarParsing.multiplicity.singleton,
		VarParsing.varType.string,
		"name"
		)


options.parseArguments()

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

#NAME = options.RUN
NAME = 'SingleMuon-Run2017A'

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/4C85F093-654C-E711-99AA-02163E01A203.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/92ED5B44-6E4C-E711-A6FF-02163E011AC8.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/A04BCF64-734C-E711-9DD7-02163E019D14.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/A4DDC7F2-794C-E711-9AE1-02163E01A20B.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/BE9B75D5-614C-E711-BD09-02163E01A4D3.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/C426AE34-894C-E711-9319-02163E019B6A.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/E4A6AF0C-7E4C-E711-903C-02163E0143F9.root',
       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/F4E4645B-6D4C-E711-87D1-02163E019DCC.root',

    ),
   #lumisToProcess = cms.untracked.VLuminosityBlockRange('275657:1-275657:max'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( options.maxEvents ) )

process.TFileService=cms.Service("TFileService",fileName=cms.string( 'TriggerValAndEff_'+NAME+'.root' ) )

process.PFHTAK4jetsriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		#baseTrigger = cms.string("HLT_PFHT510"),
		baseTrigger = cms.string("HLT_Mu50"),
		triggerPass = cms.vstring([ "HLT_PFHT1050" ] ), 
		recoJets = cms.InputTag("slimmedJets"),
		AK8jets = cms.bool( False )
)

process.PFHTAK8jetsriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		#baseTrigger = cms.string("HLT_PFHT510"),
		baseTrigger = cms.string("HLT_Mu50"),
		triggerPass = cms.vstring([ "HLT_PFHT1050" ] ), 
		#recoJets = cms.InputTag("slimmedJets"),
		#AK8jets = cms.bool( False )
		recoJets = cms.InputTag("slimmedJetsAK8"),
		AK8jets = cms.bool( True )
)

process.PFHTAK4jets650TrimMass50 = process.PFHTAK4jetsriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_PFHTAK4jets650_TrimR0p1PT0p03Mass50"]),
		)


process.p = cms.Path(
		process.PFHTAK4jetsriggerEfficiency
		* process.PFHTAK8jetsriggerEfficiency
		#* process.PFHTAK4jets650TrimMass50
		)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
