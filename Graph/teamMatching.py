team_preferences = {
    "Team A": ["Alice", "Bob", "Charlie"],
    "Team B": ["Bob", "Charlie", "Alice"],
    "Team C": ["Charlie", "Alice", "Bob"]
}
candidate_preferences = {
    "Alice": ["Team B", "Team A", "Team C"],
    "Bob": ["Team A", "Team C", "Team B"],
    "Charlie": ["Team B", "Team C", "Team A"]
}


# output: {"Team A": "Charlie", "Team B": "Bob", "Team C": "Alice"}

from typing import Dict

def match_teams_with_candidates(team_preferences, candidate_preferences) -> Dict[str, str]:
    team_count = len(team_preferences)
    teams_matched = {}
    candidates_matched = {}
    while len(teams_matched) < team_count:
        for team, candidates in team_preferences.items():
            if team not in teams_matched:
                for candidate in candidates:
                    if candidate not in candidates_matched:
                        teams_matched[team] = candidate
                        candidates_matched[candidate] = team
                        break
                    else:
                        current_team = candidates_matched[candidate]
                        if candidate_preferences[candidate].index(team) < candidate_preferences[candidate].index(current_team):
                            teams_matched[team] = candidate
                            teams_matched[current_team] = None
                            candidates_matched[candidate] = team
                            break
    return teams_matched

print(match_teams_with_candidates(team_preferences,candidate_preferences))