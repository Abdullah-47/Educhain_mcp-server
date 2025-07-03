# Educhain MCP Server

This project implements an MCP server for Educhain, featuring two custom Tools and one Resource for educational content generation.

---

## Features

- **MCQ Generator Tool:** Generate multiple-choice questions for any topic.
- **Flashcard Generator Tool:** Create flashcards for quick revision.
- **Lesson Plan Resource:** Dynamically generate detailed lesson plans.

---

## Installation

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/educhain-mcp-server.git
cd educhain-mcp-server
```

---

### 2. Install with [uv](https://github.com/astral-sh/uv) (Recommended)

```sh
uv init
uv add "mcp[cli]" educhain
```
---

### 3. Alternatively, Install with pip

```sh
pip install "mcp[cli]" educhain
# On Windows:
.\.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

```
---

### 4. Activate the Virtual Environment

```sh
# On Windows:
.\.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```
## Configuration

- Set your API keys in a `.env` file:
  ```
  OPENAI_API_KEY=your-openai-key
  GEMINI_API_KEY=your-gemini-key
  ```

---


## Using Claude Desktop

You can interact with the MCP server using Claude Desktop for a seamless chat experience.

- **Download Claude Desktop:** [https://claude.ai/desktop](https://claude.ai/desktop)

- **Install server on Claude Desktop:**
  ```sh
  mcp install server.py
  ```
> _Leave space here for a screenshot of Claude Desktop_

---

## Inspecting Resources with MCP Inspector

To explore and test your MCP resources, use the [MCP Inspector]:
- **Run Inspector:**
  ```sh
  mcp dev server.py
  ```

> _Leave space here for a screenshot of MCP Inspector_

---

## Contributing

Feel free to fork and submit pull requests!

---

## License

MIT
