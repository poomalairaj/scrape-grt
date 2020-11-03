# scrape-grt - scrape GRT jewels for gold price and plot it

This little python script scrapes GRT jewels (grtjewels.com/) and gets the latest gold price. The scraped prices are stored in a csv file.
This csv file is used to plot the gold price graph. I use this to track the 22ct gold price. This may be schedule in a cron job so that the updated price is automatically updated.

### To get the latest price:

```bash
docker-compose run --rm grt
```


### To plot the price graph

```bash
docker-compose run --rm plot
```

The output of the plot is a html file called `gold_price.html`
