import yaml

from pathlib import Path

class YamlReader:
    
    @staticmethod
    def _get_framework_root() -> Path:
        return Path(__file__).resolve().parents[1]
    
    @staticmethod
    def read_yaml(filename: str, folder: str = "data") ->dict:
        
        path = YamlReader._get_framework_root() / folder / filename
        
        if not path.exists():
            raise FileNotFoundError(f"Yaml file not found: {path}")
        
        with path.open("r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}