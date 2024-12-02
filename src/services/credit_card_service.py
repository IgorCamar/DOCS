from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.documentintelligence.models import AnalyzeDocumentRequest
from ultils.Config import Config

def analyze_credit_card(card_url):
    try:
        credential = AzureKeyCredential(Config.KEY)

        document_Client = DocumentIntelligenceClient(Config.ENDPOINT, credential)

        card_info = document_Client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))
        result =card_info.result()

        return result
    except Exception as ex:
        return None
