# ClickX
### Automated Clicking. Simplified.

**ClickX** is a Python-based autoclicker designed to automate mouse clicking through a command-line interface (CLI).

It provides two editions, allowing users to choose between a beginner-friendly experience and an advanced configuration experience.

---

## ✨ Features

- **TOKEN Mode:** Automatically performs a specified number of clicks.
- **INFINITE Mode:** Continuously performs mouse clicks.
- **Beginner CLI:** A simplified interface for users who prefer straightforward operation.
- **Advanced CLI:** An edition offering additional configuration options.
- **Failsafe Support:** Uses PyAutoGUI's built-in failsafe mechanism.

---

## 📦 Available Editions

ClickX currently offers two editions:

| Edition | Description |
|---|---|
| Beginner CLI | Designed for a straightforward user experience. |
| Advanced CLI | Designed for users who prefer additional configuration options. |

Choose the edition that best suits your needs.

---

## ⚙️ Requirements

Before running ClickX, make sure you have:

- Python 3.11 or newer.
- pip (Python package installer).
- PyAutoGUI.

---

## 📥 Installation

### 1. Download ClickX

Download the repository using GitHub's **Code → Download ZIP** option.

Alternatively, clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Extract the files

If you downloaded the ZIP file, extract it into your preferred directory.

### 3. Install dependencies

Open a terminal inside the ClickX directory and execute:

```bash
pip install -r requirements.txt
```

This installs the required Python dependencies.

---

## ▶️ Getting Started

Navigate to your ClickX project directory using your terminal.

### Beginner CLI

Run the Beginner edition:

```bash
python AutoClickerBeginner.py
```

### Advanced CLI

Run the Advanced edition:

```bash
python AutoClickerPower.py
```

Follow the instructions provided by the application.

*Note: If your uploaded Python filenames differ, use their actual filenames in these commands.*

---

## 🖱️ Clicking Modes

ClickX provides two clicking modes:

### TOKEN Mode

Allows users to specify how many clicks they want the application to perform.

### INFINITE Mode

Allows users to continuously perform clicks until the operation is stopped.

---

## 🛡️ Safety

ClickX uses PyAutoGUI's failsafe mechanism.

When enabled, moving your mouse to the upper-left corner of the screen triggers the failsafe and interrupts the automation.

Use the application responsibly and avoid leaving automated clicking running unattended.

---

## 🗂️ Project Structure

```text
ClickX/
│
├── README.md
├── LICENSE
├── requirements.txt
├── CHANGELOG.md
│
├── AutoClickerBeginner.py
└── AutoClickerPower.py
```

---

## 📌 Version Information

**Current Release:** v1.4.0

**Release Type:** Initial Public Release

ClickX follows a version-based release system.

For information about changes between versions, refer to [CHANGELOG.md](CHANGELOG.md).

---

## 🔧 Troubleshooting

**PyAutoGUI not found?**

Install the dependency:

```bash
pip install pyautogui
```

**Python command not recognized?**

Make sure Python is installed and added to your system PATH.

**Application not starting?**

Check that you are running the correct Python file and have installed all required dependencies.

---

## 👨‍💻 Developer

Developed by **Rithwik B.**

---

## 📄 License

ClickX is distributed under the MIT License.

See the [LICENSE](LICENSE) file for more information.

---

## ⭐ Support

If you find ClickX useful, consider giving the repository a ⭐ on GitHub!

Thank you for checking out ClickX.

**ClickX — Automated Clicking. Simplified.**

