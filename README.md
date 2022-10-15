# MAL-Profile-Scraper

This is a python project that scrapes a MyAnimeList profile without the use of the official MyAnimeList API. This project was created with Python version 3.9.6.

There are 3 modules used: - requests - beautiful soup - datetime

## Functionality

This code basically scans the HTML of given MyAnimeList profile page for: - Number of days watched (`Days`) - Total number of user entries (`Total Entries`) - Total number of episodes watched (`Episodes`) - Number of entries completed (`Completed`) - Number of entries currently being watched (`Watching`) - Number of entries planned to watch (`Planned`) - Number of entries user has rewatched (`Rewatched`) - Average scoring a user scores (`MeanScore`)
