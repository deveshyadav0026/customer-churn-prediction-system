-- CHURN ANALYSIS PROJECT (SQL + INSIGHTS)
--===============================================

-- Objective: Identify churn patterns and business actions



-- 1. Preview data
-------------------------


SELECT * 
FROM churn_predictions
LIMIT 5;

-- Insight:
-- Dataset contains customer demographics, behavior, and churn prediction metrics.
-- Ready for deeper analysis.







-- 2. Identify high-risk customers
----------------------------------------

SELECT *
FROM churn_predictions
WHERE risk_level = 'High'
ORDER BY churn_probability DESC;

-- Insight:
-- High-risk customers have the highest probability of churn.
-- These customers should be targeted immediately with retention offers.






-- 3. Percentage of high-risk customers
----------------------------------------------
SELECT 
    COUNT(*) * 100.0 / (SELECT COUNT(*) FROM churn_predictions) AS high_risk_pct
FROM churn_predictions
WHERE risk_level = 'High';

-- Insight:
-- Shows proportion of customers at risk.
-- If percentage is high → business is losing customers fast.
-- Requires urgent intervention strategy.






-- 4. Churn rate by marital status
---------------------------------------
SELECT 
    MaritalStatus,
    AVG(Churn) * 100 AS churn_rate
FROM churn_predictions
GROUP BY MaritalStatus;

-- Insight:
-- Helps identify which customer segment is more likely to churn.
-- Marketing strategies can be personalized for high-risk groups.






-- 5. Average engagement score of churned customers
--------------------------------------------------------
SELECT 
    AVG(Engagement_Score) AS avg_engagement
FROM churn_predictions
WHERE Churn = 1;

-- Insight:
-- Lower engagement usually indicates higher churn risk.
-- Improving engagement can reduce churn significantly.






-- 6. Top 10 highest risk customers
-- -----------------------------------------
SELECT *
FROM churn_predictions
ORDER BY Churn_Probability DESC
LIMIT 10;

-- Insight:
-- These are the most critical customers.
-- Business can directly target them with personalized retention campaigns.







-- 7. Churn distribution by preferred category
---------------------------------------------------

SELECT 
    PreferedOrderCat,
    COUNT(*) AS total_customers,
    SUM(Churn) AS churned_customers
FROM churn_predictions
GROUP BY PreferedOrderCat;

-- Insight:
-- Identifies which product categories have higher churn.
-- Poor experience in specific categories may be causing churn.







-- 8. Avg cashback vs churn
---------------------------------
SELECT 
    Churn,
    AVG(CashbackAmount) AS avg_cashback
FROM churn_predictions
GROUP BY Churn;

-- Insight:
-- Helps understand if cashback influences retention.
-- If churned users have low cashback → incentives need improvement.








-- 9. Device usage vs churn
----------------------------------
SELECT 
    NumberOfDeviceRegistered,
    AVG(Churn) * 100 AS churn_rate
FROM churn_predictions
GROUP BY NumberOfDeviceRegistered;

-- Insight:
-- Shows relationship between device usage and churn.
-- Low device usage may indicate weak engagement.









-- 10. Engagement score vs risk level
---------------------------------------------
SELECT 
    Risk_Level,
    AVG(Engagement_Score) AS avg_engagement
FROM churn_predictions
GROUP BY Risk_Level;

-- Insight:
-- Confirms that high-risk customers generally have lower engagement.
-- Reinforces importance of engagement-driven retention strategies.