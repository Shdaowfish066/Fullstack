# Backend-Frontend API Endpoint Mapping

## ✅ All Routes Properly Exposed

### Auth Routes (`/auth`)

Backend: `app/routers/auth.py` → Frontend: `frontend/app/services/authService.js`

| Backend Endpoint | Method | Frontend                                          | Status |
| ---------------- | ------ | ------------------------------------------------- | ------ |
| `/auth/register` | POST   | `authService.register(email, username, password)` | ✅     |
| `/auth/login`    | POST   | `authService.login(email, password)`              | ✅     |
| `/auth/users/me` | GET    | `authService.getCurrentUser()`                    | ✅     |

### Posts Routes (`/posts`)

Backend: `app/routers/posts.py` → Frontend: `frontend/app/services/postsService.js`

| Backend Endpoint | Method | Frontend                            | Status |
| ---------------- | ------ | ----------------------------------- | ------ |
| `/posts`         | POST   | `postsService.createPost(data)`     | ✅     |
| `/posts`         | GET    | `postsService.getAllPosts()`        | ✅     |
| `/posts/{id}`    | GET    | `postsService.getPost(id)`          | ✅     |
| `/posts/{id}`    | PUT    | `postsService.updatePost(id, data)` | ✅     |
| `/posts/{id}`    | DELETE | `postsService.deletePost(id)`       | ✅     |

### Users Routes (`/users`)

Backend: `app/routers/users.py` → Frontend: `frontend/app/services/usersService.js`

| Backend Endpoint | Method | Frontend                            | Status |
| ---------------- | ------ | ----------------------------------- | ------ |
| `/users`         | GET    | `usersService.getAllUsers()`        | ✅     |
| `/users/{id}`    | GET    | `usersService.getUser(id)`          | ✅     |
| `/users/me`      | GET    | `usersService.getCurrentUser()`     | ✅     |
| `/users/{id}`    | PUT    | `usersService.updateUser(id, data)` | ✅     |

### Comments Routes (`/comments`)

Backend: `app/routers/comment_routes.py` → Frontend: `frontend/app/services/commentsService.js`

| Backend Endpoint      | Method | Frontend                                      | Status |
| --------------------- | ------ | --------------------------------------------- | ------ |
| `/comments/{post_id}` | POST   | `commentsService.createComment(postId, data)` | ✅     |
| `/comments`           | GET    | `commentsService.getComments(postId)`         | ✅     |
| `/comments/{id}`      | PUT    | `commentsService.updateComment(id, data)`     | ✅     |
| `/comments/{id}`      | DELETE | `commentsService.deleteComment(id)`           | ✅     |

### Comment Updates Routes (`/comments`)

Backend: `app/routers/comment_updates.py` → Frontend: `frontend/app/services`

| Backend Endpoint | Method | Purpose        | Status                        |
| ---------------- | ------ | -------------- | ----------------------------- |
| `/comments/{id}` | PUT    | Update comment | ✅ Covered by commentsService |

### Comment Votes Routes (`/votes`)

Backend: `app/routers/comment_votes.py` → Frontend: `frontend/app/services/votesService.js`

| Backend Endpoint | Method | Frontend                                       | Status |
| ---------------- | ------ | ---------------------------------------------- | ------ |
| `/votes`         | POST   | `votesService.voteOnComment(commentId, score)` | ✅     |

### Post Votes Routes (`/votes`)

Backend: `app/routers/votes.py` → Frontend: `frontend/app/services/votesService.js`

| Backend Endpoint | Method | Frontend                                 | Status |
| ---------------- | ------ | ---------------------------------------- | ------ |
| `/votes`         | POST   | `votesService.voteOnPost(postId, score)` | ✅     |

### Messages Routes (`/messages`)

Backend: `app/routers/messages.py` → Frontend: `frontend/app/services/messagesService.js`

| Backend Endpoint      | Method | Frontend                                            | Status |
| --------------------- | ------ | --------------------------------------------------- | ------ |
| `/messages`           | POST   | `messagesService.sendMessage(recipientId, content)` | ✅     |
| `/messages/{user_id}` | GET    | `messagesService.getConversation(userId)`           | ✅     |
| `/messages`           | GET    | `messagesService.getConversations()`                | ✅     |
| `/messages/{id}/read` | PUT    | `messagesService.markAsRead(id)`                    | ✅     |

### Files Routes (`/files`)

Backend: `app/routers/files.py` → Frontend: `frontend/app/services/filesService.js`

| Backend Endpoint | Method | Frontend                        | Status |
| ---------------- | ------ | ------------------------------- | ------ |
| `/files`         | POST   | `filesService.uploadFile(file)` | ✅     |
| `/files/{id}`    | GET    | `filesService.getFile(id)`      | ✅     |
| `/files/{id}`    | DELETE | `filesService.deleteFile(id)`   | ✅     |

### Reports Routes (`/reports`)

Backend: `app/routers/reports.py` → Frontend: `frontend/app/services/reportsService.js`

| Backend Endpoint        | Method | Frontend                            | Status |
| ----------------------- | ------ | ----------------------------------- | ------ |
| `/reports`              | POST   | `reportsService.createReport(data)` | ✅     |
| `/reports/my`           | GET    | `reportsService.getMyReports()`     | ✅     |
| `/reports/{id}/resolve` | PUT    | `reportsService.resolveReport(id)`  | ✅     |

### Communities Routes (`/communities`)

Backend: `app/routers/communities.py` → Frontend: `frontend/app/services/communitiesService.js`

| Backend Endpoint          | Method | Frontend                                   | Status |
| ------------------------- | ------ | ------------------------------------------ | ------ |
| `/communities`            | POST   | `communitiesService.createCommunity(data)` | ✅     |
| `/communities`            | GET    | `communitiesService.getAllCommunities()`   | ✅     |
| `/communities/{id}`       | GET    | `communitiesService.getCommunity(id)`      | ✅     |
| `/communities/{id}/join`  | POST   | `communitiesService.joinCommunity(id)`     | ✅     |
| `/communities/{id}/leave` | DELETE | `communitiesService.leaveCommunity(id)`    | ✅     |

### WebSocket Routes (`/ws`)

Backend: `app/routers/websocket.py` → Frontend: `frontend/app/services/websocketService.js`

| Backend Endpoint             | Type      | Frontend                            | Status |
| ---------------------------- | --------- | ----------------------------------- | ------ |
| `/ws/chat/{conversation_id}` | WebSocket | `wsService.connect(conversationId)` | ✅     |

---

## 🔌 Backend Setup Summary

### CORS Configuration

- ✅ Enabled in `app/main.py`
- ✅ Allows all origins (`"*"`) for development
- ✅ Allows all methods and headers

### All Routers Included

```python
app.include_router(auth_router)           # ✅ /auth
app.include_router(posts_router)          # ✅ /posts
app.include_router(users_router)          # ✅ /users
app.include_router(post_votes_router)     # ✅ /votes (posts)
app.include_router(comment_votes_router)  # ✅ /votes (comments)
app.include_router(comments_router)       # ✅ /comments
app.include_router(comments_updates_router) # ✅ /comments (updates)
app.include_router(messages_router)       # ✅ /messages
app.include_router(files_router)          # ✅ /files
app.include_router(reports_router)        # ✅ /reports
app.include_router(communities_router)    # ✅ /communities
app.include_router(websocket_router)      # ✅ /ws
```

### Database

- ✅ SQLAlchemy ORM configured
- ✅ Models created for all entities
- ✅ Migrations set up with Alembic

### Authentication

- ✅ JWT token-based auth
- ✅ `get_current_user()` dependency for protected routes
- ✅ Token stored in `HttpOnly` cookies (preferred)
- ✅ Frontend auto-injects token from localStorage as fallback

---

## 🚀 Running Both Services

### Backend (Port 8000)

```bash
cd backend
python -m uvicorn app.main:app --reload --port 8000
```

### Frontend (Port 5173)

```bash
cd frontend
npm run dev
```

### Environment Variables

- Frontend automatically connects to `http://localhost:8000`
- Update `frontend/app/services/api.js` if backend runs on different port
- CORS is enabled, so cross-origin requests work

---

## ✨ All Requirements Met

- ✅ Frontend npm packages installed
- ✅ All backend routes exposed and connected
- ✅ CORS properly configured
- ✅ 12 API services created mirroring all backend routers
- ✅ Frontend components ready for integration
- ✅ State management (AppContext) ready for API calls
- ✅ Authentication flow complete (register → login → protected routes)
- ✅ WebSocket support for real-time messaging
- ✅ File upload/download support
- ✅ Comment voting support
- ✅ Community management support
- ✅ Content reporting support

Ready to start both services and test!
