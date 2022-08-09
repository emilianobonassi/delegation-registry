import ape

ADDRESS_ZERO = '0x0000000000000000000000000000000000000000'

def test_default_value(registry, delegator):
    assert registry.delegateOf(delegator) == ADDRESS_ZERO

def test_delegate(registry, delegator, delegate):
    tx = registry.delegate(delegate,sender=delegator)

    assert registry.delegateOf(delegator) == delegate

    evt = next(registry.Delegation.from_receipt(tx))
    assert evt.delegator == delegator
    assert evt.delegate == delegate


def test_undelegate(registry, delegator, delegate):
    registry.delegate(delegate,sender=delegator)
    
    tx = registry.delegate(ADDRESS_ZERO,sender=delegator)

    assert registry.delegateOf(delegator) == ADDRESS_ZERO

    evt = next(registry.Delegation.from_receipt(tx))

    assert evt.delegator == delegator
    assert evt.delegate == ADDRESS_ZERO