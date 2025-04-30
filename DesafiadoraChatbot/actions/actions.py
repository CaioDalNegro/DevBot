from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# Action personalizada para buscar livro por título
class ActionBuscarLivroTitulo(Action):
    def name(self) -> Text:
        return "action_buscar_livro_titulo"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        titulo = tracker.get_slot('titulo_livro')
        if titulo:
            response = requests.get(f"https://openlibrary.org/search.json?title={titulo}")
            data = response.json()
            if data['docs']:
                book = data['docs'][0]
                mensagem = f"Encontrei: '{book['title']}' de {book.get('author_name', ['Autor desconhecido'])[0]}."
            else:
                mensagem = "Não encontrei nenhum livro com esse título."
        else:
            mensagem = "Qual título de livro você gostaria de buscar?"

        dispatcher.utter_message(text=mensagem)
        return []

# Action personalizada para buscar livro por autor
class ActionBuscarLivroAutor(Action):
    def name(self) -> Text:
        return "action_buscar_livro_autor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        autor = tracker.get_slot('nome_autor')
        if autor:
            response = requests.get(f"https://openlibrary.org/search.json?author={autor}")
            data = response.json()
            if data['docs']:
                book = data['docs'][0]
                mensagem = f"Encontrei: '{book['title']}' de {book.get('author_name', ['Autor desconhecido'])[0]}."
            else:
                mensagem = "Não encontrei livros desse autor."
        else:
            mensagem = "Qual autor você gostaria de buscar?"

        dispatcher.utter_message(text=mensagem)
        return []

# Action para buscar livros por assunto
class ActionBuscarLivroAssunto(Action):
    def name(self) -> Text:
        return "action_buscar_livro_assunto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        assunto = tracker.get_slot('assunto_livro')
        if assunto:
            response = requests.get(f"https://openlibrary.org/search.json?subject={assunto}")
            data = response.json()
            if data['docs']:
                book = data['docs'][0]
                mensagem = f"Encontrei: '{book['title']}' sobre {assunto}."
            else:
                mensagem = f"Não encontrei livros sobre {assunto}."
        else:
            mensagem = "Sobre qual assunto você gostaria de buscar livros?"

        dispatcher.utter_message(text=mensagem)
        return []
