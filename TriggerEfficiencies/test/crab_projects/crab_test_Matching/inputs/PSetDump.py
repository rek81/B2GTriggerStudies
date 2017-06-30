import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/06561401-594C-E711-8978-02163E01A3AD.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/26A5BDE8-5D4C-E711-8C7D-02163E01A436.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/4E0A99BD-614C-E711-A6B3-02163E019E8D.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/62E27FA0-514C-E711-B153-02163E01A23C.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/8480DC3F-684C-E711-AA6E-02163E019DC8.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/84DAF470-564C-E711-956E-02163E019E2E.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/B0018943-5B4C-E711-88AA-02163E011AC8.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/C6968DD2-534C-E711-A255-02163E0138BF.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/173/00000/D0122F4E-324D-E711-A46D-02163E019B54.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/174/00000/1A200418-144D-E711-A702-02163E019C36.root', 
        '/store/data/Run2017A/JetHT/MINIAOD/PromptReco-v2/000/296/172/00000/AA96C0EB-554C-E711-8302-02163E01A32D.root')
)
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.PFHTAK4jets650TrimMass50 = cms.EDAnalyzer("TriggerValidationAndEfficiencies",
    AK8jets = cms.bool(False),
    baseTrigger = cms.string('HLT_PFJet40_v'),
    recoJets = cms.InputTag("slimmedJets"),
    triggerPass = cms.vstring('HLT_PFHTAK4jets650_TrimR0p1PT0p03Mass50')
)


process.PFHTAK4jetsTriggerEfficiency = cms.EDAnalyzer("TriggerValidationAndEfficiencies",
    AK8jets = cms.bool(False),
    baseTrigger = cms.string('HLT_PFJet40_v'),
    recoJets = cms.InputTag("slimmedJets"),
    triggerPass = cms.vstring('HLT_PFHT1050_v')
)


process.PFHTAK8jetsTriggerEfficiency = cms.EDAnalyzer("TriggerValidationAndEfficiencies",
    AK8jets = cms.bool(True),
    baseTrigger = cms.string('HLT_PFJet40_v'),
    recoJets = cms.InputTag("slimmedJetsAK8"),
    triggerPass = cms.vstring('HLT_PFHT1050_v')
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring('FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(10000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('INFO')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring('warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.TFileService = cms.Service("TFileService",
    fileName = cms.string('TriggerValAndEff_JetHT_Run2016C.root')
)


process.p = cms.Path(process.PFHTAK4jetsTriggerEfficiency+process.PFHTAK8jetsTriggerEfficiency)


