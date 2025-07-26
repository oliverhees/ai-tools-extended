# 🚀 Coolify Deployment Guide

## Schritt 1: Repository vorbereiten

1. **Repository auf GitHub/GitLab pushen:**
```bash
git init
git add .
git commit -m "Initial commit: AI Tools Extended"
git remote add origin <your-repo-url>
git push -u origin main
```

## Schritt 2: Coolify Service erstellen

### Option A: Docker Compose Service

1. **In Coolify Dashboard:**
   - "New Resource" → "Docker Compose"
   - Repository URL eingeben
   - Branch: `main`
   - Docker Compose File: `docker-compose.coolify.yml`

2. **Environment Variables setzen:**
```env
WHISPER_MODEL=base
TTS_ENGINE=kokoro
MAX_FILE_SIZE=500MB
MAX_VIDEO_DURATION=600
N8N_USER=admin
N8N_PASSWORD=DEIN_SICHERES_PASSWORT
```

### Option B: Einzelne Services

1. **AI Tools Service:**
   - "New Resource" → "Docker Image"
   - Build from Git Repository
   - Dockerfile: `Dockerfile`
   - Port: 8000 (alle Services)

2. **N8N Service:**
   - "New Resource" → "Docker Image" 
   - Image: `n8nio/n8n:latest`
   - Port: 5678

## Schritt 3: Domain konfigurieren (Vereinfacht!)

### Unified AI Tools Platform
- **Domain**: `ai-tools.deine-domain.com`
- **Port**: 8000 (Haupt-Port für alle Services)
- **SSL**: Automatisch via Coolify
- **Routing**: 
  - `/api/*` - Original AI Tools
  - `/youtube/*` - YouTube Extensions  
  - `/workflows/*` - N8N Dashboard
  - `/docs` - API Dokumentation

## Schritt 4: Persistent Storage

### Volume Mounts in Coolify:
```
/app/media -> ai_tools_media (100GB)
/app/cache -> ai_tools_cache (50GB)  
/tmp -> ai_tools_temp (20GB)
/home/node/.n8n -> n8n_data (10GB)
```

## Schritt 5: Health Checks

Coolify überwacht automatisch:
- **AI Tools**: `GET /health` (Port 8000)
- **YouTube API**: `GET /` (Port 8080)
- **N8N**: `GET /healthz` (Port 5678)

## Schritt 6: Reverse Proxy Konfiguration

### Traefik Labels (automatisch von Coolify):
```yaml
labels:
  - "traefik.enable=true"
  - "traefik.http.routers.ai-tools.rule=Host(`ai-tools.deine-domain.com`)"
  - "traefik.http.routers.ai-tools.tls.certresolver=letsencrypt"
```

## Schritt 7: Monitoring Setup

### Resource Limits setzen:
```yaml
deploy:
  resources:
    limits:
      memory: 4G
      cpus: "2"
    reservations:
      memory: 2G
      cpus: "1"
```

### Logs überwachen:
- Coolify Dashboard → Logs Tab
- Real-time Log Streaming verfügbar

## Schritt 8: Community URLs teilen

Nach dem Deployment sind deine Services verfügbar unter:

### 🔗 API Endpoints:
- **Haupt-API**: `https://ai-tools.deine-domain.com/api/`
- **YouTube API**: `https://ai-tools.deine-domain.com/youtube/`
- **N8N Workflows**: `https://ai-tools.deine-domain.com/workflows/`

### 📖 API Dokumentation:
- **Swagger UI**: `https://ai-tools.deine-domain.com/docs`
- **ReDoc**: `https://ai-tools.deine-domain.com/redoc`

## Schritt 9: Sicherheit

### 1. N8N Authentication
```env
N8N_USER=admin
N8N_PASSWORD=super_sicheres_passwort_123
```

### 2. API Rate Limiting (bereits implementiert)
- 5 Requests/Minute für YouTube API
- Automatisches IP-basiertes Limiting

### 3. File Upload Limits
```env
MAX_FILE_SIZE=500MB  # Anpassen je nach Server
```

## Schritt 10: Backup Strategy

### Automatische Backups in Coolify:
1. **Database Backups**: N8N SQLite Datenbank
2. **Volume Backups**: Media Files, Cache
3. **Frequency**: Täglich um 2:00 Uhr

## Performance Tuning

### Für kleine Communities (1-10 Nutzer):
```env
WHISPER_MODEL=tiny
MAX_FILE_SIZE=100MB
MEMORY_LIMIT=2g
```

### Für mittlere Communities (10-50 Nutzer):
```env
WHISPER_MODEL=base
MAX_FILE_SIZE=500MB
MEMORY_LIMIT=4g
```

### Für große Communities (50+ Nutzer):
```env
WHISPER_MODEL=medium
MAX_FILE_SIZE=1GB
MEMORY_LIMIT=8g
```

## Troubleshooting

### Problem: Service startet nicht
**Lösung**: Logs in Coolify Dashboard prüfen
```bash
# Häufige Probleme:
- Nicht genügend RAM (mindestens 4GB empfohlen)
- Port bereits belegt
- Environment Variables falsch gesetzt
```

### Problem: Langsame Transcription
**Lösung**: Kleineres Whisper Model verwenden
```env
WHISPER_MODEL=tiny  # Schneller, weniger genau
```

### Problem: Disk Space voll
**Lösung**: Cleanup Job aktivieren
```bash
# In Coolify Cron Jobs:
0 2 * * * docker exec ai-tools-extended find /tmp -type f -mtime +1 -delete
```

## Updates durchführen

### Automatische Updates:
1. **Git Webhook** in Coolify aktivieren
2. **Auto-Deploy** bei Git Push aktivieren
3. **Health Checks** überwachen Deployment

### Manuelle Updates:
1. Coolify Dashboard → Deployments
2. "Redeploy" Button klicken
3. Logs überwachen

## Community Sharing

### Nach erfolgreichem Deployment:

1. **URLs teilen:**
   - `https://ai-tools.deine-domain.com/api/` - Haupt-API
   - `https://ai-tools.deine-domain.com/workflows/` - N8N Dashboard

2. **N8N Login Info:**
   - User: `admin`
   - Password: `[dein-passwort]`

3. **Getting Started Guide:**
   - Link zur API Dokumentation
   - Beispiel-Workflows importieren
   - Community Discord/Slack einladen

## 🎉 Fertig!

Deine AI Tools Extended Community Platform läuft jetzt auf Coolify mit:
- ✅ Automatisches SSL
- ✅ Health Monitoring  
- ✅ Auto-Deployment
- ✅ Backup Strategy
- ✅ Performance Monitoring
- ✅ Log Management

**Kosten**: ~€10-20/Monat je nach Server-Größe bei Hetzner/DigitalOcean