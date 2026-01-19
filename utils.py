import random
import string

WORDS = [
    "apple", "brave", "crisp", "delta", "eagle", "flame", "grove", "hazel",
    "ivory", "jewel", "karma", "lunar", "maple", "noble", "ocean", "pearl",
    "quest", "river", "solar", "tiger", "ultra", "vivid", "waltz", "xenon",
    "yacht", "zephyr", "amber", "blaze", "cloud", "drift", "ember", "frost",
    "gleam", "haven", "ideal", "jazzy", "knack", "lemon", "mango", "north",
    "oasis", "prism", "quilt", "rusty", "spice", "trace", "unity", "velvet"
]

def generate_id(length: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return "".join(random.choice(chars) for _ in range(length))

def generate_name() -> str:
    return f"{random.choice(WORDS)}-{random.choice(WORDS)}"
