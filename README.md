# 🕉️ Srimad Bhagavad Gita – Full-Stack Verse API

> **Production-grade REST API serving 700+ verses from Bhagavad-gītā As It Is**  
> Demonstrating API design, Unicode handling, cloud deployment, and clean architecture separation

[![Live Demo](https://img.shields.io/badge/demo-live-success?style=for-the-badge)](https://srimad-bhagavad-gita-as-it-is.netlify.app/)
[![API Status](https://img.shields.io/badge/API-active-blue?style=for-the-badge)](https://srimad-bg-api.onrender.com/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

---

## 📋 Table of Contents
- [Overview](#-overview)
- [Live Deployment](#-live-deployment)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [API Documentation](#-api-documentation)
- [Local Setup](#-local-setup)
- [Engineering Highlights](#-engineering-highlights)
- [Performance & Scaling](#-performance--scaling)
- [Roadmap](#-roadmap)

---

## 🎯 Overview

A **full-stack spiritual reference application** built to showcase:

- ✅ **RESTful API Design** – Clean endpoints with proper HTTP semantics
- ✅ **Unicode Text Handling** – Correct rendering of Devanagari Sanskrit
- ✅ **Cross-Origin Architecture** – CORS-enabled API consumed by decoupled frontend
- ✅ **Cloud Deployment** – Automated CI/CD pipeline via GitHub → Render/Netlify
- ✅ **Production Patterns** – Error handling, CORS, Gunicorn, environment configs

**Real-world use case:** Enables developers, researchers, and spiritual practitioners to programmatically access authentic Bhagavad Gita verses with translations and commentary.

---

## 🌐 Live Deployment

| Service | URL | Purpose |
|---------|-----|---------|
| **Frontend** | [srimad-bhagavad-gita-as-it-is.netlify.app](https://srimad-bhagavad-gita-as-it-is.netlify.app/) | Static UI hosted on Netlify |
| **Backend API** | [srimad-bg-api.onrender.com](https://srimad-bg-api.onrender.com/) | Flask REST API on Render |
| **Random Verse** | [/api/shlok/random](https://srimad-bg-api.onrender.com/api/shlok/random) | Example endpoint |

**⚠️ First Request Note:** Render free tier has cold-start latency (~30-50s). Subsequent requests are instant.

---

## ✨ Key Features

### For Users
- 🎲 **Random Verse Generator** – Get a new teaching on each refresh
- 🔎 **Chapter/Verse Lookup** – Direct access via URL (e.g., `/api/shlok/2/47`)
- 🕉️ **Authentic Sanskrit** – Proper Devanagari rendering with diacritics
- 📖 **Word-by-Word Synonyms** – Learn Sanskrit vocabulary in context
- 📚 **Complete Purports** – Śrīla Prabhupāda's detailed commentary
- 📱 **Responsive Design** – Mobile-first UI

### For Developers
- 🔌 **Public REST API** – No authentication required
- 📄 **JSON Responses** – Clean, structured data format
- 🌍 **CORS Enabled** – Use from any frontend framework
- 📦 **Simple Integration** – Fetch API or Axios compatible
- 🚀 **Zero Database Setup** – JSON file-based storage for simplicity

---

## 🏗 Architecture

```
┌─────────────────┐
│   User Browser  │
└────────┬────────┘
         │ HTTPS Request
         ▼
┌─────────────────────┐
│  Netlify (Frontend) │  ← Static HTML/CSS/JS
│  CDN Edge Delivery  │
└────────┬────────────┘
         │ fetch('/api/shlok/random')
         ▼
┌─────────────────────┐
│  Render (Backend)   │  ← Flask + Gunicorn
│  Flask REST API     │
└────────┬────────────┘
         │ JSON.load()
         ▼
┌─────────────────────┐
│   gita_db.json      │  ← 700+ verses
│   UTF-8 Dataset     │     (in-memory)
└─────────────────────┘
```

**Design Principles:**
- **Stateless API** – No sessions, fully cacheable responses
- **Decoupled Frontend** – UI can be rebuilt in React/Vue without touching backend
- **Single Source of Truth** – JSON file as authoritative dataset
- **Zero External Dependencies** – No database, no auth, minimal complexity

---

## 🛠 Tech Stack

### Backend
| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core runtime |
| **Flask 2.0** | Web framework & routing |
| **Flask-CORS** | Cross-origin resource sharing |
| **Gunicorn** | WSGI production server |
| **JSON** | Data storage (700+ verses) |

### Frontend
| Technology | Purpose |
|------------|---------|
| **HTML5** | Semantic markup |
| **CSS3** | Styling & responsiveness |
| **Vanilla JavaScript** | Fetch API & DOM manipulation |

### Infrastructure
| Service | Role |
|---------|------|
| **Render** | Backend hosting + auto-deploy from Git |
| **Netlify** | Frontend CDN + continuous deployment |
| **GitHub** | Version control & CI/CD trigger |

---

## 🔌 API Documentation

### Base URL
```
https://srimad-bg-api.onrender.com
```

### Endpoints

#### 1. Health Check
```http
GET /
```
**Response:**
```json
{
  "message": "Bhagavad Gita API is running",
  "endpoints": {
    "random": "/api/shlok/random",
    "specific": "/api/shlok/{chapter}/{verse}"
  }
}
```

---

#### 2. Get Random Verse
```http
GET /api/shlok/random
```
**Response:** `200 OK`
```json
{
  "chapter": 2,
  "verse": 47,
  "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
  "synonyms": "karmaṇi — work; eva — only; adhikāraḥ — right; te — your...",
  "english_translation": "You have a right to perform your prescribed duty...",
  "prabhupada_purport": "There are three considerations here..."
}
```

---

#### 3. Get Specific Verse
```http
GET /api/shlok/{chapter}/{verse}
```
**Parameters:**
- `chapter` (int, 1-18) – Chapter number
- `verse` (int) – Verse number within chapter

**Example:**
```bash
curl https://srimad-bg-api.onrender.com/api/shlok/2/47
```

**Response:** Same as random endpoint structure

**Error Response:** `404 Not Found`
```json
{
  "error": "Verse not found"
}
```

---

### Response Schema
```typescript
interface Verse {
  chapter: number;
  verse: number;
  sanskrit: string;          // Devanagari text
  synonyms: string;          // Word-by-word breakdown
  english_translation: string;
  prabhupada_purport: string; // Commentary (can be 1000+ chars)
}
```

---

## 💻 Local Setup

### Prerequisites
- Python 3.9+
- pip
- (Optional) virtualenv

### Backend Setup
```bash
# Clone repository
git clone <your-repo-url>
cd Srimad_BG_as_it_is/Backend

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
python app.py
```
✅ API now running at `http://localhost:5000`

### Frontend Setup
```bash
cd ../Frontend

# Option 1: Direct file
open index.html  # macOS
start index.html # Windows

# Option 2: Live Server (VS Code)
# Install "Live Server" extension
# Right-click index.html → Open with Live Server
```

### Testing Endpoints
```bash
# Health check
curl http://localhost:5000/

# Random verse
curl http://localhost:5000/api/shlok/random

# Specific verse
curl http://localhost:5000/api/shlok/2/47
```

---

## 🎓 Engineering Highlights

### 1. **Unicode Correctness**
- Proper UTF-8 encoding for Devanagari Sanskrit
- JSON files stored with `encoding='utf-8'`
- Flask configured to serve UTF-8 responses
- Frontend meta charset declaration

### 2. **API Design Patterns**
- RESTful resource naming (`/api/shlok/{id}`)
- Proper HTTP methods (GET only for read operations)
- JSON content-type headers
- Meaningful HTTP status codes (200, 404)

### 3. **CORS Handling**
```python
# Backend allows cross-origin requests
CORS(app, resources={r"/api/*": {"origins": "*"}})
```
Enables frontend hosted on different domain to consume API.

### 4. **Error Handling**
- Graceful 404s for invalid chapter/verse
- Safe fallbacks for missing data fields
- JSON error responses instead of HTML errors

### 5. **Deployment Automation**
- **Render:** Auto-deploys on Git push to `main` branch
- **Netlify:** Continuous deployment from repository
- No manual deployment steps required

---

## ⚡ Performance & Scaling

### Current Architecture
| Metric | Value |
|--------|-------|
| **Data Load** | In-memory (all verses loaded on startup) |
| **Latency** | ~50ms (after cold start) |
| **Throughput** | ~100 req/sec (Gunicorn workers) |
| **Storage** | ~2MB JSON file |
| **Complexity** | O(1) lookup by chapter/verse |

### Limitations
- ❌ **Memory Constraint:** Entire dataset must fit in RAM
- ❌ **Horizontal Scaling:** No shared state (each instance loads full JSON)
- ❌ **Updates:** Require code redeployment
- ❌ **Search:** No full-text search capability

### Production Scaling Path
```
Current (MVP)          →    Production Scale
─────────────────────────────────────────────
JSON file             →    PostgreSQL + indexes
In-memory cache       →    Redis distributed cache
Single Gunicorn       →    Kubernetes pods (autoscale)
No search             →    Elasticsearch full-text
Manual JSON edits     →    Admin CMS interface
No analytics          →    DataDog/NewRelic monitoring
```

**When to migrate:**
- 10,000+ requests/day
- Need user accounts/bookmarks
- Multi-language support
- Advanced search features

---

## 🚧 Roadmap

### Phase 1: Core Enhancements ✅
- [x] Basic API + frontend
- [x] Random verse endpoint
- [x] Chapter/verse lookup
- [x] Cloud deployment

### Phase 2: User Features (Next)
- [ ] **Daily Verse** – Deterministic verse-of-the-day (same for all users)
- [ ] **Bookmark System** – Save favorite verses (localStorage)
- [ ] **Share Button** – Generate shareable links
- [ ] **Dark Mode** – Theme toggle
- [ ] **Print Layout** – Printer-friendly CSS

### Phase 3: Advanced Features
- [ ] **Keyword Search** – Find verses by topic (e.g., "karma", "dharma")
- [ ] **Audio Recitation** – Sanskrit pronunciation (Web Speech API)
- [ ] **Multi-language** – Hindi, Spanish, French translations
- [ ] **Verse Comparison** – Side-by-side translations
- [ ] **API Key System** – Rate limiting for public API

### Phase 4: Infrastructure
- [ ] **Database Migration** – PostgreSQL with Prisma ORM
- [ ] **Caching Layer** – Redis for hot verses
- [ ] **CI/CD Tests** – Automated endpoint validation
- [ ] **API Versioning** – `/v1/api/` for backward compatibility
- [ ] **Monitoring** – Sentry error tracking + analytics

---

## 🧪 Testing Strategy

### Current Manual Tests
✅ Random verse returns valid JSON  
✅ Chapter/verse endpoint works for all 18 chapters  
✅ Unicode renders correctly in browser  
✅ CORS allows cross-origin requests  
✅ 404 returns proper error JSON  

### Future Automated Tests
```python
# pytest example
def test_random_verse():
    response = client.get('/api/shlok/random')
    assert response.status_code == 200
    data = response.get_json()
    assert 'sanskrit' in data
    assert 'chapter' in data

def test_invalid_chapter():
    response = client.get('/api/shlok/99/1')
    assert response.status_code == 404
```

---

## 🔒 Design Tradeoffs

### Why JSON Instead of Database?

| Aspect | JSON File | PostgreSQL |
|--------|-----------|------------|
| **Setup** | ✅ Zero config | ❌ Requires hosting |
| **Portability** | ✅ Git-trackable | ❌ Separate service |
| **Speed** | ✅ O(1) in-memory | ⚠️ Network latency |
| **Updates** | ❌ Code redeploy | ✅ SQL insert |
| **Scale** | ❌ Single instance | ✅ Horizontal |
| **Search** | ❌ Manual parsing | ✅ Indexed queries |

**Decision:** JSON is perfect for this read-heavy, static dataset. Database adds complexity without immediate benefit.

---

## 📜 Content Attribution

**Source Text:**  
*Bhagavad-gītā As It Is* by A. C. Bhaktivedanta Swami Prabhupāda  
Published by The Bhaktivedanta Book Trust International

**License:**  
Educational & non-commercial use. Respects original copyright.

---

## 👨‍💻 Author

**Aditya Rana**  
Computer Science (AI) Student

[![GitHub](https://img.shields.io/badge/GitHub-Profile-181717?style=flat&logo=github)](https://github.com/Adeptaadi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/aditya-rana-31940332b/)


---

## 🤝 Contributing

Contributions welcome! Areas needing help:

- [ ] Add unit tests for API endpoints
- [ ] Improve frontend accessibility (ARIA labels)
- [ ] Add verse validation schema
- [ ] Create OpenAPI/Swagger documentation
- [ ] Build example integrations (React/Vue components)

---

## ⭐ Show Your Support

If this project helped you learn API design or spiritual wisdom, give it a star! ⭐

---

**Built with 🙏 to share timeless wisdom through modern technology**
