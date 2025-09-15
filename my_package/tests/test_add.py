from appak import add, hello_world


def test_add():
    assert add(2, 3) == 5


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert "Hello World" in captured.out