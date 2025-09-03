SELECT 
  j.job_id,
  j.job_title,
  COUNT(a.application_id) AS total_applications
FROM 
  recruitment_demo.jobs j
JOIN 
  recruitment_demo.applications a
ON 
  j.job_id = a.job_id
GROUP BY 
  j.job_id, j.job_title
ORDER BY 
  total_applications DESC
LIMIT 5;
