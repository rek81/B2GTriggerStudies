// system include files
#include <memory>
#include <cmath>
#include <TH1.h>
#include <TH2.h>
#include <TLorentzVector.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include "DataFormats/Math/interface/deltaR.h"
#include "HLTrigger/HLTcore/interface/HLTConfigProvider.h"
#include "FWCore/Common/interface/TriggerNames.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/HLTReco/interface/TriggerObject.h"
#include "DataFormats/HLTReco/interface/TriggerEvent.h"
#include "DataFormats/PatCandidates/interface/TriggerObjectStandAlone.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "B2GTriggerStudies/TriggerEfficiencies/interface/CommonVariablesStructure.h"

using namespace edm;
using namespace std;

class TriggerValidationAndEfficiencies : public EDAnalyzer {

	public:
		explicit TriggerValidationAndEfficiencies(const ParameterSet&);
      		static void fillDescriptions(ConfigurationDescriptions & descriptions);
		~TriggerValidationAndEfficiencies() {}

	private:
		virtual void analyze(const Event&, const EventSetup&) override;
      		virtual void beginJob() override;

	EDGetTokenT<TriggerResults> triggerBits_;
	EDGetTokenT<pat::TriggerObjectStandAloneCollection> triggerObjects_;
	EDGetTokenT<pat::PackedTriggerPrescales> triggerPrescales_;
	EDGetTokenT<pat::JetCollection> jetToken_;
	string baseTrigger_;
      	vector<string> triggerPass_;
	string hltObjectPt_;
	string hltObjectMass_;
	double recojetPt_;
	bool AK8jets_;

	Service<TFileService> fs_;
	map< string, TH1D* > histos1D_;
	map< string, TH2D* > histos2D_;
};

TriggerValidationAndEfficiencies::TriggerValidationAndEfficiencies(const ParameterSet& iConfig):
	triggerBits_(consumes<TriggerResults>(iConfig.getParameter<InputTag>("bits"))),
	triggerObjects_(consumes<pat::TriggerObjectStandAloneCollection>(iConfig.getParameter<InputTag>("objects"))),
	triggerPrescales_(consumes<pat::PackedTriggerPrescales>(iConfig.getParameter<InputTag>("prescales"))),
	jetToken_(consumes<pat::JetCollection>(iConfig.getParameter<InputTag>("recoJets")))
{
	baseTrigger_ = iConfig.getParameter<string>("baseTrigger");
	triggerPass_ = iConfig.getParameter<vector<string>>("triggerPass");
	hltObjectPt_ = iConfig.getParameter<string>("hltObjectPt");
	hltObjectMass_ = iConfig.getParameter<string>("hltObjectMass");
	recojetPt_ = iConfig.getParameter<double>("recojetPt");
	AK8jets_ = iConfig.getParameter<bool>("AK8jets");
}

void TriggerValidationAndEfficiencies::analyze(const Event& iEvent, const EventSetup& iSetup) {

	Handle<TriggerResults> triggerBits;
	Handle<pat::TriggerObjectStandAloneCollection> triggerObjects;
	Handle<pat::PackedTriggerPrescales> triggerPrescales;
	Handle<pat::JetCollection> jets;

	iEvent.getByToken(triggerBits_, triggerBits);
	iEvent.getByToken(triggerObjects_, triggerObjects);
	iEvent.getByToken(triggerPrescales_, triggerPrescales);
	iEvent.getByToken(jetToken_, jets);

	const TriggerNames &names = iEvent.triggerNames(*triggerBits);
	/*
	 * I dont understand why this does not work
  	bool baseTrigger = checkTriggerBitsMiniAOD( names, triggerBits, triggerPrescales, baseTrigger_, false );
  	bool ORTriggers = checkORListOfTriggerBitsMiniAOD( names, triggerBits, triggerPrescales, triggerPass_, true );
	//LogWarning("trigger fired") << "Based " << baseTrigger << "OR " << ORTriggers;
	*/

	bool baseTrigger = 0;
	bool ORTriggers = 0;
	vector<bool> triggersFired;
	for (unsigned int i = 0, n = triggerBits->size(); i < n; ++i) {
		//LogWarning("all triggers") << triggerNames.triggerName(i) << " " <<  triggerBits->accept(i) << " " << triggerPrescales->getPrescaleForIndex(i);
		if (TString(names.triggerName(i)).Contains(baseTrigger_) && (triggerBits->accept(i)))  baseTrigger = true;
		for (size_t t = 0; t < triggerPass_.size(); t++) {
			if (TString(names.triggerName(i)).Contains(triggerPass_[t]) && (triggerBits->accept(i))) triggersFired.push_back( true );
			else triggersFired.push_back( false );
		}
	}
	ORTriggers = any_of(triggersFired.begin(), triggersFired.end(), [](bool v) { return v; }); 
	triggersFired.clear();
	//LogWarning("trigger fired") << "Based " << baseTrigger << " OR " << ORTriggers;
	if ( TString(baseTrigger_).Contains("empty") ) baseTrigger = true;


	///// TO TEST HLT OBJECTS
	double hltPt = 0;
	double hltMass = 0;
	for (pat::TriggerObjectStandAlone obj : *triggerObjects) { // note: not "const &" since we want to call unpackPathNames
		obj.unpackPathNames(names);
		obj.unpackFilterLabels(iEvent, *triggerBits );
		for (unsigned h = 0; h < obj.filterLabels().size(); ++h){
			TString filterLabel = obj.filterLabels()[h];

			if ( filterLabel.Contains( hltObjectPt_ ) ) {
				cout << "\tTrigger object Pt:  pt " << obj.pt() 
									<< ", eta " << obj.eta() 
									<< ", phi " << obj.phi() 
									<< ", mass " << obj.mass() << endl;
				hltPt = obj.pt();
				histos1D_[ "hltObjectPt" ]->Fill( hltPt );
			}

			if ( filterLabel.Contains( hltObjectMass_ ) ) {
				/*cout << "\tTrigger object Mass:  pt " << obj.pt() 
									<< ", eta " << obj.eta() 
									<< ", phi " << obj.phi() 
									<< ", mass " << obj.mass() << endl; 
				*/
				hltMass = obj.mass();
				histos1D_[ "hltObjectMass" ]->Fill( hltMass );
			}
		}
	}
	if ( hltPt > 0 ) histos2D_[ "hltObjectPtvsMass" ]->Fill( hltPt, hltMass );
	////////////////////////////////////////////////////////////////////////////////////////////////////

	/// TRIGGER EFFICENCY
	if ( baseTrigger || ORTriggers ) {

		double HT = 0;
		int k = 0;
		for (const pat::Jet &jet : *jets) {

			if( jet.pt() < recojetPt_ ) continue;
			if( TMath::Abs(jet.eta()) > 2.5 ) continue;
			//LogWarning("jets") << jet.pt();
			HT += jet.pt();

			if (++k==1){
				histos1D_[ "jet1Mass" ]->Fill( jet.mass() );
				histos1D_[ "jet1Pt" ]->Fill( jet.pt() );

				if ( AK8jets_ ) {
					histos1D_[ "jet1SoftDropMass" ]->Fill( jet.userFloat( "ak8PFJetsPuppiSoftDropMass" ) );
					if ( baseTrigger ) {
						histos1D_[ "jet1SoftDropMassDenom" ]->Fill( jet.userFloat( "ak8PFJetsPuppiSoftDropMass" ) );
						histos1D_[ "jet1PtDenom" ]->Fill( jet.pt() );
						if ( ORTriggers ){
							histos1D_[ "jet1SoftDropMassPassing" ]->Fill( jet.userFloat( "ak8PFJetsPuppiSoftDropMass" ) );
							histos1D_[ "jet1PtPassing" ]->Fill( jet.pt() );
						}
					}
				}
			}

		}
		histos1D_[ "HT" ]->Fill( HT );
		
		if ( baseTrigger ) {
			histos1D_[ "HTDenom" ]->Fill( HT );

			if ( ORTriggers ){
				histos1D_[ "HTPassing" ]->Fill( HT );
			}
		}
	}
}

void TriggerValidationAndEfficiencies::beginJob() {

	histos1D_[ "hltObjectPt" ] = fs_->make< TH1D >( "hltObjectPt", "hltObjectPt", 2000, 0., 2000. );
	histos1D_[ "hltObjectMass" ] = fs_->make< TH1D >( "hltObjectMass", "hltObjectMass", 2000, 0., 2000. );

	histos2D_[ "hltObjectPtvsMass" ] = fs_->make< TH2D >( "hltObjectPtvsMass", "hltObjectPtvsMass", 2000, 0., 2000., 2000, 0., 2000. );

	histos1D_[ "jet1Mass" ] = fs_->make< TH1D >( "jet1Mass", "jet1Mass", 1000, 0., 1000. );
	histos1D_[ "jet1SoftDropMass" ] = fs_->make< TH1D >( "jet1SoftDropMass", "jet1SoftDropMass", 1000, 0., 1000. );
	histos1D_[ "jet1Pt" ] = fs_->make< TH1D >( "jet1Pt", "jet1Pt", 1000, 0., 1000. );
	histos1D_[ "HT" ] = fs_->make< TH1D >( "HT", "HT", 100, 0., 2000. );


	histos1D_[ "HTDenom" ] = fs_->make< TH1D >( "HTDenom", "HTDenom", 2000, 0., 2000. );
	histos1D_[ "HTPassing" ] = fs_->make< TH1D >( "HTPassing", "HTPassing", 2000, 0., 2000. );
	histos1D_[ "jet1SoftDropMassDenom" ] = fs_->make< TH1D >( "jet1SoftDropMassDenom", "jet1SoftDropMassDenom", 1000, 0., 1000. );
	histos1D_[ "jet1SoftDropMassPassing" ] = fs_->make< TH1D >( "jet1SoftDropMassPassing", "jet1SoftDropMassPassing", 1000, 0., 1000. );
	histos1D_[ "jet1PtDenom" ] = fs_->make< TH1D >( "jet1PtDenom", "jet1PtDenom", 1000, 0., 1000. );
	histos1D_[ "jet1PtPassing" ] = fs_->make< TH1D >( "jet1PtPassing", "jet1PtPassing", 1000, 0., 1000. );


	///// Sumw2 all the histos
	for( auto const& histo : histos1D_ ) histos1D_[ histo.first ]->Sumw2();
	for( auto const& histo : histos2D_ ) histos2D_[ histo.first ]->Sumw2();
}

void TriggerValidationAndEfficiencies::fillDescriptions(ConfigurationDescriptions & descriptions) {

	ParameterSetDescription desc;
	desc.add<InputTag>("bits", 	InputTag("TriggerResults", "", "HLT"));
	desc.add<InputTag>("prescales", 	InputTag("patTrigger", "", "RECO"));
	desc.add<InputTag>("objects", 	InputTag("slimmedPatTrigger"));
	desc.add<string>("baseTrigger", 	"HLT_PFHT800");
	desc.add<string>("hltObjectPt", 	"hltPFHT1050Jet30");
	desc.add<string>("hltObjectMass", 	"hltPFHT1050Jet30");
	desc.add<double>("recojetPt", 	50);
	desc.add<bool>("AK8jets", 	true);
	desc.add<InputTag>("recoJets", 	InputTag("slimmedJetsAK8"));
	vector<string> HLTPass;
	HLTPass.push_back("HLT_AK8PFHT650_TrimR0p1PT0p03Mass50");
	desc.add<vector<string>>("triggerPass",	HLTPass);
	descriptions.addDefault(desc);
}
      
//define this as a plug-in
DEFINE_FWK_MODULE(TriggerValidationAndEfficiencies);
