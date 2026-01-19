import hashlib
import sys

def _integrity_check():
    FILE = __file__

    with open(FILE, "rb") as f:
        data = f.read()

    current_hash = hashlib.sha256(data).hexdigest()

    ORIGINAL_HASH = "f38d8b572d02e0d7a70a83bebfd2f43c21e719abf68dff4dd342d5decd98f851"

    if current_hash != ORIGINAL_HASH:
        print("🚫 تم اكتشاف تلاعب بالمكتبة!")
        sys.exit()

_integrity_check()
