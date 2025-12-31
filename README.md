# 🎬 CineQuest 📌 Project Description
CineQuest is a full-stack movie discovery platform that allows users to search for films, view details, and curate personal watchlists. The system uses a modern cloud-native architecture, separating frontend and backend services to ensure scalability and secure data persistence in the cloud.

## ⚙️ System Architecture
The application follows a decoupled client-server architecture with cloud database integration:
* **React (Vercel)** → Client-side user interface and state management
* **Flask (Render)** → REST API for handling requests and database logic
* **MySQL (Aiven)** → Cloud-based relational storage for user watchlists
* **TMDB API** → External source for real-time movie data

## 🚜 Features
* Real-time movie search via the TMDB API
* Persistent storage of user watchlists in Aiven MySQL
* Secure backend communication using SSL certificates
* Dynamic, responsive user interface built with React
* Cloud-deployed architecture (Vercel + Render)

## 🧪 Data Managed
* Movie Titles
* Poster Images
* User Watchlist IDs
* Movie Metadata (Release Dates, Ratings)

## 🛠️ Tech Stack
**Frontend**
* React.js
* CSS
* Fetch API

**Backend**
* Python
* Flask

**Database**
* MySQL (Aiven Cloud)

**Deployment & Tools**
* Vercel (Frontend)
* Render (Backend)
* Git
* VS Code
