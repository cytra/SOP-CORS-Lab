# SOP-CORS-Lab

This project demonstrates the concepts of Same-Origin Policy (SOP) and Cross-Origin Resource Sharing (CORS) using a simple web application. The application consists of two servers to illustrate how SOP and CORS affect web requests.

## Prerequisites

- Python 3.x installed on your machine.
- Flask library for running the server. You can install it using pip:

  ```bash
  pip install Flask
  ```

## Setup Instructions

Follow these steps to set up and run the lab:

1. **Clone the Repository**

   Clone this repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd SOP-CORS-Lab
   ```

3. **Start Server 1 (CORS-Enabled Server)**

   Execute the following command to start Server 1 on Port 5000:

   ```bash
   python server.py
   ```

   This server handles cross-origin requests and is configured to demonstrate CORS.

4. **Start Server 2 (Static File Server)**

   Execute the following command to start Server 2 on Port 5500:

   ```bash
   python -m http.server 5500
   ```

   This server serves static files and is used to demonstrate same-origin requests.

5. **Access the Application**

   Open your web browser and navigate to:

   ```
   http://127.0.0.1:5500/index.html
   ```

   Use the buttons on the page to test same-origin and cross-origin requests.

## Project Structure

- `index.html`: The main HTML file containing the UI and JavaScript for making requests.
- `server.py`: The Flask server script handling API requests.
- `data.html`: A static HTML file served by Server 2.
- `README.md`: This file, providing setup instructions and project details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## Contact

For any questions or feedback, please contact [Your Name] at [Your Email].
