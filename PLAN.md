# MovieMatch v1 agent plan

Fictional test project for the Marrow original Pass 1 trial. No real user data.

Status: plan written by the coding agent for the v1 milestone.

## Scope

1. `recommend(user_id, limit, genre)` API in `moviematch/api.py`.
2. Genre-affinity ranking from the user's own ratings (`moviematch/ranking.py`).
3. Never re-recommend a title the user already rated.
4. Optional genre filter and result limit.
5. GitHub Actions `acceptance` check runs `pytest` on every pull request.

## Out of scope for v1

- Social features and shared watch lists.
- Editorial collections.

## Done when

All acceptance tests pass on `main` through a pull request.
