# AuctionSpot

AuctionSpot is an online auction system developed in Django Python, designed to provide a platform for users to participate in auctions and manage their bids. Utilizing the WebSockets protocol through Django Channels with Daphne, AuctionSpot offers real-time bid updates and interactive auction experiences.

## Installation

Before running the project, ensure that Redis and Python are installed on your computer.

### Redis Installation

Redis is used as a backend for handling channels in Django Channels. You can install Redis by following the instructions on the [official Redis website](https://redis.io/download).

### Project Setup

1. Clone the repository using the following command:
```git clone https://github.com/n-pradip/AuctionSpot.git```

2. Navigate to the project directory:
```cd AuctionSpot```

3. Install the required Python packages:
```pip install -r requirements.txt```

4. Apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```

To start the development server, run the following command:

```python manage.py runserver```

Once the server is running, you can access the application at `http://localhost:8000`.
