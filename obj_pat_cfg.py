# $Id: obj_pat_cfg.py,v 1.1 2012/06/19 02:58:15 sakuma Exp $

##____________________________________________________________________________||
from PhysicsTools.PatAlgos.patTemplate_cfg import *

##____________________________________________________________________________||
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))
process.MessageLogger.cerr.FwkReport.reportEvery = 10

##____________________________________________________________________________||
from PhysicsTools.PatAlgos.tools.pfTools import *
switchToPFMET(process, input=cms.InputTag('pfMet'))

##____________________________________________________________________________||
process.source = cms.Source(
    "PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/cms/Tutorials/TWIKI_DATA/MET/TTJets_AODSIM_532_numEvent100.root'
        )
    )

##____________________________________________________________________________||
process.p = cms.Path(
    process.patDefaultSequence
)

##____________________________________________________________________________||
process.out.fileName = cms.untracked.string('patTuple.root')
process.out.outputCommands = cms.untracked.vstring(
    'drop *',
    'keep patMETs_patMETs__PAT',
    ) 

##____________________________________________________________________________||
