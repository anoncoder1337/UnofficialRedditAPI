# Plan for Unofficial Reddit API

## Phase 1: Basic Scraping
Make basic modules for scraping reddit, with a similar folder structure to the reddit api for consistency.
Running modules standalone, will return scraped data, all this code will be in the "backend" directory.

We will use a ABC(Abstract Class)/interface to implement different scraping instances for different endpoints.
We will support scraping via the old reddit site and the new one. This means we have a fallback if reddit changes their site, and makes the scraping more versatile.

## Phase 2: API server for endpoints
Start devloping API endpoints in the "frontend" folder, in FastAPI to connect to the scraping backend and provide complient Endpoints.

## Phase 3: API key Authentication & Database to allow multiple users to use the same API server.
Support creating API keys and having a database to store user credentials safely (this might be a bit difficult). But this allows for multi user setups.