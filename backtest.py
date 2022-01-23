from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed


class BuyAndHoldStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        super(BuyAndHoldStrategy, self).__init__(feed)
        self.instrument = instrument
        self.setUseAdjustedValues(True)
        self.position = None

    def onEnterOk(self, position):
        self.info(f"{position.getEntryOrder().getExecutionInfo()}")

    def onBars(self, bars):
        bar = bars[self.instrument]
    
        if self.position is None:
            close = bar.getAdjClose()
            broker = self.getBroker()
            cash = broker.getCash()
            quantity = cash / close
            self.position = self.enterLong(self.instrument, quantity)

# Load the bar feed from the CSV file
feed = yahoofeed.Feed()
feed.addBarsFromCSV("SPY", "SPY.csv")

# Evaluate the strategy with the feed's bars.
strategy = BuyAndHoldStrategy(feed, "SPY")
strategy.run()

portfolio_value = strategy.getBroker().getEquity() + strategy.getBroker().getCash()
print(portfolio_value)
