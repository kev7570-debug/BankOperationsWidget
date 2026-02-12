import pytest

from src.decorators import log


@pytest.fixture
def clear_log_file(tmp_path):
    log_file = tmp_path / "test.log"
    log_file.touch()
    yield log_file
    log_file.unlink(missing_ok=True)


def test_successful_execution(capsys):
    @log()
    def successful_function(x, y):
        return x + y

    successful_function(1, 2)
    captured = capsys.readouterr()
    assert "successful_function" in captured.out
    assert "(1, 2)" in captured.out
    assert "returned 3" in captured.out


def test_error_handling(capsys):
    @log()
    def failing_function(x, y):
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        failing_function(1, 2)
    captured = capsys.readouterr()
    assert "failing_function" in captured.out
    assert "(1, 2)" in captured.out
    assert "raised ValueError:" in captured.out


def test_logging_to_file(clear_log_file):
    @log(filename=str(clear_log_file))
    def logged_function(x, y):
        return x + y

    logged_function(1, 2)
    with open(clear_log_file, "r") as f:
        content = f.read()
        assert "logged_function" in content
        assert "(1, 2)" in content
        assert "returned 3" in content
