from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckProblema(Action):
    def name(self) -> str:
        return "action_check_problema"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Ação personalizada para verificar o problema
        dispatcher.utter_message(text="Entendi, você está com um problema de login.")
        return []

class ActionRecomendarSolucao(Action):
    def name(self) -> str:
        return "action_recomendar_solucao"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        # Ação personalizada para recomendar a solução
        dispatcher.utter_message(text="Recomendo que você tente redefinir sua senha através da opção 'Esqueci a senha'.")
        return []
