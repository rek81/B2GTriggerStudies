./path_maker.py -i hlt_B2GTriggers_2016Data.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet360_SDMass00_v1 -c "hltPreAK8PFJet360SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass00.MinMass=cms.double( 60.0 )" -r "Mass60" -o hlt_tmp2.py

./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 10.0 )" -r "Mass10" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 20.0 )" -r "Mass20" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 30.0 )" -r "Mass30" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 40.0 )" -r "Mass40" -o hlt_tmp2.py
./path_maker.py -i hlt_tmp2.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 50.0 )" -r "Mass50" -o hlt_tmp1.py
./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet300_SDMass00_v1 -c "hltPreAK8PFJet300SDMass00.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet300SDMass00.MinMass=cms.double( 60.0 )" -r "Mass60" -o hlt_tmp2.py

#./path_maker.py -i hlt_tmp1.py -p HLT_AK8PFJet360_SDMass10_v1 -c "hltPreAK8PFJet360SDMass10.offset=cms.uint32( 0 )"  "hltAK8SinglePFJet360SDMass10.MinMass=cms.double( 00.0 )" "hltAK8SinglePFJet360SDMass10.MinMass=cms.double( 00.0 )" -r "Mass00" -o hlt_tmp2.py
