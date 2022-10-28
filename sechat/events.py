import enum

class Events(enum.Enum):
  MESSAGE = 1
  EDIT = 2
  JOIN = 3
  LEAVE = 4
  NAME_CHANGE = 5
  MESSAGE_STARRED = 6
  DEBUG = 7
  MENTION = 8
  FLAG = 9
  DELETE = 10
  FILE_UPLOAD = 11
  MODERATOR_FLAG = 12
  SETTINGS_CHANGED = 13
  GLOBAL_NOTIFICATION = 14
  ACCESS_CHANGED = 15
  USER_NOTIFICATION = 16
  INVITATION = 17
  REPLY = 18
  MESSAGE_MOVED_OUT = 19
  MESSAGE_MOVED_IN = 20
  TIME_BREAK = 21
  FEED_TICKER = 22
  USER_SUSPENSION = 23
  USER_MERGE = 24
  USER_NAME_OR_AVATAR_CHANGE = 25

  SECHAT_ERROR = -1
  SECHAT_CONN_CLOSE = -2

