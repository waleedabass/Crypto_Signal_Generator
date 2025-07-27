from pydantic import BaseModel
from typing import List, Union

class TradeSignal(BaseModel):
    symbol: str
    recommendation: str
    timeframe: str
    position_type: str
    entry_range: List[Union[float, str]]
    dca: Union[float, str]
    stoploss: Union[float, str]
    targets: List[Union[float, str]]
    analysis: str
    note: str


    def render(self) -> str:
        output = []
        output.append(f"#{self.symbol} {self.recommendation} {self.timeframe} 🚀🚀")
        output.append(f"OR #{self.symbol} {self.position_type} 🚀🚀\n")

        # Entry range
        if isinstance(self.entry_range, list) and len(self.entry_range) == 2:
            try:
                entry_start = float(self.entry_range[0])
                entry_end = float(self.entry_range[1])
                output.append(f"✳️ Entry:   {entry_start:.4f} - {entry_end:.4f}")
            except:
                output.append(f"✳️ Entry:   {self.entry_range}")
        else:
            output.append(f"✳️ Entry:   {self.entry_range}")

        # DCA
        try:
            dca_val = float(self.dca)
            output.append(f"DCA:  {dca_val:.4f}\n")
        except:
            output.append(f"DCA:  {self.dca}\n")

        # Stoploss
        try:
            stop = float(self.stoploss)
            output.append(f"🔴 Stoploss: {stop:.4f}\n")
        except:
            output.append(f"🔴 Stoploss: {self.stoploss}\n")

        # Targets
        output.append("🟢 Targets :\n")
        for i, target in enumerate(self.targets, 1):
            try:
                target_val = float(target)
                output.append(f"    🎯{i}) {target_val:.4f}")
            except:
                output.append(f"    🎯{i}) {target}")

        # Analysis and Note
        output.append(f"\n📊 Analysis:\n{self.analysis}")
        output.append(f"\n⚠️ {self.note}")
        return "\n".join(output)
