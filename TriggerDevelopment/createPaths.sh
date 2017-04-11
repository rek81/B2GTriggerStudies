./path_maker.py -i hlt_B2GTriggers.py -p HLT_AK8PFJet360eta2p4_TrimMass30_v1 -c "hltPreAK8PFJet360eta2p4TrimMass30.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360eta2p4TrimModMass30.MinPt=cms.double( 340.0 )" -r "Pt340" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet360eta2p4_TrimMass30_v1 -c "hltPreAK8PFJet360eta2p4TrimMass30.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360eta2p4TrimModMass30.MinPt=cms.double( 320.0 )" -r "Pt320" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet360eta2p4_TrimMass30_v1 -c "hltPreAK8PFJet360eta2p4TrimMass30.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360eta2p4TrimModMass30.MinPt=cms.double( 300.0 )" -r "Pt300" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass50pt200_v1 -c "hltPreAK8PFHT800TrimMass50pt200.offset=cms.uint32( 0 )"  "hltAK8Ht700.MinHt=cms.vdouble( 550.0 )"   "hltAK8PFHT800pt200.minHt=cms.vdouble( 750.0 )" -r "HT750" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass50pt200_v1 -c "hltPreAK8PFHT800TrimMass50pt200.offset=cms.uint32( 0 )"  "hltAK8Ht700.MinHt=cms.vdouble( 500.0 )"   "hltAK8PFHT800pt200.minHt=cms.vdouble( 700.0 )" -r "HT700" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass50pt200_v1 -c "hltPreAK8PFHT800TrimMass50pt200.offset=cms.uint32( 0 )"  "hltAK8Ht700.MinHt=cms.vdouble( 650.0 )"   "hltAK8PFHT800pt200.minHt=cms.vdouble( 850.0 )" -r "HT850" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFHT800_TrimMass50pt200_v1 -c "hltPreAK8PFHT800TrimMass50pt200.offset=cms.uint32( 0 )"  "hltAK8Ht700.MinHt=cms.vdouble( 700.0 )"   "hltAK8PFHT800pt200.minHt=cms.vdouble( 900.0 )" -r "HT900" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFHT800_TrimMass50pt200_v1 -c "hltPreAK8PFHT800TrimMass50pt200.offset=cms.uint32( 0 )"  "hltAK8Ht700.MinHt=cms.vdouble( 750.0 )"   "hltAK8PFHT800pt200.minHt=cms.vdouble( 950.0 )" -r "HT950" -o hlt_tmp1.py

