# Spotify Song Recommender

This project is a Spotify Song Recommender application that enables users to log in with their Spotify account and receive personalized song recommendations based on their listening habits, favorite artists, and top songs. Built with a user-centered approach, this app helps users discover new music tailored to their tastes.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Spotify Login Integration**: Allows users to log in using their Spotify credentials.
- **Top Song and Artist Retrieval**: Fetches users' top songs and artists directly from their Spotify accounts.
- **Song Recommendations**: Generates music recommendations based on liked songs and favorite artists.
- **Intuitive UI**: Built with a user-friendly interface for seamless music discovery.

## Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

- **Node.js** (v14+)
- **Spotify Developer Account**: You’ll need to register an application on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to obtain a client ID and secret.

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/JulianCruzet/Spotify-Song-Recommender.git
   cd Spotify-Song-Recommender
   ```

2. **Install dependencies:**

   ```bash
   npm install
   ```

3. **Set up environment variables:**

   Create a `.env` file in the root directory and add your Spotify API credentials:

   ```bash
   SPOTIFY_CLIENT_ID=your_spotify_client_id
   SPOTIFY_CLIENT_SECRET=your_spotify_client_secret
   REDIRECT_URI=http://localhost:3000/callback
   ```

4. **Run the application:**

   ```bash
   npm start
   ```

5. **Access the application:**

   Open your browser and navigate to `http://localhost:3000`.

## Usage

1. **Login with Spotify**: Click the "Login with Spotify" button to authenticate your account.
2. **View Top Artists and Songs**: Once logged in, you can view your top artists and songs.
3. **Get Recommendations**: Based on your top songs and artists, receive curated song recommendations.

## Technologies Used

- **Frontend**: React, CSS, Framer Motion
- **Backend**: Node.js, Express
- **Spotify Web API**: For accessing user data and recommendations
- **Authentication**: OAuth 2.0 for secure login

## Contributing

Contributions are welcome! Please fork this repository and create a pull request with your changes.

## License

Distributed under the MIT License. See `LICENSE` for more information.