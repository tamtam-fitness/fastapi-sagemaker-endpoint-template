from src.module.temp_class import TempClass


class TestTempClass:
    def test_add_temp(self) -> None:
        got = TempClass().add_temp("test_input_str_")

        assert "test_input_str_temp" == got
