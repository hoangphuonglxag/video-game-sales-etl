# video-game-sales-etl
ETL project for video game sales data using Python

20 / 06 / 2025
video-game-sales-etl

ETL (Extract – Transform – Load) project for video game sales data using Python and PostgreSQL.

Mục tiêu

Thực hiện pipeline ETL xử lý dữ liệu vgsales.csv.
Làm sạch và chuẩn hóa dữ liệu.
Nạp dữ liệu vào cơ sở dữ liệu PostgreSQL để phục vụ phân tích sau này.
Cấu trúc thư mục

video-game-sales-etl/ ├── data/ # Thư mục chứa dữ liệu gốc │ └── vgsales.csv ├── etl/ # Chứa các bước ETL │ ├── extract.py │ ├── transform.py │ └── load.py ├── database/ # Chứa file định nghĩa cấu trúc bảng │ └── schema.sql ├── main.py # Chạy toàn bộ pipeline ├── requirements.txt # Các thư viện cần cài └── README.md

Công nghệ sử dụng

Python (pandas, psycopg2)
PostgreSQL
Git + GitHub
VSCode / WSL hoặc Linux
Cách sử dụng

Tạo môi trường ảo (nếu cần): python3 -m venv venv source venv/bin/activate

Cài đặt thư viện: pip install -r requirements.txt

Khởi tạo CSDL: Tạo bảng từ file database/schema.sql bằng PostgreSQL.

**Chạy ETL pipeline: python main.py

Dataset
Dữ liệu được lấy từ Kaggle - Video Game Sales

Ghi chú

Dự án mang tính học tập và thực hành xử lý dữ liệu ETL.
Dữ liệu có thể được mở rộng để phân tích xu hướng thị trường game.