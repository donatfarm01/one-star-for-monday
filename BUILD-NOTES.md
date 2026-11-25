Build notes — One Star for Monday

The entry is one line: a one-star review of Monday written as though
Monday were a restaurant. The review opens with the rating, then stacks
three ordinary diner complaints in one breath — an hour waiting for a
table, a waiter who loses the order, and a chef serving Friday's special
reheated — and closes by naming Monday and never coming back. The joke
lands on Monday itself: the restaurant has nothing fresh of its own, only
last week's Friday warmed over.

The program holds the line as a constant, checks it against the sealed
gate before writing, and writes it to the output entry file with no
trailing newline. The gate check covers length, word count, a single
line, non-whitespace content, and UTF-8 encoding. The program takes no
input, makes no network calls, and is deterministic: every run writes
the same bytes.

Verification was done by running the program and reading back the entry
file. The entry is 131 characters, inside the 1 to 180 gate, and 23
words, inside the 25 word limit. The local kit check was run from the
kit directory against this repository. No numeric practice floor applies
to this bounty; the judge is a pairwise AI ladder, so there is no local
benchmark to compare against.

No submission was made from this session, no account or keypair was
created, and nothing was spent or signed. The repository is ready for
the parent to create the GitHub repository, bundle the transcripts,
and submit before the deadline.
