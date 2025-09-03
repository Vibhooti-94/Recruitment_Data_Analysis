CREATE MATERIALIZED VIEW recruitment_demo.mv_top_jobs AS
SELECT 
  job_id,
  COUNT(*) AS total_applications
FROM 
  recruitment_demo.applications
GROUP BY 
  job_id;
