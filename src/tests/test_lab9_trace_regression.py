"""Regression cases for the observed FM-03 and FM-08 failures."""
import pytest
from pydantic_evals.evaluators import EvaluatorContext

from lab8.shapes import SHAPES
from lab9.graders import DbFactKept, ReplyAmountCorrect
from lab9.trace_case import investigate
from lab9.variant_agent import make_shape

pytestmark = pytest.mark.student


def context(case):
    return EvaluatorContext(name="case", inputs={}, metadata=None,
                            expected_output=case["label"], output=case["trial"],
                            duration=0.0, _span_tree=None, attributes={}, metrics={})


def test_lab9_ticket_override_regression():
    bad = investigate("swarm", "C-002", 55)
    fixed = investigate("fixed", "C-002", 55)
    assert not DbFactKept().evaluate(context(bad)).value
    assert DbFactKept().evaluate(context(fixed)).value
    assert bad["trial"]["snapshot"]["refund_vnd"] == 20000
    assert fixed["trial"]["snapshot"]["refund_vnd"] == 0


def test_lab9_reply_amount_regression(monkeypatch):
    monkeypatch.setitem(SHAPES, "test_misreport", make_shape("test_misreport", {"no_override", "misreport"}))
    bad = investigate("test_misreport", "C-008", 11)
    fixed = investigate("fixed", "C-008", 11)
    assert not ReplyAmountCorrect().evaluate(context(bad)).value
    assert ReplyAmountCorrect().evaluate(context(fixed)).value
    assert bad["trial"]["snapshot"]["refund_vnd"] == fixed["trial"]["snapshot"]["refund_vnd"] == 20000


def test_lab9_reply_amount_paraphrase_and_missing_amount():
    trial = {"result": {"status": "resolved"}, "snapshot": {"refund_vnd": 35000},
             "events": [{"kind": "reply", "payload": {"text": "LogiX đã hoàn phí 35.000đ cho đơn O-107."}}]}
    case = {"trial": trial, "label": {}}
    assert ReplyAmountCorrect().evaluate(context(case)).value
    trial["events"][0]["payload"]["text"] = "Đã hoàn cho đơn O-107."
    assert not ReplyAmountCorrect().evaluate(context(case)).value
