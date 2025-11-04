print("Hello from Python!")
import random
import datetime

def generate_random_data():
    """Generate some random data for testing"""
    names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
    return {
        "name": random.choice(names),
        "age": random.randint(18, 65),
        "score": random.uniform(0, 100),
        "timestamp": datetime.datetime.now().isoformat()
    }

def generate_team_data():
    """Generate team-based data for advanced testing"""
    teams = ["Development", "QA", "DevOps", "Design", "Marketing"]
    return {
        "team": random.choice(teams),
        "project_count": random.randint(1, 10),
        "success_rate": random.uniform(0.5, 1.0),
        "last_updated": datetime.datetime.now().isoformat()
    }

if __name__ == "__main__":
    print("=== Individual Records ===")
    for i in range(5):
        data = generate_random_data()
        print(f"Record {i+1}: {data}")
    
    print("\n=== Team Records ===")
    for i in range(3):
        team_data = generate_team_data()
        print(f"Team {i+1}: {team_data}")