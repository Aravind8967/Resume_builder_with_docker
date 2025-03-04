# Resume_builder_with_docker

# Resume Builder Project

A modern, Dockerized Resume Builder web application that allows users to create, edit, and print their resumes. The application uses a sleek dark theme for an impressive editing experience and automatically switches to a clean white layout with black text when printing. It leverages Flask as the backend framework and MongoDB for data storage, all containerized with Docker and orchestrated using Docker Compose.

## Table of Contents

- [Features](#features)
- [Architecture & Services](#architecture--services)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Dynamic Resume Builder**: Enter personal details, work experience, education, and project information.
- **Add/Remove Functionality**: Easily add or remove sections (work experience, education, projects) as needed.
- **Print & Edit Options**: Generate a resume with Print and Edit buttons (no download button).
- **Dark Theme with Print Override**: Enjoy a modern dark interface during editing that automatically converts to a white background with black text when printing.
- **Dockerized Setup**: Both the Flask application and MongoDB are containerized for a hassle-free local setup.

## Architecture & Services

This project comprises the following services:

- **Flask**: Serves as the web backend that handles routing, form submissions, and resume generation.
- **MongoDB**: Stores user resume data in a NoSQL database. The database is configured to use the `resume_builder` database.
- **Docker & Docker Compose**: Containerizes the application, ensuring that the Flask app and MongoDB run seamlessly together. Data persistence for MongoDB is handled via a named Docker volume.

## Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed.
- (Optional) Git installed to clone the repository.

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/resume-builder.git
   cd resume-builder

2. **Build and Run the Containers**

  ```bash
  docker compose -f .\docker-compose.yaml up --build -d
```

**This command will:**
  
  Build the Flask application container from the Dockerfile located in the ./backend directory.
  Pull and run the official MongoDB image, exposing it on port 27017.
  Create a Docker volume (mongo_data) to persist MongoDB data.
  Expose the Flask app on port 80 of your host machine

3. **Access the Application**

Open your web browser and navigate to:

```bash
  http://localhost/
```





