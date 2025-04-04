import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')


query = """
    SELECT 
        Customer.CustomerId, 
        Customer.FirstName || ' ' || Customer.LastName AS CustomerName, 
        SUM(Invoice.Total) AS TotalSpent
    FROM Invoice
    JOIN Customer ON Invoice.CustomerId = Customer.CustomerId
    GROUP BY Customer.CustomerId
    ORDER BY TotalSpent DESC
    LIMIT 5;
"""
top_customers = pd.read_sql(query, conn)

print("Top 5 Customers by Total Purchases:")
print(top_customers)

conn.close()

conn = sqlite3.connect('chinook.db')

query = """
    WITH AlbumTracks AS (
        SELECT Album.AlbumId, COUNT(Track.TrackId) AS TotalTracks
        FROM Album
        JOIN Track ON Album.AlbumId = Track.AlbumId
        GROUP BY Album.AlbumId
    ),
    CustomerPurchases AS (
        SELECT Invoice.CustomerId, InvoiceLine.TrackId, Album.AlbumId
        FROM InvoiceLine
        JOIN Track ON InvoiceLine.TrackId = Track.TrackId
        JOIN Album ON Track.AlbumId = Album.AlbumId
        GROUP BY Invoice.CustomerId, Album.AlbumId, InvoiceLine.TrackId
    ),
    CustomerAlbumPurchases AS (
        SELECT CustomerPurchases.CustomerId, CustomerPurchases.AlbumId, COUNT(CustomerPurchases.TrackId) AS TracksBought
        FROM CustomerPurchases
        GROUP BY CustomerPurchases.CustomerId, CustomerPurchases.AlbumId
    )
    SELECT 
        (SELECT COUNT(DISTINCT CustomerId) FROM CustomerAlbumPurchases WHERE TracksBought < (SELECT TotalTracks FROM AlbumTracks WHERE AlbumTracks.AlbumId = CustomerAlbumPurchases.AlbumId)) AS IndividualTrackBuyers,
        (SELECT COUNT(DISTINCT CustomerId) FROM CustomerAlbumPurchases WHERE TracksBought = (SELECT TotalTracks FROM AlbumTracks WHERE AlbumTracks.AlbumId = CustomerAlbumPurchases.AlbumId)) AS AlbumBuyers,
        (SELECT COUNT(DISTINCT CustomerId) FROM CustomerAlbumPurchases) AS TotalCustomers;
"""

summary = pd.read_sql(query, conn)
conn.close()

summary['Individual Track Buyers %'] = (summary['IndividualTrackBuyers'] / summary['TotalCustomers']) * 100
summary['Album Buyers %'] = (summary['AlbumBuyers'] / summary['TotalCustomers']) * 100

print("\nPercentage of Customers Buying Individual Tracks vs. Full Albums:")
print(summary[['Individual Track Buyers %', 'Album Buyers %']])