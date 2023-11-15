# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Coroutine, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.interfaces import Tracker
from rasa_sdk.types import DomainDict

from actions.resources import file_resources, IndexTopic
from actions.resources.authorization import allowed_person
from actions.resources.type import SlotName


# the best practice for giving class name is Validate<NameForm>
# inherritance from class FormValidationAction
# the total function in the class depend on slot total in a form
class ValidateAuthorizationForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_authorization_form"

    # the best practice for giving name function is validate_<name_slot>
    def validate_nrp(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ):
        if slot_value.lower() in allowed_person:
            return {SlotName.NRP.value: slot_value}
        dispatcher.utter_message(
            f"mohon maaf {slot_value}, Anda tidak dapat mengakses lebih lanjut, silakan coba lagi"
        )
        return {SlotName.NRP.value: None}


class ActionFileList(Action):
    def name(self) -> Text:
        return "action_daftar_file"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        _text = ""
        prefix = f'kami mempunyai daftar file sebanyak {len(file_resources["names"])}\n'
        _text += prefix
        names = file_resources["names"]
        for idx, name in enumerate(names):
            temp_text = f"{idx+1} - {name}\n"
            _text += temp_text

        dispatcher.utter_message(text=_text)
        return []


class ActionFileAccess(Action):
    def name(self) -> Text:
        return "action_access_file"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: DomainDict
    ) -> List[Dict[Text, Any]]:
        _text = ""
        intent = tracker.get_slot("file_name")
        intents: List[str] = file_resources["intents_name"]
        urls: List[str] = file_resources["urls"]
        names: List[str] = file_resources["names"]

        print(intent)

        try:
            index = intents.index(intent)
            temp = f"berikut adalah url file {names[index]}:\n{urls[index]}"
            _text += temp
        except:
            _text += "mohon maaf, file tidak ditemukan"

        dispatcher.utter_message(text=_text)
        return []
