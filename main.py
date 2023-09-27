from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import heapq
from collections import defaultdict

app = FastAPI()


class Transaction(BaseModel):
    payer: str
    points: int
    timestamp: str


class SpendPoints(BaseModel):
    points: int


transactions = []
balances = defaultdict(int)
global_balance = 0


@app.post("/add")
async def add(transaction: Transaction):
    global global_balance
    heapq.heappush(
        transactions, (datetime.fromisoformat(transaction.timestamp[:-1]), transaction)
    )  # We ensure that the transactions are sorted by timestamp, worst case O(n log n)
    balances[transaction.payer] += transaction.points
    global_balance += transaction.points
    return


@app.post("/spend")
async def spend(spend_points: SpendPoints):
    global global_balance
    points = spend_points.points
    if points > global_balance:
        raise HTTPException(status_code=400, detail="Not enough points")
    spent = defaultdict(int)
    while points > 0 and transactions:
        timestamp, oldest_transaction = heapq.heappop(transactions)
        payer = oldest_transaction.payer
        available_points = min(points, balances[payer], oldest_transaction.points)
        balances[payer] -= available_points
        global_balance -= available_points
        points -= available_points
        spent[payer] -= available_points
        # If the transaction had more points than used, push it back with the remaining points
        remaining_points = oldest_transaction.points - available_points
        if remaining_points > 0:
            heapq.heappush(
                transactions,
                (
                    timestamp,
                    Transaction(
                        payer=payer, points=remaining_points, timestamp=str(timestamp)
                    ),
                ),
            )
    return [{"payer": k, "points": v} for k, v in spent.items()]


@app.get("/balance")
async def balance():
    return balances
