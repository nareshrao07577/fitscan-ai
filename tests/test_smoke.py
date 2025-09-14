def test_imports():
    import importlib
    modules = ["pose_engine", "exercise_logic", "analytics", "gamification"]
    for m in modules:
        importlib.import_module(m)
    assert True
