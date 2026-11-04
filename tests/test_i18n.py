from logparse.i18n import tr


def test_unknown_lang_falls_back_to_en():
    assert tr("xx", "parsed") == "parsed lines"
