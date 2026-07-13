from dataclasses import dataclass


@dataclass
class Trade:

    side: str

    entry: float

    exit: float

    profit: float

    win: bool


class Simulator:

    def __init__(self):

        self.balance = 10000.0

        self.initial_balance = 10000.0

        self.position = None

        self.trades = []

    def open_trade(
        self,
        side: str,
        price: float,
    ):

        if self.position is not None:
            return

        self.position = {
            "side": side,
            "entry": price,
        }

    def close_trade(
        self,
        price: float,
    ):

        if self.position is None:
            return

        side = self.position["side"]

        entry = self.position["entry"]

        if side == "BUY":

            profit = (
                (price - entry)
                / entry
            ) * 100

        else:

            profit = (
                (entry - price)
                / entry
            ) * 100

        self.balance *= (
            1 + profit / 100
        )

        trade = Trade(

            side=side,

            entry=round(entry, 2),

            exit=round(price, 2),

            profit=round(profit, 2),

            win=profit > 0,

        )

        self.trades.append(trade)

        self.position = None

    def total_trades(self):

        return len(self.trades)

    def winners(self):

        return len(
            [
                t
                for t in self.trades
                if t.win
            ]
        )

    def losers(self):

        return len(
            [
                t
                for t in self.trades
                if not t.win
            ]
        )

    def win_rate(self):

        if not self.trades:
            return 0

        return round(

            self.winners()
            / len(self.trades)
            * 100,

            2,

        )

    def net_profit(self):

        return round(

            self.balance
            - self.initial_balance,

            2,

        )

    def summary(self):

        return {

            "initialBalance": round(
                self.initial_balance,
                2,
            ),

            "finalBalance": round(
                self.balance,
                2,
            ),

            "netProfit": self.net_profit(),

            "totalTrades": self.total_trades(),

            "winningTrades": self.winners(),

            "losingTrades": self.losers(),

            "winRate": self.win_rate(),

            "trades": [

                trade.__dict__

                for trade in self.trades

            ],

        }