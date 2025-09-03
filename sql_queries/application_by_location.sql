SELECT 
  j.location,
  COUNT(a.application_id) AS total_applications
FROM 
  recruitment_demo.jobs j
JOIN 
  recruitment_demo.applications a
ON 
  j.job_id = a.job_id
GROUP BY 
  j.location
ORDER BY 
  total_applications DESC;
