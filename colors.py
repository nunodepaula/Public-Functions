from dataclasses import dataclass, asdict

@dataclass
class Rgb:
    red: int
    green: int
    blue: int

    @property
    def to_hex(self) -> str:
        return f"#%02x%02x%02x" % (self.red, self.green, self.blue)

    @property
    def to_dict(self) -> dict:
        return asdict(self)