def test_import():
    import jmaplib  # noqa: PLC0415  # testing for import

    assert jmaplib.Client
    assert jmaplib.methods
    assert jmaplib.models
    assert jmaplib.errors
