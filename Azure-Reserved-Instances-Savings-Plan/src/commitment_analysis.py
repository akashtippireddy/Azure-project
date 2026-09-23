"""Starter calculations for Azure commitment analysis."""

from dataclasses import dataclass


@dataclass
class CommitmentEstimate:
    on_demand_cost: float
    committed_cost: float

    @property
    def estimated_savings(self) -> float:
        return self.on_demand_cost - self.committed_cost

    @property
    def savings_rate(self) -> float:
        if self.on_demand_cost <= 0:
            return 0.0
        return self.estimated_savings / self.on_demand_cost


def estimate_commitment(on_demand_cost: float, committed_cost: float) -> CommitmentEstimate:
    """Return a simple cost and savings estimate for a commitment option."""
    if on_demand_cost < 0 or committed_cost < 0:
        raise ValueError("Costs must be non-negative")
    return CommitmentEstimate(on_demand_cost, committed_cost)
