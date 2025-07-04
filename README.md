# 🤖 AI Tools Extended - Community Edition

> **Erweiterte AI-Powered Content Creation Suite basierend auf gyoridavid's AI Agents No-Code Tools**

[![Deploy to Coolify](https://img.shields.io/badge/Deploy%20to-Coolify-blue)](./COOLIFY-DEPLOYMENT.md)
[![Docker](https://img.shields.io/badge/Docker-Ready-green)](./docker-compose.yml)
[![N8N](https://img.shields.io/badge/N8N-Workflows-orange)](./n8n-workflows/)

## 🚀 Features

### 🎯 Original AI Tools (Port 8000)
- **🗣️ Text-to-Speech** - Kokoro & Chatterbox Engines
- **🎤 Speech-to-Text** - Whisper Integration
- **📁 Media Storage** - Upload, Download, Status, Delete
- **🎬 Video Frame Extraction** - Einzelne Frames extrahieren
- **📺 Captioned TTS Videos** - Mit Ken Burns Effekt
- **🎞️ Video Merging** - Kombinieren mit Hintergrundmusik

### 🎥 YouTube Extensions (Port 8080)
- **📝 YouTube Transcription** - Videos direkt transkribieren
- **🎵 YouTube → TTS** - Videos in Audio umwandeln
- **🎬 YouTube → Captioned Video** - Caption-Videos erstellen
- **🖼️ Thumbnail Extraction** - Thumbnails speichern

### 🔧 N8N Workflow Suite (Port 5678)
- **📰 Newsletter Generator** - YouTube → Multi-Format Content
- **📱 Shorts Creator** - Lange Videos → Social Clips
- **🌍 Multi-Language Processor** - Automatische Übersetzung
- **♻️ Content Repurposing** - 1 Video → 20+ Formate

## 🏃‍♂️ Schnellstart

### Option 1: Mit Coolify (Empfohlen)

1. **Repository forken und klonen**
2. **In Coolify Dashboard:**
   - New Resource → Docker Compose
   - Repository URL eingeben
   - `docker-compose.coolify.yml` auswählen
   - Environment Variables setzen
   - Deploy! 🚀

[📖 Vollständige Coolify Anleitung](./COOLIFY-DEPLOYMENT.md)

### Option 2: Lokales Docker Setup

```bash
git clone <your-repo-url>
cd ai-tools-extended
cp .env.example .env
# .env anpassen
docker-compose up -d
```

## 🌐 Services nach Deployment

| Service | URL | Beschreibung |
|---------|-----|--------------|
| 🤖 AI Tools API | `https://ai-tools.domain.com` | Haupt-API für alle Features |
| 🎥 YouTube API | `https://youtube-api.domain.com` | YouTube-spezifische Endpoints |
| 🔧 N8N Workflows | `https://workflows.domain.com` | Workflow Dashboard |
| 📊 API Docs | `https://ai-tools.domain.com/docs` | Swagger Dokumentation |

## 📚 API Quick Reference

### YouTube Transcription
```bash
POST https://youtube-api.domain.com/youtube/transcribe
{
  "url": "https://youtube.com/watch?v=VIDEO_ID",
  "language": "de"
}
```

### Text-to-Speech
```bash
POST https://ai-tools.domain.com/text-to-speech
{
  "text": "Hallo Welt!",
  "voice": "de-DE-KatjaNeural"
}
```

### Captioned Video erstellen
```bash
POST https://ai-tools.domain.com/generate-captioned-video
{
  "image_id": "uploaded-image-id",
  "text": "Dein Text hier",
  "style": "gradient"
}
```

## 🎯 Community Use Cases

### 🎓 Bildung
- **Vorlesungen transkribieren** → Automatische Notizen
- **Videos untertiteln** → Barrierefreiheit
- **Multi-Language Content** → Internationale Reichweite

### 📱 Content Creation
- **YouTube → Blog Posts** → SEO Content
- **Long-Form → Shorts** → Social Media
- **Videos → Podcasts** → Audio Content

### 🏢 Business
- **Webinare repurposen** → Marketing Material
- **Schulungsvideos** → Dokumentation
- **Meetings transkribieren** → Protokolle

## 🔧 N8N Workflow Import

1. **N8N Dashboard öffnen** (`https://workflows.domain.com`)
2. **Login** (admin / dein-passwort)
3. **Import** → Upload JSON aus `/n8n-workflows/`
4. **Workflows aktivieren** und konfigurieren

### Verfügbare Workflows:
- 📰 `youtube-newsletter.json` - Newsletter Generator
- 📱 `shorts-creator.json` - Social Media Clips
- 🌍 `multi-language-processor.json` - Übersetzungen
- ♻️ `content-repurposing.json` - Content Multiplikator

## ⚙️ Konfiguration

### Performance Settings

**Kleine Community (1-10 Nutzer):**
```env
WHISPER_MODEL=tiny
MAX_FILE_SIZE=100MB
MEMORY_LIMIT=2g
```

**Mittlere Community (10-50 Nutzer):**
```env
WHISPER_MODEL=base
MAX_FILE_SIZE=500MB
MEMORY_LIMIT=4g
```

**Große Community (50+ Nutzer):**
```env
WHISPER_MODEL=medium
MAX_FILE_SIZE=1GB
MEMORY_LIMIT=8g
```

## 📊 Monitoring & Health

### Health Checks
```bash
curl https://ai-tools.domain.com/health
curl https://youtube-api.domain.com/
curl https://workflows.domain.com/healthz
```

### Resource Monitoring
- **CPU Usage** - Coolify Dashboard
- **Memory Usage** - Automatic alerts bei >80%
- **Disk Space** - Automatic cleanup
- **API Requests** - Rate limiting logs

## 🛡️ Sicherheit

### Authentifizierung
- **N8N**: Basic Auth (admin/password)
- **API Rate Limiting**: 5 req/min für YouTube API
- **File Upload Limits**: Konfigurierbar

### Best Practices
```env
# Starke Passwörter verwenden
N8N_PASSWORD=super_secure_password_123

# HTTPS aktivieren (automatisch mit Coolify)
N8N_PROTOCOL=https

# Backup aktivieren
BACKUP_ENABLED=true
```

## 🚀 Deployment Optionen

### Cloud Providers
| Provider | Kosten/Monat | RAM | CPU | Empfehlung |
|----------|--------------|-----|-----|------------|
| Hetzner | €4-16 | 4-16GB | 2-4 | ⭐ Beste Preis/Leistung |
| DigitalOcean | $20-40 | 4-8GB | 2-4 | ⭐ Einfaches Setup |
| Linode | $20-40 | 4-8GB | 2-4 | ⭐ Gute Performance |

### Managed Services
- **Railway** - $5-20/Monat
- **Render** - $7-25/Monat  
- **Fly.io** - $10-30/Monat

## 🤝 Community

### Beitragen
1. **Fork** das Repository
2. **Feature Branch** erstellen
3. **Changes** implementieren
4. **Pull Request** erstellen

### Support
- 🐛 **Bug Reports**: GitHub Issues
- 💡 **Feature Requests**: GitHub Discussions
- 📖 **Dokumentation**: Wiki
- 💬 **Community Chat**: Discord/Slack

### Workflow Sharing
Teile deine N8N Workflows in `/community-workflows/`:
```
community-workflows/
├── education/
├── marketing/
├── social-media/
└── business/
```

## 📈 Roadmap

### 🔜 Geplante Features
- [ ] **GPT Integration** für Summaries
- [ ] **Automatische Chapter Detection**
- [ ] **Sentiment Analysis**
- [ ] **SEO Optimization Tools**
- [ ] **Social Media Scheduler**
- [ ] **Advanced Analytics Dashboard**

### 🎯 Community Requests
- [ ] **Batch Processing** für multiple Videos
- [ ] **Custom Voice Training**
- [ ] **Live Stream Integration**
- [ ] **White-Label Branding**

## 📄 Lizenz

MIT License - Frei nutzbar für die Community

## 🙏 Credits

- **Base**: [gyoridavid/ai-agents-no-code-tools](https://github.com/gyoridavid/ai_agents_az)
- **Whisper**: OpenAI
- **yt-dlp**: yt-dlp Team
- **N8N**: N8N Community
- **Coolify**: Coolify Team

---

<div align="center">

**🚀 Starte noch heute und baue die kreativste AI-Community auf!**

[Deploy to Coolify](./COOLIFY-DEPLOYMENT.md) • [API Docs](./api-docs.md) • [Community Guide](./community-guide.md)

</div>