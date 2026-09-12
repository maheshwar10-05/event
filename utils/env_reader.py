from utils.yamlreader import YamlReader

class EnvReader:
    
    _config = None # cached config
    
    @classmethod
    def load(cls) -> dict:
        if cls._config is None:
            main_config = YamlReader.read_yaml("config.yaml",folder="config")
            env_name=main_config.get("env","qa")
            env_config=YamlReader.read_yaml(f"{env_name}.yaml",folder="config")
            cls._config={**main_config,**env_config}
        return cls._config
    @classmethod
    def get_env_config(cls) -> dict:
        return cls.load()