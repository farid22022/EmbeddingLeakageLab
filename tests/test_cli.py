from embedding_leakage.cli.main import main


def test_status_command(capsys) -> None:
    assert main(["status"]) == 0
    assert "Phase 0" in capsys.readouterr().out


def test_phase_show_command(capsys) -> None:
    assert main(["phase", "show", "0"]) == 0
    assert "Literature Review" in capsys.readouterr().out


def test_unknown_phase_returns_error(capsys) -> None:
    assert main(["phase", "show", "99"]) == 2
    assert "not in the roadmap" in capsys.readouterr().err


def test_roadmap_lists_phases(capsys) -> None:
    assert main(["roadmap"]) == 0
    assert "Repository Foundation" in capsys.readouterr().out


def test_help(capsys) -> None:
    import pytest

    with pytest.raises(SystemExit) as exit_info:
        main(["--help"])
    assert exit_info.value.code == 0
    assert "EmbeddingLeakageLab" in capsys.readouterr().out
