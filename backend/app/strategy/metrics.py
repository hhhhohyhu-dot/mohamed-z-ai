from typing import List


def calculate_profit_factor(
    profits: List[float],
) -> float:

    gross_profit = sum(
        p for p in profits if p > 0
    )

    gross_loss = abs(
        sum(
            p for p in profits if p < 0
        )
    )

    if gross_loss == 0:
        return 999.99

    return round(
        gross_profit / gross_loss,
        2,
    )


def calculate_average_trade(
    profits: List[float],
) -> float:

    if not profits:
        return 0.0

    return round(
        sum(profits) / len(profits),
        2,
    )


def calculate_max_drawdown(
    balances: List[float],
) -> float:

    if not balances:
        return 0.0

    peak = balances[0]

    max_drawdown = 0.0

    for balance in balances:

        if balance > peak:
            peak = balance

        drawdown = (
            (peak - balance)
            / peak
        ) * 100

        if drawdown > max_drawdown:
            max_drawdown = drawdown

    return round(
        max_drawdown,
        2,
    )


def build_metrics(
    balances: List[float],
    profits: List[float],
):

    return {

        "profitFactor":
            calculate_profit_factor(
                profits
            ),

        "averageTrade":
            calculate_average_trade(
                profits
            ),

        "maxDrawdown":
            calculate_max_drawdown(
                balances
            ),

    }