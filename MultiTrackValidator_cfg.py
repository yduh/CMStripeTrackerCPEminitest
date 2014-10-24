import FWCore.ParameterSet.Config as cms

process = cms.Process("MULTITRACKVALIDATOR")

# message logger
process.MessageLogger = cms.Service("MessageLogger",
     default = cms.untracked.PSet( limit = cms.untracked.int32(10) )
)


#Adding SimpleMemoryCheck service:
process.SimpleMemoryCheck=cms.Service("SimpleMemoryCheck",
                                   ignoreTotal=cms.untracked.int32(1),
                                   oncePerEventMode=cms.untracked.bool(True)
)

process.Timing = cms.Service("Timing"
    ,summaryOnly = cms.untracked.bool(True)
)

# source
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
#source = cms.Source ("PoolSource",fileNames = readFiles)
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-RECO/PRE_LS172_V11-v1/00000/5485433C-A93F-E411-8025-0026189437EC.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-RECO/PRE_LS172_V11-v1/00000/5C4CAD9E-A43F-E411-9CE8-003048FFD76E.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-RECO/PRE_LS172_V11-v1/00000/A613C082-A13F-E411-8904-00248C0BE005.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-RECO/PRE_LS172_V11-v1/00000/B001AC46-A93F-E411-ADD2-002618943869.root'
#        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/3222BBA4-8F3F-E411-BA7C-0026189438AD.root'
#        '/RelValQCD_Pt_3000_3500_13/CMSSW_7_2_0_pre6-PRE_LS172_V11-v1/GEN-SIM-DIGI-RAW-HLTDEBUG'
#       '/store/relval/CMSSW_7_2_0_pre6/RelValProdQCD_Pt_3000_3500_13/GEN-SIM-RAW/PRE_LS172_V11-v1/00000/6E65CAF8-A73F-E411-943E-0025905B857C.root'
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/504CC6BD-37D1-E311-BF1C-00248C55CC40.root'
#       '/store/relval/CMSSW_7_1_0/RelValTTbar_13/GEN-SIM-RECO/PU25ns_POSTLS171_V15-v1/00000/12CAFE96-F9FE-E311-B68B-0025905964CC.root'
                  ] )


secFiles.extend( [
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/3222BBA4-8F3F-E411-BA7C-0026189438AD.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/44519064-913F-E411-B45F-0025905B860C.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/4E1B9331-8E3F-E411-A242-0026189438B0.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/94DFDD7D-923F-E411-8521-0025905A6126.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/C4905E6D-913F-E411-8CD8-0025905A609E.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/D896A1AC-953F-E411-AAFD-0025905A60D6.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/EEC8A359-8F3F-E411-B711-0025905B85D8.root',
        '/store/relval/CMSSW_7_2_0_pre6/RelValQCD_Pt_3000_3500_13/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_LS172_V11-v1/00000/FC528EA8-953F-E411-9AE9-0025905A6134.root'

#        '/store/relval/CMSSW_7_2_0_pre6/RelValProdQCD_Pt_3000_3500_13/GEN-SIM-RAW/PRE_LS172_V11-v1/00000/82DF1228-A23F-E411-9A99-0025905A60D0.root',
#        '/store/relval/CMSSW_7_2_0_pre6/RelValProdQCD_Pt_3000_3500_13/GEN-SIM-RAW/PRE_LS172_V11-v1/00000/8EC38703-943F-E411-8E8D-0025905A6118.root',
#        '/store/relval/CMSSW_7_2_0_pre6/RelValProdQCD_Pt_3000_3500_13/GEN-SIM-RAW/PRE_LS172_V11-v1/00000/EC96736B-A53F-E411-A4F6-0025905A48E4.root',
#        '/store/relval/CMSSW_7_2_0_pre6/RelValProdQCD_Pt_3000_3500_13/GEN-SIM-RAW/PRE_LS172_V11-v1/00000/FA127F00-A83F-E411-B495-0025905A60DE.root'

#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/504CC6BD-37D1-E311-BF1C-00248C55CC40.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/68C00613-43D1-E311-91F4-00248C55CC62.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/6E6ED860-97D1-E311-8531-0025905A6118.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/842CC4B1-4FD1-E311-9E6B-0025905A60AA.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/8EEB4CBC-52D1-E311-BDD1-0025905A6080.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/ACDED197-54D1-E311-B39D-002590596486.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/EC01DCAE-3ED1-E311-A8D8-002618943875.root'

#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/9E420320-EFFE-E311-AF6C-0026189438CC.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/1C86C22E-F1FE-E311-BFF9-002354EF3BDE.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/34143955-EFFE-E311-82E6-0025905A6104.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/44F3997B-F1FE-E311-8A94-002618FDA208.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/54B6EB62-F4FE-E311-A5CF-0025905A6104.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/60C85922-EFFE-E311-9937-002354EF3BDD.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/7A883CA4-F1FE-E311-BA87-0025905A60A0.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/8A16120E-F1FE-E311-A2E8-0025905A6110.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/A4C4137F-F2FE-E311-82BC-0025905A6136.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/B05AA00F-F2FE-E311-BA9F-002618943978.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/C0347495-EFFE-E311-9B7D-003048FFD728.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/C82CD020-EFFE-E311-9894-00261894389F.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/CA3E4B23-EFFE-E311-87D2-002618943943.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/D2F1A740-F1FE-E311-8BBD-0025905822B6.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/E4D57925-EFFE-E311-BA2E-0025905A48B2.root',
#       '/store/relval/CMSSW_7_1_0_pre7/RelValQCD_Pt_3000_3500/GEN-SIM-DIGI-RAW-HLTDEBUG/PRE_STA71_V3-v1/00000/EAE281B4-EFFE-E311-96E1-0025905A6090.root'
                 ] )
process.source = source
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(400) )

### conditions
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:startup', '')
process.GlobalTag.globaltag = cms.string('PRE_LS172_V11::All')

### standard includes
process.load('Configuration/StandardSequences/Services_cff')
process.load('Configuration.StandardSequences.Geometry_cff')
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load('Configuration.StandardSequences.EndOfProcess_cff')


### validation-specific includes
#process.load("SimTracker.TrackAssociation.TrackAssociatorByHits_cfi")
process.load("SimTracker.TrackAssociation.quickTrackAssociatorByHits_cfi")
process.load("SimTracker.TrackAssociation.trackingParticleRecoTrackAsssociation_cfi")
process.load("Validation.RecoTrack.cuts_cff")
process.load("Validation.RecoTrack.MultiTrackValidator_cff")
process.load("DQMServices.Components.EDMtoMEConverter_cff")
process.load("Validation.Configuration.postValidation_cff")
process.quickTrackAssociatorByHits.SimToRecoDenominator = cms.string('reco')




########### configuration MultiTrackValidator ########
process.multiTrackValidator.associators = ['quickTrackAssociatorByHits']
process.multiTrackValidator.skipHistoFit=cms.untracked.bool(False)
#process.cutsRecoTracks.quality = cms.vstring('','highPurity')
#process.cutsRecoTracks.quality = cms.vstring('')
process.multiTrackValidator.label = ['cutsRecoTracks']
process.multiTrackValidator.useLogPt=cms.untracked.bool(True)
process.multiTrackValidator.minpT = cms.double(0.1)
process.multiTrackValidator.maxpT = cms.double(3000.0)
process.multiTrackValidator.nintpT = cms.int32(40)
process.multiTrackValidator.UseAssociators = cms.bool(True)


process.load("Validation.RecoTrack.cuts_cff")
process.cutsRecoTracks.quality = cms.vstring('highPurity')
#process.cutsRecoTracks.ptMin    = cms.double(0.5)
#process.cutsRecoTracks.minHit   = cms.int32(10)
#process.cutsRecoTracks.minRapidity  = cms.int32(-1.0)
#process.cutsRecoTracks.maxRapidity  = cms.int32(1.0)

process.quickTrackAssociatorByHits.useClusterTPAssociation = cms.bool(True)
process.load("SimTracker.TrackerHitAssociation.clusterTpAssociationProducer_cfi")

process.validation = cms.Sequence(
    process.tpClusterProducer *
    process.multiTrackValidator
)

# paths
process.val = cms.Path(
      process.cutsRecoTracks
    * process.validation
)

# Output definition
process.DQMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    outputCommands = process.DQMEventContent.outputCommands,
    fileName = cms.untracked.string('file:MTV_inDQM_test1.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('DQM')
    )
)

process.endjob_step = cms.EndPath(process.endOfProcess)
process.DQMoutput_step = cms.EndPath(process.DQMoutput)


process.schedule = cms.Schedule(
      process.val,process.endjob_step,process.DQMoutput_step
)

process.options = cms.untracked.PSet(
    numberOfThreads = cms.untracked.uint32(8),
    numberOfStreams = cms.untracked.uint32(8),
    wantSummary = cms.untracked.bool(True)
)



