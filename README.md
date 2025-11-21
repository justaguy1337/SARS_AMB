# SARS - Smart Ambulance Routing System

Complete frontend application for AI-powered emergency ambulance dispatch.

## 🚀 Features Implemented

### ✅ Core Components
- **Sidebar Navigation** - Professional multi-role navigation with admin/dispatcher/driver views
- **Top Navigation Bar** - Mobile-responsive header with search and notifications
- **Status Panel** - Real-time system status, weather, traffic predictions
- **Audio Upload** - Drag-and-drop MP3 call recording upload
- **Dispatch Form** - AI auto-filled patient details form
- **Map View** - Interactive Google Maps with ambulance tracking and ETA
- **Ambulance Card** - Individual ambulance information cards

### 🎨 UI Design
- Material-UI (MUI) components
- Professional color scheme (Blue primary, Red emergency)
- Consistent elevation and borders
- Responsive grid layout
- Mobile-first design
- Dark sidebar with light content area

### 📱 Responsive Design
- Desktop: Sidebar + Main content + Status panel (3 columns)
- Tablet: Sidebar + Main content (2 columns)
- Mobile: Hamburger menu + Full-width content

## 🛠️ Tech Stack

Frontend:
- React 19.2
- Material-UI (MUI) 5
- Google Maps API
- Axios
- React Router

## 📦 Installation

```bash
npm install
```

## 🚀 Running the App

```bash
npm start
```

The app runs on `http://localhost:3000`

## 📂 Project Structure

```
src/
├── components/
│   ├── AudioUpload.js          # MP3 upload
│   ├── DispatchForm.js         # Patient form
│   ├── MapView.js              # Google Maps
│   ├── Sidebar.js              # Navigation
│   ├── TopNavBar.js            # Mobile nav
│   └── StatusPanel.js          # Status info
├── pages/
│   └── Dashboard.js            # Main page
└── services/
    └── api.js                  # API integration
```

## 🎯 Workflow

1. Upload emergency call recording (MP3)
2. AI transcribes and extracts patient info
3. Review and edit auto-filled form
4. Select fastest ambulance from map
5. Dispatch with optimized route

## 🗺️ Map Features

- Live ambulance tracking
- Patient location marker
- Route visualization with traffic
- Real-time ETA calculations
- Nearby hospitals

## 📊 Status Panel

- Active ambulances count
- Active emergencies
- Average response time
- Traffic prediction
- Weather conditions
- System health

---

**Built for saving lives 🚑**
