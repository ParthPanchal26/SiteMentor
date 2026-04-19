# 🌐 Site Mentor

Convert any webpage into structured learning content using AI.

## 🚀 Overview

**Site Mentor** allows users to:

* Input a **website URL**
* Provide a **custom prompt** (what they want to learn)
* Generate **AI-powered explanations or summaries**
* View the output as a structured **Markdown tutor (`Tutor.md`)** in a Streamlit UI

---

## ⚙️ How It Works

1. User enters:

   * URL
   * Prompt (e.g., “Explain this like I’m a beginner”)

2. System:

   * Fetches webpage content
   * Sends it to AI model
   * Generates structured output

3. Output:

   * Saved to `Tutor.md`
   * Rendered in Streamlit UI

---

## 🛠️ Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/ParthPanchal26/SiteMentor.git
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

```bash
source .venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables

Create a `.env` file in the root directory:

```env
NVIDIA_API_KEY=your_api_key_here
MODEL_NAME=your_model_name
MODEL_PROVIDER=your_provider_name
```

---

## ▶️ Run the Application

```bash
streamlit run main.py
```

---

## 📂 Project Structure

```
.
├── main.py          # Streamlit app
├── Tutor.md         # Generated output (AI response)
├── .env             # Environment variables (ignored)
|-- .env.sample
├── .venv/           # Virtual environment (ignored)
|-- .gitignore
|-- README.md
|-- requirement.txt
```

---

## 🧠 Example Use Cases

* Learn concepts from blogs quickly
* Summarize documentation
* Convert tutorials into structured notes
* Extract key insights from long articles