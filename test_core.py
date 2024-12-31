from sentinel_og.core import run_sentinel

def test_run_sentinel(capsys):
    run_sentinel()
    captured = capsys.readouterr()
    assert "Sentinel OG está listo para la acción." in captured.out