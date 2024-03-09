import feedparser

euro_to_try = feedparser.parse("https://www.ecb.europa.eu/rss/fxref-try.html")["entries"]
euro_to_dollar = feedparser.parse("https://www.ecb.europa.eu/rss/fxref-usd.html")["entries"]

euro_exchange = 1
euro_try_exchange = float(euro_to_try[0]["title"][:5])
euro_dollar_exchange = float(euro_to_dollar[0]["title"][:5])
dollar_try_exchange = (euro_exchange / euro_dollar_exchange) * euro_try_exchange
print("{0:.5g}".format(euro_try_exchange))
print("{0:.5g}".format(dollar_try_exchange))
print("{0:.5g}".format(euro_dollar_exchange))
