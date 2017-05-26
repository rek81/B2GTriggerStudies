// system include files
#include <memory>
#include <vector>
#include <TLorentzVector.h>
#include <TVector3.h>
#include <TH1.h>
#include <TTree.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Math/interface/LorentzVector.h"

#include "FWCore/Framework/interface/GetterOfProducts.h"
#include "FWCore/Framework/interface/ProcessMatch.h"

// Jet Corrections
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"

using namespace edm;
using namespace std;



inline bool checkTriggerBits( Handle<vector<string>> triggerNames, Handle<vector<float>> triggerBits, TString HLTtrigger  ){

	float triggerFired = 0;
	for (size_t t = 0; t < triggerNames->size(); t++) {
		if ( TString( (*triggerNames)[t] ).Contains( HLTtrigger ) ) {
			triggerFired = (*triggerBits)[t];
			//LogWarning("triggerbit") << (*triggerNames)[t] << " " <<  (*triggerBits)[t];
		}
	}
	if ( HLTtrigger.Contains( "NOTRIGGER" ) ) triggerFired = 1;

	return triggerFired;
}	

inline bool checkORListOfTriggerBits( Handle<vector<string>> triggerNames, Handle<vector<float>> triggerBits, vector<string>  triggerPass  ){

	vector<bool> triggersFired;
	for (size_t t = 0; t < triggerPass.size(); t++) {
		bool triggerFired = checkTriggerBits( triggerNames, triggerBits, triggerPass[t] );
		triggersFired.push_back( triggerFired );
		//if ( triggerFired ) LogWarning("test") << triggerPass[t] << " " << triggerFired;
	}
	
	bool ORTriggers = !none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	//if( ORTriggers ) LogWarning("OR") << std::none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	
	return ORTriggers;
}

inline bool checkTriggerBitsMiniAOD( TriggerNames triggerNames, Handle<TriggerResults> triggerBits, TString HLTtrigger  ){

  	bool triggerFired = 0;
	for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
		if (TString(triggerNames.triggerName(i)).Contains(HLTtrigger) && (triggerBits->accept(i))) {
		       	triggerFired=1;
			//LogWarning("test") << "Trigger " << triggerNames.triggerName(i) << ": " << (triggerBits->accept(i) ? "PASS" : "fail (or not run)") ;
		}
	}

	return triggerFired;
}	

inline bool checkORListOfTriggerBitsMiniAOD( TriggerNames triggerNames, Handle<TriggerResults> triggerBits, vector<string>  triggerPass  ){

	vector<bool> triggersFired;
	for (size_t t = 0; t < triggerPass.size(); t++) {
		bool triggerFired = checkTriggerBitsMiniAOD( triggerNames, triggerBits, triggerPass[t] );
		triggersFired.push_back( triggerFired );
		//if ( triggerFired ) LogWarning("test") << triggerPass[t] << " " << triggerFired;
	}
	
	bool ORTriggers = !none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	//if( ORTriggers ) LogWarning("OR") << std::none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	
	return ORTriggers;
}

/*inline bool checkTriggerBitsAOD( HLTConfigProvider hltConfig, TString HLTtrigger ){

  	bool triggerFired = 0;
	triggerBit = -1;
	for (size_t j = 0; j < hltConfig.triggerNames().size(); j++) {
		std::cout << TString(hltConfig.triggerNames()[j]) << std::endl;
		if (TString(hltConfig.triggerNames()[j]).Contains(triggerPath)) triggerBit = j;
	}
	std::cout << triggerBit << std::endl;
	if (triggerBit == -1) cout << "HLT path not found" << endl;

	for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
		if (TString(triggerNames.triggerName(i)).Contains(HLTtrigger) && (triggerBits->accept(i))) {
		       	triggerFired=1;
			//LogWarning("test") << "Trigger " << triggerNames.triggerName(i) << ": " << (triggerBits->accept(i) ? "PASS" : "fail (or not run)") ;
		}
	}

	return triggerFired;
}	

inline bool checkORListOfTriggerBitsAOD( TriggerNames triggerNames, Handle<TriggerResults> triggerBits, vector<string>  triggerPass  ){

	vector<bool> triggersFired;
	for (size_t t = 0; t < triggerPass.size(); t++) {
		bool triggerFired = checkTriggerBitsMiniAOD( triggerNames, triggerBits, triggerPass[t] );
		triggersFired.push_back( triggerFired );
		//if ( triggerFired ) LogWarning("test") << triggerPass[t] << " " << triggerFired;
	}
	
	bool ORTriggers = !none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	//if( ORTriggers ) LogWarning("OR") << std::none_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	
	return ORTriggers;
}
*/
