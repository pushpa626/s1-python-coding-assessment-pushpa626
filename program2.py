def decode_message(s: str, p: str) -> bool:
    s_ptr, p_ptr = 0, 0

    while p_ptr < len(p):
        if s_ptr < len(s) and p[p_ptr] == s[s_ptr]:
            s_ptr += 1
            p_ptr += 1
        else:
            return False
