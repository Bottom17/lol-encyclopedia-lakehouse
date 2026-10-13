import lol_encyclopedia_lakehouse


def test_main_prints_greeting(capsys):
    lol_encyclopedia_lakehouse.main()
    captured = capsys.readouterr()

    assert captured.out == "Hello from lol-encyclopedia-lakehouse!\n"
