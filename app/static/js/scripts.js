function updatePortfolio(data) {
    const cashBalanceElement = document.getElementById("cash-balance");
    cashBalanceElement.innerText = `$${data.cash_balance}`;
}

// Buy Stock function
function buyStock() {
    const stockId = prompt("Enter Stock ID:");
    const stockName = prompt("Enter Stock Name:");
    const stockPrice = parseFloat(prompt("Enter Stock Price:"));
    const shares = parseInt(prompt("Enter number of shares to buy:"));

    fetch('/buy', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stock_id: stockId, stock_name: stockName, stock_price: stockPrice, shares: shares })
    })
    .then(response => response.json())
    .then(data => {
        if (data.cash_balance) {
            updatePortfolio(data);  // Update the cash balance in UI
            alert(data.message);
        } else {
            alert("Transaction failed: " + data.message);
        }
    });
}

// Sell Stock function
function sellStock() {
    const stockName = prompt("Enter Stock Name:");
    const shares = parseInt(prompt("Enter number of shares to sell:"));

    fetch('/sell', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ stock_name: stockName, shares: shares })
    })
    .then(response => response.json())
    .then(data => {
        if (data.cash_balance) {
            updatePortfolio(data);  // Update the cash balance in UI
            alert(data.message);
        } else {
            alert("Transaction failed: " + data.message);
        }
    });
}
