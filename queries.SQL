WITH order_summary AS (
SELECT
o.orderNumber,
o.orderDate,
o.status,
o.customerNumber,
SUM(od.quantityOrdered * od.priceEach) AS totalSales,
SUM(od.quantityOrdered * p.buyPrice) AS totalCost,
SUM((od.quantityOrdered * od.priceEach) - (od.quantityOrdered * p.buyPrice)) AS
totalProfit
FROM
orders o
INNER JOIN orderdetails od ON o.orderNumber = od.orderNumber
INNER JOIN products p ON od.productCode = p.productCode
GROUP BY
o.orderNumber, o.orderDate, o.status, o.customerNumber
)
SELECT
os.orderNumber,
os.orderDate,
os.status,
c.customerName,
c.country,
e.employeeNumber AS salesRepEmployeeNumber,
CONCAT(e.firstName,
' '
, e.lastName) AS salesRep,
os.totalSales,
os.totalCost,
os.totalProfit
FROM
order_summary os
INNER JOIN customers c ON os.customerNumber = c.customerNumber
LEFT JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber;
