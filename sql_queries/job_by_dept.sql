SELECT 
  department,
  COUNT(*) AS total_jobs
FROM 
  recruitment_demo.jobs
GROUP BY 
  department
ORDER BY 
  total_jobs DESC;
