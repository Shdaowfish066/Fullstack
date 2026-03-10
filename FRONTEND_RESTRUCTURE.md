# Frontend Restructuring Guide

## Overview

Your frontend has been completely restructured from TypeScript (`.tsx`) to JavaScript (`.jsx`) with a new **API services layer** that directly mirrors your backend routers.

## New Frontend Structure

### 1. **API Services Layer** (`frontend/app/services/`)

Each service directly calls your backend API endpoints, mirroring the backend router structure:

```
services/
├── api.js               # Base API client (mirrors app/main.py)
├── authService.js       # /auth endpoints
├── postsService.js      # /posts endpoints
├── messagesService.js   # /messages endpoints
├── usersService.js      # /users endpoints (mirrors routers/users.py)
├── communitiesService.js # /communities endpoints
├── commentsService.js   # /comments endpoints
├── votesService.js      # /votes endpoints
├── filesService.js      # /files endpoints
├── reportsService.js    # /reports endpoints
├── websocketService.js  # /ws/chat endpoints
└── index.js            # Central export (mirrors routers/__init__.py)
```

**Key Features:**

- Centralized API configuration (`API_BASE_URL`)
- Automatic token management
- All Backend endpoints covered
- Ready for WebSocket integration

### 2. **State Management** (`frontend/app/store/`)

#### AppContext.jsx

- User state management
- CRUD operations for posts, comments, communities
- Message and report handling
- Direct integration with API services

#### ToastContext.jsx

- Toast notifications
- Success, error, warning, and celebration messages
- Auto-dismiss functionality

### 3. **Pages** (`frontend/app/pages/`)

All converted to `.jsx` with API integration:

| Page                    | Service Used       | Status                          |
| ----------------------- | ------------------ | ------------------------------- |
| AuthPage.jsx            | authService        | ✅ Login/Register with API      |
| FeedPage.jsx            | postsService       | ✅ Load all posts from backend  |
| MessagesPage.jsx        | messagesService    | ✅ Real-time messaging          |
| CommunitiesPage.jsx     | communitiesService | ✅ Join/Leave communities       |
| SinglePostPage.jsx      | postsService       | ✅ View post details + comments |
| ProfilePage.jsx         | usersService       | 🔄 Placeholder                  |
| ReportsPage.jsx         | reportsService     | 🔄 Placeholder                  |
| CommunityDetailPage.jsx | communitiesService | 🔄 Placeholder                  |

### 4. **Layout Components** (`frontend/app/components/layout/`)

- RootLayout.jsx - Main app wrapper with navigation

### 5. **Store Files**

- App.jsx - App entry point
- routes.jsx - React Router configuration
- main.jsx - Vite entry point
- index.html - HTML template

## How to Use the Services

### Example: Login User

```javascript
import { authService } from "../services";

try {
  const user = await authService.login(email, password);
  // Token automatically saved
} catch (error) {
  console.error(error);
}
```

### Example: Fetch Posts

```javascript
import { postsService } from "../services";

try {
  const posts = await postsService.getAllPosts();
} catch (error) {
  console.error(error);
}
```

### Example: Send Message

```javascript
import { messagesService } from "../services";

try {
  const response = await messagesService.sendMessage(userId, "Hello!");
} catch (error) {
  console.error(error);
}
```

### Example: WebSocket Connection

```javascript
import { wsService } from "../services";

// Connect to WebSocket
await wsService.connect(token, otherUserId);

// Listen for messages
wsService.on("message", (msg) => {
  console.log("Received:", msg);
});

// Send message
wsService.sendMessage({ content: "Hi!" });

// Disconnect when done
wsService.disconnect();
```

## Migration Checklist

- ✅ Convert all `.tsx` files to `.jsx`
- ✅ Remove TypeScript type annotations
- ✅ Create API services layer
- ✅ Update imports to use new services
- ✅ Create entry points (main.jsx, index.html)
- ✅ Update App.jsx and routes.jsx
- ✅ Create basic page components
- ✅ Set up AppContext and ToastContext
- 🔄 Convert remaining components (UI components)
- 🔄 Connect form components to API services
- 🔄 Add WebSocket integration

## Next Steps

### 1. Finish Component Conversion

Convert remaining `.tsx` files to `.jsx`:

- `/components/posts/` - PostCard, CreatePostModal
- `/components/shared/` - VoteScore, EmptyState, etc.
- `/components/layout/` - Sidebar, MobileNav, etc.
- `/components/toasts/` - ToastSystem, ToastShowcase
- `/components/ui/` - All Radix UI components (these can stay as-is)

### 2. Update Form Components

Create new form components that use the API services:

```javascript
// Example: CreatePostForm.jsx
import { postsService } from "../services";

export function CreatePostForm() {
  const handleCreate = async (title, content) => {
    const response = await postsService.createPost(title, content);
  };
}
```

### 3. Integrate WebSocket

Replace mock data in conversations with real WebSocket:

```javascript
useEffect(() => {
  wsService.connect(token, otherUserId);
  wsService.on("message", (msg) => {
    setMessages((prev) => [...prev, msg]);
  });
  return () => wsService.disconnect();
}, []);
```

### 4. Remove Mock Data

Delete INITIAL_POSTS, MOCK_USERS, etc. from AppContext and load from backend instead.

### 5. Error Handling

Wrap API calls with try/catch and use `useToast` for error notifications.

## Backend ↔ Frontend Mapping

### API Routes

```
Backend Routers     →  Frontend Services
/auth              →  authService
/posts             →  postsService
/messages          →  messagesService
/users             →  usersService
/communities       →  communitiesService
/comments          →  commentsService
/votes             →  votesService
/files             →  filesService
/reports           →  reportsService
/ws/chat           →  wsService
```

## Configuration

### API Base URL

Set in `frontend/app/services/api.js`:

```javascript
const API_BASE_URL =
  typeof window !== "undefined" && window.location.origin === "file://"
    ? "http://localhost:8000"
    : `${window.location.protocol}//${window.location.hostname}:8000`;
```

### WebSocket URL

Set in `frontend/app/services/websocketService.js`:

```javascript
const WS_URL =
  typeof window !== "undefined" && window.location.origin === "file://"
    ? "ws://localhost:8000"
    : `${window.location.protocol === "https:" ? "wss:" : "ws:"}//${window.location.hostname}:8000`;
```

## Running the Project

### Backend

```bash
cd backend
source venv/bin/activate  # or venv\Scripts\activate on Windows
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Visit `http://localhost:5173` (or whatever port Vite shows)

## Development Tips

1. **Use Services for API Calls**: Always import from `frontend/app/services/`
2. **Handle Errors**: Use `useToast().showError()` for error messages
3. **Manage State**: Use `useApp()` context for app-wide state
4. **Keep Components Simple**: Move logic to services and contexts
5. **Type-Free Code**: No TypeScript, just plain JavaScript with JSDoc if needed

## Troubleshooting

### CORS Errors

Ensure backend is running on `http://localhost:8000` and CORS middleware is enabled.

### 404 API Errors

Check that the backend endpoints match your service calls.

### WebSocket Connection Fails

Verify backend WebSocket router is working and token is valid.

### Import Errors

Check that service imports use the correct path: `import { authService } from '../services'`

---

**Status**: ✅ **Ready for Backend Connection**

All frontend files are now in `.jsx` format with a complete API services layer ready to connect to your FastAPI backend!
