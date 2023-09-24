# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict

from actions.resources import file_resources, IndexTopic


class ActionFileList(Action):
    def name(self) -> Text:
        return "action_daftar_file"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        _text = ""
        prefix = f"kami mempunyai daftar file sebanyak {len(file_resources)}\n"
        names = file_resources["names"]
        # urls = file_resources["urls"]
        for idx, name in enumerate(names):
            temp_text = f"{idx+1} - {name}\n"
            _text += temp_text

        dispatcher.utter_message(text=_text)
        return []
