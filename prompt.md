# Backend Interview Takehome Assignment

We need a management system for storing and editing simple quotes.

Tasks:

- Code a simple web server with a CRUD REST API for quotes with additional method to fetch all quotes at the same time.
- Add HTTP basic authentication to all REST API methods
- Test your endpoints
  - Scenario:
    - create 3 quotes
    - delete the second quote
    - update the last quote with a new author
    - update the first quote with a new content

Each quote has the following properties:

- `author`
- `quote`

You can use additional properties for a better experience like `id` and `created_at`.

Example quotes:

Quote #1:

    Author: Seneca
    Quote: As long as you live, keep learning how to live.

Quote #2:

    Author: Linus Torvalds
    Quote: Theory and practice sometimes clash. And when that happens, theory loses.
    Every single time.

Quote #3:

    Author: John Carmack
    Quote: I'd rather have a search engine or a compiler on a deserted island than a game.

Additional requirements:

- Handle basic authentication header with:
  - username: admin
  - password: password

Keep it simple - this means:

- no need for the database - you can keep the data in the memory if it makes it easier for you
- no need for cors handling
- you can use any framework or library you want
- you can use any existing code you have/find
- there is no defined way to solve this task. We want to see - how will you come to solution
- end results needs to be presented with some HTTP client calls (browser, postman, unit tests… does not matter what you use)
