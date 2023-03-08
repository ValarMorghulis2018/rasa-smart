#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   actions.py
@Time    :   2023/03/08
@Author  :   liujie
@Desc    :   None
'''

from typing import Any, Text, Dict, List
from datetime import datetime, timedelta

from rasa_sdk.interfaces import Action, Tracker
from rasa_sdk.types import DomainDict
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa.core.actions.forms import FormAction
from rasa_sdk.forms import REQUESTED_SLOT

from rasa_sdk.events import AllSlotsReset


class ActionCheckMutations(Action):
    def name(self) -> Text:
        return "action_check_mutations"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_genesymbol = tracker.get_slot("genesymbol") or "null"
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_mutations {}-{}".format(text_genesymbol, text_sampleid))

        return [AllSlotsReset()]


class ActionCheckMoreMutations(Action):
    def name(self) -> Text:
        return "action_check_more_mutations"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_genesymbol = tracker.get_slot("genesymbol") or "null"
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_more_mutations {}-{}".format(text_genesymbol, text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]


class ActionCheckLungLowMutations(Action):
    def name(self) -> Text:
        return "action_check_lung_low_mutations"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_lung_low_mutations {}".format(text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]


class ActionCheckContaminationData(Action):
    def name(self) -> Text:
        return "action_check_contamination_data"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_contamination_data {}".format(text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]


class ActionCheckLungHotMutations(Action):
    def name(self) -> Text:
        return "action_check_lung_hot_mutations"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_lung_hot_mutations {}".format(text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]


class ActionCheckMsiResult(Action):
    def name(self) -> Text:
        return "action_check_msi_result"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_msi_result {}".format(text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]


class ActionCheckTmbResult(Action):
    def name(self) -> Text:
        return "action_check_tmb_result"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        text_sampleid = tracker.get_slot("sampleid") or "null"
        dispatcher.utter_message(
            text="action_check_tmb_result {}".format(text_sampleid))
        # tracker.custorm_reset_slot
        return [AllSlotsReset()]
