#!/usr/bin/env python3
"""
🎨 GitHub Contribution Graph Pattern Maker
==========================================
Draw custom patterns on your GitHub contribution graph by creating
backdated commits with specific dates.

HOW IT WORKS:
- GitHub's contribution graph is 52 weeks × 7 days (rows = Sun-Sat)
- Each cell = 1 day. More commits = darker green.
- This script creates commits on specific past dates to "paint" a pattern.

HOW TO USE:
1. Edit the PATTERN grid below (7 rows × up to 52 columns)
   - '.' = no commits (empty cell)
   - '1' = light green (1-3 commits)
   - '2' = medium green (4-6 commits)  
   - '3' = dark green (7-9 commits)
   - '4' = darkest green (10+ commits)
   
2. Set START_WEEKS_AGO to position when the pattern starts
3. Run: python3 contribute.py
4. Push: git push origin main

The graph reads LEFT to RIGHT, each column = 1 week (Sun at top, Sat at bottom)
"""

import os
import subprocess
from datetime import datetime, timedelta

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🎨 PATTERN CONFIGURATION                     ║
# ╠══════════════════════════════════════════════════════════════════╣
# ║  Edit the pattern below! Each row = day of week (Sun-Sat)      ║
# ║  Each column = 1 week. Use: . 1 2 3 4                          ║
# ╚══════════════════════════════════════════════════════════════════╝

# ----------- PRESET PATTERNS (uncomment the one you want) -----------

# ❤️ HEART PATTERN
HEART = [
    ". . 1 1 . . 1 1 . .",
    ". 2 2 2 2 2 2 2 2 .",
    ". 3 3 3 3 3 3 3 3 .",
    ". . 3 3 3 3 3 3 . .",
    ". . . 4 4 4 4 . . .",
    ". . . . 4 4 . . . .",
    ". . . . . . . . . .",
]

# 🌟 STAR PATTERN
STAR = [
    ". . . . 3 . . . . .",
    ". . . 3 3 3 . . . .",
    ". 2 2 3 4 3 2 2 . .",
    ". . 3 3 4 3 3 . . .",
    ". . . 4 4 4 . . . .",
    ". . 3 . 4 . 3 . . .",
    ". 2 . . . . . 2 . .",
]

# ⚡ ZIGZAG PATTERN
ZIGZAG = [
    "4 . . . . 4 . . . . 4 . . . . 4 . . . . 4",
    ". 3 . . 3 . 3 . . 3 . 3 . . 3 . 3 . . 3 .",
    ". . 2 2 . . . 2 2 . . . 2 2 . . . 2 2 . .",
    ". . . . . . . . . . . . . . . . . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
]

# 📊 DIAGONAL STRIPES
DIAGONAL = [
    "4 . . 4 . . 4 . . 4 . . 4 . . 4 . . 4 . .",
    ". 3 . . 3 . . 3 . . 3 . . 3 . . 3 . . 3 .",
    ". . 2 . . 2 . . 2 . . 2 . . 2 . . 2 . . 2",
    "4 . . 4 . . 4 . . 4 . . 4 . . 4 . . 4 . .",
    ". 3 . . 3 . . 3 . . 3 . . 3 . . 3 . . 3 .",
    ". . 2 . . 2 . . 2 . . 2 . . 2 . . 2 . . 2",
    "4 . . 4 . . 4 . . 4 . . 4 . . 4 . . 4 . .",
]

# 🔤 WRITE "HI" 
HI = [
    "3 . 3 . . 3 3 .",
    "3 . 3 . . . 3 .",
    "3 . 3 . . . 3 .",
    "3 3 3 . . . 3 .",
    "3 . 3 . . . 3 .",
    "3 . 3 . . . 3 .",
    "3 . 3 . . 3 3 .",
]

# 🔤 WRITE "MRIDUL"
MRIDUL = [
    "4 . 4 . 4 4 . . 4 3 . . 4 4 . . 4 . 4 . 4 . .",
    "4 4 4 . 4 . 4 . 4 . 3 . 4 . 4 . 4 . 4 . 4 . .",
    "4 . 4 . 4 . 4 . 4 . 3 . 4 . 4 . 4 . 4 . 4 . .",
    "4 . 4 . 4 4 . . 4 . 3 . 4 . 4 . 4 . 4 . 4 . .",
    "4 . 4 . 4 . 4 . 4 . 3 . 4 . 4 . 4 . 4 . 4 . .",
    "4 . 4 . 4 . 4 . 4 . 3 . 4 . 4 . 4 . 4 . 4 3 .",
    "4 . 4 . 4 . 4 . 4 3 . . 4 4 . . 4 4 4 . 4 3 3",
]

# 🌊 WAVE PATTERN  
WAVE = [
    ". . 3 3 . . . . . . 3 3 . . . . . . 3 3 .",
    ". 3 . . 3 . . . . 3 . . 3 . . . . 3 . . 3",
    "3 . . . . 3 . . 3 . . . . 3 . . 3 . . . .",
    ". . . . . . 3 3 . . . . . . 3 3 . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
    ". . . . . . . . . . . . . . . . . . . . .",
]

# 🏔️ MOUNTAIN PATTERN
MOUNTAIN = [
    ". . . . . . 4 . . . . . . . . . . 4 . . .",
    ". . . . . 3 3 3 . . . . . . . . 3 3 3 . .",
    ". . . . 3 . . . 3 . . . . . . 3 . . . 3 .",
    ". . . 2 . . . . . 2 . . . . 2 . . . . . 2",
    ". . 2 . . . . . . . 2 . . 2 . . . . . . .",
    ". 1 . . . . . . . . . 1 1 . . . . . . . .",
    "1 . . . . . . . . . . . . . . . . . . . .",
]

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    ⚙️  SETTINGS                                 ║
# ╠══════════════════════════════════════════════════════════════════╣
# ║  Choose your pattern and configure start position               ║
# ╚══════════════════════════════════════════════════════════════════╝

# 👇 SELECT YOUR PATTERN HERE (change to any pattern name above)
PATTERN = HEART

# How many weeks ago should the pattern START?
# - The GitHub graph shows ~52 weeks
# - Set this to position your pattern (e.g., 40 = starts 40 weeks ago)
# - The pattern draws LEFT to RIGHT from this starting point
START_WEEKS_AGO = 40

# Commit intensity multiplier (commits per intensity level)
COMMITS_PER_LEVEL = {
    '1': 2,   # light green
    '2': 5,   # medium green  
    '3': 8,   # dark green
    '4': 12,  # darkest green
}

# ╔══════════════════════════════════════════════════════════════════╗
# ║                    🚀 SCRIPT LOGIC (don't edit below)           ║
# ╚══════════════════════════════════════════════════════════════════╝

def parse_pattern(pattern):
    """Parse the text pattern into a 2D grid of intensity values."""
    grid = []
    for row in pattern:
        cells = row.strip().split()
        grid.append(cells)
    return grid


def get_start_date(weeks_ago):
    """Calculate the start date (Sunday) for the pattern."""
    today = datetime.now()
    # Find the most recent Sunday
    days_since_sunday = today.weekday() + 1  # Monday=0, so +1 to get days since Sunday
    if days_since_sunday == 7:
        days_since_sunday = 0  # Today is Sunday
    last_sunday = today - timedelta(days=days_since_sunday)
    # Go back 'weeks_ago' weeks
    start_date = last_sunday - timedelta(weeks=weeks_ago)
    return start_date


def preview_pattern(grid, start_date):
    """Show a preview of what the pattern will look like."""
    days = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    
    print("\n" + "=" * 60)
    print("📋 PATTERN PREVIEW")
    print("=" * 60)
    
    num_weeks = max(len(row) for row in grid)
    
    # Print week numbers header
    print("     ", end="")
    for w in range(num_weeks):
        date = start_date + timedelta(weeks=w)
        print(f" W{w+1:02d}", end="")
    print()
    
    # Print the grid
    for day_idx, row in enumerate(grid):
        print(f" {days[day_idx]}  ", end="")
        for cell in row:
            if cell == '.':
                print("  · ", end="")
            elif cell == '1':
                print("  ░ ", end="")
            elif cell == '2':
                print("  ▒ ", end="")
            elif cell == '3':
                print("  ▓ ", end="")
            elif cell == '4':
                print("  █ ", end="")
        print()
    
    print("=" * 60)
    
    # Calculate stats
    total_commits = 0
    total_days = 0
    for row in grid:
        for cell in row:
            if cell in COMMITS_PER_LEVEL:
                total_commits += COMMITS_PER_LEVEL[cell]
                total_days += 1
    
    end_date = start_date + timedelta(weeks=num_weeks)
    
    print(f"\n📊 Stats:")
    print(f"   Pattern size: {num_weeks} weeks × 7 days")
    print(f"   Active cells: {total_days}")
    print(f"   Total commits to create: {total_commits}")
    print(f"   Date range: {start_date.strftime('%Y-%m-%d')} → {end_date.strftime('%Y-%m-%d')}")
    print()


def make_commit(date_str, commit_num, total_commits):
    """Create a single backdated commit."""
    # Write to the data file
    with open("contributions.txt", "a") as f:
        f.write(f"Contribution: {date_str} #{commit_num}\n")
    
    # Stage and commit with the specific date
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date_str
    env['GIT_COMMITTER_DATE'] = date_str
    
    subprocess.run(['git', 'add', '.'], capture_output=True)
    subprocess.run(
        ['git', 'commit', '-m', f'🎨 contribution: {date_str}'],
        env=env,
        capture_output=True
    )


def generate_commits(grid, start_date):
    """Generate all the backdated commits for the pattern."""
    total_commits = 0
    for row in grid:
        for cell in row:
            if cell in COMMITS_PER_LEVEL:
                total_commits += COMMITS_PER_LEVEL[cell]
    
    commit_count = 0
    
    print("\n🚀 Generating commits...")
    print("-" * 50)
    
    num_weeks = max(len(row) for row in grid)
    
    for week in range(num_weeks):
        for day in range(7):
            if day >= len(grid):
                continue
            if week >= len(grid[day]):
                continue
                
            cell = grid[day][week]
            
            if cell not in COMMITS_PER_LEVEL:
                continue
            
            num_commits = COMMITS_PER_LEVEL[cell]
            target_date = start_date + timedelta(weeks=week, days=day)
            date_str = target_date.strftime('%Y-%m-%dT12:00:00')
            
            for i in range(num_commits):
                commit_count += 1
                make_commit(date_str, i + 1, total_commits)
                
                # Progress bar
                progress = int((commit_count / total_commits) * 40)
                bar = '█' * progress + '░' * (40 - progress)
                pct = (commit_count / total_commits) * 100
                print(f"\r   [{bar}] {pct:.0f}% ({commit_count}/{total_commits})", end="", flush=True)
    
    print(f"\n\n✅ Done! Created {commit_count} commits.")
    return commit_count


def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║        🎨 GitHub Contribution Pattern Maker 🎨            ║
║                                                           ║
║   Draw custom patterns on your GitHub contribution graph  ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Parse pattern
    grid = parse_pattern(PATTERN)
    
    # Calculate start date
    start_date = get_start_date(START_WEEKS_AGO)
    
    # Preview
    preview_pattern(grid, start_date)
    
    # Confirm
    print("⚠️  This will create backdated commits in this repository.")
    print("   Make sure you're in the correct repo!\n")
    
    response = input("🟢 Proceed? (yes/no): ").strip().lower()
    
    if response not in ('yes', 'y'):
        print("\n❌ Cancelled. No commits were made.")
        return
    
    # Generate commits
    commit_count = generate_commits(grid, start_date)
    
    # Final instructions
    print(f"""
╔═══════════════════════════════════════════════════════════╗
║                    📋 NEXT STEPS                          ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Push your commits to GitHub:                             ║
║                                                           ║
║    git push origin main                                   ║
║                                                           ║
║  Then visit your GitHub profile to see the pattern!       ║
║  (It may take a few minutes to update)                    ║
║                                                           ║
║  🔗 https://github.com/Itz-Mridul                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

📊 Summary:
   - Commits created: {commit_count}
   - Starting from: {start_date.strftime('%Y-%m-%d')}
   - Pattern: {len(grid[0])} weeks wide × {len(grid)} days tall
    """)


if __name__ == "__main__":
    main()
