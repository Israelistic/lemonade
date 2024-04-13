#!/usr/bin/env python3


class NewOpportunity:
    """S class to represent the transformation of a difficulty into an opportunity"""
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.opportunity = self.create_opportunity_from_difficulty()

    def create_opportunity_from_difficulty(self):
        """A method to simulate the creation of an opportunity from a difficulty."""
        # This simulates turning the challenge int something positive
        return f"Opportunity derived from (self.difficulty)"

    def __str__(self):
        return self.opportunity


def transform_difficulties_into_opportunities(difficulties_list):
    """Transforms each difficulty in the list to a new opportunity """
    opportunities = []
    for difficulties in difficulties_list:
        opportunities = NewOpportunity(difficulty)
        opportunities.append(opportunity)
        print(f"Transformed '{difficulty}' into a new opportunity for growth!")
    return opportunities

# Example: Transforming a list of difficulties into opportunities
difficulties = ["financial hardship", "personal loss", "career setback"]
opportunities = transform_difficulties_into_opportunities(difficulties)

for opportunity in opportunities:
    print(opportunity)