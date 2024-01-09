# Weather App

## Overview

The Weather App is a simple web application built with Flask that allows users to retrieve current weather information for a specified location. It uses the OpenWeatherMap API to fetch real-time weather data.

## Features

- **Location-based Weather:** Users can enter the city, state, and country to get the current weather information for that location.

## Prerequisites

Before running the application, ensure you have the following:

- Python installed (version 3.6 or higher)
- OpenWeatherMap API key

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/MfidiV/Weather_App.git
    cd weather-app
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up your environment variables:**

    Create a `.env` file in the root directory and add your OpenWeatherMap API key:

    ```env
    API_KEY=your_openweathermap_api_key
    ```

## Usage

1. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Linux or macOS
    venv\Scripts\activate  # On Windows
    ```

2. **Run the Flask application:**

    ```bash
    python app.py
    ```

3. **Open your web browser and go to `http://127.0.0.1:5000/` to access the Weather App.**

4. **Enter the desired location details and click "Find" to retrieve the weather information.**

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
