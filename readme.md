# Objective 📖

Develop a web applicadon and REST API that provides IPO-related informadon to the public. The
applicadon will display informadon such as company logo, name, price band, opening and closing
dates, issue size, issue type, lisdng date, status, IPO price, lisdng price, lisdng gain, current market
price (CMP), and current return. Addidonally, it will include downloadable RHP and DRHP PDFs.

# Features ⭐

The IPO Web Applicadon will provide the following informadon to the public:
- Company Logo
- Company Name
- Price Band
- Open Date
- Close Date
- Issue Size
- Issue Type
- Lisdng Date
- Status
- IPO Price
- Lisdng Price
- Lisdng Gain
- Current Market Price (CMP)
- Current Return
- RHP PDF
- DRHP PDF
This information will be available on both the Bluestock website/app and clients' websites/apps.

# Prerequisites 🔨

Before you begin, ensure you have met the following requirements:
- Python installed on your local machine. You can download it from [here](https://www.python.org/downloads/).
- Pip package manager installed. If you installed Python using Anaconda, you already have pip installed.
- Virtualenv installed. You can install it via pip by running `pip install virtualenv`.


# Run Locally 💻 (editing required)

1. Clone the project

```bash
  git clone https://github.com/AbhishekSingh-22/Bluestock-IPO-Backend.git
```

2. Go to the project directory

```bash
  cd space-Y-Assignment
```

3. Create virtual environment

```bash
  virtualenv venv
```

4. Activate virtual environment:

 - On Windows

 ```bash
 venv\Scripts\activate
 ```

 - On macOS and Linux

  ```bash
 source venv/bin/activate
 ```

5. Install the project dependencies

```bash
  pip install -r requirements.txt
```

6. Navigate to directory which contains manage.py file

```bash
  cd billingSystem
```

7. Run database migrations

```bash
  python manage.py migrate
```

8. Start the development server

```bash
  python manage.py runserver
```

9. Open your web browser and navigate to http://localhost:8000/ to view the project


