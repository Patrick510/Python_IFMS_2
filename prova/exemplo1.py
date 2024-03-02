from dataclasses import make_dataclass

Stock = make_dataclass("Stock", ("symbol", "current", "high", "low"))


