from pathlib import Path
import sys

ENGINE_DIR = Path(__file__).resolve().parents[3] / "engine"
if str(ENGINE_DIR) not in sys.path:
    sys.path.insert(0, str(ENGINE_DIR))

from ontomiko.diviner_v2 import divine_text  # noqa: E402

def divine_text_service(text: str):
    result = divine_text(text)
    return result.to_dict()
