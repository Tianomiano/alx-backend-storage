--  a SQL script that creates a stored procedure
--  ComputeAverageWeightedScoreForUsers that computes
--  and store the average weighted score for all students.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER |
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  UPDATE users AS User, 
    (SELECT User.id, SUM(score * weight) / SUM(weight) AS wt_avg 
    FROM users AS User 
    JOIN corrections as Corr ON User.id=Corr.user_id 
    JOIN projects AS Pro ON Corr.project_id=Pro.id 
    GROUP BY User.id)
  AS WtAvg
  SET User.average_score = WtAvg.wt_avg 
  WHERE User.id=WtAvg.id;
END;
