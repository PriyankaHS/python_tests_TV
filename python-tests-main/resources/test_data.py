class TestData:
    url = None
    browser = "chrome"
    env = "qa"  # Add the 'env' attribute

    @classmethod
    def set_environment(cls, env):
        if env == "test":
            cls.url = "https://testvagrant.myshopify.com/"
        elif env == "qa":
            cls.url = "https://testvagrant.myshopify.com/"
        elif env == "prod":
            cls.url = "https://testvagrant.myshopify.com/"
        else:
            raise ValueError(f"Unsupported environment: {env}")
