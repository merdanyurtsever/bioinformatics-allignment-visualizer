#değişkenler: match_score: int, mismatch_penalty: int, gap_penalty: int
#metotlar: score(a: str, b: str) -> int, gap() -> int

#if no input is given, use default scoring values
match_score = 1
mismatch_penalty = -1
gap_penalty = -2

def score(a: str, b: str) -> int:
    """İki karakter arasındaki skoru döndürür."""
    if a == b:
        return match_score
    else:
        return mismatch_penalty

def gap() -> int:
    """Boşluk cezasını döndürür."""
    return gap_penalty