# 🖱️ Selenium ActionChains UI Interaction Framework

This project is a fully functional test automation framework built with **Selenium**, **PyTest**, and the **Page Object Model (POM)** structure. It demonstrates advanced user interactions using Selenium's `ActionChains`, such as hover, drag & drop, and right-click context menus.

---

## 📁 Project Structure

test_project_actionchains/
├── pages/
│ └── interaction_page.py # Page Object methods for all interactions
├── tests/
│ ├── test_interactions.py # Test cases calling page methods
│ └── conftest.py # PyTest fixture for browser setup
├── requirements.txt # Dependencies
├── .gitignore # Git ignore rules
└── README.md


---

## ✅ Features

- Page Object Model (POM) Architecture  
- Hover interaction (move to image)  
- Drag and Drop (box A → box B)  
- Right-click context menu + alert handling  
- PyTest fixtures and clean test separation  
- Modular and lightweight structure

---

## 🧪 Test Scenarios

| Test Name              | Description                                      |
|------------------------|--------------------------------------------------|
| `test_hover_action`    | Hovers over an image and verifies caption text   |
| `test_drag_and_drop`   | Drags Box A and drops onto Box B                |
| `test_right_click_alert` | Right-clicks on a box and confirms alert text  |

---

## ▶️ How to Run

### Step 1 – Install Requirements:
```bash
pip install -r requirements.txt
