import csv
import os
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher

class ActionProvideDiseaseInfo(Action):
    """
    This class is a custom action for the Rasa chatbot that provides information
    about various diseases
    """

    def name(self):
        """
        Returns the name of the action. This name is used in the configuration
        of the Rasa assistant to refer to this action.
        """
        return "action_provide_disease_info"

    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        """
        This method is executed when the action is called in the dialogue flow.
        It searches for the requested disease and provides corresponding information.
        """
        disease = tracker.get_slot('disease')
        
        if not disease:
            dispatcher.utter_message(text="I did not understand the disease.")
            return []

        description = self._get_disease_description(disease)
        
        if description:
            dispatcher.utter_message(text=description)
        else:
            dispatcher.utter_message(text="No information found about this disease.")
        
        return []

    def _get_disease_description(self, disease):
        """
        A private helper method to read the description of a disease from a CSV file.
        """
        file_path = os.path.join("data", "symptom_Description.csv")
        
        try:
            with open(file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Disease'].lower() == disease.lower():
                        return row['Description']
        except Exception as e:
            print(f"Error reading the CSV file: {e}")
        
        return None
