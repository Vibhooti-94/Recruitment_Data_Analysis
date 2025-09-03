# 🛒 Ecommerce Recruitment Demo Project (SQL + BigQuery + Looker Studio)

A full-stack analytics project to simulate recruitment workflows for an ecommerce company using **BigQuery**, **SQL**, **Python**, and **Looker Studio**. This demo leverages **500MB+ of synthetic data** to showcase realistic reporting, joins, materialized views, and subqueries — ideal for beginners or portfolio projects.

---

## 📘 Project Overview

Recruitment is a key process for growing teams. This dataset simulates how HR analytics might look in a real company using mock (non-sensitive) data:

- **Job postings**
- **Candidates**
- **Applications**
- **Job locations**
- **Interview results**
- **Departments & Hiring teams**

All records are fake but modeled on **real-life HR systems** to reflect practical insights for dashboards, KPIs, and business decisions.

---

## 📦 Dataset Structure

The project contains the following tables in BigQuery:

| Table Name            | Description                                 |
|-----------------------|---------------------------------------------|
| `jobs`                | List of job postings                        |
| `candidates`          | Personal and profile info of applicants     |
| `applications`        | Applications submitted by candidates        |
| `locations`           | Cities and countries for each job           |
| `departments`         | Company departments (Engineering, etc.)     |
| `interview_results`   | Results and interview scores for applicants |

📄 Each table contains **100,000+ records** for scalable querying.

---

## 🔗 ER Diagram

![ERD](https://your-upload-link-or-local-path.com/erd.png)

**Legend**:
- 🔑 = Primary Key
- 🧩 = Foreign Key
- ➖ One-to-Many, ⬌ Many-to-Many

---

## ⚙️ Step-by-Step Guide

### 1️⃣ Generate Dummy Data (Python)

Run this script to create the CSV files (~500MB+ total):

```bash
python generate_recruitment_data.py
