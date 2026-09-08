from dataclasses import replace
from concurrent.futures import ThreadPoolExecutor
import json
import pytest
from ledger.ledger import LedgerEvent, RelationalLedger, OPERATIVE


def event(payload):
    return LedgerEvent('r', 'CONSENT', 'a', 'consent', payload, projection_status=OPERATIVE)

@pytest.mark.parametrize('access', ['input','append_result','events','projection'])
def test_F029_nested_read_or_caller_mutation_cannot_change_retained_event(access):
    payload = {'active': True, 'nested': {'list': ['a'], 'set': {'a'}, 'dict': {'x': 1}}}
    original = event(payload); ledger = RelationalLedger(); returned = ledger.append(original)
    views = {'input': payload, 'append_result': returned.payload,
             'events': ledger.events('r')[0].payload, 'projection': ledger.project('r')['consent']}
    selected = views[access]
    selected['active'] = False; selected['nested']['list'].clear()
    selected['nested']['set'].add('outsider'); selected['nested']['dict']['x'] = 0
    retained = ledger.events('r')[0].payload
    assert retained == {'active': True, 'nested': {'list': ['a'], 'set': {'a'}, 'dict': {'x': 1}}}
    assert ledger.project('r')['consent'] == retained
    assert len(ledger.events('r')) == 1


def test_F029_serialization_and_explicit_event_have_separate_history():
    ledger = RelationalLedger(); e = event({'nested': {'active': True}}); ledger.append(e)
    projected = json.loads(json.dumps(ledger.project('r')))
    projected['consent']['nested']['active'] = False
    ledger.append(event(projected['consent']))
    assert ledger.events()[0].payload['nested']['active'] is True
    assert ledger.project('r')['consent']['nested']['active'] is False


def test_F029_concurrent_duplicate_identity_one_append():
    ledger = RelationalLedger(); e = event({'active': True})
    def append(_):
        try: ledger.append(e); return True
        except ValueError: return False
    with ThreadPoolExecutor(4) as pool:
        assert sum(pool.map(append, range(8))) == 1
    assert len(ledger.events()) == 1
    with pytest.raises(ValueError): ledger.append(replace(e, payload={'active': False}))
    assert ledger.project('r')['consent']['active'] is True


def test_custom_copy_bypass_and_cycles_rejected_before_append():
    class Aliased:
        def __deepcopy__(self, memo): return self
    ledger = RelationalLedger()
    with pytest.raises(ValueError): ledger.append(event({'x': Aliased()}))
    cyclic = {}; cyclic['self'] = cyclic
    with pytest.raises(ValueError): ledger.append(event(cyclic))
    assert not ledger.events()
