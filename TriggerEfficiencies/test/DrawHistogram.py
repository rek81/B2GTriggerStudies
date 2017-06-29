#!/usr/bin/env python
'''
File: DrawHistogram.py
Author: Alejandro Gomez Espinosa
Email: gomez@physics.rutgers.edu
Description: My Draw histograms. Check for options at the end.
'''

from ROOT import *
import time, os, math, sys
import argparse
import B2GTriggerStudies.TriggerEfficiencies.CMS_lumi as CMS_lumi 
import B2GTriggerStudies.TriggerEfficiencies.tdrstyle as tdrstyle

#gROOT.Reset()
gROOT.SetBatch()
gROOT.ForceStyle()
tdrstyle.setTDRStyle()

gStyle.SetOptStat(0)


def plotTriggerEfficiency( inFileSample, sample, triggerDenom, name, cut, xmin, xmax, xlabel, rebin, labX, labY, log):
	"""docstring for plot"""

	outputFileName = name+'_'+cut+'_'+triggerDenom+"_"+args.trigger+'_'+sample+'_'+'_TriggerEfficiency'+args.version+'.'+args.extension
	print 'Processing.......', outputFileName

	DenomOnly = inFileSample.Get( 'PFHT'+cut+'TriggerEfficiency/'+name+'Denom' ) #+cut ) 
	DenomOnly.Rebin(rebin)
	Denom = DenomOnly.Clone()
	PassingOnly = inFileSample.Get( 'PFHT'+cut+'TriggerEfficiency/'+name+'Passing' ) #+cut ) 
	PassingOnly.Rebin(rebin)
	Passing = PassingOnly.Clone()
	print Denom, Passing
	Efficiency = TGraphAsymmErrors( Passing, Denom, 'cp'  )
	#Efficiency = TEfficiency( Passing, Denom )

	binWidth = DenomOnly.GetBinWidth(1)

	legend=TLegend(0.50,0.75,0.90,0.90)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.04)

	DenomOnly.SetLineWidth(2)
	DenomOnly.SetLineColor(kRed-4)
	PassingOnly.SetLineWidth(2)
	PassingOnly.SetLineColor(kBlue-4)

	can = TCanvas('c1', 'c1',  10, 10, 750, 750 )
	pad1 = TPad("pad1", "Histo",0,0.46,1.00,1.00,-1)
	pad2 = TPad("pad2", "Efficiency",0,0.00,1.00,0.531,-1);
	pad1.Draw()
	pad2.Draw()

	pad1.cd()
	if log: pad1.SetLogy()

	legend.AddEntry( DenomOnly, triggerDenom+' (baseline trigger)', 'l' )
	legend.AddEntry( PassingOnly, args.trigger, 'l' )
	#DenomOnly.SetMinimum(10)
	DenomOnly.GetXaxis().SetRangeUser( xmin, xmax )
	DenomOnly.Draw('histe')
	DenomOnly.GetYaxis().SetTitleSize(0.06)
	DenomOnly.GetYaxis().SetTitleOffset(0.8)
	DenomOnly.GetYaxis().SetLabelSize(0.06)
	DenomOnly.GetXaxis().SetTitleOffset(0.8)
	DenomOnly.GetXaxis().SetTitleSize(0.06)
	DenomOnly.GetXaxis().SetLabelSize(0.05)
	PassingOnly.Draw('histe same')
	DenomOnly.GetYaxis().SetTitle( 'Events / '+str(binWidth) )

	CMS_lumi.CMS_lumi(pad1, 4, 0)
	legend.Draw()

	pad2.cd()
	pad2.SetTopMargin(0)
	pad2.SetBottomMargin(0.3)
	Efficiency.SetMarkerStyle(8)
	Efficiency.SetLineWidth(2)
	Efficiency.SetLineColor(kBlue-4)
	#Efficiency.SetFillStyle(1001)
	Efficiency.GetYaxis().SetTitle("Efficiency")
	Efficiency.GetYaxis().SetLabelSize(0.06)
	Efficiency.GetXaxis().SetLabelSize(0.06)
	Efficiency.GetYaxis().SetTitleSize(0.06)
	Efficiency.GetYaxis().SetTitleOffset(0.8)
	Efficiency.SetMinimum(-0.1)
	Efficiency.SetMaximum(1.1)
	Efficiency.GetXaxis().SetLimits( xmin, xmax )
	Efficiency.GetXaxis().SetTitle( xlabel )
	Efficiency.Draw()

	can.SaveAs( 'Plots/'+outputFileName.replace('.','Extended.') )
	del can

	#### Fitting
	#errF = TF1('errF', '0.5*(1+TMath::Erf((x-[0])/[1]))', 500, 1500 )
	#errF = TF1('errF', '0.5*(1+TMath::Erf(([0]*x-[1])/[2]))', 400, 1000 )  ## HT
	#errF = TF1('errF', '0.5*(1+TMath::Erf(([0]*x-[1])/[2]))', 0, 100 )  ## Mass
	#Efficiency.SetStatisticOption(TEfficiency.kFWilson)
	#for i in range(5): eff.Fit(errF, '+')
	#for i in range(5): Efficiency.Fit('errF', 'MIR')
	#print '&'*10, '900', errF.Eval(900)
	#print '&'*10, '1000', errF.Eval(1000)
	gStyle.SetOptFit(1)
	can1 = TCanvas('c1', 'c1',  10, 10, 750, 500 )
	Efficiency.SetMarkerStyle(8)
	Efficiency.SetMarkerColor(kGray)
	Efficiency.SetMinimum(-0.15)
	#Efficiency.SetMinimum(0.8)
	Efficiency.SetMaximum(1.15)
	Efficiency.GetXaxis().SetTitle( xlabel )
	Efficiency.GetYaxis().SetLabelSize(0.05)
	Efficiency.GetXaxis().SetLabelSize(0.05)
	Efficiency.GetYaxis().SetTitleSize(0.06)
	Efficiency.GetYaxis().SetTitleOffset(0.8)
	Efficiency.GetXaxis().SetTitleOffset(0.8)
	#Efficiency.GetXaxis().SetLimits( 400, 1200 )
	#Efficiency.GetXaxis().SetLimits( 700, 1050 )
	Efficiency.GetXaxis().SetLimits( xmin, xmax )
	Efficiency.Draw('AP')
	'''
	errF.SetLineColor(kRed)
	errF.SetLineWidth(2)
	errF.Draw('sames')
	can1.Update()
	st1 = Efficiency.GetListOfFunctions().FindObject("stats")
	st1.SetX1NDC(.60);
	st1.SetX2NDC(.90);
	st1.SetY1NDC(.20);
	st1.SetY2NDC(.50);
#	#eff.Draw("same")
	can1.Modified()
	'''
	
	'''
	rightmax = 1.2*PassingOnly.GetMaximum()
	rightmin = PassingOnly.GetMinimum()
	scale = gPad.GetUymax()/rightmax
	PassingOnly.SetLineColor(kBlue-5)
	PassingOnly.Scale( scale )
	PassingOnly.Draw( 'hist same' )
	#axis = TGaxis( gPad.GetUxmax(), gPad.GetUymin(), gPad.GetUxmax(), gPad.GetUymax(),-3,rightmax,710,"+L")
	axis = TGaxis( gPad.GetUxmax(), gPad.GetUymin(), gPad.GetUxmax(), gPad.GetUymax(),rightmin,rightmax,10,"+L")
	axis.SetTitle('Events / '+str(binWidth) )
	axis.SetTitleColor(kBlue-5)
	axis.SetTitleSize(0.06)
	axis.SetLabelSize(0.05)
	axis.SetTitleFont(42)
	axis.SetLabelFont(42)
	axis.SetLineColor(kBlue-5)
	axis.SetLabelColor(kBlue-5)
	axis.SetTitleOffset(0.7)
	axis.Draw()
	'''
	CMS_lumi.relPosX = 0.11
	CMS_lumi.cmsTextSize = 0.7
	CMS_lumi.extraOverCmsTextSize = 0.6
	CMS_lumi.CMS_lumi(can1, 4, 0)

	can1.SaveAs( 'Plots/'+outputFileName )
	del can1

	return Efficiency

def plotDiffEff( listOfEff, name ):
	"""docstring for plotDiffEff"""

	can = TCanvas('c1', 'c1',  10, 10, 750, 500 )

	legend=TLegend(0.60,0.25,0.90,0.40)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.04)

	dummy = 1
	for sample in listOfEff: 
		legend.AddEntry( listOfEff[ sample ], sample, 'l' )

		listOfEff[ sample ].SetMarkerStyle(8)
		listOfEff[ sample ].SetLineWidth(2)
		listOfEff[ sample ].SetLineColor(dummy)
		listOfEff[ sample ].GetYaxis().SetTitle("Efficiency")
		listOfEff[ sample ].GetYaxis().SetLabelSize(0.06)
		listOfEff[ sample ].GetXaxis().SetLabelSize(0.06)
		listOfEff[ sample ].GetYaxis().SetTitleSize(0.06)
		listOfEff[ sample ].GetYaxis().SetTitleOffset(0.8)
		listOfEff[ sample ].SetMinimum(0.8)
		listOfEff[ sample ].SetMaximum(1.05)
		#listOfEff[ sample ].GetXaxis().SetLimits( 850, 950 )
		listOfEff[ sample ].GetXaxis().SetLimits( 0, 200 )
		if dummy == 1:
			labelAxis( name, listOfEff[ sample ], 'Pruned')
			listOfEff[ sample ].Draw()
		else: 
			listOfEff[ sample ].Draw('same')
		dummy+=1

	legend.Draw('same')
	CMS_lumi.lumi_13TeV = ""
	CMS_lumi.relPosX = 0.11
	CMS_lumi.cmsTextSize = 0.7
	CMS_lumi.extraOverCmsTextSize = 0.6
	CMS_lumi.CMS_lumi(can, 4, 0)
	can.SaveAs( 'Plots/'+name+'_DiffEfficiencies.'+args.extension )
	del can


def plot2DTriggerEfficiency( inFileSample, dataset, triggerSel, triggerDenom, name, cut, xlabel, ylabel, Xmin, Xmax, rebinx, Ymin, Ymax, rebiny, labX, labY, PU ):
	"""docstring for plot"""

	outputFileName = name+'_'+cut+'_'+triggerDenom+"_"+triggerSel+'_'+dataset+'_'+'TriggerEfficiency'+args.version+'.'+args.extension
	print 'Processing.......', outputFileName

	print 'TriggerEfficiency'+triggerSel+'/'+name+'Denom_'+cut
	rawDenom = inFileSample.Get( 'TriggerEfficiency'+triggerSel+'/'+name+'Denom_'+cut )
	#profileDenom = rawDenom.ProfileX( name+'Denom_'+cut+'_pfy', 50, -1, 'o')
	#newDenom = TH1F( 'newDenom', 'newDenom', profileDenom.GetXaxis().GetNbins(), profileDenom.GetXaxis().GetBinLowEdge(1), profileDenom.GetXaxis().GetBinLowEdge(profileDenom.GetMaximumBin()+1) )
	#for i in range(1,profileDenom.GetXaxis().GetNbins()):
	#	print newDenom
	#	newDenom.SetBinContent( i, profileDenom.GetBinContent(i) )
	#	newDenom.SetBinError( i, profileDenom.GetBinError(i) )
	#newDenom.Rebin( rebinx )
	Denom = Rebin2D( rawDenom, rebinx, rebiny )

	rawPassing = inFileSample.Get( 'TriggerEfficiency'+triggerSel+'/'+name+'Passing_'+cut )
	#profilePassing = rawPassing.ProfileX( name+'Passing_'+cut+'_pfy', 50, -1, 'o')
	#newPassing = TH1F( 'newPassing', 'newPassing', profilePassing.GetXaxis().GetNbins(), profilePassing.GetXaxis().GetBinLowEdge(1), profilePassing.GetXaxis().GetBinLowEdge(profilePassing.GetMaximumBin()+1) )
	#for j in range(1,profilePassing.GetXaxis().GetNbins()):
	#	newPassing.SetBinContent( j, profilePassing.GetBinContent(j) )
	#	newPassing.SetBinError( j, profilePassing.GetBinError(j) )
	#newPassing.Rebin( rebinx )
	Passing = Rebin2D( rawPassing, rebinx, rebiny )

	
	'''
	if ( TEfficiency.CheckConsistency( Passing, Denom ) ): Efficiency = TEfficiency( Passing, Denom )
	else: 
		print '--- Passing and Denom are inconsistent.'
		#sys.exit(0)
	'''

	Efficiency = Denom.Clone() 
	Efficiency.Reset()
	Efficiency.Divide( Passing, Denom, 1, 1, 'B' )

	'''
	for i in range( Efficiency.GetNbinsX() ):
		for j in range( Efficiency.GetNbinsY() ):
			if Efficiency.GetXaxis().GetBinLowEdge(i) == 400: print '400: ', round( Efficiency.GetBinContent( i, j ),2), '\pm', round( Efficiency.GetBinError( i , j), 4 )
			if Efficiency.GetXaxis().GetBinLowEdge(i) == 500: print '500: ', round( Efficiency.GetBinContent( i, j ),2), '\pm', round( Efficiency.GetBinError( i , j), 4 )
			if Efficiency.GetXaxis().GetBinLowEdge(i) == 550: print '550: ', round( Efficiency.GetBinContent( i, j ),2), '\pm', round( Efficiency.GetBinError( i , j), 4 )
	'''
	#Efficiency.SetTitle( ';'+xlabel+';'+ ylabel )
	#eff = Efficiency.CreateHistogram()
	
	tdrStyle.SetPadRightMargin(0.12)
	can = TCanvas('c1', 'c1',  10, 10, 1000, 750 )
	gStyle.SetPaintTextFormat("4.2f")
	Efficiency.SetMarkerSize(0.01)
	Efficiency.SetMaximum(1)
	Efficiency.SetMinimum(0)
	Efficiency.Draw('colz')
	Efficiency.Draw('same text')
	#gPad.Update()
	Efficiency.GetYaxis().SetTitleOffset(1.0)
	Efficiency.SetMarkerSize(2)
	Efficiency.GetXaxis().SetRange( int(Xmin/(10.*rebinx)), int(Xmax/(10.*rebinx)) )
	Efficiency.GetXaxis().SetTitle( xlabel )
	Efficiency.GetYaxis().SetTitle( ylabel )
	Efficiency.GetYaxis().SetRange( int(Ymin/(10.*rebiny)), int(Ymax/(10.*rebiny)) )
	#gPad.Update()

	CMS_lumi.relPosX = 0.13
	CMS_lumi.CMS_lumi(can, 4, 0)

	can.SaveAs( 'Plots/'+outputFileName )
	del can

#	##### 1D Efficiency
#	newEfficiency = TGraphAsymmErrors( newPassing, newDenom, 'cp'  )
#	binWidth = rebinx
#
#	#legend=TLegend(0.50,0.75,0.90,0.90)
#	#legend.SetFillStyle(0)
#	#legend.SetTextSize(0.04)
#
#	#gStyle.SetOptFit(1)
#	can1 = TCanvas('can1', 'can1',  10, 10, 750, 500 )
#	newEfficiency.SetMarkerStyle(8)
#	newEfficiency.SetMarkerColor(kGray)
#	newEfficiency.SetMinimum(-0.15)
#	#newEfficiency.SetMinimum(0.7)
#	newEfficiency.SetMaximum(1.15)
#	newEfficiency.GetYaxis().SetLabelSize(0.05)
#	newEfficiency.GetXaxis().SetLabelSize(0.05)
#	newEfficiency.GetYaxis().SetTitleSize(0.06)
#	newEfficiency.GetYaxis().SetTitleOffset(0.8)
#	newEfficiency.GetXaxis().SetTitleOffset(0.8)
#	#newEfficiency.GetXaxis().SetLimits( 400, 1200 )
#	#newEfficiency.GetXaxis().SetLimits( 700, 1050 )
#	newEfficiency.GetXaxis().SetLimits( 0, 200 ) #xmin, xmax )
#	newEfficiency.Draw('AP')
#	labelAxis( name, newEfficiency, 'Pruned')
#	CMS_lumi.relPosX = 0.11
#	CMS_lumi.cmsTextSize = 0.7
#	CMS_lumi.extraOverCmsTextSize = 0.6
#	CMS_lumi.CMS_lumi(can1, 4, 0)
#
#	outputFileName = outputFileName.replace( 'jet1Pt', ''  )
#	can1.SaveAs( 'Plots/'+outputFileName )
#	del can1
#
#	return Efficiency


def diffplotTriggerEfficiency( inFileSamples, triggerSel, name, cut, xmin, xmax, rebin, labX, labY, log, PU ):
	"""docstring for plot"""

	outputFileName = name+'_'+cut+"_"+triggerSel+'_'+'_TriggerEfficiency'+args.version+'.'+args.extension
	print 'Processing.......', outputFileName

	diffEffDenom = {}
	diffEffPassing = {}
	diffEff = {}
	for sam in inFileSamples:
		diffEffDenom[ sam ] = inFileSamples[ sam ].Get( 'TriggerEfficiency'+triggerSel+'/'+name+'Denom_'+cut ) #cutDijet' ) #+cut )
		diffEffDenom[ sam ].Rebin(rebin)
		diffEffPassing[ sam ] = inFileSamples[ sam ].Get( 'TriggerEfficiency'+triggerSel+'/'+name+'Passing_'+cut ) #cutHT' ) #+cut )
		diffEffPassing[ sam ].Rebin(rebin)
		diffEff[ sam ] = TGraphAsymmErrors( diffEffPassing[sam], diffEffDenom[sam], 'cp'  )
		#Efficiency = TEfficiency( Passing, Denom )

	#binWidth = DenomOnly.GetBinWidth(1)

	legend=TLegend(0.50,0.75,0.90,0.90)
	legend.SetFillStyle(0)
	legend.SetTextSize(0.04)

	can1 = TCanvas('c1', 'c1',  10, 10, 750, 500 )
	dummy=1
	for q in diffEff:
		diffEff[q].SetMarkerStyle(8)
		diffEff[q].SetMarkerColor(dummy)
		legend.AddEntry( diffEff[ q ], q, 'pl' )
		dummy+=1

	diffEff[diffEff.iterkeys().next()].SetMinimum(0.8)
	diffEff[diffEff.iterkeys().next()].SetMaximum(1.15)
	diffEff[diffEff.iterkeys().next()].GetYaxis().SetLabelSize(0.05)
	diffEff[diffEff.iterkeys().next()].GetXaxis().SetLabelSize(0.05)
	diffEff[diffEff.iterkeys().next()].GetYaxis().SetTitleSize(0.06)
	diffEff[diffEff.iterkeys().next()].GetYaxis().SetTitleOffset(0.8)
	diffEff[diffEff.iterkeys().next()].GetXaxis().SetTitleOffset(0.8)
	diffEff[diffEff.iterkeys().next()].GetXaxis().SetLimits( xmin, xmax )
	diffEff[diffEff.iterkeys().next()].Draw('AP')
	for q in diffEff: diffEff[q].Draw("P same")
	labelAxis( name, diffEff[diffEff.iterkeys().next()], 'SoftDrop')
	CMS_lumi.relPosX = 0.11
	CMS_lumi.cmsTextSize = 0.7
	CMS_lumi.extraOverCmsTextSize = 0.6
	CMS_lumi.CMS_lumi(can1, 4, 0)
	legend.Draw()

	can1.SaveAs( 'Plots/'+outputFileName )
	del can1



if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-p', '--proc', action='store', default='1D', help='Process to draw, example: 1D, 2D, MC.' )
	parser.add_argument('-d', '--dataset', action='store', default='JetHT', help='Dataset: JetHT, SingleMuon, etc.' )
	parser.add_argument('-v', '--version', action='store', default='v01', help='Version of the files' )
	parser.add_argument('-C', '--cut', action='store', default='_cutDEta', help='cut, example: cutDEta' )
	parser.add_argument('-s', '--single', action='store', default='all', help='single histogram, example: massAve_cutDijet.' )
	parser.add_argument('-l', '--lumi', action='store', default='15.5', help='Luminosity, example: 1.' )
	parser.add_argument('-t', '--trigger', action='store', default='AK8PFHT700TrimMass50', help="Trigger used, name of directory" )
	parser.add_argument('-e', '--extension', action='store', default='png', help='Extension of plots.' )

	try:
		args = parser.parse_args()
	except:
		parser.print_help()
		sys.exit(0)

	triggerlabX = 0.15
	triggerlabY = 1.0
	jetMassHTlabX = 0.87
	jetMassHTlabY = 0.20

	HTMinX = 300
	HTMaxX = 1500
	ptMinX = 100
	ptMaxX = 800

	plotList = [ 

		[ '1D', 'HT', 500, 2000, 'HT [GeV]', 20, triggerlabX, triggerlabY, True],
		#[ '1D', 'HT', 800, 1200, 1, triggerlabX, triggerlabY, True],
		[ '1D', 'jet1Pt', ptMinX, ptMaxX, 'Leading Jet Pt [GeV]',  10, triggerlabX, triggerlabY, True],
#		[ '1D', 'jet2Pt', ptMinX, ptMaxX, 2, triggerlabX, triggerlabY, True],
		[ '1D', 'jet1SoftDropMass', 0, 500, 'Leading Jet Softdrop Mass [GeV]', 10, triggerlabX, triggerlabY, True],
		[ '1D', 'massAve', 0, 500, 10, triggerlabX, triggerlabY, True],
		[ 'tmp', 'jet1SoftDropMass', 0, 500, 1, triggerlabX, triggerlabY, True],

		#[ '2D', 'jetMassHTDenom_noTrigger', 'Leading Trimmed Jet Mass [GeV]', 'H_{T} [GeV]', 0, 200, 2, 100, HTMaxX, 5, 0.85, 0.2],
		#[ '2D', 'jetTrimmedMassHTDenom_noTrigger', 'Leading Trimmed Jet Mass [GeV]', 'H_{T} [GeV]', 0, 200, 2, 100, HTMaxX, 5, 0.85, 0.2],
		#[ '2D', 'jetMassHTDenom_triggerOne', 'Leading Trimmed Jet Mass [GeV]', 'H_{T} [GeV]', 0, 200, 2, 100, HTMaxX, 5, 0.85, 0.2],
		#[ '2D', 'jetMassHTDenom_triggerTwo', 'Leading Trimmed Jet Mass [GeV]', 'H_{T} [GeV]', 0, 200, 2, 100, HTMaxX, 5, 0.85, 0.2],
		#[ '2D', 'jetMassHTDenom_triggerOneAndTwo', 'Leading Trimmed Jet Mass [GeV]', 'H_{T} [GeV]', 0, 200, 2, 100, HTMaxX, 5, 0.85, 0.25],


		[ '2D', 'prunedMassAveHT', 'Leading Jet Pruned Mass [GeV]', 'HT [GeV]', 20, 200, 2, HTMinX, 1200, 10, jetMassHTlabX, jetMassHTlabY],
		#[ '2D', 'jetMassHT', 20, 200, 2, HTMinX, 1200, 10, jetMassHTlabX, jetMassHTlabY],
		[ '2D', 'jet4PtHT', '4th jet Pt [GeV]', 'HT [GeV]',  60, 300, 2, HTMinX, 1200, 10, jetMassHTlabX, jetMassHTlabY],
		]

	if 'all' in args.single: Plots = [ x[1:] for x in plotList if x[0] in args.proc ]
	else: Plots = [ y[1:] for y in plotList if ( ( y[0] in args.proc ) and ( y[1] in args.single ) )  ]


	effList = {}
	bkgFiles = {}
	signalFiles = {}
	CMS_lumi.extraText = "Preliminary"

	Samples = {}

	Samples[ 'SingleMuon2017' ] = [ 'TriggerValAndEff_JetHT_Run2016C.root', 0 ] 
	Samples[ 'SingleMuonB' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016B_V2p4_'+args.version+'.root', 5928.83 ] 
	Samples[ 'SingleMuonC' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016C_V2p4_'+args.version+'.root', 2632.18 ] 
	Samples[ 'SingleMuonD' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016D_V2p4_'+args.version+'.root', 4344.64 ] 
	Samples[ 'SingleMuonE' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016E_V2p4_'+args.version+'.root', 4117.09 ] 
	Samples[ 'SingleMuonF' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016F_V2p4_'+args.version+'.root', 3185.97 ] 
	Samples[ 'SingleMuonG' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016G_V2p4_'+args.version+'.root', 7721.06 ]
	Samples[ 'SingleMuonH' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016H_V2p4_'+args.version+'.root', 8629.24 ] 
	Samples[ 'SingleMuonAll' ] = [ 'RUNTriggerEfficiencies_SingleMuon_Run2016_V2p4_'+args.version+'.root', 35864. ] 

	Samples[ 'JetHT2017' ] = [ 'TriggerValAndEff_JetHT_Run2016C.root', 0 ] 
	Samples[ 'JetHTB' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016B_V2p1_'+args.version+'.root', 40.49 ] 
	Samples[ 'JetHTC' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016C_V2p1_'+args.version+'.root', 2.13 ] 
	Samples[ 'JetHTD' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016D_V2p1_'+args.version+'.root', 1.58 ] 
	Samples[ 'JetHTE' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016E_V2p1_'+args.version+'.root', 1.84 ] 
	Samples[ 'JetHTF' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016F_V2p1_'+args.version+'.root', 0.78 ] 
	Samples[ 'JetHTG' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016G_V2p1_'+args.version+'.root', 0.982 ] 
	Samples[ 'JetHTH' ] = [ 'RUNTriggerEfficiencies_JetHT_Run2016H_V2p1_'+args.version+'.root',  ] 


	processingSamples = {}
	if 'all' in args.dataset: 
		for sam in Samples: processingSamples[ sam ] = Samples[ sam ]
	else:
		for sam in Samples: 
			if sam.startswith( args.dataset ): processingSamples[ sam ] = Samples[ sam ]

	if len(processingSamples)==0: print 'No sample found. \n Have a nice day :)'

	for sam in processingSamples:

		CMS_lumi.lumi_13TeV = str( round( (processingSamples[sam][1]/1000.), 1 ) )+" fb^{-1}"
		if 'SingleMu' in sam: BASEDTrigger = 'IsoMu27'
		elif 'JetHT' in sam: BASEDTrigger = 'PFJet40'

		for i in Plots:
			if '1D' in args.proc:
				effList[ sam ] = plotTriggerEfficiency( TFile.Open('Rootfiles/'+processingSamples[sam][0]), 
									sam, 
									BASEDTrigger, 
									i[0], args.cut, i[1], i[2], i[3], i[4], i[5], i[6], i[7] )
			elif '2D' in args.proc:
				plot2DTriggerEfficiency( TFile.Open('Rootfiles/'+processingSamples[sam][0]), 
							sam, 
							args.trigger, 
							BASEDTrigger, 
							i[0], args.cut, i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], PU )

