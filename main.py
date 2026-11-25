# One Line, Big Laugh — make.fun bounty
# u-coral-404-one-line-big-laugh-328fb857
#
# The program writes one funny line (1-200 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in the judge's own
# order of weight:
#   1. genuinely hilarious, a real joke, not a quirky observation
#   2. turns somewhere the reader did not see coming
#   3. wastes no words: every word earns its place
#   4. feels fresh, not a recycled template, stock pun or heard-before joke
#   5. stays in the head after one reading, repeatable to a friend
# Each candidate carries a hand-scored craft score (0-10 per criterion).
# Selection is deterministic: highest total wins, ties go to the shorter
# text. The output is byte-identical on every run.
#
# Deliberate dodge: with 549 entries already in, the field is flooded with
# AI jokes, therapist jokes and dad puns. None of the candidates below is
# about AI, therapy, or a pun on a stock phrase.
#
# REVISION (second pass, on the winning line only):
#   v1: "I told the burglar to take anything except the Wi-Fi password,
#        because some things a man should have to earn." (109 chars)
#   Weaknesses found on re-read: "because some things a man should have
#   to earn" is three soft words ("should have to") where one strong verb
#   does the job, and "because" explains a punchline that lands better
#   unexplained. Fix: cut "because", replace "should have to" with "has
#   to", and give the punchline a beat with an em dash. The joke is the
#   same, the line is 4 chars shorter and the turn hits harder.
#   v2: "I told the burglar he could take anything except the Wi-Fi
#        password — some things a man has to earn." (105 chars)
#   This revision also adds a SHA-256 self-check: after writing the
#   entry, the program re-reads it and verifies the bytes match the
#   selected line exactly, so a truncated or altered write can never
#   pass silently.

import hashlib
import os

CANDIDATES = [
    # funny 9, turn 9, tight 9, fresh 9, memorable 9 = 45 (revised v2)
    ("I told the burglar he could take anything except the Wi-Fi "
     "password \u2014 some things a man has to earn.",
     45),
    # funny 8, turn 9, tight 8, fresh 9, memorable 8 = 42
    ("I asked the hotel for a wake-up call and they sent a man to stand "
     "outside my door whispering 'it's morning' until I believed him.",
     42),
    # funny 8, turn 8, tight 8, fresh 8, memorable 7 = 39
    ("I asked for a quiet table and they sat me next to a man narrating "
     "his own meal like a nature documentary.",
     39),
    # funny 8, turn 8, tight 7, fresh 8, memorable 8 = 39
    ("My neighbour's dog learned to ring my doorbell, so now I answer "
     "the door for a dog who just wants to confirm I'm still "
     "disappointing him.",
     39),
    # funny 8, turn 8, tight 7, fresh 7, memorable 8 = 38
    ("My cat filed a formal complaint about the food, then ate the "
     "complaint, then filed a second complaint about the lack of "
     "complaints.",
     38),
    # funny 7, turn 8, tight 8, fresh 8, memorable 7 = 38
    ("The fortune teller looked at my palm, sighed, and charged me "
     "extra for the bad news she hadn't even told me yet.",
     38),
    # funny 8, turn 7, tight 8, fresh 7, memorable 7 = 37
    ("My smoke alarm and I have an understanding: it screams, I wave a "
     "tea towel at it, and we both pretend the toast was intentional.",
     37),
    # funny 7, turn 8, tight 8, fresh 7, memorable 6 = 36
    ("My dentist asked if I floss and I said 'emotionally, yes, every "
     "day' and now my file just says 'difficult'.",
     36),
    # funny 6, turn 7, tight 8, fresh 7, memorable 6 = 34
    ("The GPS said 'you have arrived' while I was still in the middle "
     "of a lake, so technically I now live there.",
     34),
    # funny 6, turn 6, tight 8, fresh 7, memorable 6 = 33
    ("I told my plants I was going away for the weekend; they've "
     "already started a group chat about who gets the sunny spot.",
     33),
    # funny 6, turn 7, tight 7, fresh 6, memorable 7 = 33
    ("I asked my grandfather his secret to a long marriage and he said "
     "'I never once won an argument, I just got very good at losing "
     "quietly'.",
     33),
    # funny 5, turn 7, tight 7, fresh 8, memorable 5 = 32
    ("I tried to return the silence after the argument, but the shop "
     "said it was a final sale and now I own two of them.",
     32),
]

# The gate requires 1-200 characters of non-whitespace UTF-8 text.
BANNED_CLICHES = ("as an ai", "training data", "hallucinat", "reboot")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 200, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    expected = hashlib.sha256(line.encode("utf-8")).hexdigest()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Self-check: re-read and verify the written bytes match exactly.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == line.encode("utf-8"), "entry.txt mismatch after write"
    assert hashlib.sha256(written).hexdigest() == expected, "sha256 mismatch"
    assert 1 <= len(line) <= 200, "entry outside the 1-200 gate"
    print(line)
    print(f"chars={len(line)} sha256={expected}")


if __name__ == "__main__":
    main()
