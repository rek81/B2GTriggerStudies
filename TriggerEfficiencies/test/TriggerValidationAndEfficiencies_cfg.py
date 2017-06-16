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

NAME = options.RUN
#NAME = 'SingleMuon-Run2017A'

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/4C85F093-654C-E711-99AA-02163E01A203.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/92ED5B44-6E4C-E711-A6FF-02163E011AC8.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/A04BCF64-734C-E711-9DD7-02163E019D14.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/A4DDC7F2-794C-E711-9AE1-02163E01A20B.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/BE9B75D5-614C-E711-BD09-02163E01A4D3.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/C426AE34-894C-E711-9319-02163E019B6A.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/E4A6AF0C-7E4C-E711-903C-02163E0143F9.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/173/00000/F4E4645B-6D4C-E711-87D1-02163E019DCC.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/172/00000/66D29210-674C-E711-AFD2-02163E01A270.root',
#       '/store/data/Run2017A/SingleMuon/MINIAOD/PromptReco-v2/000/296/174/00000/F89D7E25-7C4C-E711-B14D-02163E01A270.root',
	
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/06561401-594C-E711-8978-02163E01A3AD.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/26A5BDE8-5D4C-E711-8C7D-02163E01A436.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/4E0A99BD-614C-E711-A6B3-02163E019E8D.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/62E27FA0-514C-E711-B153-02163E01A23C.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/8480DC3F-684C-E711-AA6E-02163E019DC8.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/84DAF470-564C-E711-956E-02163E019E2E.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/B0018943-5B4C-E711-88AA-02163E011AC8.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/C6968DD2-534C-E711-A255-02163E0138BF.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/D0122F4E-324D-E711-A46D-02163E019B54.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/174/00000/1A200418-144D-E711-A702-02163E019C36.root',
       '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/172/00000/AA96C0EB-554C-E711-8302-02163E01A32D.root',
    ),
   #lumisToProcess = cms.untracked.VLuminosityBlockRange('275657:1-275657:max'),
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32( options.maxEvents ) )

process.TFileService=cms.Service("TFileService",fileName=cms.string( 'TriggerValAndEff_'+NAME+'.root' ) )

process.PFHTAK4jetsTriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		baseTrigger = cms.string("HLT_PFJet40_v"),
		#baseTrigger = cms.string("HLT_IsoMu27_v"),
		triggerPass = cms.vstring([ "HLT_PFHT1050_v" ] ), 
		recoJets = cms.InputTag("slimmedJets"),
		AK8jets = cms.bool( False )
)

process.PFHTAK8jetsTriggerEfficiency = cms.EDAnalyzer('TriggerValidationAndEfficiencies',
		baseTrigger = cms.string("HLT_PFJet40_v"),
		#baseTrigger = cms.string("HLT_IsoMu27_v"),
		triggerPass = cms.vstring([ "HLT_PFHT1050_v" ] ), 
		#recoJets = cms.InputTag("slimmedJets"),
		#AK8jets = cms.bool( False )
		recoJets = cms.InputTag("slimmedJetsAK8"),
		AK8jets = cms.bool( True )
)

process.PFHTAK4jets650TrimMass50 = process.PFHTAK4jetsTriggerEfficiency.clone( 
		triggerPass = cms.vstring(["HLT_PFHTAK4jets650_TrimR0p1PT0p03Mass50"]),
		)


process.p = cms.Path(
		process.PFHTAK4jetsTriggerEfficiency
		* process.PFHTAK8jetsTriggerEfficiency
		#* process.PFHTAK4jets650TrimMass50
		)

process.MessageLogger.cerr.FwkReport.reportEvery = 10000
