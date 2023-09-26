from config.settings import Settings


class TestConfig:
    def test_load_config(self):
        assert (
            Settings.get_config() == {"environment": "development"}
        ), Settings().model_dump()
