FROM python:3.11.3-slim-buster

WORKDIR /app



# Copy requirements.txt và cài đặt các gói Python
COPY requirements.txt requirements.txt
# Install packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

# Copy tất cả các file trong thư mục hiện tại vào /app
COPY . .
# CMD để chạy ứng dụng của bạn khi container khởi chạy
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
