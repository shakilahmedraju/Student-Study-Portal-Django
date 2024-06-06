# Student Study Portal | Django Application

This is a Student Study Portal built using Django, HTML, CSS, and JavaScript. The application integrates various APIs such as Google Books API, YouTube API, Wikipedia API, and Dictionary API to fetch relevant data when a student searches. It includes features like signup and signin, notes, homework, todo lists, and sections for YouTube, books, dictionary, Wikipedia, and unit conversion.

## Features

- **User Authentication**: Signup and signin functionality.
- **API Integrations**:
  - **Google Books API**: Fetch book information.
  - **YouTube API**: Retrieve YouTube videos.
  - **Wikipedia API**: Get Wikipedia content.
  - **Dictionary API**: Look up word definitions.
- **Sections**:
  - **Notes**: Create and manage study notes.
  - **Homework**: Track homework assignments.
  - **ToDo List**: Organize tasks and to-dos.
  - **YouTube**: Search and watch educational videos.
  - **Books**: Find and read book information.
  - **Dictionary**: Look up word meanings and definitions.
  - **Wikipedia**: Search and read Wikipedia articles.
  - **Conversion**: Perform various unit conversions.

## Demo

### Home
![Alt text](/studentStudyPortal/static/images/Student-dashboard.png "Home")

### Youtube
![Alt text](/studentStudyPortal/static/images/Youtube.png "youtube")

### Books
![Alt text](/studentStudyPortal/static/images/books.png "books")


## Getting Started

### Prerequisites

Make sure you have Python and Django installed. You can download Python from [python.org](https://www.python.org/) and install Django using pip.

### Installation

1. Clone the repository:

   ```run
   git clone https://github.com/shakilahmedraju/Student-Study-Portal-Django.git

2. Navigate to the project directory:

   ```run: 
   cd studentStudyPortal
   
3. Create a virtual environment:

   ```run
  python -m venv venv

4. Activate the virtual environment:

   ```run
   .\venv\Scripts\activate

5. Install the required packages:

   ```run: 
   pip install -r requirements.txt

6. Apply migrations:

   ```run: 
   python manage.py migrate

7. Start the development server:

   ```run: 
   python manage.py runserver

##  Technologies Used
- **Django:** A high-level Python web framework.
- **HTML/CSS/JavaScript:** For frontend development.
- **Google Books API:** To fetch book data.
- **YouTube API:** To retrieve videos.
- **Wikipedia API:** To get Wikipedia content.
- **Dictionary API:** To look up word definitions.
## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (\`git checkout -b feature/your-feature-name\`).
3. Make your changes.
4. Commit your changes (\`git commit -am 'Add some feature'\`).
5. Push to the branch (\`git push origin feature/your-feature-name\`).
6. Create a new Pull Request.

## Contact
If you have any questions or feedback, please feel free to reach out to me at iamshakilahmedraju@gmail.com.
