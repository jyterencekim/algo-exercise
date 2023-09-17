type Stock struct {
    price int
    lteCount int
}

type StockSpanner struct {
    stocks []Stock
}


func Constructor() StockSpanner {
    return StockSpanner { stocks: make([]Stock, 0) }
}


func (this *StockSpanner) Next(price int) int {
    lteCount := 1 // itself
    for len(this.stocks) > 0 && this.stocks[len(this.stocks)-1].price <= price {
        lteCount += this.stocks[len(this.stocks)-1].lteCount
        this.stocks = this.stocks[:len(this.stocks)-1]
    }
    this.stocks = append(this.stocks, Stock {price: price, lteCount: lteCount})
    
    return this.stocks[len(this.stocks)-1].lteCount
}


/**
 * Your StockSpanner object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Next(price);
 */