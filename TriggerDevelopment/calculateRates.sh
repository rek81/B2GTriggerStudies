#nominal=HLT_PFHT900_v4
#nominalRate="13.23"
#nominal=HLT_PFHT750_4JetPt50_v6
#nominalRate="19.8296"
#nominal=HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v3
#nominalRate="28.82"
#nominal=HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v6
#nominalRate="19.15"
nominal=HLT_AK8PFJet360_TrimMass30_v5
nominalRate="9.51"
totalEvtNominal=`awk '{ sum+=$3 } END {print sum}' ${nominal}*`
totalPassNominal=`awk '{ sum+=$6 } END {print sum}' ${nominal}*`

listTriggers="HLT_AK8PFJet360_TrimMass30_v5
	HLT_AK8PFJet360_TrimMass30_Jet380_v1
	HLT_AK8PFJet360_TrimMass30_Jet400_v1
	HLT_AK8PFJet360_TrimMass30_Jet420_v1
	HLT_AK8PFJet360_TrimMass30_Jet440_v1
	HLT_AK8PFJet360_TrimMass30_Jet460_v1"
#listTriggers="HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_v6
#	HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_HT750_v1
#	HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_HT800_v1
#	HLT_AK8PFHT700_TrimR0p1PT0p03Mass50_HT850_v1"
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_v4
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT650_v1
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT700_v1
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT750_v1
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT800_v1
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT850_v1
#	HLT_AK8PFHT600_TrimR0p1PT0p03Mass50_BTagCSV_p20_HT900_v1
#	HLT_PFHT750_4JetPt50_v6
#	HLT_PFHT750_4JetPt50_mod_v6
#	HLT_PFHT750_4JetPt50_mod_Pt60_v1
#	HLT_PFHT750_4JetPt50_mod_Pt70_v1
#	HLT_PFHT750_4JetPt50_mod_Pt80_v1
#	HLT_PFHT750_4JetPt50_mod_Pt90_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_v3
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt300Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt320Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt340Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt300Pt220_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt300Pt240_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt300Pt260_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt320Pt220_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt320Pt240_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_Pt320Pt260_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v3
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt340Pt200_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt220_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt240_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt260_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt220_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt240_v1
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt260_v1
#	HLT_PFHT800_v5"
#listTriggers="HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt220_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt240_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt300Pt260_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt220_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt240_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt320Pt260_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_Pt340Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p20_v3_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt300Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt300Pt220_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt300Pt240_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt300Pt260_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt320Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt320Pt220_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt320Pt240_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt320Pt260_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_Pt340Pt200_v1_info.txt
#	HLT_AK8DiPFJet280_200_TrimMass30_BTagCSV_p56_v1_info.txt"


for trigger in $listTriggers; do
	
	totalEvtNew=`awk '{ sum+=$3 } END {print sum}' ${trigger}*`
	totalPassNew=`awk '{ sum+=$6 } END {print sum}' ${trigger}*`

	#echo ${totalEvtNominal}, ${totalPassNominal}
	#echo ${totalEvtNew}, ${totalPassNew}
	rate=`bc -l <<< $(echo "${nominalRate}"*"${totalPassNew} / ${totalPassNominal}" )`
	echo ${trigger} Rate ${rate}

done
