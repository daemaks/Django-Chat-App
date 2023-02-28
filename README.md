# Django Chat Application
This is a Django chat application that allows two users to communicate with each other by exchanging messages. The application provides endpoints for creating and deleting threads, sending and receiving messages, marking messages as read, and getting the number of unread messages for a user.

## Installation and Setup

To run the application, you should have python 3 and pip installed on your machine. Once you have these installed, follow these steps:

1. Clone the repo:
    ```
    git clone https://github.com/daemaks/Django-Chat-App
    ```
2. Enter the project directory:
    ```
    cd Django-Chat-App
    ```
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
4. Apply the db migrations:
    ```
    python3 manage.py migrate
    ```
5. Start the server:
    ```
    python3 manage.py runserver
    ```
## Usage
    The app provides the following endpoints:
*   **`POST /api/user/register/`** : Create a user.
    #### JSON example
    ```
    {
    "username": "tester",
    "password": "superstrongpassword"
    }
    ```
*   **`POST /token/refresh/`** : Get an access and refresh token.
    #### JSON example
    ```
    {
    "username": "tester",
    "password": "superstrongpassword"
    }
    ```
*   **`POST /api/threads/`** : Create a new thread for the **authenticated** user
    #### JSON example
    ```
    {
    "participants": [1,2]
    }
    ```
* **`GET /api/threads/`** : Get a list of threads for the **authenticated** user
* **`GET /api/threads/<thread_id>/`** : Get a thread with the specified ID.
* **`DElETE /api/threads/<thread_id>/`** : Delete a thread with the specified ID.
* **`POST /api/threads/<thread_id>/messages`** : Create a new message for the specified thread.
    #### JSON example
    ```
    {
    "text": "Lorem ipsum"
    }
    ```
* **`GET /api/threads/<thread_id>/messages/`** : Get a list of messages for the specified thread.
* **`PATCH /api/threads/<thread_id>/mark_read`** : Mark all unread messages in the specified thread as read.
* **`GET /api/threads/<thread_id>/unread_count`** : Get a number of unread messages in the specified thread.

    ***To access any of the endpoints that require authentification. You can use you access token in the 'Authorization' header***



