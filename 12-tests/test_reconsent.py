from continuity.continuity import requires_reconsent


def test_material_continuity_change_requires_reconsent():
    assert requires_reconsent({"MODEL_REPLACEMENT"}) is True
    assert requires_reconsent({"MEMORY_MIGRATION"}) is True
    assert requires_reconsent({"CAPABILITY_EXPANSION"}) is True


def test_inherited_authority_requires_reconsent_even_without_named_change_type():
    assert requires_reconsent(set(), inherited_authority=True) is True


def test_nonmaterial_change_does_not_force_reconsent_in_reference_rule():
    assert requires_reconsent({"UI_LABEL_CHANGE"}) is False
