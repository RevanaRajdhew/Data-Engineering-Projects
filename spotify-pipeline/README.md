# 🎧 Spotify Data Engineering Pipeline (AWS)

This is an end-to-end data engineering pipeline built using AWS services and real-world Spotify data. It demonstrates how raw music metadata can be transformed, queried, and analyzed using serverless cloud tools.

---

## 📌 Project Overview

We used datasets containing **Spotify albums**, **artists**, and **track data** and built a pipeline to:

- Ingest the data into **Amazon S3** (raw zone)
- Use **AWS Glue and PySpark** to transform and join the datasets
- Store processed data in **S3** (processed/data warehouse layer)
- Catalog the data using **Glue Crawlers** and **Glue Data Catalog**
- Query the processed data using **Amazon Athena**
- Visualize or explore the insights further using **Amazon QuickSight**
- Enable **query logging** using Athena to track all data access patterns

This project simulates the type of scalable, serverless pipelines used in modern data lake architectures.

---

## 📊 Example Queries and Insights

With the cleaned and structured data, we can answer analytical questions such as:

- 🎵 **Top 10 longest songs** by duration
- 🧑‍🎤 **Most prolific artists** by number of tracks
- 📀 **Albums with highest total duration**
- 📅 **Song releases by year**
- 🔍 **Average track duration** per artist or album
- 🗂️ **Track filtering** by genre, release year, or keyword

## 📐 Architecture

![Architecture Diagram](https://github.com/user-attachments/assets/62d63368-5ec8-4c9c-b9cc-35f50c524dca)

## 🛠️ Tech Stack

- Python (PySpark)
- AWS Glue
- AWS Glue Crawler
- Amazon S3
- Amazon Athena

## 📸 Screenshots

| Step          | Screenshot                                                                                              |
|---------------|-------------------------------------------------------------------------------------------------------- |
| S3 Structure  |  ![S3 Bucket Structure](https://github.com/user-attachments/assets/b3b5542c-d13e-409f-a147-ad76596aa3b2)|
| Glue Job      | ![Visual ETL Diagram](https://github.com/user-attachments/assets/6244d3e5-dce7-46ae-b39c-89871bb77120)  |
| Athena Query  | ![Athena SQL Query](https://github.com/user-attachments/assets/29938b33-d4cd-4b8d-aa5b-af0f393d95c1)    |

## 🔁 Next Steps

- Add a QuickSight dashboard export (if possible)
- Create a Terraform or CloudFormation version
- Try extending this with streaming data (e.g., Kinesis)

## 👩‍💻 Author

Revana Rajdhew  
[LinkedIn](www.linkedin.com/in/revanarajdhew)  
[GitHub](https://github.com/RevanaRajdhew)

