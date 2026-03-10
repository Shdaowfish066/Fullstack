# Frontend-Backend Integration Guide

## Summary of Changes Made

### Backend Changes

#### 1. **Added User List Endpoint** (`app/routers/users.py`)

- **New Route**: `GET /users/list/all`
- **Purpose**: Retrieve all users except the current user
- **Authentication**: Required (Bearer token)
- **Response**: List of `UserOut` objects

```
GET http://localhost:8000/users/list/all
Authorization: Bearer {token}
```

#### 2. **Added HTML Serving** (`app/main.py`)

- **New Route**: `GET /`
- **Purpose**: Serves the `websocket_chat.html` file directly from the backend
- **Access**: `http://localhost:8000`
- **Imports Added**:
  - `FileResponse` from `fastapi.responses`
  - `StaticFiles` from `fastapi.staticfiles` (for future use)
  - `os` module for path handling

### Frontend Changes

#### 1. **Configurable API Base URL** (`websocket_chat.html`)

- Added dynamic API URL configuration
- Automatically detects if running locally or remotely
- **Configuration Location**: Line ~359 in the script section

```javascript
const API_BASE_URL =
  window.location.origin === "file://"
    ? "http://localhost:8000"
    : `${window.location.protocol}//${window.location.hostname}:8000`;
```

#### 2. **Replaced User Loading Logic**

- **Before**: Looped through user IDs 1-50 (inefficient)
- **After**: Uses new `/users/list/all` endpoint (efficient)
- **Fallback**: Gracefully handles errors with empty user list

#### 3. **Improved Error Handling**

- Added response status checking in all fetch calls
- Added try-catch blocks around JSON parsing
- Better error messages for users
- WebSocket connection error alerts

#### 4. **Enhanced User Selection**

- Properly closes previous WebSocket connections when switching users
- Fixed active user indicator styling
- Validates WebSocket connection before sending messages

#### 5. **Consistent URL Usage**

- All API calls now use `API_BASE_URL` variable
- Updated endpoints:
  - `POST /auth/login` ✓
  - `GET /users/me` ✓
  - `GET /users/list/all` ✓ (NEW)
  - `WS /ws/chat/{user_id}` ✓
  - `GET /messages/conversation/{user_id}` ✓

## How to Run

### 1. Start the Backend Server

```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Access the Frontend

Open your browser and navigate to:

```
http://localhost:8000
```

The HTML file will be automatically served!

## Testing Checklist

### ✓ Authentication Flow

- [ ] Navigate to http://localhost:8000
- [ ] Login with credentials (default: testuser1_1771432731@example.com / TestPass123!)
- [ ] Verify "Connected as [username]" message appears
- [ ] Verify login button becomes disabled

### ✓ User Loading

- [ ] After login, verify users list appears in sidebar
- [ ] Verify current user is NOT in the list
- [ ] Verify all other users are displayed
- [ ] No inefficient 50-request loop in network tab

### ✓ Chat Functionality

- [ ] Click on a user to start chatting
- [ ] Verify user name appears in chat header
- [ ] Verify online indicator appears (green dot)
- [ ] Verify previous message history loads
- [ ] Type a message and send (press Enter or click Send)
- [ ] Verify message appears in chat
- [ ] Switch to another user and back
- [ ] Verify conversation history is preserved

### ✓ WebSocket Connection

- [ ] Check browser console for "WebSocket connected to" message
- [ ] Verify green online indicator when connected
- [ ] Verify Connection is maintained while chatting
- [ ] Check console for any connection errors

### ✓ Error Handling

- [ ] Remove/disable internet temporarily to test error messages
- [ ] Verify alert appears when WebSocket disconnects
- [ ] Verify errors in console are logged clearly

## API Endpoints Summary

| Method | Endpoint                           | Auth Required   | Purpose                  |
| ------ | ---------------------------------- | --------------- | ------------------------ |
| POST   | `/auth/login`                      | No              | User login               |
| POST   | `/auth/register`                   | No              | User registration        |
| GET    | `/auth/login` (check docs)         | No              | See login docs           |
| GET    | `/users/me`                        | Yes             | Get current user         |
| GET    | `/users/{id}`                      | No              | Get user by ID           |
| GET    | `/users/list/all`                  | Yes             | Get all users (**NEW**)  |
| GET    | `/messages/conversation/{user_id}` | Yes             | Get conversation history |
| POST   | `/messages/`                       | Yes             | Send a message           |
| WS     | `/ws/chat/{user_id}`               | Yes (via token) | WebSocket connection     |

## Troubleshooting

### "Not Connected" Status

- Check if backend server is running
- Check browser console for connection errors
- Verify API_BASE_URL is correct
- Check CORS configuration in main.py

### Users List Not Loading

- Verify login was successful
- Check network tab for `/users/list/all` request status
- Check browser console for errors
- Verify authentication token is being sent

### WebSocket Connection Failed

- Ensure token is valid (logs out and re-login)
- Check console for detailed WebSocket error
- Verify URL ws://localhost:8000/ws/chat/{id}?token={token}
- Check if backend WebSocket router is working (check logs)

### Messages Not Loading

- Verify `/messages/conversation/{user_id}` endpoint is called
- Check network tab response status
- Ensure both users have messages in conversation

## Environment Variables

Make sure your `.env` file includes:

```env
JWT_SECRET_KEY=your_secret_key
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRE_MINUTES=60
DATABASE_URL=your_database_url
```

## Browser Console Output

When working correctly, you should see:

```
Connecting to WebSocket: ws://localhost:8000/ws/chat/2?token=...
WebSocket connected to testuser2
Received message: {sender_id: 1, recipient_id: 2, content: "Hello", ...}
```

## Performance Notes

- **Before**: 50 HTTP requests to load user list (1-50 IDs)
- **After**: 1 HTTP request to load user list
- **Benefit**: Faster login, less server load, cleaner network tab

## Future Improvements

Potential enhancements to consider:

1. Add pagination to user list endpoint
2. Add typing indicators
3. Add read receipts
4. Add user online status
5. Add message search functionality
6. Implement user groups/channels
7. Add file sharing in messages
8. Add message reactions/emojis
