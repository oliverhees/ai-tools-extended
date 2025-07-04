# 🤖 AI Tools Extended - Community Edition

> **Erweiterte AI-Powered Content Creation Suite basierend auf gyoridavid's AI Agents No-Code Tools**

[![Deploy to Coolify](https://img.shields.io/badge/Deploy%20to-Coolify-blue)](./COOLIFY-DEPLOYMENT.md)
[![Docker](https://img.shields.io/badge/Docker-Ready-green)](./docker-compose.yml)
[![N8N](https://img.shields.io/badge/N8N-Workflows-orange)](./n8n-workflows/)
[![Tutorial](https://img.shields.io/badge/N8N-Tutorial-purple)](./N8N-COMMUNITY-TUTORIAL.md)

## 🚀 Features

### 🎯 Original AI Tools (Port 8000)
- **🗣️ Text-to-Speech** - Kokoro & Chatterbox Engines mit 20+ Stimmen
- **🎤 Speech-to-Text** - Whisper Integration mit Auto-Language Detection
- **📁 Media Storage** - Upload, Download, Status, Delete (bis 500MB)
- **🎬 Video Frame Extraction** - Einzelne Frames aus Videos extrahieren
- **📺 Captioned TTS Videos** - Mit Ken Burns Effekt und 4 Design-Styles
- **🎞️ Video Merging** - Videos kombinieren mit optionaler Hintergrundmusik

### 🎥 YouTube Extensions (Port 8080)
- **📝 YouTube Transcription** - Videos direkt transkribieren (max. 10min)
- **🎵 YouTube → TTS** - Videos in Audio umwandeln mit Custom Voice
- **🎬 YouTube → Captioned Video** - Caption-Videos mit Thumbnail erstellen
- **🖼️ Thumbnail Extraction** - High-Quality Thumbnails speichern

### 🔧 N8N Workflow Suite (Port 5678)
- **🎓 Beginner Tutorial Workflow** - Interaktives Lernen für Einsteiger
- **🏭 Advanced Content Factory** - 1 Video → 15+ Content-Formate
- **📰 Newsletter Generator** - YouTube → Multi-Format Content
- **📱 Shorts Creator** - Lange Videos → Social Media Clips
- **🌍 Multi-Language Processor** - Automatische Mehrsprachigkeit
- **♻️ Content Repurposing** - Twitter, LinkedIn, Instagram, TikTok, Blog

## 🏃‍♂️ Schnellstart

### Option 1: Mit Coolify (Empfohlen)

1. **Repository forken und klonen**
2. **In Coolify Dashboard:**
   - New Resource → Docker Compose
   - Repository URL: `https://github.com/oliverhees/ai-tools-extended`
   - Compose File: `docker-compose.coolify.yml`
   - Deploy! 🚀

[📖 Vollständige Coolify Anleitung](./COOLIFY-DEPLOYMENT.md)

### Option 2: Lokales Docker Setup

```bash
git clone https://github.com/oliverhees/ai-tools-extended
cd ai-tools-extended
cp .env.example .env
# .env anpassen
docker-compose up -d
```

## 🌐 Services nach Deployment

| Service | URL | Beschreibung | Auth |
|---------|-----|--------------|------|
| 🤖 AI Tools API | `https://ai-tools.domain.com` | Haupt-API für alle Features | None |
| 🎥 YouTube API | `https://youtube-api.domain.com` | YouTube-spezifische Endpoints | None |
| 🔧 N8N Workflows | `https://workflows.domain.com` | **Kein Login nötig!** | Open |
| 📊 API Docs | `https://ai-tools.domain.com/docs` | Swagger Dokumentation | None |

## 📚 N8N Tutorial & Workflows

### 🎓 **Für Einsteiger**
**[📖 Komplettes N8N Community Tutorial](./N8N-COMMUNITY-TUTORIAL.md)**
- Step-by-Step Anleitung für alle Endpoints
- Praktische Code-Beispiele
- Troubleshooting & Best Practices
- Community Use Cases

### 🚀 **Ready-to-Use Workflows**

#### Beginner-Friendly:
- 🎓 **[Beginner Tutorial](./n8n-workflows/beginner-youtube-tutorial.json)** - YouTube → Blog Post (mit Erklärungen)
- 📰 **[Newsletter Generator](./n8n-workflows/youtube-newsletter.json)** - Video → Newsletter Content

#### Advanced Workflows:
- 🏭 **[Content Factory](./n8n-workflows/advanced-content-factory.json)** - 1 Video → 15+ Formate
- 📱 **[Shorts Creator](./n8n-workflows/shorts-creator.json)** - Social Media Clips
- 🌍 **[Multi-Language](./n8n-workflows/multi-language-processor.json)** - Automatische Übersetzung
- ♻️ **[Content Repurposing](./n8n-workflows/content-repurposing.json)** - Multi-Platform Content

### 🔧 Workflow Import (Super einfach!)

1. **N8N Dashboard öffnen** → `https://workflows.domain.com`
2. **Kein Login nötig** - direkt loslegen! 🎉
3. **Import** → Upload JSON aus `/n8n-workflows/`
4. **Execute** und sofort nutzen!

## 📚 API Quick Reference

### YouTube Transcription
```bash
POST https://youtube-api.domain.com/youtube/transcribe
{
  "url": "https://youtube.com/watch?v=VIDEO_ID",
  "language": "de"  # oder "auto" für Auto-Detection
}
```

### Text-to-Speech (20+ Stimmen)
```bash
POST https://ai-tools.domain.com/text-to-speech
{
  "text": "Hallo Welt!",
  "voice": "de-DE-KatjaNeural",  # Deutsch
  "speed": 1.0
}
```

### Captioned Video erstellen
```bash
POST https://ai-tools.domain.com/generate-captioned-video
{
  "image_id": "uploaded-image-id",
  "text": "Dein Text hier",
  "style": "gradient",  # minimal, bold, gradient, neon
  "add_music": true,
  "ken_burns": true
}
```

### YouTube Content Factory
```bash
POST https://youtube-api.domain.com/youtube/to-captioned-video
{
  "youtube_url": "https://youtube.com/watch?v=VIDEO_ID",
  "style": "gradient",
  "music": true
}
```

## 🎯 Community Use Cases

### 🎓 Bildung & E-Learning
- **Vorlesungen automatisch transkribieren** → Barrierefreie Notizen
- **Videos in 5+ Sprachen** → Internationale Reichweite
- **Lernmaterialien generieren** → Quiz, Zusammenfassungen, Podcasts
- **Tutorial-Workflows**: [Education Examples](./N8N-COMMUNITY-TUTORIAL.md#🎓-bildungseinrichtungen)

### 📱 Content Creator & Marketing
- **1 YouTube Video → 20+ Posts** für alle Plattformen
- **Automatische Social Media Pipeline** → Twitter, LinkedIn, Instagram, TikTok
- **SEO-optimierte Blog Posts** → Organischer Traffic
- **Multi-Format Content**: [Creator Workflows](./N8N-COMMUNITY-TUTORIAL.md#📱-content-creator)

### 🏢 Business & Enterprise
- **Meeting Dokumentation** → Automatische Protokolle
- **Webinar Repurposing** → Marketing Content
- **Customer Support** → Call Transcription & Analysis
- **Compliance Training** → Mehrsprachige Schulungsvideos

### 🎨 Creative & Entertainment
- **Podcast Production** → Auto-Transcription & Chapters
- **Video Editing Workflows** → Frame Extraction & Merging
- **Voice-Over Production** → 20+ Professional Voices
- **Content Localization** → Global Audience Reach

## ⚙️ Performance & Skalierung

### **Kleine Community (1-10 Nutzer):**
```env
WHISPER_MODEL=tiny      # Schnell, 1GB RAM
MAX_FILE_SIZE=100MB     # Basis Limits
MEMORY_LIMIT=2g         # Minimaler Server
```
💰 **Kosten**: €4-8/Monat (Hetzner/DigitalOcean)

### **Mittlere Community (10-50 Nutzer):**
```env
WHISPER_MODEL=base      # Ausgewogen, 2GB RAM
MAX_FILE_SIZE=500MB     # Standard Limits  
MEMORY_LIMIT=4g         # Empfohlener Server
```
💰 **Kosten**: €8-16/Monat

### **Große Community (50+ Nutzer):**
```env
WHISPER_MODEL=medium    # Beste Qualität, 4GB RAM
MAX_FILE_SIZE=1GB       # Erweiterte Limits
MEMORY_LIMIT=8g         # High-Performance Server
```
💰 **Kosten**: €16-32/Monat

## 📊 Monitoring & Health

### Automated Health Checks
```bash
curl https://ai-tools.domain.com/health       # AI Tools Status
curl https://youtube-api.domain.com/          # YouTube Extensions
curl https://workflows.domain.com/healthz     # N8N Status
```

### Performance Monitoring
- **CPU Usage** → Coolify Dashboard
- **Memory Usage** → Auto-alerts bei >80%
- **API Rate Limits** → 5 req/min YouTube, 20 req/min TTS
- **Storage Management** → Auto-cleanup temporärer Dateien

## 🛡️ Sicherheit & Best Practices

### Aktuelle Sicherheitsfeatures
- ✅ **N8N ohne Authentication** → Einfacher Community-Zugang
- ✅ **Rate Limiting** → Schutz vor Überlastung
- ✅ **File Size Limits** → Server-Schutz
- ✅ **HTTPS via Coolify** → Automatische SSL-Zertifikate
- ✅ **Docker Isolation** → Sichere Container-Umgebung

### Empfohlene Sicherheitsmaßnahmen
```bash
# Für Production-Umgebungen
ENABLE_API_KEYS=true        # (geplantes Feature)
MAX_CONCURRENT_JOBS=3       # Server-Schutz
BACKUP_ENABLED=true         # Automatische Backups
```

## 🚀 Deployment Optionen

### ⭐ Empfohlene Cloud Provider

| Provider | Kosten/Monat | RAM | CPU | Features | Rating |
|----------|--------------|-----|-----|----------|--------|
| **Hetzner** | €4-16 | 4-16GB | 2-4 | Beste Preis/Leistung, EU-Server | ⭐⭐⭐⭐⭐ |
| **DigitalOcean** | $20-40 | 4-8GB | 2-4 | Einfaches Setup, gute Docs | ⭐⭐⭐⭐ |
| **Linode** | $20-40 | 4-8GB | 2-4 | Zuverlässig, gute Performance | ⭐⭐⭐⭐ |

### 🔄 Managed Platform Services
- **Railway** → $5-20/Monat → Einfaches Git-Deploy
- **Render** → $7-25/Monat → Auto-Scaling
- **Fly.io** → $10-30/Monat → Edge Computing

### 📈 Enterprise Solutions
- **AWS ECS/Fargate** → Vollständig managed, Auto-Scaling
- **Google Cloud Run** → Pay-per-Use, Serverless
- **Azure Container Instances** → Enterprise Integration

## 🤝 Community & Support

### 🔗 Wichtige Links
- 📚 **[N8N Tutorial](./N8N-COMMUNITY-TUTORIAL.md)** → Komplette Anleitung
- 🚀 **[Coolify Deployment](./COOLIFY-DEPLOYMENT.md)** → Step-by-Step Setup
- 🌟 **[Community Guide](./community-guide.md)** → Use Cases & Beispiele
- 🐛 **[GitHub Issues](https://github.com/oliverhees/ai-tools-extended/issues)** → Bug Reports
- 💡 **[Discussions](https://github.com/oliverhees/ai-tools-extended/discussions)** → Feature Requests

### 🎯 Community Beitrag

#### Workflow Sharing
Teile deine N8N Workflows mit der Community:
```
community-workflows/
├── education/          # Bildung & E-Learning
├── marketing/          # Content Marketing  
├── social-media/       # Social Media Automation
├── business/           # Business Prozesse
└── creative/           # Kreative Projekte
```

#### Code Beitrag
1. **Fork** das Repository
2. **Feature Branch** erstellen: `git checkout -b feature/amazing-feature`
3. **Changes implementieren** mit Tests
4. **Pull Request** mit detaillierter Beschreibung

### 🎓 Community Learning

#### Skill Level Workflows
- 🟢 **Beginner**: Basic YouTube → Text Workflows
- 🟡 **Intermediate**: Multi-Platform Content Generation  
- 🔴 **Advanced**: Custom Business Process Automation

#### Workshop Ideas
- **"N8N Basics"** → Erste Schritte Tutorial
- **"Content Factory Setup"** → 1 Video → 20 Posts
- **"Business Automation"** → Meeting → Protokoll → Tasks
- **"AI Voice Production"** → Professional TTS Workflows

## 📈 Roadmap & Updates

### 🔜 Nächste Features (Q1 2025)
- [ ] **GPT Integration** → Automatische Summaries & Content-Verbesserung
- [ ] **API Key Management** → User-spezifische Rate Limits
- [ ] **Advanced Analytics** → Usage Dashboard & Insights
- [ ] **Batch Processing** → Multiple Videos gleichzeitig
- [ ] **Social Media Scheduler** → Direktes Posting zu Plattformen

### 🎯 Community Requests
- [ ] **Custom Voice Training** → Eigene Stimmen trainieren
- [ ] **Live Stream Integration** → Real-time Transcription
- [ ] **Chapter Detection** → Automatische Video-Segmentierung
- [ ] **White-Label Branding** → Custom UI für Communities
- [ ] **Webhook Integrations** → Zapier, Make.com Support

### 🔄 Maintenance & Updates
- **Monthly Updates** → Bug Fixes & Performance Improvements
- **Quarterly Features** → Neue Endpoints & Workflows
- **Community Feedback** → Feature Prioritization via GitHub Discussions

## 📊 Community Stats & Success Stories

### 🎯 Aktuelle Metriken
- **20+ AI Endpoints** verfügbar
- **6 Professional Workflows** ready-to-use
- **4 Deployment Options** (Coolify, Docker, Cloud)
- **50+ Code Beispiele** in Tutorial
- **15+ Use Cases** dokumentiert

### 🌟 Success Stories
*Coming Soon - Teile deine Erfolgsgeschichte mit der Community!*

## 📄 Lizenz & Credits

### 📜 Open Source Lizenz
**MIT License** - Frei nutzbar für kommerzielle und private Projekte

### 🙏 Credits & Danksagungen
- **Base Framework**: [gyoridavid/ai-agents-no-code-tools](https://github.com/gyoridavid/ai_agents_az)
- **AI Engine**: OpenAI Whisper & TTS
- **Video Processing**: yt-dlp Team & FFmpeg
- **Workflow Platform**: N8N Community
- **Deployment**: Coolify Team
- **Container Orchestration**: Docker

---

<div align="center">

## 🚀 Ready to Transform Your Content Creation?

**Starte jetzt und baue die innovativste AI-Community auf!**

[![Deploy Now](https://img.shields.io/badge/🚀_Deploy_Now-Coolify-blue?style=for-the-badge)](./COOLIFY-DEPLOYMENT.md)
[![Learn N8N](https://img.shields.io/badge/📚_Learn_N8N-Tutorial-purple?style=for-the-badge)](./N8N-COMMUNITY-TUTORIAL.md)
[![Join Community](https://img.shields.io/badge/🤝_Join_Community-GitHub-green?style=for-the-badge)](https://github.com/oliverhees/ai-tools-extended/discussions)

**[Deploy to Coolify](./COOLIFY-DEPLOYMENT.md) • [N8N Tutorial](./N8N-COMMUNITY-TUTORIAL.md) • [Community Guide](./community-guide.md)**

</div>