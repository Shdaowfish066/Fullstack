# 🚀 Quick Start Guide - Backend & Frontend Ready to Go

## ✅ What's Done

### Frontend Setup

- ✅ npm dependencies installed
- ✅ 25 React components (`.jsx`) created
- ✅ 12 API services configured
- ✅ State management ready (AppContext + ToastContext)
- ✅ All 8 pages implemented with real functionality
- ✅ Router configuration complete

### Backend Setup

- ✅ FastAPI configured with CORS enabled
- ✅ 12 routers properly exposed:
  - Auth (register, login, getCurrentUser)
  - Posts (CRUD operations)
  - Users (profile info, list users)
  - Comments (create, update, delete, get)
  - Votes (for posts and comments)
  - Messages (send, get conversations, WebSocket)
  - Files (upload, download, delete)
  - Reports (create, view, resolve)
  - Communities (create, join, leave)
  - WebSocket (real-time chat)

---

## 🎯 Start Here

### Option A: Run Both in Separate Terminals (Recommended for Development)

#### Terminal 1 - Backend:

```powershell
cd "c:\Users\Windows 11\Desktop\CSE-2100-PROJECT\backend"
python -m uvicorn app.main:app --reload --port 8000
```

#### Terminal 2 - Frontend:

```powershell
cd "c:\Users\Windows 11\Desktop\CSE-2100-PROJECT\frontend"
npm run dev
```

Then open your browser to: **http://localhost:5173**

---

### Option B: Quick Test of Backend API Only

```powershell
cd "c:\Users\Windows 11\Desktop\CSE-2100-PROJECT\backend"
python -m uvicorn app.main:app --reload --port 8000
```

Then visit: **http://localhost:8000/docs** to see interactive API documentation

---

## 📋 Testing Checklist

### Authentication Flow

- [ ] Click "Sign In" and see login form
- [ ] Try registration with new email/username/password
- [ ] Login returns success message and redirects to feed
- [ ] Logout button appears on profile page
- [ ] Token persists in localStorage

### Feed & Posts

- [ ] See list of posts with titles and content
- [ ] Click "Create Post" button
- [ ] Fill form and submit - post appears in feed
- [ ] Upvote/downvote posts with arrow buttons
- [ ] Vote counts update in real-time
- [ ] Click post title to see full post detail

### Communities

- [ ] "Communities" page shows list of all communities
- [ ] Can join/leave communities
- [ ] Community detail page shows members and community posts
- [ ] Can create new community (if captain feature enabled)

### Messages

- [ ] "Messages" page shows conversation list
- [ ] Can click conversation to open chat
- [ ] Can type and send messages (if WebSocket working)
- [ ] New messages appear in real-time

### Profile

- [ ] "Profile" page shows current user info
- [ ] Shows statistics (posts, communities, joined)
- [ ] "Log Out" button works and returns to login

### Reports

- [ ] "Reports" page shows your submitted reports
- [ ] Status shows "Open" or "Resolved"
- [ ] Can create new report from post menu

---

## 🐛 Debugging Tips

### If Frontend Won't Load

1. Check in `frontend` folder: `npm install` (already done)
2. Verify `npm run dev` shows `VITE v6.3.5`
3. Check browser console (F12) for JavaScript errors
4. Try clearing cache: `Ctrl+Shift+Delete` → Clear browsing data

### If Backend Errors

1. Check Python version: `python --version` (should be 3.8+)
2. Verify venv activated: `.venv\Scripts\Activate.ps1`
3. Check dependencies: `pip list | findstr fastapi`
4. Check database: Look for `app.db` in backend folder

### If API Calls Fail (Network Errors)

1. Verify backend running on port 8000: `http://localhost:8000/docs`
2. Check frontend API URL: `frontend/app/services/api.js` line 1
   - Should be: `API_BASE_URL = 'http://localhost:8000'`
3. Check browser Network tab (F12) to see failed requests
4. Look at backend terminal for error messages

### If WebSocket Chat Fails

1. WebSocket is only tested in Messages page
2. Check browser console for WebSocket connection errors
3. Backend should show connection attempts in terminal

---

## 🔧 Environment Variables

### Backend

None needed! Uses defaults:

- Port: 8000
- Database: SQLite (app.db)
- Environment: development (CORS allows all origins)

### Frontend

None needed! Uses hardcoded defaults:

- Backend API: `http://localhost:8000`
- Frontend Port: 5173 (assigned by Vite)

---

## 📊 Project Structure

```
CSE-2100-PROJECT/
├── backend/                          # FastAPI server
│   ├── app/
│   │   ├── main.py                  # ✅ All routers included
│   │   ├── models/                  # Database models
│   │   ├── schemas/                 # Pydantic request/response schemas
│   │   ├── routers/                 # ✅ 12 API routers exposed
│   │   │   ├── auth.py              # /auth
│   │   │   ├── posts.py             # /posts
│   │   │   ├── users.py             # /users
│   │   │   ├── comments.py          # /comments
│   │   │   ├── comment_routes.py    # /comments (create)
│   │   │   ├── comment_updates.py   # /comments (update)
│   │   │   ├── votes.py             # /votes (posts)
│   │   │   ├── comment_votes.py     # /votes (comments)
│   │   │   ├── messages.py          # /messages
│   │   │   ├── files.py             # /files
│   │   │   ├── reports.py           # /reports ✅ (NOW INCLUDED)
│   │   │   ├── communities.py       # /communities
│   │   │   └── websocket.py         # /ws (WebSocket)
│   │   ├── database.py              # SQLAlchemy setup
│   │   └── config.py                # Settings
│   ├── requirements.txt             # Python dependencies
│   └── README                        # Backend docs
│
├── frontend/                        # React/Vite app
│   ├── app/
│   │   ├── App.jsx                  # ✅ Root component
│   │   ├── main.jsx                 # ✅ Entry point
│   │   ├── routes.jsx               # ✅ React Router config
│   │   ├── pages/                   # ✅ 8 pages
│   │   │   ├── AuthPage.jsx         # Login/Register
│   │   │   ├── FeedPage.jsx         # Posts feed
│   │   │   ├── SinglePostPage.jsx   # Post detail
│   │   │   ├── MessagesPage.jsx     # Chat/messages
│   │   │   ├── CommunitiesPage.jsx  # Community list
│   │   │   ├── CommunityDetailPage.jsx # Community detail
│   │   │   ├── ProfilePage.jsx      # User profile
│   │   │   └── ReportsPage.jsx      # Reports
│   │   ├── components/              # ✅ Reusable components
│   │   ├── store/                   # ✅ State management
│   │   │   ├── AppContext.jsx       # Global app state
│   │   │   └── ToastContext.jsx     # Notifications
│   │   └── services/                # ✅ 12 API services
│   │       ├── api.js               # Base HTTP client
│   │       ├── authService.js
│   │       ├── postsService.js
│   │       ├── usersService.js
│   │       ├── communitiesService.js
│   │       ├── commentsService.js
│   │       ├── messagesService.js
│   │       ├── votesService.js
│   │       ├── filesService.js
│   │       ├── reportsService.js
│   │       ├── websocketService.js
│   │       └── index.js
│   ├── package.json                 # ✅ npm scripts: dev, build, preview
│   ├── main.jsx                     # ✅ Vite entry
│   └── index.html                   # ✅ HTML template
│
├── BACKEND_FRONTEND_MAPPING.md      # ✅ NEW - API endpoint mapping
├── FRONTEND_RESTRUCTURE_COMPLETE.md # ✅ Conversion details
└── QUICK_START.md                   # This file
```

---

## 🎁 What's Ready to Use

### Authentication

```javascript
// frontend/app/services/authService.js
authService.register(email, username, password);
authService.login(email, password);
authService.getCurrentUser();
```

### Create & View Posts

```javascript
// frontend/app/services/postsService.js
postsService.createPost(title, content, anonymous);
postsService.getAllPosts();
postsService.getPost(id);
postsService.updatePost(id, data);
postsService.deletePost(id);
```

### Voting System

```javascript
// frontend/app/services/votesService.js
votesService.voteOnPost(postId, score); // score: 1 (up), -1 (down), 0 (remove)
votesService.voteOnComment(commentId, score);
```

### Communities

```javascript
// frontend/app/services/communitiesService.js
communitiesService.createCommunity(name, description);
communitiesService.getAllCommunities();
communitiesService.getCommunity(id);
communitiesService.joinCommunity(id);
communitiesService.leaveCommunity(id);
```

### Real-Time Messaging

```javascript
// frontend/app/services/websocketService.js
wsService.connect(conversationId);
wsService.sendMessage(messageContent);
wsService.on("message", (msg) => {
  /* handle message */
});
wsService.disconnect();
```

---

## 📝 Notes

- Both services use **localhost** (not accessible from other machines)
- For production, update `API_BASE_URL` and deploy both together
- WebSocket requires HTTP (not HTTPS) during development
- File uploads are stored in `backend/uploads/` directory
- Database is stored as `backend/app.db` (SQLite)

---

## 🚨 Common Issues & Fixes

| Issue                               | Fix                                           |
| ----------------------------------- | --------------------------------------------- |
| Port 8000 already in use            | Change port in backend command: `--port 8001` |
| Port 5173 already in use            | Vite auto-assigns next port                   |
| "Cannot find module" errors         | Run `npm install` in frontend folder          |
| "ModuleNotFoundError" on backend    | Activate venv: `.venv\Scripts\Activate.ps1`   |
| CORS errors in browser              | Backend already allows `*` origins            |
| Blank page on frontend              | Check F12 console for errors                  |
| Login returns "Invalid credentials" | Check user exists in database                 |

---

## ✨ Next Steps

1. **Start Backend**:

   ```powershell
   cd backend && python -m uvicorn app.main:app --reload --port 8000
   ```

2. **Start Frontend**:

   ```powershell
   cd frontend && npm run dev
   ```

3. **Open Browser**:

   ```
   http://localhost:5173
   ```

4. **Test Registration/Login**:
   Create an account and try all features

5. **Check Logs**:
   Both terminal windows will show real-time logs of requests/errors

---

**Status**: ✅ Everything is ready. Start the services!

Generated: March 10, 2026
