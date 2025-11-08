import pytest
from um import main

def test_no_um(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "This has no filler word.")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "0"

def test_simple_um(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "um")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "1"

    monkeypatch.setattr('builtins.input', lambda _: "Um um")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "2"

    monkeypatch.setattr('builtins.input', lambda _: "UM")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "1"

def test_um_with_punctuation(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Um! um. uM?")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "3"

def test_um_in_sentence(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Um, I think, um, maybe.")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "2"

    monkeypatch.setattr('builtins.input', lambda _: "Summary of the umbrella.")
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "0"
