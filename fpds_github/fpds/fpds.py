
from bs4 import BeautifulSoup
import requests
import json
# from enum import Enum



# def __init__(self, initial_search_url, output_file_path):
#     self.initial_search_url = initial_search_url
#     self.output_file_path = output_file_path
#     self.entries = None
#     self.metadata = None
        

def get_api_fields():
    flds = [
            { 'parent_tag':'author', 'child_tag':'name', 'field_name':'feedAuthorName', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'awardContractID', 'child_tag':'agencyID', 'field_name':'awardAgencyID', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'awardContractID', 'child_tag':'modNumber', 'field_name':'awardModNumber', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'awardContractID', 'child_tag':'PIID', 'field_name':'awardPIID', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'awardContractID', 'child_tag':'transactionNumber', 'field_name':'awardTransactionNumber', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isCorporateEntityNotTaxExempt', 'field_name':'vendorIsCorporateEntityNotTaxExempt', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isCorporateEntityTaxExempt', 'field_name':'vendorIsCorporateEntityTaxExempt', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isInternationalOrganization', 'field_name':'vendorIsInternationalOrganization', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isPartnershipOrLimitedLiabilityPartnership', 'field_name':'vendorIsPartnershipOrLimitedLiabilityPartnership', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isSmallAgriculturalCooperative', 'field_name':'vendorIsSmallAgriculturalCooperative', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isSolePropreitorship', 'field_name':'vendorIsSolePropreitorship', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'businessOrOrganizationType', 'child_tag':'isUSGovernmentEntity', 'field_name':'vendorIsUSGovernmentEntity', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'ccrRegistrationDetails', 'child_tag':'registrationDate', 'field_name':'samRegistrationDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'ccrRegistrationDetails', 'child_tag':'renewalDate', 'field_name':'samRenewalDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'A76Action', 'field_name':'competitionA76Action', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'alternativeAdvertising', 'field_name':'competitionAlternativeAdvertising', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'commercialItemAcquisitionProcedures', 'field_name':'competitionCommercialItemAcquisitionProcedures', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'commercialItemTestProgram', 'field_name':'competitionCommercialItemTestProgram', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'competitiveProcedures', 'field_name':'competitionCompetitiveProcedures', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'evaluatedPreference', 'field_name':'competitionEvaluatedPreference', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'extentCompeted', 'field_name':'competitionExtentCompeted', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'fedBizOpps', 'field_name':'competitionFedBizOpps', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'IDVnumberOfOffersReceived', 'field_name':'competitionIDVnumberOfOffersReceived', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'IDVTypeOfSetAside', 'field_name':'competitionIDVTypeOfSetAside', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'localAreaSetAside', 'field_name':'competitionLocalAreaSetAside', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'numberOfOffersReceived', 'field_name':'competitionNumberOfOffersReceived', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'numberOfOffersSource', 'field_name':'competitionNumberOfOffersSource', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'preAwardSynopsisRequirement', 'field_name':'competitionPreAwardSynopsisRequirement', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'priceEvaluationPercentDifference', 'field_name':'competitionPriceEvaluationPercentDifference', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'reasonNotCompeted', 'field_name':'competitionReasonNotCompeted', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'research', 'field_name':'competitionResearch', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'smallBusinessCompetitivenessDemonstrationProgram', 'field_name':'competitionSmallBusinessCompetitivenessDemonstrationProgram', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'solicitationProcedures', 'field_name':'competitionSolicitationProcedures', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'statutoryExceptionToFairOpportunity', 'field_name':'competitionStatutoryExceptionToFairOpportunity', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'synopsisWaiverException', 'field_name':'competitionSynopsisWaiverException', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'typeOfSetAside', 'field_name':'competitionTypeOfSetAside', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'competition', 'child_tag':'typeOfSetAsideSource', 'field_name':'competitionTypeOfSetAsideSource', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'consortiaInformation', 'child_tag':'consortiaFlag', 'field_name':'consortiaFlag', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'consortiaInformation', 'child_tag':'primaryConsortiaMemberCageCode', 'field_name':'consortiaMemberCageCode', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'consortiaInformation', 'child_tag':'primaryConsortiaMemberName', 'field_name':'consortiaMemberName', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'consortiaInformation', 'child_tag':'primaryConsortiaMemberUEI', 'field_name':'consortiaMemberUEI', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'consolidatedContract', 'field_name':'contractConsolidatedContract', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'contingencyHumanitarianPeacekeepingOperation', 'field_name':'contractContingencyHumanitarianPeacekeepingOperation', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'contractActionType', 'field_name':'contractActionType', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'contractFinancing', 'field_name':'contractFinancing', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'costAccountingStandardsClause', 'field_name':'contractCostAccountingStandardsClause', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'costOrPricingData', 'field_name':'contractCostOrPricingData', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'descriptionOfContractRequirement', 'field_name':'contractDescriptionOfContractRequirement', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'GFE-GFP', 'field_name':'contractGFEorGFP', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'inherentlyGovernmentalFunction', 'field_name':'contractInherentlyGovernmentalFunction', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'majorProgramCode', 'field_name':'contractMajorProgramCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'multipleOrSingleAwardIDC', 'field_name':'contractMultipleOrSingleAwardIDC', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'multiYearContract', 'field_name':'contractMultiYearContract', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'nationalInterestActionCode', 'field_name':'contractNationalInterestActionCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'nonTraditionalGovernmentContractorParticipation', 'field_name':'contractNonTraditionalGovernmentContractorParticipation', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'numberOfActions', 'field_name':'contractNumberOfActions', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'performanceBasedServiceContract', 'field_name':'contractPerformanceBasedServiceContract', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'programAcronym', 'field_name':'contractProgramAcronym', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'purchaseCardAsPaymentMethod', 'field_name':'contractPurchaseCardAsPaymentMethod', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'reasonForModification', 'field_name':'contractReasonForModification', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'referencedIDVMultipleOrSingle', 'field_name':'contractReferencedIDVMultipleOrSingle', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'referencedIDVPart8OrPart13', 'field_name':'contractReferencedIDVPart8OrPart13', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'referencedIDVType', 'field_name':'contractReferencedIDVType', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'seaTransportation', 'field_name':'contractSeaTransportation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'solicitationID', 'field_name':'contractSolicitationID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'typeOfAgreement', 'field_name':'contractTypeOfAgreement', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'typeOfContractPricing', 'field_name':'contractTypeOfContractPricing', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'typeOfIDC', 'field_name':'contractTypeOfIDC', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractData', 'child_tag':'undefinitizedAction', 'field_name':'contractUndefinitizedAction', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractDetail', 'child_tag':'PSCCode', 'field_name':'contractPSCCode', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'emailAddress', 'field_name':'marketingEmailAddress', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'feePaidForUseOfService', 'field_name':'marketingFeePaidForUseOfService', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'fixedFeeValue', 'field_name':'marketingFixedFeeValue', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'individualOrderLimit', 'field_name':'marketingIndividualOrderLimit', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'orderingProcedure', 'field_name':'marketingOrderingProcedure', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'totalEstimatedOrderValue', 'field_name':'marketingTotalEstimatedOrderValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'typeOfFeeForUseOfService', 'field_name':'marketingTypeOfFeeForUseOfService', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'websiteURL', 'field_name':'marketingWebsiteURL', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'contractMarketingData', 'child_tag':'whoCanUse', 'field_name':'marketingWhoCanUse', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'dollarValues', 'child_tag':'baseAndAllOptionsValue', 'field_name':'contractBaseAndAllOptionsValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'dollarValues', 'child_tag':'baseAndExercisedOptionsValue', 'field_name':'contractBaseAndExercisedOptionsValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'dollarValues', 'child_tag':'nonGovernmentalDollars', 'field_name':'contractNonGovernmentalDollars', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'dollarValues', 'child_tag':'obligatedAmount', 'field_name':'contractObligatedAmount_dollarValues', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'entityIdentifiers', 'child_tag':'cageCode', 'field_name':'contractCageCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'entry', 'child_tag':'link', 'field_name':'entryLink', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'entry', 'child_tag':'modified', 'field_name':'entryModified', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'entry', 'child_tag':'title', 'field_name':'entryTitle', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'federalGovernment', 'child_tag':'isFederalGovernment', 'field_name':'entityIsFederalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'federalGovernment', 'child_tag':'isFederalGovernmentAgency', 'field_name':'entityIsFederalGovernmentAgency', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'federalGovernment', 'child_tag':'isFederallyFundedResearchAndDevelopmentCorp', 'field_name':'entityIsFederallyFundedResearchAndDevelopmentCorp', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'feed', 'child_tag':'link', 'field_name':'feedLink', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'feed', 'child_tag':'modified', 'field_name':'feedModified', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'feed', 'child_tag':'title', 'field_name':'feedTitle', 'inFeed':'1', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean01', 'field_name':'genericBoolean01', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean02', 'field_name':'genericBoolean02', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean03', 'field_name':'genericBoolean03', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean04', 'field_name':'genericBoolean04', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean05', 'field_name':'genericBoolean05', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean06', 'field_name':'genericBoolean06', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean07', 'field_name':'genericBoolean07', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean08', 'field_name':'genericBoolean08', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean09', 'field_name':'genericBoolean09', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericBooleans', 'child_tag':'genericBoolean10', 'field_name':'genericBoolean10', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericFloats', 'child_tag':'genericFloat01', 'field_name':'genericFloat01', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericFloats', 'child_tag':'genericFloat02', 'field_name':'genericFloat02', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericIntegers', 'child_tag':'genericInteger01', 'field_name':'genericInteger01', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericIntegers', 'child_tag':'genericInteger02', 'field_name':'genericInteger02', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString01', 'field_name':'genericString01', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString02', 'field_name':'genericString02', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString03', 'field_name':'genericString03', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString04', 'field_name':'genericString04', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString05', 'field_name':'genericString05', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString06', 'field_name':'genericString06', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString07', 'field_name':'genericString07', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString08', 'field_name':'genericString08', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString09', 'field_name':'genericString09', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'genericStrings', 'child_tag':'genericString10', 'field_name':'genericString10', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'IDVID', 'child_tag':'agencyID', 'field_name':'idvidAgencyID', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'IDVID', 'child_tag':'modNumber', 'field_name':'idvidModNumber', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'IDVID', 'child_tag':'PIID', 'field_name':'idvidPIID', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'ClingerCohenAct', 'field_name':'mandatesClingerCohenAct', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'constructionWageRateRequirements', 'field_name':'mandatesConstructionWageRateRequirements', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'interagencyContractingAuthority', 'field_name':'mandatesInteragencyContractingAuthority', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'laborStandards', 'field_name':'mandatesLaborStandards', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'materialsSuppliesArticlesEquipment', 'field_name':'mandatesMaterialsSuppliesArticlesEquipment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'legislativeMandates', 'child_tag':'otherStatutoryAuthority', 'field_name':'mandatesOtherStatutoryAuthority', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'listOfAdditionalReportingValues', 'child_tag':'additionalReportingValue', 'field_name':'mandatesAdditionalReportingValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isCityLocalGovernment', 'field_name':'entityIsCityLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isCountyLocalGovernment', 'field_name':'entityIsCountyLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isInterMunicipalLocalGovernment', 'field_name':'entityIsInterMunicipalLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isLocalGovernment', 'field_name':'entityIsLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isLocalGovernmentOwned', 'field_name':'entityIsLocalGovernmentOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isMunicipalityLocalGovernment', 'field_name':'entityIsMunicipalityLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isSchoolDistrictLocalGovernment', 'field_name':'entityIsSchoolDistrictLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'localGovernment', 'child_tag':'isTownshipLocalGovernment', 'field_name':'entityIsTownshipLocalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isAsianPacificAmericanOwnedBusiness', 'field_name':'vendorIsAsianPacificAmericanOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isBlackAmericanOwnedBusiness', 'field_name':'vendorIsBlackAmericanOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isHispanicAmericanOwnedBusiness', 'field_name':'vendorIsHispanicAmericanOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isMinorityOwned', 'field_name':'vendorIsMinorityOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isNativeAmericanOwnedBusiness', 'field_name':'vendorIsNativeAmericanOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isOtherMinorityOwned', 'field_name':'vendorIsOtherMinorityOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'minorityOwned', 'child_tag':'isSubContinentAsianAmericanOwnedBusiness', 'field_name':'vendorIsSubContinentAsianAmericanOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionAwardContractID', 'child_tag':'agencyID', 'field_name':'otherTrxAwardIDAgencyID', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionAwardContractID', 'child_tag':'modNumber', 'field_name':'otherTrxAwardIDModNumber', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionAwardContractID', 'child_tag':'PIID', 'field_name':'otherTrxAwardIDPIID', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionIDVContractID', 'child_tag':'agencyID', 'field_name':'otherTrxAwardIDAgencyID', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionIDVContractID', 'child_tag':'modNumber', 'field_name':'otherTrxAwardIDModNumber', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'OtherTransactionIDVContractID', 'child_tag':'PIID', 'field_name':'otherTrxAwardIDPIID', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'placeOfPerformance', 'child_tag':'placeOfPerformanceCongressionalDistrict', 'field_name':'placeOfPerformanceCongressionalDistrict', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'placeOfPerformance', 'child_tag':'placeOfPerformanceZIPCode', 'field_name':'placeOfPerformanceZIPCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'preferencePrograms', 'child_tag':'reasonNotAwardedToSmallBusiness', 'field_name':'reasonNotAwardedToSmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'preferencePrograms', 'child_tag':'reasonNotAwardedToSmallDisadvantagedBusiness', 'field_name':'reasonNotAwardedToSmallDisadvantagedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'preferencePrograms', 'child_tag':'subcontractPlan', 'field_name':'subcontractPlan', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'city', 'field_name':'primaryConsortiaCity', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'congressionalDistrictCode', 'field_name':'primaryConsortiaCongressionalDistrictCode', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'countryCode', 'field_name':'primaryConsortiaCountryCode', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'state', 'field_name':'primaryConsortiaState', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'streetAddress1', 'field_name':'primaryConsortiastreetAddress1', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'streetAddress2', 'field_name':'primaryConsortiastreetAddress2', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'primaryConsortiaLocation', 'child_tag':'ZIPCode', 'field_name':'primaryConsortiaZipCode', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'principalPlaceOfPerformance', 'child_tag':'countryCode', 'field_name':'placeOfPerformanceCountryCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'principalPlaceOfPerformance', 'child_tag':'locationCode', 'field_name':'placeOfPerformanceLocationCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'principalPlaceOfPerformance', 'child_tag':'stateCode', 'field_name':'placeOfPerformanceStateCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'claimantProgramCode', 'field_name':'prodOrSvcClaimantProgramCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'contractBundling', 'field_name':'prodOrSvcContractBundling', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'countryOfOrigin', 'field_name':'prodOrSvcCountryOfOrigin', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'IDVNAICS', 'field_name':'prodOrSvcIDVNAICS', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'informationTechnologyCommercialItemCategory', 'field_name':'prodOrSvcInformationTechnologyCommercialItemCategory', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'manufacturingOrganizationType', 'field_name':'prodOrSvcManufacturingOrganizationType', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'NAICSSource', 'field_name':'prodOrSvcNAICSSource', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'placeOfManufacture', 'field_name':'prodOrSvcPlaceOfManufacture', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'principalNAICSCode', 'field_name':'prodOrSvcPrincipalNAICSCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'productOrServiceCode', 'field_name':'prodOrSvcProductOrServiceCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'recoveredMaterialClauses', 'field_name':'prodOrSvcRecoveredMaterialClauses', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'systemEquipmentCode', 'field_name':'prodOrSvcSystemEquipmentCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'productOrServiceInformation', 'child_tag':'useOfEPADesignatedProducts', 'field_name':'prodOrSvcUseOfEPADesignatedProducts', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'profitStructure', 'child_tag':'isForProfitOrganization', 'field_name':'vendorIsForProfitOrganization', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'profitStructure', 'child_tag':'isNonprofitOrganization', 'field_name':'vendorIsNonprofitOrganization', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'profitStructure', 'child_tag':'isOtherNotForProfitOrganization', 'field_name':'vendorIsOtherNotForProfitOrganization', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'contractingOfficeAgencyID', 'field_name':'purchaserContractingOfficeAgencyID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'contractingOfficeID', 'field_name':'purchaserContractingOfficeID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'foreignFunding', 'field_name':'purchaserForeignFunding', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'fundingRequestingAgencyID', 'field_name':'purchaserFundingRequestingAgencyID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'fundingRequestingOfficeID', 'field_name':'purchaserFundingRequestingOfficeID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'purchaserInformation', 'child_tag':'purchaseReason', 'field_name':'purchaserPurchaseReason', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'referencedIDVID', 'child_tag':'agencyID', 'field_name':'referencedIdvIDAgencyID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'referencedIDVID', 'child_tag':'modNumber', 'field_name':'referencedIdvIDModNumber', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'referencedIDVID', 'child_tag':'PIID', 'field_name':'referencedIdvIDPIID', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'currentCompletionDate', 'field_name':'contractCurrentCompletionDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'effectiveDate', 'field_name':'contractEffectiveDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'fiscalYear', 'field_name':'contractFiscalYear', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'lastDateToOrder', 'field_name':'contractLastDateToOrder', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'signedDate', 'field_name':'contractSignedDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'relevantContractDates', 'child_tag':'ultimateCompletionDate', 'field_name':'contractUltimateCompletionDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'totalDollarValues', 'child_tag':'totalBaseAndAllOptionsValue', 'field_name':'contractTotalBaseAndAllOptionsValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'totalDollarValues', 'child_tag':'totalBaseAndExercisedOptionsValue', 'field_name':'contractTotalBaseAndExercisedOptionsValue', 'inFeed':'0', 'inAward':'1', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'totalDollarValues', 'child_tag':'totalNonGovernmentalDollars', 'field_name':'contractTotalNonGovernmentalDollars', 'inFeed':'0', 'inAward':'0', 'inIDV':'0', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'totalDollarValues', 'child_tag':'totalObligatedAmount', 'field_name':'contractTotalObligatedAmount', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'approvedBy', 'field_name':'transactionApprovedBy', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'approvedDate', 'field_name':'transactionApprovedDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'closedBy', 'field_name':'transactionClosedBy', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'closedDate', 'field_name':'transactionClosedDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'closedStatus', 'field_name':'transactionClosedStatus', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'createdBy', 'field_name':'transactionCreatedBy', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'createdDate', 'field_name':'transactionCreatedDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'lastModifiedBy', 'field_name':'transactionLastModifiedBy', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'lastModifiedDate', 'field_name':'transactionLastModifiedDate', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'1', 'inIDVClosedFeed':'1' }, 
            { 'parent_tag':'transactionInformation', 'child_tag':'status', 'field_name':'transactionStatus', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccount', 'child_tag':'initiative', 'field_name':'treasuryAcctInitiative', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccount', 'child_tag':'obligatedAmount', 'field_name':'treasuryAcctObligatedAmount', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'agencyIdentifier', 'field_name':'treasuryAcctAgencyIdentifier', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'allocationTransferAgencyIdentifier', 'field_name':'treasuryAcctAllocationTransferAgencyIdentifier', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'availabilityTypeCode', 'field_name':'treasuryAcctAvailabilityTypeCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'beginningPeriodOfAvailability', 'field_name':'treasuryAcctBeginningPeriodOfAvailability', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'endingPeriodOfAvailability', 'field_name':'treasuryAcctEndingPeriodOfAvailability', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'mainAccountCode', 'field_name':'treasuryAcctMainAccountCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'subAccountCode', 'field_name':'treasuryAcctSubAccountCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'treasuryAccountSymbol', 'child_tag':'subLevelPrefixCode', 'field_name':'treasuryAcctSubLevelPrefixCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'is1862LandGrantCollege', 'field_name':'entityIs1862LandGrantCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'is1890LandGrantCollege', 'field_name':'entityIs1890LandGrantCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'is1994LandGrantCollege', 'field_name':'entityIs1994LandGrantCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isAlaskanNativeServicingInstitution', 'field_name':'entityIsAlaskanNativeServicingInstitution', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isHistoricallyBlackCollegeOrUniversity', 'field_name':'entityIsHistoricallyBlackCollegeOrUniversity', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isMinorityInstitution', 'field_name':'entityIsMinorityInstitution', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isNativeHawaiianServicingInstitution', 'field_name':'entityIsNativeHawaiianServicingInstitution', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isPrivateUniversityOrCollege', 'field_name':'entityIsPrivateUniversityOrCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isSchoolOfForestry', 'field_name':'entityIsSchoolOfForestry', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isStateControlledInstitutionofHigherLearning', 'field_name':'entityIsStateControlledInstitutionofHigherLearning', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isTribalCollege', 'field_name':'entityIsTribalCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfEducationalEntity', 'child_tag':'isVeterinaryCollege', 'field_name':'entityIsVeterinaryCollege', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isAirportAuthority', 'field_name':'entityIsAirportAuthority', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isCouncilOfGovernments', 'field_name':'entityIsCouncilOfGovernments', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isHousingAuthoritiesPublicOrTribal', 'field_name':'entityIsHousingAuthoritiesPublicOrTribal', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isInterstateEntity', 'field_name':'entityIsInterstateEntity', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isPlanningCommission', 'field_name':'entityIsPlanningCommission', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isPortAuthority', 'field_name':'entityIsPortAuthority', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'typeOfGovernmentEntity', 'child_tag':'isTransitAuthority', 'field_name':'entityIsTransitAuthority', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendor', 'child_tag':'CCRException', 'field_name':'vendorCCRException', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendor', 'child_tag':'contractingOfficerBusinessSizeDetermination', 'field_name':'vendorContractingOfficerBusinessSizeDetermination', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendor', 'child_tag':'IDVcontractingOfficerBusinessSize', 'field_name':'vendorIDVcontractingOfficerBusinessSize', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendor', 'child_tag':'IDVcontractingOfficerBusinessSizeSource', 'field_name':'vendorIDVcontractingOfficerBusinessSizeSource', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorBusinessTypes', 'child_tag':'isCommunityDevelopedCorporationOwnedFirm', 'field_name':'vendorIsCommunityDevelopedCorporationOwnedFirm', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorBusinessTypes', 'child_tag':'isForeignGovernment', 'field_name':'vendorIsForeignGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorBusinessTypes', 'child_tag':'isLaborSurplusAreaFirm', 'field_name':'vendorIsLaborSurplusAreaFirm', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorBusinessTypes', 'child_tag':'isStateGovernment', 'field_name':'vendorIsStateGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorBusinessTypes', 'child_tag':'isTribalGovernment', 'field_name':'vendorIsTribalGovernment', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isDOTCertifiedDisadvantagedBusinessEnterprise', 'field_name':'vendorIsDOTCertifiedDisadvantagedBusinessEnterprise', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSBACertified8AJointVenture', 'field_name':'vendorIsSBACertified8AJointVenture', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSBACertified8AProgramParticipant', 'field_name':'vendorIsSBACertified8AProgramParticipant', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSBACertifiedHUBZone', 'field_name':'vendorIsSBACertifiedHUBZone', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSBACertifiedSmallDisadvantagedBusiness', 'field_name':'vendorIsSBACertifiedSmallDisadvantagedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSelfCertifiedHUBZoneJointVenture', 'field_name':'vendorIsSelfCertifiedHUBZoneJointVenture', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorCertifications', 'child_tag':'isSelfCertifiedSmallDisadvantagedBusiness', 'field_name':'vendorIsSelfCertifiedSmallDisadvantagedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorHeader', 'child_tag':'vendorAlternateName', 'field_name':'vendorAlternateName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorHeader', 'child_tag':'vendorDoingAsBusinessName', 'field_name':'vendorDoingAsBusinessName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorHeader', 'child_tag':'vendorEnabled', 'field_name':'vendorEnabled', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorHeader', 'child_tag':'vendorLegalOrganizationName', 'field_name':'vendorLegalOrganizationName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorHeader', 'child_tag':'vendorName', 'field_name':'vendorName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isCommunityDevelopmentCorporation', 'field_name':'vendorLOBIsCommunityDevelopmentCorporation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isDomesticShelter', 'field_name':'vendorLOBIsDomesticShelter', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isEducationalInstitution', 'field_name':'vendorLOBIsEducationalInstitution', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isFoundation', 'field_name':'vendorLOBIsFoundation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isHispanicServicingInstitution', 'field_name':'vendorLOBIsHispanicServicingInstitution', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isHospital', 'field_name':'vendorLOBIsHospital', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isManufacturerOfGoods', 'field_name':'vendorLOBIsManufacturerOfGoods', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLineOfBusiness', 'child_tag':'isVeterinaryHospital', 'field_name':'vendorLOBIsVeterinaryHospital', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'city', 'field_name':'vendorCity', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'congressionalDistrictCode', 'field_name':'vendorCongressionalDistrictCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'countryCode', 'field_name':'vendorCountryCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'entityDataSource', 'field_name':'vendorEntityDataSource', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'faxNo', 'field_name':'vendorFaxNo', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'phoneNo', 'field_name':'vendorPhoneNo', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'province', 'field_name':'vendorProvince', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'state', 'field_name':'vendorState', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'streetAddress', 'field_name':'vendorStreetAddress', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'streetAddress2', 'field_name':'vendorStreetAddress2', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'streetAddress3', 'field_name':'vendorStreetAddress3', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'vendorLocationDisabledFlag', 'field_name':'vendorLocationDisabledFlag', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'0', 'inOtherTrxIDV':'0', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorLocation', 'child_tag':'ZIPCode', 'field_name':'vendorZIPCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'countryOfIncorporation', 'field_name':'vendorCountryOfIncorporation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'isForeignOwnedAndLocated', 'field_name':'vendorIsForeignOwnedAndLocated', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'isLimitedLiabilityCorporation', 'field_name':'vendorIsLimitedLiabilityCorporation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'isShelteredWorkshop', 'field_name':'vendorsShelteredWorkshop', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'isSubchapterSCorporation', 'field_name':'vendorIsSubchapterSCorporation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'organizationalType', 'field_name':'vendorOrganizationalType', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorOrganizationFactors', 'child_tag':'stateOfIncorporation', 'field_name':'vendorStateOfIncorporation', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorRelationshipWithFederalGovernment', 'child_tag':'receivesContracts', 'field_name':'vendorReceivesContracts', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorRelationshipWithFederalGovernment', 'child_tag':'receivesContractsAndGrants', 'field_name':'vendorReceivesContractsAndGrants', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorRelationshipWithFederalGovernment', 'child_tag':'receivesGrants', 'field_name':'vendorReceivesGrants', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSiteDetails', 'child_tag':'divisionName', 'field_name':'siteDivisionName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSiteDetails', 'child_tag':'divisionNumberOrOfficeCode', 'field_name':'siteDivisionNumberOrOfficeCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSiteDetails', 'child_tag':'vendorAlternateSiteCode', 'field_name':'siteVendorAlternateSiteCode', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isAlaskanNativeOwnedCorporationOrFirm', 'field_name':'vendorIsAlaskanNativeOwnedCorporationOrFirm', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isAmericanIndianOwned', 'field_name':'vendorIsAmericanIndianOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isEconomicallyDisadvantagedWomenOwnedSmallBusiness', 'field_name':'vendorIsEconomicallyDisadvantagedWomenOwnedSmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isIndianTribe', 'field_name':'vendorIsIndianTribe', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness', 'field_name':'vendorIsJointVentureEconomicallyDisadvantagedWomenOwnedSmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isJointVentureWomenOwnedSmallBusiness', 'field_name':'vendorIsJointVentureWomenOwnedSmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isNativeHawaiianOwnedOrganizationOrFirm', 'field_name':'vendorIsNativeHawaiianOwnedOrganizationOrFirm', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isServiceRelatedDisabledVeteranOwnedBusiness', 'field_name':'vendorIsServiceRelatedDisabledVeteranOwnedBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isTriballyOwnedFirm', 'field_name':'vendorIsTriballyOwnedFirm', 'inFeed':'0', 'inAward':'0', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isVerySmallBusiness', 'field_name':'vendorIsVerySmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isVeteranOwned', 'field_name':'vendorIsVeteranOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isWomenOwned', 'field_name':'vendorIsWomenOwned', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorSocioEconomicIndicators', 'child_tag':'isWomenOwnedSmallBusiness', 'field_name':'vendorIsWomenOwnedSmallBusiness', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'domesticParentUEI', 'field_name':'vendorDomesticParentUEI', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'domesticParentUEIName', 'field_name':'vendorDomesticParentUEIName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'immediateParentUEI', 'field_name':'vendorImmediateParentUEI', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'immediateParentUEIName', 'field_name':'vendorImmediateParentUEIName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'UEI', 'field_name':'vendorUEI', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'UEILegalBusinessName', 'field_name':'vendorUEILegalBusinessName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'ultimateParentUEI', 'field_name':'vendorUltimateParentUEI', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }, 
            { 'parent_tag':'vendorUEIInformation', 'child_tag':'ultimateParentUEIName', 'field_name':'vendorUltimateParentUEIName', 'inFeed':'0', 'inAward':'1', 'inIDV':'1', 'inOtherTrxAward':'1', 'inOtherTrxIDV':'1', 'inAwardClosedFeed':'0', 'inIDVClosedFeed':'0' }
            ]
    return flds



def get_fpds_search_results(initial_search_url = ''):      # return_json = False
    ''' 
        if data_to_return = 1 the function returns entries only 
        if data_to_return = 2 the function returns metadata only 
        if data_to_return = 3 the function returns BOTH entries and metadata  
    '''

    # 1) declare page arrays & page counter
    first_link      = []    # should only be populated once (fron initial search results page) 
    last_link       = []    # should only be populated once (fron initial search results page)  
    all_pages       = []    # should be populated every time new page is loaded 
    metadata        = {}
    
    # 2) define output structure
    # parent dictionary
    results = {}

    # metadata info
    page_counter    = 0
    entry_counter   = 0
    pages_visited   = []    # populated with api links to each page
    alternate_pages = []    # populated with html links to api results
    feed            = {}   
    
    # api data entries
    entries         = {} 


    # 3) get the first set of link references
    source = requests.get(initial_search_url)
    soup = BeautifulSoup(source.content,'xml')


    # 4) log feed level data ... from the first page only - initial page links
    links = [{'tag_parent': tag.parent.name, 'tag_name': tag.name, 'tag': tag} for tag in soup.find_all('link') if tag.parent.name == 'feed']

    first_link.append(initial_search_url)
    all_pages.append(initial_search_url)

    for i in links:
        tag_name = i['tag'].get('rel')
        link_value = i['tag'].get('href')
        match tag_name:
            case 'last':
                if len(last_link) == 0: last_link.append(link_value)
            case 'next':
                if link_value not in all_pages: all_pages.append(i['tag'].get('href'))
            case 'alternate':
                if link_value not in alternate_pages: alternate_pages.append(i['tag'].get('href'))    

    # 5) loop through each page in the result set
    for page in all_pages:
        if page not in pages_visited:
            page_counter += 1
            source = requests.get(page)
            soup = BeautifulSoup(source.content,'xml')

            links = [{'tag_parent': tag.parent.name, 'tag_name': tag.name, 'tag': tag} for tag in soup.find_all('link') if tag.parent.name == 'feed']
            for i in links:
                tag_name = i['tag'].get('rel')
                link_value = i['tag'].get('href')
                if tag_name == 'next': 
                    if link_value not in all_pages: all_pages.append(i['tag'].get('href')) 
                if tag_name == 'alternate':
                    if link_value not in alternate_pages: alternate_pages.append(i['tag'].get('href'))                     

            # process the feed section for the current page
            feed_title = [{'tag_parent': tag.parent.name, 'tag_name': tag.name, 'tag': tag.text} for tag in soup.find_all('title') if tag.parent.name == 'feed']
            feed_modified = [{'tag_parent': tag.parent.name, 'tag_name': tag.name, 'tag': tag.text} for tag in soup.find_all('modified') if tag.parent.name == 'feed']
            feed_author = [{'tag_parent': tag.parent.name, 'tag_name': tag.name, 'tag': tag.text} for tag in soup.find_all('name') if tag.parent.name == 'author']
            
            feed['feedTitle'] = feed_title[0]['tag']
            feed['feedModified'] = feed_modified[0]['tag']
            feed['feedAuthor'] = feed_author[0]['tag']

            # now set the scope to only entries data 
            entry_xml = [tag for tag in soup.find_all('entry')]        

            # loop through each entry in the current page
            api_fields = get_api_fields()

            for e in entry_xml:
                entry_counter += 1
                entry = {}
                for f in api_fields:
                    result = [(entry_counter, f['field_name'], tag.text) for tag in e.find_all(f['child_tag']) if tag.name == f['child_tag'] and tag.parent.name == f['parent_tag'] ]  
                    if result: 
                        entry[result[0][1]] = result[0][2]
                entries[entry_counter]=entry 
                                        
            pages_visited.append(page)
                
    metadata['entry_count']= entry_counter
    metadata['feed_info'] = feed
    metadata['page_count'] = page_counter
    metadata['pages_visited'] = pages_visited
    metadata['alternate_pages'] = alternate_pages

    # if return_json:
    #     json.dumps(entries, indent=4)
    #     json.dumps(metadata, indent=4)
    
    json.dumps(entries, indent=4)
    json.dumps(metadata, indent=4)
    
    results['entries'] = entries
    results['metadata'] = metadata

    # self.entries = entries
    # self.metadata = metadata

    # if data_to_return == 1:
    #     return entries
    # if data_to_return == 2:
    #     return metadata
    # else:
    return results
        


def write_fpds_results_to_file(results, output_filepath=None):
    with open(output_filepath, 'w') as file:
        file.write(json.dumps(results, indent=4))
    



def extract_fpds_fields_to_list_of_tuples(entries):     
    results = []     
    for entry_number, record in entries.items():
        for field, field_value in record.items():
            results.append((entry_number, field, field_value))
    return results


