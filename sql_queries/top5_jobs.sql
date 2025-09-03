SELECT 
  job_id, 
  COUNT(*) AS total_applications
FROM 
  recruitment_demo.applications
GROUP BY 
  job_id
ORDER BY 
  total_applications DESC
LIMIT 5;
