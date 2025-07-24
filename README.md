# 🐔 Chicken Records CLI Application

## 📌 Project Overview

This is a **work-in-progress Proof of Concept (PoC)** application being developed for a local Chicken Breeder. The goal is to help them transition from a paper-based system to a local, digital database to manage their chicken records more efficiently.

Over the next **4 weeks**, this application will evolve from a simple CLI-based menu system into a more functional record-keeping solution. The initial version will store chicken data in a basic in-memory list, with future enhancements including optional CSV/text file storage.

---

## 🎯 Project Objective

To build a **command-line interface (CLI)** that allows the user to:

```

Menu:
0 - Exit App
1 - Print List of Chicken Records
2 - Create New Chicken Record
3 - Update Existing Chicken Record
4 - Delete a Chicken Record

````

---

## ✅ Current Functionality (Week 1–2)

- [x] Print to screen  
- [x] Clear the screen  
- [x] Accept user input  
- [x] Store chicken names in a Python list  

> **Example Chicken Names** used for demonstration:  
> George, Fleur, Devon, Casey, Marigold, Apple Mint

---

## 🚧 Planned Enhancements

- [x] Save and retrieve chicken records using CSV or text files
- [x] Migrate to saving and retrieving from a MySQL Database 
- [x] Add validation and error handling  
- [x] Improve user experience and interface flow  
- [x] Possibly refactor to use classes or a more modular design

---

## 🧰 Tools & Technologies

| Tool       | Purpose                            |
|------------|----------------------------------|
| **Python** | Main programming language         |
| **VS Code**| Integrated Development Environment|
| **Git**    | Version control                   |
| **GitHub** | Remote code repository & documentation |

---

## 📁 Project Setup Instructions

1. Install **Python** (latest version recommended)  
2. Install **VS Code**  
3. Clone or download this repository
4. Navigate to correct directory   
4. Run the main program using:  
```bash
   python app.py
````

---

## 🗂 Project Structure (Subject to Change)

```
chicken-records-cli/
│
├── week_1/
│   ├── src/
│   │   ├── app.py
│   │   └── test_app.py
│   └── notes/
│       └── notes.txt
│
├── week_2/
│   ├── src/
│   │   ├── app.py
│   │   └── test_app.py
│   ├── notes/
│   │   └── notes.txt
│   └── data/
│       └── chickens.csv
│
└── README.md
```

---

## 🧪 Development Phases & Timeline

### Phase 1 – Setup (Week 1)

* ✅ Install tools and initialize repo
* ✅ Create base CLI structure

### Phase 2 – Build & Test (Weeks 2–3)

* 🔧 Build core functionality
* 🧪 Test and refine interactions

### Phase 3 – Deliverables (Week 4)

* 🎥 5-minute live demo
* 🖥 Client-facing presentation
* 🧑‍🏫 Whiteboard session explaining design & alternatives

---

## 🗒️ Developer Notes

This project is being tracked and documented via **commits** and this `README.md`. Updates will include:

Here’s your **README-friendly version** of the content you provided, written in clean Markdown for GitHub and other documentation purposes:

---

## 📘 Progress Reflections

Over the course of this project, I implemented a simple object-oriented chicken management system with persistent storage using a MySQL database. The transition from list-based in-memory data handling to a relational database presented several challenges, especially around ID management and data consistency.

### 🔑 Key Learning Milestones

* Understanding the balance between OOP and relational database design (e.g., removing the `id` attribute from class instances when using `AUTO_INCREMENT` in SQL).
* Managing database connections, integrity errors, and writing safe SQL queries.
* Using `CREATE TABLE IF NOT EXISTS` to prevent redundant or error-prone table creation.
* Troubleshooting common MySQL connector issues, including authentication plugin errors and environment misconfigurations.

### 💡 This project reinforced my understanding of:

* SQL fundamentals (DDL & DML)
* Python database connectivity using `mysql.connector`
* How to achieve data persistence beyond a single runtime session

---

## ⚙️ Implementation Decisions

* **Database Over Lists**: Transitioned from storing chickens in Python lists to using a persistent MySQL database for better scalability and persistence.
* **Auto-Increment IDs**: Relied on MySQL's `AUTO_INCREMENT` to handle unique identifiers automatically, eliminating the need to manually manage `id`s in Python.
* **Simplified Chicken Class**: Removed the `id` field from the `Chicken` class since the database now handles it.
* **Environment Variables**: Utilized a `.env` file with Docker Compose to securely store and access sensitive data such as database credentials.
* **Error Handling**: Added input confirmations and exception handling to manage bad input and improve user experience.
* **Modular Functions**: Broke logic into reusable functions for maintainability (e.g., `string_input_validation()`, `confirmation()`).

---

## 🧑‍💻 User Instructions

### 1️⃣ Setup

**Prerequisites**:

* Python 3.x
* Docker

**Steps**:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/chicken-manager.git
   cd chicken-manager
   ```

2. Ensure a `.env` file exists in the project root with the following:

   ```env
   MYSQL_ROOT_PASSWORD=yourpassword
   MYSQL_DATABASE=yourdb
   MYSQL_USER=youruser
   MYSQL_PASSWORD=yourpassword
   ```

3. Launch the MySQL Docker container:

   ```bash
   docker-compose up --build
   ```

---

You should add the **installation of dependencies** (using `pip install -r requirements.txt`) just **after setting up the virtual environment and before running the application**. This ensures all required Python packages are available before the app is launched.

Here’s the **updated section** to insert under the `🧑‍💻 User Instructions` > `2️⃣ Running the Application` heading:

---

### 2️⃣ Running the Application

**Optional (recommended): Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On macOS/Linux
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

> This installs all required Python packages listed in `requirements.txt`.

**Run the app**

```bash
python main.py
```

---

This keeps your README clear, complete, and installation-friendly. Let me know if you'd like a fresh copy of the full README with that section already integrated.


---

### 3️⃣ Available Actions

* 🐔 View all chickens
* ➕ Add a new chicken
* 📝 Update existing chicken details
* ❌ Delete a chicken
* 🚪 Exit the program

---

### 4️⃣ Notes

* IDs are **auto-generated** by the MySQL database.
* All records are stored persistently and will remain after the script ends.
* Ensure the **MySQL container is running** before starting the script.

---

Feel free to fork or clone the repo to try the application yourself.

---

## 📅 Deadline

**4 Weeks from Project Initiation**
📌 *Expected Completion: \[30/07/2025 + 4 Weeks]*
    *Actual Completion: \[23/07/2025]*
