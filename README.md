# SFERA AI Carousel Generator

AI-powered carousel generator in Glassmorphism style for Instagram, LinkedIn, and presentations.

## Quick Setup (Railway)

### Prerequisites
- GitHub account
- OpenAI API key (sk-...)
- Railway account

### Deployment

1. **Fork/Clone this repository to your GitHub**
2. **Go to Railway**: https://railway.app
3. **Create new project** → Deploy from GitHub
4. **Select** `andxsexai/sfera-ai-carousel`
5. **Add environment variables** in Railway:
   - `OPENAI_API_KEY` = your_openai_key
   - `ENV` = production
6. **Set Start Command**:
   ```
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
7. **Deploy** and wait for domain

## Local Development

```bash
pip install -r requirements.txt
playwright install chromium

uvicorn app.main:app --reload
```

Visit: `http://localhost:8000`

## Features
- 🎨 AI-generated carousel content
- 🎭 Glassmorphism design (Purple/Cyberpunk)
- 📱 Instagram, LinkedIn formats
- 🚀 One-click deployment to Railway

## Tech Stack
- FastAPI (backend)
- OpenAI API (content generation)
- Playwright (HTML to image rendering)
- Jinja2 (templating)

## License
MIT
