from pathlib import Path

# Get the project root directory (where setup.py is located)
# This file is in src/mlproject/constants/, so we go up 3 levels
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent

CONFIG_FILE_PATH = PROJECT_ROOT / "config" / "config.yaml"
PARAMS_FILE_PATH = PROJECT_ROOT / "params.yaml"
SCHEMA_FILE_PATH = PROJECT_ROOT / "schema.yaml"