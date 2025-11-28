from Npp import *
import socket, struct

def ip_key(ip):
    try:
        return struct.unpack("!L", socket.inet_aton(ip.strip()))[0]
    except:
        return 0

editor.beginUndoAction()
lines = [editor.getLine(i).strip() for i in range(editor.getLineCount()) if editor.getLine(i).strip()]
lines.sort(key=ip_key)
editor.setText('\n'.join(lines))
editor.endUndoAction()
