document.addEventListener("DOMContentLoaded", function() {
    console.log("Bull Market Simulator Loaded");

    // Mockup function to display a market event
    function displayMarketEvent(event) {
        const eventContainer = document.getElementById("market-event");
        eventContainer.innerText = event;
    }

    // Function to simulate market conditions
    window.triggerMarketEvent = function() {
        fetch('/market')
            .then(response => response.json())
            .then(data => {
                displayMarketEvent(data.event);
            });
    };

    // Function to handle stock buying
    window.buyStock = function() {
        const stockId = prompt("Enter Stock ID to Buy:");
        const shares = prompt("Enter number of shares:");
        fetch('/buy', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ stock_id: stockId, shares: shares })
        })
        .then(response => response.json())
        .then(data => alert(data.message));
    };

    // Function to handle stock selling
    window.sellStock = function() {
        const stockId = prompt("Enter Stock ID to Sell:");
        const shares = prompt("Enter number of shares:");
        fetch('/sell', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ stock_id: stockId, shares: shares })
        })
        .then(response => response.json())
        .then(data => alert(data.message));
    };
});
